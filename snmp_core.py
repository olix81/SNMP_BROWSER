"""Client SNMP (v1 / v2c / v3) basato su pysnmp, eseguito su un event loop asyncio dedicato."""

import asyncio
import concurrent.futures
import threading
from dataclasses import dataclass, asdict, fields

from pysnmp.hlapi.v3arch.asyncio import (
    SnmpEngine, CommunityData, UsmUserData, UdpTransportTarget, Udp6TransportTarget,
    ContextData, ObjectType, ObjectIdentity,
    get_cmd, next_cmd, bulk_cmd, set_cmd, walk_cmd, bulk_walk_cmd,
    usmNoAuthProtocol, usmHMACMD5AuthProtocol, usmHMACSHAAuthProtocol,
    usmHMAC128SHA224AuthProtocol, usmHMAC192SHA256AuthProtocol,
    usmHMAC256SHA384AuthProtocol, usmHMAC384SHA512AuthProtocol,
    usmNoPrivProtocol, usmDESPrivProtocol, usm3DESEDEPrivProtocol,
    usmAesCfb128Protocol, usmAesCfb192Protocol, usmAesCfb256Protocol,
    usmAesBlumenthalCfb192Protocol, usmAesBlumenthalCfb256Protocol,
)
from pysnmp.proto.rfc1902 import OctetString
from pysnmp.proto.rfc1905 import EndOfMibView

VERSIONS = ("v1", "v2c", "v3")
SECURITY_LEVELS = ("noAuthNoPriv", "authNoPriv", "authPriv")

AUTH_PROTOCOLS = {
    "MD5": usmHMACMD5AuthProtocol,
    "SHA": usmHMACSHAAuthProtocol,
    "SHA-224": usmHMAC128SHA224AuthProtocol,
    "SHA-256": usmHMAC192SHA256AuthProtocol,
    "SHA-384": usmHMAC256SHA384AuthProtocol,
    "SHA-512": usmHMAC384SHA512AuthProtocol,
}

PRIV_PROTOCOLS = {
    "DES": usmDESPrivProtocol,
    "3DES": usm3DESEDEPrivProtocol,
    "AES-128": usmAesCfb128Protocol,
    "AES-192": usmAesCfb192Protocol,
    "AES-256": usmAesCfb256Protocol,
    "AES-192 (Cisco)": usmAesBlumenthalCfb192Protocol,
    "AES-256 (Cisco)": usmAesBlumenthalCfb256Protocol,
}


ERROR_HINTS = {
    "before timeout": "nessuna risposta: verificare host/porta, community o credenziali v3, firewall",
    "Wrong SNMP PDU digest": "autenticazione fallita: password o protocollo di autenticazione errati",
    "Unknown USM user": "utente SNMPv3 non configurato sull'agent",
    "ciphertext is broken": "decifratura fallita: password o protocollo di privacy errati",
    "Unsupported security level": "livello di sicurezza non ammesso per questo utente",
    "Unknown SNMP engine ID": "engine ID non valido: lasciare vuoto il campo Security Engine ID",
    "Not in time window": "orologio/boots dell'agent fuori finestra: riprovare",
}


class SnmpError(Exception):
    pass


class Cancelled(Exception):
    pass


@dataclass
class AgentConfig:
    host: str = "127.0.0.1"
    port: int = 161
    version: str = "v2c"
    read_community: str = "public"
    write_community: str = "private"
    timeout: float = 2.0
    retries: int = 1
    max_repetitions: int = 25
    # SNMPv3
    user: str = ""
    security_level: str = "authPriv"
    auth_protocol: str = "SHA"
    auth_password: str = ""
    priv_protocol: str = "AES-128"
    priv_password: str = ""
    context_name: str = ""
    context_engine_id: str = ""   # esadecimale, opzionale
    security_engine_id: str = ""  # esadecimale, opzionale (di norma scoperto automaticamente)

    SECRET_FIELDS = ("auth_password", "priv_password")

    def to_dict(self, include_secrets=False):
        d = asdict(self)
        if not include_secrets:
            for f in self.SECRET_FIELDS:
                d.pop(f, None)
        return d

    @classmethod
    def from_dict(cls, d):
        names = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in (d or {}).items() if k in names})


def _hex_octets(text):
    text = text.strip().replace(":", "").replace(" ", "")
    if text.lower().startswith("0x"):
        text = text[2:]
    return OctetString(hexValue=text) if text else None


class SnmpClient:
    """Esegue le richieste SNMP su un thread separato; i metodi pubblici restituiscono Future."""

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self.loop.run_forever, name="snmp-loop", daemon=True)
        self._thread.start()
        self._engine = None
        self._engine_key = None

    # --- infrastruttura -------------------------------------------------

    def _submit(self, coro):
        return asyncio.run_coroutine_threadsafe(coro, self.loop)

    def _engine_for(self, cfg):
        # Con v3 l'engine memorizza utenti e chiavi localizzate: lo ricreiamo se cambiano le credenziali.
        key = (cfg.version,)
        if cfg.version == "v3":
            key += (cfg.host, cfg.port, cfg.user, cfg.security_level, cfg.auth_protocol, cfg.auth_password,
                    cfg.priv_protocol, cfg.priv_password, cfg.security_engine_id)
        if key != self._engine_key:
            if self._engine is not None:
                try:
                    self._engine.close_dispatcher()
                except Exception:
                    pass
            self._engine = SnmpEngine()
            self._engine_key = key
        return self._engine

    def _auth(self, cfg, write=False):
        if cfg.version in ("v1", "v2c"):
            community = cfg.write_community if write else cfg.read_community
            return CommunityData(community, mpModel=0 if cfg.version == "v1" else 1)
        if not cfg.user:
            raise SnmpError("SNMPv3: specificare il nome utente")
        kw = {"authProtocol": usmNoAuthProtocol, "privProtocol": usmNoPrivProtocol}
        if cfg.security_level in ("authNoPriv", "authPriv"):
            if len(cfg.auth_password) < 8:
                raise SnmpError("SNMPv3: la password di autenticazione deve avere almeno 8 caratteri")
            kw["authKey"] = cfg.auth_password
            kw["authProtocol"] = AUTH_PROTOCOLS[cfg.auth_protocol]
        if cfg.security_level == "authPriv":
            if len(cfg.priv_password) < 8:
                raise SnmpError("SNMPv3: la password di privacy deve avere almeno 8 caratteri")
            kw["privKey"] = cfg.priv_password
            kw["privProtocol"] = PRIV_PROTOCOLS[cfg.priv_protocol]
        engine_id = _hex_octets(cfg.security_engine_id)
        if engine_id is not None:
            kw["securityEngineId"] = engine_id
        return UsmUserData(cfg.user, **kw)

    def _context(self, cfg):
        if cfg.version != "v3":
            return ContextData()
        return ContextData(contextEngineId=_hex_octets(cfg.context_engine_id), contextName=cfg.context_name)

    async def _target(self, cfg):
        cls = Udp6TransportTarget if ":" in cfg.host else UdpTransportTarget
        try:
            return await cls.create((cfg.host, int(cfg.port)), timeout=float(cfg.timeout), retries=int(cfg.retries))
        except Exception as exc:
            raise SnmpError(f"Indirizzo non valido '{cfg.host}': {exc}") from exc

    async def _prepare(self, cfg, write=False):
        return self._engine_for(cfg), self._auth(cfg, write), await self._target(cfg), self._context(cfg)

    @staticmethod
    def _check(err_ind, err_status, err_index, var_binds):
        if err_ind:
            msg = str(err_ind)
            hint = next((h for k, h in ERROR_HINTS.items() if k in msg), None)
            raise SnmpError(f"{msg}\n→ {hint}" if hint else msg)
        if err_status and int(err_status):
            where = ""
            if err_index and int(err_index) and int(err_index) <= len(var_binds):
                where = f" su {var_binds[int(err_index) - 1][0]}"
            raise SnmpError(f"{err_status.prettyPrint()}{where}")

    @staticmethod
    def _rows(var_binds):
        return [(tuple(vb[0]), vb[1]) for vb in var_binds]

    # --- operazioni -----------------------------------------------------

    async def _get(self, cfg, oids):
        eng, auth, tgt, ctx = await self._prepare(cfg)
        r = await get_cmd(eng, auth, tgt, ctx, *[ObjectType(ObjectIdentity(o)) for o in oids], lookupMib=False)
        self._check(*r)
        return self._rows(r[3])

    async def _get_next(self, cfg, oids):
        eng, auth, tgt, ctx = await self._prepare(cfg)
        r = await next_cmd(eng, auth, tgt, ctx, *[ObjectType(ObjectIdentity(o)) for o in oids], lookupMib=False)
        self._check(*r)
        return self._rows(r[3])

    async def _get_bulk(self, cfg, oids, non_repeaters, max_repetitions):
        if cfg.version == "v1":
            raise SnmpError("GetBulk non è disponibile in SNMPv1")
        eng, auth, tgt, ctx = await self._prepare(cfg)
        r = await bulk_cmd(eng, auth, tgt, ctx, non_repeaters, max_repetitions,
                           *[ObjectType(ObjectIdentity(o)) for o in oids], lookupMib=False)
        self._check(*r)
        return self._rows(r[3])

    async def _set(self, cfg, oid, value):
        eng, auth, tgt, ctx = await self._prepare(cfg, write=True)
        r = await set_cmd(eng, auth, tgt, ctx, ObjectType(ObjectIdentity(oid), value), lookupMib=False)
        self._check(*r)
        return self._rows(r[3])

    async def _walk(self, cfg, oid, on_rows, stop_event, use_bulk):
        eng, auth, tgt, ctx = await self._prepare(cfg)
        root = ObjectType(ObjectIdentity(oid))
        if use_bulk and cfg.version != "v1":
            gen = bulk_walk_cmd(eng, auth, tgt, ctx, 0, int(cfg.max_repetitions), root,
                                lexicographicMode=False, lookupMib=False)
        else:
            gen = walk_cmd(eng, auth, tgt, ctx, root, lexicographicMode=False, lookupMib=False)
        total = 0
        try:
            async for err_ind, err_status, err_index, var_binds in gen:
                if stop_event is not None and stop_event.is_set():
                    raise Cancelled()
                # In v1 il "noSuchName" segna la fine della MIB: non è un errore.
                if cfg.version == "v1" and err_status and err_status.prettyPrint() == "noSuchName":
                    break
                self._check(err_ind, err_status, err_index, var_binds)
                rows = [r for r in self._rows(var_binds)
                        if not isinstance(r[1], EndOfMibView) and r[0][:len(oid)] == tuple(oid)]
                if rows:
                    total += len(rows)
                    on_rows(rows)
        finally:
            await gen.aclose()
        return total

    # --- API pubblica (thread-safe, restituisce concurrent.futures.Future) ---

    def get(self, cfg, oids) -> concurrent.futures.Future:
        return self._submit(self._get(cfg, oids))

    def get_next(self, cfg, oids) -> concurrent.futures.Future:
        return self._submit(self._get_next(cfg, oids))

    def get_bulk(self, cfg, oids, non_repeaters=0, max_repetitions=10) -> concurrent.futures.Future:
        return self._submit(self._get_bulk(cfg, oids, non_repeaters, max_repetitions))

    def set(self, cfg, oid, value) -> concurrent.futures.Future:
        return self._submit(self._set(cfg, oid, value))

    def walk(self, cfg, oid, on_rows, stop_event=None, use_bulk=True) -> concurrent.futures.Future:
        """on_rows(list[(oid, value)]) viene chiamato dal thread SNMP per ogni blocco ricevuto."""
        return self._submit(self._walk(cfg, tuple(oid), on_rows, stop_event, use_bulk))
