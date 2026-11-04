"""Invia trap/inform di prova (v1, v2c, v3) a un ricevitore.

    python test_trap_sender.py [host] [porta]        (default 127.0.0.1 162)

Per le v3 usa l'utente 'trapuser' (SHA / AES-128, password auth 'authkey1', priv 'privkey1'):
configurarlo nel ricevitore senza engine ID.
"""

import asyncio
import sys

from pysnmp.hlapi.v3arch.asyncio import (
    SnmpEngine, CommunityData, UsmUserData, UdpTransportTarget, ContextData, NotificationType, ObjectIdentity,
    ObjectType, send_notification, usmHMACSHAAuthProtocol, usmAesCfb128Protocol,
)
from pysnmp.proto.rfc1902 import OctetString, Integer32

LINK_DOWN = "1.3.6.1.6.3.1.1.5.3"
IF_INDEX = "1.3.6.1.2.1.2.2.1.1.3"
IF_DESCR = "1.3.6.1.2.1.2.2.1.2.3"


def notification():
    return NotificationType(ObjectIdentity(LINK_DOWN)).add_varbinds(
        ObjectType(ObjectIdentity(IF_INDEX), Integer32(3)),
        ObjectType(ObjectIdentity(IF_DESCR), OctetString("eth0 (test)")),
    )


async def main():
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 162
    target = await UdpTransportTarget.create((host, port), timeout=2, retries=0)
    v3 = UsmUserData("trapuser", "authkey1", "privkey1",
                     authProtocol=usmHMACSHAAuthProtocol, privProtocol=usmAesCfb128Protocol)
    cases = [
        ("v1 trap", CommunityData("public", mpModel=0), "trap"),
        ("v2c trap", CommunityData("public", mpModel=1), "trap"),
        ("v2c inform", CommunityData("public", mpModel=1), "inform"),
        ("v3 trap authPriv", v3, "trap"),
        ("v3 inform authPriv", v3, "inform"),
    ]
    for label, auth, kind in cases:
        err, status, _, _ = await send_notification(SnmpEngine(), auth, target, ContextData(), kind, notification())
        print(f"{label:22} {'OK' if not err and not status else f'ERRORE: {err or status.prettyPrint()}'}")


if __name__ == "__main__":
    asyncio.run(main())
