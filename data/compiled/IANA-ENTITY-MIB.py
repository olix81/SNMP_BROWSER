# SNMP MIB module (IANA-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IANA-ENTITY-MIB
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

ianaEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 216)
)
if mibBuilder.loadTexts:
    ianaEntityMIB.setRevisions(
        ("2015-07-16 00:00",
         "2015-07-16 00:00",
         "2013-04-05 00:00")
    )
if mibBuilder.loadTexts:
    ianaEntityMIB.setLastUpdated("201507160000Z")
if mibBuilder.loadTexts:
    ianaEntityMIB.setOrganization("IANA")
if mibBuilder.loadTexts:
    ianaEntityMIB.setContactInfo("Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Phone: +1-310-301-5800 EMail: iana&iana.org")
if mibBuilder.loadTexts:
    ianaEntityMIB.setDescription("This MIB module defines a TEXTUAL-CONVENTION that provides an indication of the general hardware type of a particular physical entity. Copyright (c) 2013 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). The initial version of this MIB module was published in RFC 6933; for full legal notices see the RFC itself.")


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAPhysicalClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("chassis", 3),
          ("backplane", 4),
          ("container", 5),
          ("powerSupply", 6),
          ("fan", 7),
          ("sensor", 8),
          ("module", 9),
          ("port", 10),
          ("stack", 11),
          ("cpu", 12),
          ("energyObject", 13),
          ("battery", 14),
          ("storageDrive", 15))
    )

    if mibBuilder.loadTexts:
        description = "An enumerated value that provides an indication of the general hardware type of a particular physical entity. There are no restrictions as to the number of entPhysicalEntries of each entPhysicalClass, which must be instantiated by an agent. The enumeration 'other' is applicable if the physical entity class is known but does not match any of the supported values. The enumeration 'unknown' is applicable if the physical entity class is unknown to the agent. The enumeration 'chassis' is applicable if the physical entity class is an overall container for networking equipment. Any class of physical entity, except a stack, may be contained within a chassis; a chassis may only be contained within a stack. The enumeration 'backplane' is applicable if the physical entity class is some sort of device for aggregating and forwarding networking traffic, such as a shared backplane in a modular ethernet switch. Note that an agent may model a backplane as a single physical entity, which is actually implemented as multiple discrete physical components (within a chassis or stack). The enumeration 'container' is applicable if the physical entity class is capable of containing one or more removable physical entities, possibly of different types. For example, each (empty or full) slot in a chassis will be modeled as a container. Note that all removable physical entities should be modeled within a container entity, such as field-replaceable modules, fans, or power supplies. Note that all known containers should be modeled by the agent, including empty containers. The enumeration 'powerSupply' is applicable if the physical entity class is a power-supplying component. The enumeration 'fan' is applicable if the physical entity class is a fan or other heat-reduction component. The enumeration 'sensor' is applicable if the physical entity class is some sort of sensor, such as a temperature sensor within a router chassis. The enumeration 'module' is applicable if the physical entity class is some sort of self-contained sub-system. If the enumeration 'module' is removable, then it should be modeled within a container entity; otherwise, it should be modeled directly within another physical entity (e.g., a chassis or another module). The enumeration 'port' is applicable if the physical entity class is some sort of networking port, capable of receiving and/or transmitting networking traffic. The enumeration 'stack' is applicable if the physical entity class is some sort of super-container (possibly virtual) intended to group together multiple chassis entities. A stack may be realized by a 'virtual' cable, a real interconnect cable attached to multiple chassis, or multiple interconnect cables. A stack should not be modeled within any other physical entities, but a stack may be contained within another stack. Only chassis entities should be contained within a stack. The enumeration 'cpu' is applicable if the physical entity class is some sort of central processing unit. The enumeration 'energyObject' is applicable if the physical entity is some sort of energy object, i.e., a piece of equipment that is part of or attached to a communications network that is monitored, controlled, or aids in the management of another device for Energy Management. The enumeration 'battery' is applicable if the physical entity class is some sort of battery. The enumeration 'storageDrive' is applicable if the physical entity class is some sort of entity with data storage capability as main functionality, e.g. disk drive (HDD), solid state device (SSD), hybrid (SSHD), object storage (OSD) or other."


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-ENTITY-MIB",
    **{"IANAPhysicalClass": IANAPhysicalClass,
       "ianaEntityMIB": ianaEntityMIB}
)
