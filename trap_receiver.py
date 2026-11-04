"""Ricevitore di trap/inform SNMP v1, v2c e v3, eseguito su un thread con event loop dedicato.

SNMPv3: per le trap il mittente è "autoritativo", quindi le chiavi vanno localizzate sul suo
engine ID. Gli utenti senza engine ID configurato vengono abilitati automaticamente per ogni
engine ID visto nei pacchetti in arrivo (come 'createUser' senza -e non permetterebbe in snmptrapd).
Per gli inform l'autoritativo è il ricevitore: gli utenti sono registrati anche sul nostro engine ID.
"""

import asyncio
import os
import socket
import threading
import time
from dataclasses import dataclass, asdict, fields

from pyasn1.codec.ber import decoder
from pysnmp.carrier.asyncio.dgram import udp, udp6
from pysnmp.entity import config, engine
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto import api
from pysnmp.proto.mpmod.rfc3412 import SNMPv3Message
from pysnmp.proto.rfc1902 import OctetString
from pysnmp.proto.secmod.rfc3414.service import UsmSecurityParameters

from snmp_core import AUTH_PROTOCOLS, PRIV_PROTOCOLS, _hex_octets

SNMP_TRAP_OID = (1, 3, 6, 1, 6, 3, 1, 1, 4, 1, 0)

AUTH_CONFIG = {
    "MD5": config.USM_AUTH_HMAC96_MD5, "SHA": config.USM_AUTH_HMAC96_SHA,
    "SHA-224": config.USM_AUTH_HMAC128_SHA224, "SHA-256": config.USM_AUTH_HMAC192_SHA256,
    "SHA-384": config.USM_AUTH_HMAC256_SHA384, "SHA-512": config.USM_AUTH_HMAC384_SHA512,
}
PRIV_CONFIG = {
    "DES": config.USM_PRIV_CBC56_DES, "3DES": config.USM_PRIV_CBC168_3DES,
    "AES-128": config.USM_PRIV_CFB128_AES, "AES-192": config.USM_PRIV_CFB192_AES,
    "AES-256": config.USM_PRIV_CFB256_AES, "AES-192 (Cisco)": config.USM_PRIV_CFB192_AES_BLUMENTHAL,
    "AES-256 (Cisco)": config.USM_PRIV_CFB256_AES_BLUMENTHAL,
}
assert set(AUTH_CONFIG) == set(AUTH_PROTOCOLS) and set(PRIV_CONFIG) == set(PRIV_PROTOCOLS)

# contatori d'errore -> spiegazione, per segnalare i messaggi scartati
DROP_REASONS = [
    ("SNMPv2-MIB", "snmpInASNParseErrs", "pacchetto non decodificabile"),
    ("SNMPv2-MIB", "snmpInBadCommunityNames", "community non accettata"),
    ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownUserNames", "utente SNMPv3 non configurato"),
    ("SNMP-USER-BASED-SM-MIB", "usmStatsWrongDigests", "autenticazione fallita (password o protocollo auth errati)"),
    ("SNMP-USER-BASED-SM-MIB", "usmStatsDecryptionErrors", "decifratura fallita (password o protocollo priv errati)"),
    ("SNMP-USER-BASED-SM-MIB", "usmStatsUnsupportedSecLevels", "livello di sicurezza non previsto per l'utente"),
    ("SNMP-USER-BASED-SM-MIB", "usmStatsNotInTimeWindows", "messaggio fuori dalla finestra temporale"),
    ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownEngineIDs", "engine ID sconosciuto"),
    ("SNMP-MPD-MIB", "snmpUnknownSecurityModels", "modello di sicurezza non supportato"),
]


@dataclass
class TrapUser:
    name: str
    security_level: str = "authPriv"
    auth_protocol: str = "SHA"
    auth_password: str = ""
    priv_protocol: str = "AES-128"
    priv_password: str = ""
    engine_id: str = ""  # hex del mittente; vuoto = qualsiasi (appreso dai pacchetti)

    def to_dict(self, include_secrets=True):
        d = asdict(self)
        if not include_secrets:
            d.pop("auth_password")
            d.pop("priv_password")
        return d

    @classmethod
    def from_dict(cls, d):
        names = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in d.items() if k in names})


@dataclass
class TrapEvent:
    time: float
    source: str           # "ip:porta"
    version: str          # v1 / v2c / v3
    pdu: str              # Trap / Inform
    security: str         # community o utente/livello
    context: str
    trap_oid: tuple       # snmpTrapOID (anche per le v1, convertite secondo RFC 3584)
    var_binds: list       # [(oid tuple, valore)]


@dataclass
class ReceiverConfig:
    address: str = "0.0.0.0"
    port: int = 162
    communities: str = "public"   # separate da virgola; vuoto o '*' = qualsiasi
    engine_id: str = ""           # hex del ricevitore (per gli inform v3); vuoto = generato


def new_engine_id():
    # formato RFC 3411: enterprise 'pysnmp' (20408) + formato 5 (ottetti arbitrari)
    return "80004fb805" + os.urandom(8).hex()


class TrapReceiver:
    def __init__(self, on_event, on_drop=None):
        """on_event(TrapEvent) e on_drop(sorgente, motivo) vengono chiamati dal thread del ricevitore."""
        self.on_event = on_event
        self.on_drop = on_drop
        self._thread = None
        self._loop = None
        self._engine = None
        self.running = False

    # --- avvio / arresto --------------------------------------------------

    def start(self, cfg: ReceiverConfig, users):
        """Avvia il ricevitore; solleva un'eccezione se la porta non può essere aperta."""
        self.stop()
        ready = threading.Event()
        result = {}

        def run():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop = loop
            try:
                self._setup(cfg, users)
            except Exception as exc:
                result["error"] = exc
                ready.set()
                loop.close()
                return
            ready.set()
            try:
                loop.run_forever()
            finally:
                try:
                    self._engine.close_dispatcher()
                except Exception:
                    pass
                self._sock.close()
                pending = [t for t in asyncio.all_tasks(loop) if not t.done()]
                for t in pending:
                    t.cancel()
                loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
                loop.close()

        self._thread = threading.Thread(target=run, name="trap-receiver", daemon=True)
        self._thread.start()
        ready.wait(10)
        if "error" in result:
            self._thread = None
            raise result["error"]
        self.running = True

    def stop(self):
        if self._thread is None:
            return
        loop = self._loop
        if loop is not None and loop.is_running():
            loop.call_soon_threadsafe(loop.stop)
        self._thread.join(5)
        self._thread = None
        self._engine = None
        self.running = False

    # --- configurazione dell'engine ------------------------------------------

    def _setup(self, cfg, users):
        eid = _hex_octets(cfg.engine_id) if cfg.engine_id else None
        snmp_engine = engine.SnmpEngine(snmpEngineID=eid) if eid is not None else engine.SnmpEngine()
        self._engine = snmp_engine

        ipv6 = ":" in cfg.address
        mod = udp6 if ipv6 else udp
        # socket creato qui per avere subito l'eventuale errore di bind (pysnmp lo apre in modo asincrono)
        sock = socket.socket(socket.AF_INET6 if ipv6 else socket.AF_INET, socket.SOCK_DGRAM)
        try:
            if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):  # Windows: niente porte condivise tra processi
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
            sock.bind((cfg.address, int(cfg.port)))
            sock.setblocking(False)
            transport = mod.UdpTransport().open_server_mode(sock=sock)
            self._sock = sock
        except Exception as exc:
            sock.close()
            hint = ""
            if int(cfg.port) == 162:
                hint = ("\n\nLa porta 162 potrebbe essere già usata dal servizio Windows 'SNMP Trap' "
                        "o da un altro ricevitore: fermarlo oppure usare un'altra porta.")
            raise OSError(f"Impossibile aprire la porta UDP {cfg.address}:{cfg.port}: {exc}{hint}") from exc
        config.add_transport(snmp_engine, mod.DOMAIN_NAME, transport)

        comms = [c.strip() for c in cfg.communities.split(",") if c.strip()]
        self._any_community = not comms or "*" in comms
        self._communities = set()
        for c in comms:
            if c != "*":
                self._add_community(c)

        self._users = {u.name: u for u in users}
        self._registered = set()  # (engine id bytes | None, utente)
        for u in users:
            fixed = _hex_octets(u.engine_id) if u.engine_id else None
            if fixed is not None:
                self._add_user(u, fixed.asOctets())
            self._add_user(u, None)  # engine ID locale: inform v3

        snmp_engine.observer.register_observer(self._on_message, "rfc3412.receiveMessage:request")
        snmp_engine.transport_dispatcher.register_routing_callback(self._pre_process)
        ntfrcv.NotificationReceiver(snmp_engine, self._on_notification)
        snmp_engine.transport_dispatcher.job_started(1)
        self._last = {}
        self._last_community = ""
        self._pending = None

    @property
    def engine_id(self):
        if self._engine is None:
            return ""
        return self._engine.snmpEngineID.asOctets().hex()

    def _add_community(self, community):
        if community in self._communities:
            return
        index = f"trap-c{len(self._communities)}"
        config.add_v1_system(self._engine, index, community)
        self._communities.add(community)

    def _add_user(self, user, engine_id_bytes):
        key = (engine_id_bytes, user.name)
        if key in self._registered:
            return
        kw = {}
        if engine_id_bytes is not None:
            kw["securityEngineId"] = OctetString(engine_id_bytes)
        auth, auth_key, priv, priv_key = config.USM_AUTH_NONE, None, config.USM_PRIV_NONE, None
        if user.security_level in ("authNoPriv", "authPriv"):
            auth, auth_key = AUTH_CONFIG[user.auth_protocol], user.auth_password
        if user.security_level == "authPriv":
            priv, priv_key = PRIV_CONFIG[user.priv_protocol], user.priv_password
        config.add_v3_user(self._engine, user.name, auth, auth_key, priv, priv_key, **kw)
        self._registered.add(key)

    # --- elaborazione dei messaggi -------------------------------------------

    def _pre_process(self, transport_domain, transport_address, message):
        """Chiamata per ogni datagramma prima di pysnmp: registra community/utenti al volo."""
        source = _addr(transport_address)
        info = None
        try:
            ver = api.decodeMessageVersion(message)
            if ver in (api.SNMP_VERSION_1, api.SNMP_VERSION_2C):
                p_mod = api.PROTOCOL_MODULES[ver]
                msg, _ = decoder.decode(message, asn1Spec=p_mod.Message())
                community = p_mod.apiMessage.get_community(msg).asOctets().decode("latin-1")
                self._last_community = community
                info = f"{'v1' if ver == api.SNMP_VERSION_1 else 'v2c'}, community '{community}'"
                if self._any_community:
                    self._add_community(community)
            elif int(ver) == 3:
                msg, _ = decoder.decode(message, asn1Spec=SNMPv3Message())
                sp, _ = decoder.decode(msg["msgSecurityParameters"], asn1Spec=UsmSecurityParameters())
                eid = sp["msgAuthoritativeEngineId"].asOctets()
                user_name = sp["msgUserName"].asOctets().decode("latin-1")
                # utente vuoto = scoperta dell'engine ID (inform): fa parte del protocollo, non è un errore
                if user_name:
                    info = f"v3, utente '{user_name}', engine ID {eid.hex() or '-'}"
                user = self._users.get(user_name)
                if user is not None and not user.engine_id and eid:
                    self._add_user(user, eid)
        except Exception:
            info = "pacchetto non riconosciuto"
        if info is not None and self.on_drop is not None:
            self._pending = (source, info, self._read_counters())
            # pysnmp elabora il datagramma in modo sincrono subito dopo: il controllo segue a ruota
            self._loop.call_soon(self._check_dropped)
        return None  # instradamento predefinito

    def _check_dropped(self):
        if self._pending is None:
            return
        source, info, before = self._pending
        self._pending = None
        after = self._read_counters()
        reasons = [label for (_, _, label), b, a in zip(DROP_REASONS, before, after) if a > b]
        if reasons:
            self.on_drop(source, f"{info}: {'; '.join(reasons)}")

    def _read_counters(self):
        values = []
        for mod, sym, _ in DROP_REASONS:
            v = 0
            for name in ("__" + mod, mod):
                try:
                    (node,) = self._engine.get_mib_builder().import_symbols(name, sym)
                    v = int(node.syntax)
                    break
                except Exception:
                    continue
            values.append(v)
        return values

    def _on_message(self, snmp_engine, execpoint, variables, cb_ctx):
        self._last = variables

    def _on_notification(self, snmp_engine, state_reference, context_engine_id, context_name, var_binds, cb_ctx):
        v = self._last or {}
        try:
            _, addr = snmp_engine.message_dispatcher.get_transport_info(state_reference)
            source = _addr(addr)
        except Exception:
            source = _addr(v.get("transportAddress"))
        mp = v.get("messageProcessingModel")
        version = {0: "v1", 1: "v2c", 3: "v3"}.get(mp, "?")
        sec_name = v.get("securityName")
        sec_name = sec_name.prettyPrint() if hasattr(sec_name, "prettyPrint") else str(sec_name or "")
        if version == "v3":
            level = {1: "noAuthNoPriv", 2: "authNoPriv", 3: "authPriv"}.get(int(v.get("securityLevel", 0)), "")
            security = f"{sec_name} ({level})"
        else:
            security = f"community '{self._last_community}'"
        pdu = v.get("pdu")
        kind = "Inform" if pdu is not None and "Inform" in pdu.__class__.__name__ else "Trap"
        rows = [(tuple(name), value) for name, value in var_binds]
        trap_oid = next((tuple(val) for oid, val in rows if oid == SNMP_TRAP_OID), ())
        ctx = context_name.prettyPrint() if hasattr(context_name, "prettyPrint") else str(context_name or "")
        self.on_event(TrapEvent(time.time(), source, version, kind, security, ctx, trap_oid, rows))


def _addr(address):
    try:
        return f"{address[0]}:{address[1]}"
    except Exception:
        return str(address)
