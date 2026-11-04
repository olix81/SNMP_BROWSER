"""Piccolo agent SNMP locale per provare il browser (v1/v2c/v3).

    python test_agent.py [porta]        (default 1161, su 127.0.0.1)

Community: public (lettura), private (lettura/scrittura)
Utenti SNMPv3 (password auth 'authkey1', priv 'privkey1'):
    usr-none           noAuthNoPriv
    usr-sha-none       authNoPriv  SHA
    usr-md5-des        authPriv    MD5 / DES
    usr-sha-aes        authPriv    SHA / AES-128
    usr-sha256-aes256  authPriv    SHA-256 / AES-256
    usr-sha512-aes192  authPriv    SHA-512 / AES-192
"""

import asyncio
import sys

from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity import config, engine
from pysnmp.entity.rfc3413 import cmdrsp, context

USERS = [
    ("usr-none", config.USM_AUTH_NONE, None, config.USM_PRIV_NONE, None, "noAuthNoPriv"),
    ("usr-sha-none", config.USM_AUTH_HMAC96_SHA, "authkey1", config.USM_PRIV_NONE, None, "authNoPriv"),
    ("usr-md5-des", config.USM_AUTH_HMAC96_MD5, "authkey1", config.USM_PRIV_CBC56_DES, "privkey1", "authPriv"),
    ("usr-sha-aes", config.USM_AUTH_HMAC96_SHA, "authkey1", config.USM_PRIV_CFB128_AES, "privkey1", "authPriv"),
    ("usr-sha256-aes256", config.USM_AUTH_HMAC192_SHA256, "authkey1", config.USM_PRIV_CFB256_AES, "privkey1",
     "authPriv"),
    ("usr-sha512-aes192", config.USM_AUTH_HMAC384_SHA512, "authkey1", config.USM_PRIV_CFB192_AES, "privkey1",
     "authPriv"),
]


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 1161
    asyncio.set_event_loop(asyncio.new_event_loop())  # da Python 3.14 non viene creato implicitamente
    snmp_engine = engine.SnmpEngine()
    config.add_transport(snmp_engine, udp.DOMAIN_NAME, udp.UdpTransport().open_server_mode(("127.0.0.1", port)))

    config.add_v1_system(snmp_engine, "area-ro", "public")
    config.add_v1_system(snmp_engine, "area-rw", "private")
    for model in (1, 2):
        config.add_vacm_user(snmp_engine, model, "area-ro", "noAuthNoPriv", (1, 3, 6))
        config.add_vacm_user(snmp_engine, model, "area-rw", "noAuthNoPriv", (1, 3, 6), (1, 3, 6))

    for name, auth, auth_key, priv, priv_key, level in USERS:
        config.add_v3_user(snmp_engine, name, auth, auth_key, priv, priv_key)
        config.add_vacm_user(snmp_engine, 3, name, level, (1, 3, 6), (1, 3, 6))

    snmp_context = context.SnmpContext(snmp_engine)
    cmdrsp.GetCommandResponder(snmp_engine, snmp_context)
    cmdrsp.SetCommandResponder(snmp_engine, snmp_context)
    cmdrsp.NextCommandResponder(snmp_engine, snmp_context)
    cmdrsp.BulkCommandResponder(snmp_engine, snmp_context)

    print(f"Agent SNMP di test in ascolto su 127.0.0.1:{port} (Ctrl+C per uscire)")
    snmp_engine.transport_dispatcher.job_started(1)
    try:
        snmp_engine.open_dispatcher()
    except KeyboardInterrupt:
        pass
    finally:
        snmp_engine.close_dispatcher()


if __name__ == "__main__":
    main()
