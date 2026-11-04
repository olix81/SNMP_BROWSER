# SNMP MIB module (UUID-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/UUID-TC-MIB
# Produced by pysmi-2.0.0 at Sat Oct 17 14:25:44 2026
# On host olix-pc platform Windows version 11 by user marco
# Using Python version 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

uuidTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 217)
)
if mibBuilder.loadTexts:
    uuidTCMIB.setRevisions(
        ("2013-04-05 00:00",)
    )
if mibBuilder.loadTexts:
    uuidTCMIB.setLastUpdated("201304050000Z")
if mibBuilder.loadTexts:
    uuidTCMIB.setOrganization("IETF Energy Management Working Group")
if mibBuilder.loadTexts:
    uuidTCMIB.setContactInfo("WG Email: eman@ietf.org Mailing list subscription info: http://www.ietf.org/mailman/listinfo/eman Dan Romascanu Avaya Park Atidim, Bldg. #3 Tel Aviv, 61581 Israel Phone: +972-3-6458414 Email: dromasca@avaya.com Juergen Quittek NEC Europe Ltd. Network Research Division Kurfuersten-Anlage 36 Heidelberg 69115 Germany Phone: +49 6221 4342-115 Email: quittek@neclab.eu Mouli Chandramouli Cisco Systems, Inc. Sarjapur Outer Ring Road Bangalore 560103 India Phone: +91 80 4429 2409 Email: moulchan@cisco.com")
if mibBuilder.loadTexts:
    uuidTCMIB.setDescription("This MIB module defines TEXTUAL-CONVENTIONs representing Universally Unique IDentifiers (UUIDs). Copyright (c) 2013 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")


# Types definitions


# TEXTUAL-CONVENTIONS



class UUID(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x-2x-2x-1x1x-6x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16

    if mibBuilder.loadTexts:
        description = "Universally Unique Identifier information. The syntax must conform to RFC 4122, Section 4.1."


class UUIDorZero(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x-2x-2x-1x1x-6x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )

    if mibBuilder.loadTexts:
        description = "Universally Unique Identifier information. The syntax must conform to RFC 4122, Section 4.1. The semantics of the value zero-length OCTET STRING are object-specific and must therefore be defined as part of the description of any object that uses this syntax."


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UUID-TC-MIB",
    **{"UUID": UUID,
       "UUIDorZero": UUIDorZero,
       "uuidTCMIB": uuidTCMIB}
)
