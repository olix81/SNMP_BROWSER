# SNMP MIB module (IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IF-MIB
# Produced by pysmi-2.0.0 at Sat Oct 17 14:25:43 2026
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
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
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ifMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 31)
)
if mibBuilder.loadTexts:
    ifMIB.setRevisions(
        ("2000-06-14 00:00",
         "1996-02-28 21:55",
         "1993-11-08 21:55")
    )
if mibBuilder.loadTexts:
    ifMIB.setLastUpdated("200006140000Z")
if mibBuilder.loadTexts:
    ifMIB.setOrganization("IETF Interfaces MIB Working Group")
if mibBuilder.loadTexts:
    ifMIB.setContactInfo(" Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 US 408-526-5260 kzm@cisco.com")
if mibBuilder.loadTexts:
    ifMIB.setDescription("The MIB module to describe generic objects for network interface sub-layers. This MIB is an updated version of MIB-II's ifTable, and incorporates the extensions defined in RFC 1229.")


# Types definitions


# TEXTUAL-CONVENTIONS



class OwnerString(TextualConvention, OctetString):
    status = "deprecated"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )

    if mibBuilder.loadTexts:
        description = "This data type is used to model an administratively assigned name of the owner of a resource. This information is taken from the NVT ASCII character set. It is suggested that this name contain one or more of the following: ASCII form of the manager station's transport address, management station name (e.g., domain name), network management personnel's name, location, or phone number. In some cases the agent itself will be the owner of an entry. In these cases, this string shall be set to a string starting with 'agent'."


class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."


class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = "This textual convention is an extension of the InterfaceIndex convention. The latter defines a greater than zero value used to identify an interface or interface sub-layer in the managed system. This extension permits the additional value of zero. the value zero is object-specific and must therefore be defined as part of the description of any object which uses this syntax. Examples of the usage of zero might include situations where interface was unknown, or when none or all interfaces need to be referenced."


# MIB Managed Objects in the order of their OIDs

_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2)
)
_IfNumber_Type = Integer32
_IfNumber_Object = MibScalar
ifNumber = _IfNumber_Object(
    (1, 3, 6, 1, 2, 1, 2, 1),
    _IfNumber_Type()
)
ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumber.setStatus("current")
if mibBuilder.loadTexts:
    ifNumber.setDescription("The number of network interfaces (regardless of their current state) present on this system.")
_IfTable_Object = MibTable
ifTable = _IfTable_Object(
    (1, 3, 6, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ifTable.setStatus("current")
if mibBuilder.loadTexts:
    ifTable.setDescription("A list of interface entries. The number of entries is given by the value of ifNumber.")
_IfEntry_Object = MibTableRow
ifEntry = _IfEntry_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1)
)
ifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifEntry.setStatus("current")
if mibBuilder.loadTexts:
    ifEntry.setDescription("An entry containing management information applicable to a particular interface.")
_IfIndex_Type = InterfaceIndex
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
if mibBuilder.loadTexts:
    ifIndex.setDescription("A unique value, greater than zero, for each interface. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re- initialization.")


class _IfDescr_Type(DisplayString):
    """Custom type ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfDescr_Type.__name__ = "DisplayString"
_IfDescr_Object = MibTableColumn
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("current")
if mibBuilder.loadTexts:
    ifDescr.setDescription("A textual string containing information about the interface. This string should include the name of the manufacturer, the product name and the version of the interface hardware/software.")
_IfType_Type = IANAifType
_IfType_Object = MibTableColumn
ifType = _IfType_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 3),
    _IfType_Type()
)
ifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifType.setStatus("current")
if mibBuilder.loadTexts:
    ifType.setDescription("The type of interface. Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention.")
_IfMtu_Type = Integer32
_IfMtu_Object = MibTableColumn
ifMtu = _IfMtu_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 4),
    _IfMtu_Type()
)
ifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMtu.setStatus("current")
if mibBuilder.loadTexts:
    ifMtu.setDescription("The size of the largest packet which can be sent/received on the interface, specified in octets. For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface.")
_IfSpeed_Type = Gauge32
_IfSpeed_Object = MibTableColumn
ifSpeed = _IfSpeed_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 5),
    _IfSpeed_Type()
)
ifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ifSpeed.setDescription("An estimate of the interface's current bandwidth in bits per second. For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed. For a sub-layer which has no concept of bandwidth, this object should be zero.")
_IfPhysAddress_Type = PhysAddress
_IfPhysAddress_Object = MibTableColumn
ifPhysAddress = _IfPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 6),
    _IfPhysAddress_Type()
)
ifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysAddress.setStatus("current")
if mibBuilder.loadTexts:
    ifPhysAddress.setDescription("The interface's address at its protocol sub-layer. For example, for an 802.x interface, this object normally contains a MAC address. The interface's media-specific MIB must define the bit and byte ordering and the format of the value of this object. For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length.")


class _IfAdminStatus_Type(Integer32):
    """Custom type ifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_IfAdminStatus_Type.__name__ = "Integer32"
_IfAdminStatus_Object = MibTableColumn
ifAdminStatus = _IfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 7),
    _IfAdminStatus_Type()
)
ifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    ifAdminStatus.setDescription("The desired state of the interface. The testing(3) state indicates that no operational packets can be passed. When a managed system initializes, all interfaces start with ifAdminStatus in the down(2) state. As a result of either explicit management action or per configuration information retained by the managed system, ifAdminStatus is then changed to either the up(1) or testing(3) states (or remains in the down(2) state).")


class _IfOperStatus_Type(Integer32):
    """Custom type ifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_IfOperStatus_Type.__name__ = "Integer32"
_IfOperStatus_Object = MibTableColumn
ifOperStatus = _IfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 8),
    _IfOperStatus_Type()
)
ifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOperStatus.setStatus("current")
if mibBuilder.loadTexts:
    ifOperStatus.setDescription("The current operational state of the interface. The testing(3) state indicates that no operational packets can be passed. If ifAdminStatus is down(2) then ifOperStatus should be down(2). If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic; it should change to dormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection); it should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state; it should remain in the notPresent(6) state if the interface has missing (typically, hardware) components.")
_IfLastChange_Type = TimeTicks
_IfLastChange_Object = MibTableColumn
ifLastChange = _IfLastChange_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 9),
    _IfLastChange_Type()
)
ifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLastChange.setStatus("current")
if mibBuilder.loadTexts:
    ifLastChange.setDescription("The value of sysUpTime at the time the interface entered its current operational state. If the current state was entered prior to the last re-initialization of the local network management subsystem, then this object contains a zero value.")
_IfInOctets_Type = Counter32
_IfInOctets_Object = MibTableColumn
ifInOctets = _IfInOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 10),
    _IfInOctets_Type()
)
ifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ifInOctets.setDescription("The total number of octets received on the interface, including framing characters. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfInUcastPkts_Type = Counter32
_IfInUcastPkts_Object = MibTableColumn
ifInUcastPkts = _IfInUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 11),
    _IfInUcastPkts_Type()
)
ifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifInUcastPkts.setDescription("The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were not addressed to a multicast or broadcast address at this sub-layer. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfInNUcastPkts_Type = Counter32
_IfInNUcastPkts_Object = MibTableColumn
ifInNUcastPkts = _IfInNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 12),
    _IfInNUcastPkts_Type()
)
ifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInNUcastPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifInNUcastPkts.setDescription("The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were addressed to a multicast or broadcast address at this sub-layer. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. This object is deprecated in favour of ifInMulticastPkts and ifInBroadcastPkts.")
_IfInDiscards_Type = Counter32
_IfInDiscards_Object = MibTableColumn
ifInDiscards = _IfInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 13),
    _IfInDiscards_Type()
)
ifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ifInDiscards.setDescription("The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfInErrors_Type = Counter32
_IfInErrors_Object = MibTableColumn
ifInErrors = _IfInErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 14),
    _IfInErrors_Type()
)
ifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInErrors.setStatus("current")
if mibBuilder.loadTexts:
    ifInErrors.setDescription("For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol. For character- oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfInUnknownProtos_Type = Counter32
_IfInUnknownProtos_Object = MibTableColumn
ifInUnknownProtos = _IfInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 15),
    _IfInUnknownProtos_Type()
)
ifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUnknownProtos.setStatus("current")
if mibBuilder.loadTexts:
    ifInUnknownProtos.setDescription("For packet-oriented interfaces, the number of packets received via the interface which were discarded because of an unknown or unsupported protocol. For character-oriented or fixed-length interfaces that support protocol multiplexing the number of transmission units received via the interface which were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter will always be 0. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfOutOctets_Type = Counter32
_IfOutOctets_Object = MibTableColumn
ifOutOctets = _IfOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 16),
    _IfOutOctets_Type()
)
ifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ifOutOctets.setDescription("The total number of octets transmitted out of the interface, including framing characters. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfOutUcastPkts_Type = Counter32
_IfOutUcastPkts_Object = MibTableColumn
ifOutUcastPkts = _IfOutUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 17),
    _IfOutUcastPkts_Type()
)
ifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifOutUcastPkts.setDescription("The total number of packets that higher-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfOutNUcastPkts_Type = Counter32
_IfOutNUcastPkts_Object = MibTableColumn
ifOutNUcastPkts = _IfOutNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 18),
    _IfOutNUcastPkts_Type()
)
ifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutNUcastPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifOutNUcastPkts.setDescription("The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. This object is deprecated in favour of ifOutMulticastPkts and ifOutBroadcastPkts.")
_IfOutDiscards_Type = Counter32
_IfOutDiscards_Object = MibTableColumn
ifOutDiscards = _IfOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 19),
    _IfOutDiscards_Type()
)
ifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ifOutDiscards.setDescription("The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfOutErrors_Type = Counter32
_IfOutErrors_Object = MibTableColumn
ifOutErrors = _IfOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 20),
    _IfOutErrors_Type()
)
ifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    ifOutErrors.setDescription("For packet-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character-oriented or fixed-length interfaces, the number of outbound transmission units that could not be transmitted because of errors. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfOutQLen_Type = Gauge32
_IfOutQLen_Object = MibTableColumn
ifOutQLen = _IfOutQLen_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 21),
    _IfOutQLen_Type()
)
ifOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutQLen.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifOutQLen.setDescription("The length of the output packet queue (in packets).")
_IfSpecific_Type = ObjectIdentifier
_IfSpecific_Object = MibTableColumn
ifSpecific = _IfSpecific_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 22),
    _IfSpecific_Type()
)
ifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpecific.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifSpecific.setDescription("A reference to MIB definitions specific to the particular media being used to realize the interface. It is recommended that this value point to an instance of a MIB object in the media-specific MIB, i.e., that this object have the semantics associated with the InstancePointer textual convention defined in RFC 2579. In fact, it is recommended that the media-specific MIB specify what value ifSpecific should/can take for values of ifType. If no MIB definitions specific to the particular media are available, the value should be set to the OBJECT IDENTIFIER { 0 0 }.")
_IfMIBObjects_ObjectIdentity = ObjectIdentity
ifMIBObjects = _IfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31, 1)
)
_IfXTable_Object = MibTable
ifXTable = _IfXTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1)
)
if mibBuilder.loadTexts:
    ifXTable.setStatus("current")
if mibBuilder.loadTexts:
    ifXTable.setDescription("A list of interface entries. The number of entries is given by the value of ifNumber. This table contains additional objects for the interface table.")
_IfXEntry_Object = MibTableRow
ifXEntry = _IfXEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ifXEntry.setStatus("current")
if mibBuilder.loadTexts:
    ifXEntry.setDescription("An entry containing additional management information applicable to a particular interface.")
_IfName_Type = DisplayString
_IfName_Object = MibTableColumn
ifName = _IfName_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 1),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("current")
if mibBuilder.loadTexts:
    ifName.setDescription("The textual name of the interface. The value of this object should be the name of the interface as assigned by the local device and should be suitable for use in commands entered at the device's `console'. This might be a text name, such as `le0' or a simple port number, such as `1', depending on the interface naming syntax of the device. If several entries in the ifTable together represent a single interface as named by the device, then each will have the same value of ifName. Note that for an agent which responds to SNMP queries concerning an interface on some other (proxied) device, then the value of ifName for such an interface is the proxied device's local name for it. If there is no local name, or this object is otherwise not applicable, then this object contains a zero-length string.")
_IfInMulticastPkts_Type = Counter32
_IfInMulticastPkts_Object = MibTableColumn
ifInMulticastPkts = _IfInMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 2),
    _IfInMulticastPkts_Type()
)
ifInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifInMulticastPkts.setDescription("The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were addressed to a multicast address at this sub-layer. For a MAC layer protocol, this includes both Group and Functional addresses. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfInBroadcastPkts_Type = Counter32
_IfInBroadcastPkts_Object = MibTableColumn
ifInBroadcastPkts = _IfInBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 3),
    _IfInBroadcastPkts_Type()
)
ifInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifInBroadcastPkts.setDescription("The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were addressed to a broadcast address at this sub-layer. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfOutMulticastPkts_Type = Counter32
_IfOutMulticastPkts_Object = MibTableColumn
ifOutMulticastPkts = _IfOutMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 4),
    _IfOutMulticastPkts_Type()
)
ifOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifOutMulticastPkts.setDescription("The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a multicast address at this sub-layer, including those that were discarded or not sent. For a MAC layer protocol, this includes both Group and Functional addresses. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfOutBroadcastPkts_Type = Counter32
_IfOutBroadcastPkts_Object = MibTableColumn
ifOutBroadcastPkts = _IfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 5),
    _IfOutBroadcastPkts_Type()
)
ifOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifOutBroadcastPkts.setDescription("The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub-layer, including those that were discarded or not sent. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCInOctets_Type = Counter64
_IfHCInOctets_Object = MibTableColumn
ifHCInOctets = _IfHCInOctets_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 6),
    _IfHCInOctets_Type()
)
ifHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ifHCInOctets.setDescription("The total number of octets received on the interface, including framing characters. This object is a 64-bit version of ifInOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCInUcastPkts_Type = Counter64
_IfHCInUcastPkts_Object = MibTableColumn
ifHCInUcastPkts = _IfHCInUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 7),
    _IfHCInUcastPkts_Type()
)
ifHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifHCInUcastPkts.setDescription("The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were not addressed to a multicast or broadcast address at this sub-layer. This object is a 64-bit version of ifInUcastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCInMulticastPkts_Type = Counter64
_IfHCInMulticastPkts_Object = MibTableColumn
ifHCInMulticastPkts = _IfHCInMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 8),
    _IfHCInMulticastPkts_Type()
)
ifHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifHCInMulticastPkts.setDescription("The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were addressed to a multicast address at this sub-layer. For a MAC layer protocol, this includes both Group and Functional addresses. This object is a 64-bit version of ifInMulticastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCInBroadcastPkts_Type = Counter64
_IfHCInBroadcastPkts_Object = MibTableColumn
ifHCInBroadcastPkts = _IfHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 9),
    _IfHCInBroadcastPkts_Type()
)
ifHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifHCInBroadcastPkts.setDescription("The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were addressed to a broadcast address at this sub-layer. This object is a 64-bit version of ifInBroadcastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCOutOctets_Type = Counter64
_IfHCOutOctets_Object = MibTableColumn
ifHCOutOctets = _IfHCOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 10),
    _IfHCOutOctets_Type()
)
ifHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ifHCOutOctets.setDescription("The total number of octets transmitted out of the interface, including framing characters. This object is a 64-bit version of ifOutOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCOutUcastPkts_Type = Counter64
_IfHCOutUcastPkts_Object = MibTableColumn
ifHCOutUcastPkts = _IfHCOutUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 11),
    _IfHCOutUcastPkts_Type()
)
ifHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifHCOutUcastPkts.setDescription("The total number of packets that higher-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent. This object is a 64-bit version of ifOutUcastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCOutMulticastPkts_Type = Counter64
_IfHCOutMulticastPkts_Object = MibTableColumn
ifHCOutMulticastPkts = _IfHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 12),
    _IfHCOutMulticastPkts_Type()
)
ifHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifHCOutMulticastPkts.setDescription("The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a multicast address at this sub-layer, including those that were discarded or not sent. For a MAC layer protocol, this includes both Group and Functional addresses. This object is a 64-bit version of ifOutMulticastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")
_IfHCOutBroadcastPkts_Type = Counter64
_IfHCOutBroadcastPkts_Object = MibTableColumn
ifHCOutBroadcastPkts = _IfHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 13),
    _IfHCOutBroadcastPkts_Type()
)
ifHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ifHCOutBroadcastPkts.setDescription("The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub-layer, including those that were discarded or not sent. This object is a 64-bit version of ifOutBroadcastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.")


class _IfLinkUpDownTrapEnable_Type(Integer32):
    """Custom type ifLinkUpDownTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IfLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_IfLinkUpDownTrapEnable_Object = MibTableColumn
ifLinkUpDownTrapEnable = _IfLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 14),
    _IfLinkUpDownTrapEnable_Type()
)
ifLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkUpDownTrapEnable.setStatus("current")
if mibBuilder.loadTexts:
    ifLinkUpDownTrapEnable.setDescription("Indicates whether linkUp/linkDown traps should be generated for this interface. By default, this object should have the value enabled(1) for interfaces which do not operate on 'top' of any other interface (as defined in the ifStackTable), and disabled(2) otherwise.")
_IfHighSpeed_Type = Gauge32
_IfHighSpeed_Object = MibTableColumn
ifHighSpeed = _IfHighSpeed_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 15),
    _IfHighSpeed_Type()
)
ifHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ifHighSpeed.setDescription("An estimate of the interface's current bandwidth in units of 1,000,000 bits per second. If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to `n+499,999'. For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. For a sub-layer which has no concept of bandwidth, this object should be zero.")
_IfPromiscuousMode_Type = TruthValue
_IfPromiscuousMode_Object = MibTableColumn
ifPromiscuousMode = _IfPromiscuousMode_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 16),
    _IfPromiscuousMode_Type()
)
ifPromiscuousMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPromiscuousMode.setStatus("current")
if mibBuilder.loadTexts:
    ifPromiscuousMode.setDescription("This object has a value of false(2) if this interface only accepts packets/frames that are addressed to this station. This object has a value of true(1) when the station accepts all packets/frames transmitted on the media. The value true(1) is only legal on certain types of media. If legal, setting this object to a value of true(1) may require the interface to be reset before becoming effective. The value of ifPromiscuousMode does not affect the reception of broadcast and multicast packets/frames by the interface.")
_IfConnectorPresent_Type = TruthValue
_IfConnectorPresent_Object = MibTableColumn
ifConnectorPresent = _IfConnectorPresent_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 17),
    _IfConnectorPresent_Type()
)
ifConnectorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConnectorPresent.setStatus("current")
if mibBuilder.loadTexts:
    ifConnectorPresent.setDescription("This object has the value 'true(1)' if the interface sublayer has a physical connector and the value 'false(2)' otherwise.")


class _IfAlias_Type(DisplayString):
    """Custom type ifAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfAlias_Type.__name__ = "DisplayString"
_IfAlias_Object = MibTableColumn
ifAlias = _IfAlias_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 18),
    _IfAlias_Type()
)
ifAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAlias.setStatus("current")
if mibBuilder.loadTexts:
    ifAlias.setDescription("This object is an 'alias' name for the interface as specified by a network manager, and provides a non-volatile 'handle' for the interface. On the first instantiation of an interface, the value of ifAlias associated with that interface is the zero-length string. As and when a value is written into an instance of ifAlias through a network management set operation, then the agent must retain the supplied value in the ifAlias instance associated with the same interface for as long as that interface remains instantiated, including across all re- initializations/reboots of the network management system, including those which result in a change of the interface's ifIndex value. An example of the value which a network manager might store in this object for a WAN interface is the (Telco's) circuit number/identifier of the interface. Some agents may support write-access only for interfaces having particular values of ifType. An agent which supports write access to this object is required to keep the value in non-volatile storage, but it may limit the length of new values depending on how much storage is already occupied by the current values for other interfaces.")
_IfCounterDiscontinuityTime_Type = TimeStamp
_IfCounterDiscontinuityTime_Object = MibTableColumn
ifCounterDiscontinuityTime = _IfCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 19),
    _IfCounterDiscontinuityTime_Type()
)
ifCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCounterDiscontinuityTime.setStatus("current")
if mibBuilder.loadTexts:
    ifCounterDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity. The relevant counters are the specific instances associated with this interface of any Counter32 or Counter64 object contained in the ifTable or ifXTable. If no such discontinuities have occurred since the last re- initialization of the local management subsystem, then this object contains a zero value.")
_IfStackTable_Object = MibTable
ifStackTable = _IfStackTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2)
)
if mibBuilder.loadTexts:
    ifStackTable.setStatus("current")
if mibBuilder.loadTexts:
    ifStackTable.setDescription("The table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub-layers run 'on top of' which other sub-layers, where each sub-layer corresponds to a conceptual row in the ifTable. For example, when the sub-layer with ifIndex value x runs over the sub-layer with ifIndex value y, then this table contains: ifStackStatus.x.y=active For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I. For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer. (If I is not involved in multiplexing, then these are the only two rows associated with I.) For example, two rows exist even for an interface which has no others stacked on top or below it: ifStackStatus.0.x=active ifStackStatus.x.0=active ")
_IfStackEntry_Object = MibTableRow
ifStackEntry = _IfStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1)
)
ifStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackHigherLayer"),
    (0, "IF-MIB", "ifStackLowerLayer"),
)
if mibBuilder.loadTexts:
    ifStackEntry.setStatus("current")
if mibBuilder.loadTexts:
    ifStackEntry.setDescription("Information on a particular relationship between two sub- layers, specifying that one sub-layer runs on 'top' of the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable.")
_IfStackHigherLayer_Type = InterfaceIndexOrZero
_IfStackHigherLayer_Object = MibTableColumn
ifStackHigherLayer = _IfStackHigherLayer_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 1),
    _IfStackHigherLayer_Type()
)
ifStackHigherLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifStackHigherLayer.setStatus("current")
if mibBuilder.loadTexts:
    ifStackHigherLayer.setDescription("The value of ifIndex corresponding to the higher sub-layer of the relationship, i.e., the sub-layer which runs on 'top' of the sub-layer identified by the corresponding instance of ifStackLowerLayer. If there is no higher sub-layer (below the internetwork layer), then this object has the value 0.")
_IfStackLowerLayer_Type = InterfaceIndexOrZero
_IfStackLowerLayer_Object = MibTableColumn
ifStackLowerLayer = _IfStackLowerLayer_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 2),
    _IfStackLowerLayer_Type()
)
ifStackLowerLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifStackLowerLayer.setStatus("current")
if mibBuilder.loadTexts:
    ifStackLowerLayer.setDescription("The value of ifIndex corresponding to the lower sub-layer of the relationship, i.e., the sub-layer which runs 'below' the sub-layer identified by the corresponding instance of ifStackHigherLayer. If there is no lower sub-layer, then this object has the value 0.")
_IfStackStatus_Type = RowStatus
_IfStackStatus_Object = MibTableColumn
ifStackStatus = _IfStackStatus_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 3),
    _IfStackStatus_Type()
)
ifStackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifStackStatus.setStatus("current")
if mibBuilder.loadTexts:
    ifStackStatus.setDescription("The status of the relationship between two sub-layers. Changing the value of this object from 'active' to 'notInService' or 'destroy' will likely have consequences up and down the interface stack. Thus, write access to this object is likely to be inappropriate for some types of interfaces, and many implementations will choose not to support write-access for any type of interface.")
_IfTestTable_Object = MibTable
ifTestTable = _IfTestTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3)
)
if mibBuilder.loadTexts:
    ifTestTable.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestTable.setDescription("This table contains one entry per interface. It defines objects which allow a network manager to instruct an agent to test an interface for various faults. Tests for an interface are defined in the media-specific MIB for that interface. After invoking a test, the object ifTestResult can be read to determine the outcome. If an agent can not perform the test, ifTestResult is set to so indicate. The object ifTestCode can be used to provide further test- specific or interface-specific (or even enterprise-specific) information concerning the outcome of the test. Only one test can be in progress on each interface at any one time. If one test is in progress when another test is invoked, the second test is rejected. Some agents may reject a test when a prior test is active on another interface. Before starting a test, a manager-station must first obtain 'ownership' of the entry in the ifTestTable for the interface to be tested. This is accomplished with the ifTestId and ifTestStatus objects as follows: try_again: get (ifTestId, ifTestStatus) while (ifTestStatus != notInUse) /* * Loop while a test is running or some other * manager is configuring a test. */ short delay get (ifTestId, ifTestStatus) } /* * Is not being used right now -- let's compete * to see who gets it. */ lock_value = ifTestId if ( set(ifTestId = lock_value, ifTestStatus = inUse, ifTestOwner = 'my-IP-address') == FAILURE) /* * Another manager got the ifTestEntry -- go * try again */ goto try_again; /* * I have the lock */ set up any test parameters. /* * This starts the test */ set(ifTestType = test_to_run); wait for test completion by polling ifTestResult when test completes, agent sets ifTestResult agent also sets ifTestStatus = 'notInUse' retrieve any additional test results, and ifTestId if (ifTestId == lock_value+1) results are valid A manager station first retrieves the value of the appropriate ifTestId and ifTestStatus objects, periodically repeating the retrieval if necessary, until the value of ifTestStatus is 'notInUse'. The manager station then tries to set the same ifTestId object to the value it just retrieved, the same ifTestStatus object to 'inUse', and the corresponding ifTestOwner object to a value indicating itself. If the set operation succeeds then the manager has obtained ownership of the ifTestEntry, and the value of the ifTestId object is incremented by the agent (per the semantics of TestAndIncr). Failure of the set operation indicates that some other manager has obtained ownership of the ifTestEntry. Once ownership is obtained, any test parameters can be setup, and then the test is initiated by setting ifTestType. On completion of the test, the agent sets ifTestStatus to 'notInUse'. Once this occurs, the manager can retrieve the results. In the (rare) event that the invocation of tests by two network managers were to overlap, then there would be a possibility that the first test's results might be overwritten by the second test's results prior to the first results being read. This unlikely circumstance can be detected by a network manager retrieving ifTestId at the same time as retrieving the test results, and ensuring that the results are for the desired request. If ifTestType is not set within an abnormally long period of time after ownership is obtained, the agent should time-out the manager, and reset the value of the ifTestStatus object back to 'notInUse'. It is suggested that this time-out period be 5 minutes. In general, a management station must not retransmit a request to invoke a test for which it does not receive a response; instead, it properly inspects an agent's MIB to determine if the invocation was successful. Only if the invocation was unsuccessful, is the invocation request retransmitted. Some tests may require the interface to be taken off-line in order to execute them, or may even require the agent to reboot after completion of the test. In these circumstances, communication with the management station invoking the test may be lost until after completion of the test. An agent is not required to support such tests. However, if such tests are supported, then the agent should make every effort to transmit a response to the request which invoked the test prior to losing communication. When the agent is restored to normal service, the results of the test are properly made available in the appropriate objects. Note that this requires that the ifIndex value assigned to an interface must be unchanged even if the test causes a reboot. An agent must reject any test for which it cannot, perhaps due to resource constraints, make available at least the minimum amount of information after that test completes.")
_IfTestEntry_Object = MibTableRow
ifTestEntry = _IfTestEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ifTestEntry.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestEntry.setDescription("An entry containing objects for invoking tests on an interface.")
_IfTestId_Type = TestAndIncr
_IfTestId_Object = MibTableColumn
ifTestId = _IfTestId_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 1),
    _IfTestId_Type()
)
ifTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestId.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestId.setDescription("This object identifies the current invocation of the interface's test.")


class _IfTestStatus_Type(Integer32):
    """Custom type ifTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInUse", 1),
          ("inUse", 2))
    )


_IfTestStatus_Type.__name__ = "Integer32"
_IfTestStatus_Object = MibTableColumn
ifTestStatus = _IfTestStatus_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 2),
    _IfTestStatus_Type()
)
ifTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestStatus.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestStatus.setDescription("This object indicates whether or not some manager currently has the necessary 'ownership' required to invoke a test on this interface. A write to this object is only successful when it changes its value from 'notInUse(1)' to 'inUse(2)'. After completion of a test, the agent resets the value back to 'notInUse(1)'.")
_IfTestType_Type = AutonomousType
_IfTestType_Object = MibTableColumn
ifTestType = _IfTestType_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 3),
    _IfTestType_Type()
)
ifTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestType.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestType.setDescription("A control variable used to start and stop operator- initiated interface tests. Most OBJECT IDENTIFIER values assigned to tests are defined elsewhere, in association with specific types of interface. However, this document assigns a value for a full-duplex loopback test, and defines the special meanings of the subject identifier: noTest OBJECT IDENTIFIER ::= { 0 0 } When the value noTest is written to this object, no action is taken unless a test is in progress, in which case the test is aborted. Writing any other value to this object is only valid when no test is currently in progress, in which case the indicated test is initiated. When read, this object always returns the most recent value that ifTestType was set to. If it has not been set since the last initialization of the network management subsystem on the agent, a value of noTest is returned.")


class _IfTestResult_Type(Integer32):
    """Custom type ifTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("inProgress", 3),
          ("notSupported", 4),
          ("unAbleToRun", 5),
          ("aborted", 6),
          ("failed", 7))
    )


_IfTestResult_Type.__name__ = "Integer32"
_IfTestResult_Object = MibTableColumn
ifTestResult = _IfTestResult_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 4),
    _IfTestResult_Type()
)
ifTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTestResult.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestResult.setDescription("This object contains the result of the most recently requested test, or the value none(1) if no tests have been requested since the last reset. Note that this facility provides no provision for saving the results of one test when starting another, as could be required if used by multiple managers concurrently.")
_IfTestCode_Type = ObjectIdentifier
_IfTestCode_Object = MibTableColumn
ifTestCode = _IfTestCode_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 5),
    _IfTestCode_Type()
)
ifTestCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTestCode.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestCode.setDescription("This object contains a code which contains more specific information on the test result, for example an error-code after a failed test. Error codes and other values this object may take are specific to the type of interface and/or test. The value may have the semantics of either the AutonomousType or InstancePointer textual conventions as defined in RFC 2579. The identifier: testCodeUnknown OBJECT IDENTIFIER ::= { 0 0 } is defined for use if no additional result code is available.")
_IfTestOwner_Type = OwnerString
_IfTestOwner_Object = MibTableColumn
ifTestOwner = _IfTestOwner_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 6),
    _IfTestOwner_Type()
)
ifTestOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestOwner.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestOwner.setDescription("The entity which currently has the 'ownership' required to invoke a test on this interface.")
_IfRcvAddressTable_Object = MibTable
ifRcvAddressTable = _IfRcvAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4)
)
if mibBuilder.loadTexts:
    ifRcvAddressTable.setStatus("current")
if mibBuilder.loadTexts:
    ifRcvAddressTable.setDescription("This table contains an entry for each address (broadcast, multicast, or uni-cast) for which the system will receive packets/frames on a particular interface, except as follows: - for an interface operating in promiscuous mode, entries are only required for those addresses for which the system would receive frames were it not operating in promiscuous mode. - for 802.5 functional addresses, only one entry is required, for the address which has the functional address bit ANDed with the bit mask of all functional addresses for which the interface will accept frames. A system is normally able to use any unicast address which corresponds to an entry in this table as a source address.")
_IfRcvAddressEntry_Object = MibTableRow
ifRcvAddressEntry = _IfRcvAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1)
)
ifRcvAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IF-MIB", "ifRcvAddressAddress"),
)
if mibBuilder.loadTexts:
    ifRcvAddressEntry.setStatus("current")
if mibBuilder.loadTexts:
    ifRcvAddressEntry.setDescription("A list of objects identifying an address for which the system will accept packets/frames on the particular interface identified by the index value ifIndex.")
_IfRcvAddressAddress_Type = PhysAddress
_IfRcvAddressAddress_Object = MibTableColumn
ifRcvAddressAddress = _IfRcvAddressAddress_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 1),
    _IfRcvAddressAddress_Type()
)
ifRcvAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifRcvAddressAddress.setStatus("current")
if mibBuilder.loadTexts:
    ifRcvAddressAddress.setDescription("An address for which the system will accept packets/frames on this entry's interface.")
_IfRcvAddressStatus_Type = RowStatus
_IfRcvAddressStatus_Object = MibTableColumn
ifRcvAddressStatus = _IfRcvAddressStatus_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 2),
    _IfRcvAddressStatus_Type()
)
ifRcvAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifRcvAddressStatus.setStatus("current")
if mibBuilder.loadTexts:
    ifRcvAddressStatus.setDescription("This object is used to create and delete rows in the ifRcvAddressTable.")


class _IfRcvAddressType_Type(Integer32):
    """Custom type ifRcvAddressType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("volatile", 2),
          ("nonVolatile", 3))
    )


_IfRcvAddressType_Type.__name__ = "Integer32"
_IfRcvAddressType_Object = MibTableColumn
ifRcvAddressType = _IfRcvAddressType_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 3),
    _IfRcvAddressType_Type()
)
ifRcvAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifRcvAddressType.setStatus("current")
if mibBuilder.loadTexts:
    ifRcvAddressType.setDescription("This object has the value nonVolatile(3) for those entries in the table which are valid and will not be deleted by the next restart of the managed system. Entries having the value volatile(2) are valid and exist, but have not been saved, so that will not exist after the next restart of the managed system. Entries having the value other(1) are valid and exist but are not classified as to whether they will continue to exist after the next restart.")
_IfTableLastChange_Type = TimeTicks
_IfTableLastChange_Object = MibScalar
ifTableLastChange = _IfTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 5),
    _IfTableLastChange_Type()
)
ifTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableLastChange.setStatus("current")
if mibBuilder.loadTexts:
    ifTableLastChange.setDescription("The value of sysUpTime at the time of the last creation or deletion of an entry in the ifTable. If the number of entries has been unchanged since the last re-initialization of the local network management subsystem, then this object contains a zero value.")
_IfStackLastChange_Type = TimeTicks
_IfStackLastChange_Object = MibScalar
ifStackLastChange = _IfStackLastChange_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 6),
    _IfStackLastChange_Type()
)
ifStackLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStackLastChange.setStatus("current")
if mibBuilder.loadTexts:
    ifStackLastChange.setDescription("The value of sysUpTime at the time of the last change of the (whole) interface stack. A change of the interface stack is defined to be any creation, deletion, or change in value of any instance of ifStackStatus. If the interface stack has been unchanged since the last re-initialization of the local network management subsystem, then this object contains a zero value.")
_IfConformance_ObjectIdentity = ObjectIdentity
ifConformance = _IfConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31, 2)
)
_IfGroups_ObjectIdentity = ObjectIdentity
ifGroups = _IfGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31, 2, 1)
)
_IfCompliances_ObjectIdentity = ObjectIdentity
ifCompliances = _IfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31, 2, 2)
)
ifEntry.registerAugmentions(
    ("IF-MIB",
     "ifXEntry")
)
ifXEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("IF-MIB",
     "ifTestEntry")
)
ifTestEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

ifGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 1)
)
ifGeneralGroup.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifSpeed"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifLastChange"),
        ("IF-MIB", "ifLinkUpDownTrapEnable"),
        ("IF-MIB", "ifConnectorPresent"),
        ("IF-MIB", "ifHighSpeed"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    ifGeneralGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifGeneralGroup.setDescription("A collection of objects deprecated in favour of ifGeneralInformationGroup.")

ifFixedLengthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 2)
)
ifFixedLengthGroup.setObjects(
      *(("IF-MIB", "ifInOctets"),
        ("IF-MIB", "ifOutOctets"),
        ("IF-MIB", "ifInUnknownProtos"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    ifFixedLengthGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifFixedLengthGroup.setDescription("A collection of objects providing information specific to non-high speed (non-high speed interfaces transmit and receive at speeds less than or equal to 20,000,000 bits/second) character-oriented or fixed-length-transmission network interfaces.")

ifHCFixedLengthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 3)
)
ifHCFixedLengthGroup.setObjects(
      *(("IF-MIB", "ifHCInOctets"),
        ("IF-MIB", "ifHCOutOctets"),
        ("IF-MIB", "ifInOctets"),
        ("IF-MIB", "ifOutOctets"),
        ("IF-MIB", "ifInUnknownProtos"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"))
)
if mibBuilder.loadTexts:
    ifHCFixedLengthGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifHCFixedLengthGroup.setDescription("A collection of objects providing information specific to high speed (greater than 20,000,000 bits/second) character- oriented or fixed-length-transmission network interfaces.")

ifPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 4)
)
ifPacketGroup.setObjects(
      *(("IF-MIB", "ifInOctets"),
        ("IF-MIB", "ifOutOctets"),
        ("IF-MIB", "ifInUnknownProtos"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"),
        ("IF-MIB", "ifMtu"),
        ("IF-MIB", "ifInUcastPkts"),
        ("IF-MIB", "ifInMulticastPkts"),
        ("IF-MIB", "ifInBroadcastPkts"),
        ("IF-MIB", "ifInDiscards"),
        ("IF-MIB", "ifOutUcastPkts"),
        ("IF-MIB", "ifOutMulticastPkts"),
        ("IF-MIB", "ifOutBroadcastPkts"),
        ("IF-MIB", "ifOutDiscards"),
        ("IF-MIB", "ifPromiscuousMode"))
)
if mibBuilder.loadTexts:
    ifPacketGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifPacketGroup.setDescription("A collection of objects providing information specific to non-high speed (non-high speed interfaces transmit and receive at speeds less than or equal to 20,000,000 bits/second) packet-oriented network interfaces.")

ifHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 5)
)
ifHCPacketGroup.setObjects(
      *(("IF-MIB", "ifHCInOctets"),
        ("IF-MIB", "ifHCOutOctets"),
        ("IF-MIB", "ifInOctets"),
        ("IF-MIB", "ifOutOctets"),
        ("IF-MIB", "ifInUnknownProtos"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"),
        ("IF-MIB", "ifMtu"),
        ("IF-MIB", "ifInUcastPkts"),
        ("IF-MIB", "ifInMulticastPkts"),
        ("IF-MIB", "ifInBroadcastPkts"),
        ("IF-MIB", "ifInDiscards"),
        ("IF-MIB", "ifOutUcastPkts"),
        ("IF-MIB", "ifOutMulticastPkts"),
        ("IF-MIB", "ifOutBroadcastPkts"),
        ("IF-MIB", "ifOutDiscards"),
        ("IF-MIB", "ifPromiscuousMode"))
)
if mibBuilder.loadTexts:
    ifHCPacketGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifHCPacketGroup.setDescription("A collection of objects providing information specific to high speed (greater than 20,000,000 bits/second but less than or equal to 650,000,000 bits/second) packet-oriented network interfaces.")

ifVHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 6)
)
ifVHCPacketGroup.setObjects(
      *(("IF-MIB", "ifHCInUcastPkts"),
        ("IF-MIB", "ifHCInMulticastPkts"),
        ("IF-MIB", "ifHCInBroadcastPkts"),
        ("IF-MIB", "ifHCOutUcastPkts"),
        ("IF-MIB", "ifHCOutMulticastPkts"),
        ("IF-MIB", "ifHCOutBroadcastPkts"),
        ("IF-MIB", "ifHCInOctets"),
        ("IF-MIB", "ifHCOutOctets"),
        ("IF-MIB", "ifInOctets"),
        ("IF-MIB", "ifOutOctets"),
        ("IF-MIB", "ifInUnknownProtos"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"),
        ("IF-MIB", "ifMtu"),
        ("IF-MIB", "ifInUcastPkts"),
        ("IF-MIB", "ifInMulticastPkts"),
        ("IF-MIB", "ifInBroadcastPkts"),
        ("IF-MIB", "ifInDiscards"),
        ("IF-MIB", "ifOutUcastPkts"),
        ("IF-MIB", "ifOutMulticastPkts"),
        ("IF-MIB", "ifOutBroadcastPkts"),
        ("IF-MIB", "ifOutDiscards"),
        ("IF-MIB", "ifPromiscuousMode"))
)
if mibBuilder.loadTexts:
    ifVHCPacketGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifVHCPacketGroup.setDescription("A collection of objects providing information specific to higher speed (greater than 650,000,000 bits/second) packet- oriented network interfaces.")

ifRcvAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 7)
)
ifRcvAddressGroup.setObjects(
      *(("IF-MIB", "ifRcvAddressStatus"),
        ("IF-MIB", "ifRcvAddressType"))
)
if mibBuilder.loadTexts:
    ifRcvAddressGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifRcvAddressGroup.setDescription("A collection of objects providing information on the multiple addresses which an interface receives.")

ifTestGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 8)
)
ifTestGroup.setObjects(
      *(("IF-MIB", "ifTestId"),
        ("IF-MIB", "ifTestStatus"),
        ("IF-MIB", "ifTestType"),
        ("IF-MIB", "ifTestResult"),
        ("IF-MIB", "ifTestCode"),
        ("IF-MIB", "ifTestOwner"))
)
if mibBuilder.loadTexts:
    ifTestGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifTestGroup.setDescription("A collection of objects providing the ability to invoke tests on an interface.")

ifStackGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 9)
)
ifStackGroup.setObjects(
    ("IF-MIB", "ifStackStatus")
)
if mibBuilder.loadTexts:
    ifStackGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifStackGroup.setDescription("The previous collection of objects providing information on the layering of MIB-II interfaces.")

ifGeneralInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 10)
)
ifGeneralInformationGroup.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifSpeed"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifLastChange"),
        ("IF-MIB", "ifLinkUpDownTrapEnable"),
        ("IF-MIB", "ifConnectorPresent"),
        ("IF-MIB", "ifHighSpeed"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifNumber"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifTableLastChange"))
)
if mibBuilder.loadTexts:
    ifGeneralInformationGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifGeneralInformationGroup.setDescription("A collection of objects providing information applicable to all network interfaces.")

ifStackGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 11)
)
ifStackGroup2.setObjects(
      *(("IF-MIB", "ifStackStatus"),
        ("IF-MIB", "ifStackLastChange"))
)
if mibBuilder.loadTexts:
    ifStackGroup2.setStatus("current")
if mibBuilder.loadTexts:
    ifStackGroup2.setDescription("A collection of objects providing information on the layering of MIB-II interfaces.")

ifOldObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 12)
)
ifOldObjectsGroup.setObjects(
      *(("IF-MIB", "ifInNUcastPkts"),
        ("IF-MIB", "ifOutNUcastPkts"),
        ("IF-MIB", "ifOutQLen"),
        ("IF-MIB", "ifSpecific"))
)
if mibBuilder.loadTexts:
    ifOldObjectsGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    ifOldObjectsGroup.setDescription("The collection of objects deprecated from the original MIB- II interfaces group.")

ifCounterDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 13)
)
ifCounterDiscontinuityGroup.setObjects(
    ("IF-MIB", "ifCounterDiscontinuityTime")
)
if mibBuilder.loadTexts:
    ifCounterDiscontinuityGroup.setStatus("current")
if mibBuilder.loadTexts:
    ifCounterDiscontinuityGroup.setDescription("A collection of objects providing information specific to interface counter discontinuities.")


# Notification objects

linkDown = NotificationType(
    (1, 3, 6, 1, 6, 3, 1, 1, 5, 3)
)
linkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    linkDown.setDescription("A linkDown trap signifies that the SNMP entity, acting in an agent role, has detected that the ifOperStatus object for one of its communication links is about to enter the down state from some other state (but not from the notPresent state). This other state is indicated by the included value of ifOperStatus.")

linkUp = NotificationType(
    (1, 3, 6, 1, 6, 3, 1, 1, 5, 4)
)
linkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    linkUp.setDescription("A linkUp trap signifies that the SNMP entity, acting in an agent role, has detected that the ifOperStatus object for one of its communication links left the down state and transitioned into some other state (but not into the notPresent state). This other state is indicated by the included value of ifOperStatus.")


# Notifications groups

linkUpDownNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 14)
)
linkUpDownNotificationsGroup.setObjects(
      *(("IF-MIB", "linkUp"),
        ("IF-MIB", "linkDown"))
)
if mibBuilder.loadTexts:
    linkUpDownNotificationsGroup.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    linkUpDownNotificationsGroup.setDescription("The notifications which indicate specific changes in the value of ifOperStatus.")


# Agent capabilities


# Module compliance

ifCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 31, 2, 2, 1)
)
ifCompliance.setObjects(
      *(("IF-MIB", "ifGeneralGroup"),
        ("IF-MIB", "ifStackGroup"),
        ("IF-MIB", "ifFixedLengthGroup"),
        ("IF-MIB", "ifHCFixedLengthGroup"),
        ("IF-MIB", "ifPacketGroup"),
        ("IF-MIB", "ifHCPacketGroup"),
        ("IF-MIB", "ifTestGroup"),
        ("IF-MIB", "ifRcvAddressGroup"))
)
if mibBuilder.loadTexts:
    ifCompliance.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    ifCompliance.setDescription("A compliance statement defined in a previous version of this MIB module, for SNMP entities which have network interfaces.")

ifCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 31, 2, 2, 2)
)
ifCompliance2.setObjects(
      *(("IF-MIB", "ifGeneralInformationGroup"),
        ("IF-MIB", "ifStackGroup2"),
        ("IF-MIB", "ifCounterDiscontinuityGroup"),
        ("IF-MIB", "ifFixedLengthGroup"),
        ("IF-MIB", "ifHCFixedLengthGroup"),
        ("IF-MIB", "ifPacketGroup"),
        ("IF-MIB", "ifHCPacketGroup"),
        ("IF-MIB", "ifRcvAddressGroup"))
)
if mibBuilder.loadTexts:
    ifCompliance2.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    ifCompliance2.setDescription("A compliance statement defined in a previous version of this MIB module, for SNMP entities which have network interfaces.")

ifCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 31, 2, 2, 3)
)
ifCompliance3.setObjects(
      *(("IF-MIB", "ifGeneralInformationGroup"),
        ("IF-MIB", "linkUpDownNotificationsGroup"),
        ("IF-MIB", "ifFixedLengthGroup"),
        ("IF-MIB", "ifHCFixedLengthGroup"),
        ("IF-MIB", "ifPacketGroup"),
        ("IF-MIB", "ifHCPacketGroup"),
        ("IF-MIB", "ifVHCPacketGroup"),
        ("IF-MIB", "ifCounterDiscontinuityGroup"),
        ("IF-MIB", "ifRcvAddressGroup"))
)
if mibBuilder.loadTexts:
    ifCompliance3.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ifCompliance3.setDescription("The compliance statement for SNMP entities which have network interfaces.")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IF-MIB",
    **{"OwnerString": OwnerString,
       "InterfaceIndex": InterfaceIndex,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "interfaces": interfaces,
       "ifNumber": ifNumber,
       "ifTable": ifTable,
       "ifEntry": ifEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "ifType": ifType,
       "ifMtu": ifMtu,
       "ifSpeed": ifSpeed,
       "ifPhysAddress": ifPhysAddress,
       "ifAdminStatus": ifAdminStatus,
       "ifOperStatus": ifOperStatus,
       "ifLastChange": ifLastChange,
       "ifInOctets": ifInOctets,
       "ifInUcastPkts": ifInUcastPkts,
       "ifInNUcastPkts": ifInNUcastPkts,
       "ifInDiscards": ifInDiscards,
       "ifInErrors": ifInErrors,
       "ifInUnknownProtos": ifInUnknownProtos,
       "ifOutOctets": ifOutOctets,
       "ifOutUcastPkts": ifOutUcastPkts,
       "ifOutNUcastPkts": ifOutNUcastPkts,
       "ifOutDiscards": ifOutDiscards,
       "ifOutErrors": ifOutErrors,
       "ifOutQLen": ifOutQLen,
       "ifSpecific": ifSpecific,
       "ifMIB": ifMIB,
       "ifMIBObjects": ifMIBObjects,
       "ifXTable": ifXTable,
       "ifXEntry": ifXEntry,
       "ifName": ifName,
       "ifInMulticastPkts": ifInMulticastPkts,
       "ifInBroadcastPkts": ifInBroadcastPkts,
       "ifOutMulticastPkts": ifOutMulticastPkts,
       "ifOutBroadcastPkts": ifOutBroadcastPkts,
       "ifHCInOctets": ifHCInOctets,
       "ifHCInUcastPkts": ifHCInUcastPkts,
       "ifHCInMulticastPkts": ifHCInMulticastPkts,
       "ifHCInBroadcastPkts": ifHCInBroadcastPkts,
       "ifHCOutOctets": ifHCOutOctets,
       "ifHCOutUcastPkts": ifHCOutUcastPkts,
       "ifHCOutMulticastPkts": ifHCOutMulticastPkts,
       "ifHCOutBroadcastPkts": ifHCOutBroadcastPkts,
       "ifLinkUpDownTrapEnable": ifLinkUpDownTrapEnable,
       "ifHighSpeed": ifHighSpeed,
       "ifPromiscuousMode": ifPromiscuousMode,
       "ifConnectorPresent": ifConnectorPresent,
       "ifAlias": ifAlias,
       "ifCounterDiscontinuityTime": ifCounterDiscontinuityTime,
       "ifStackTable": ifStackTable,
       "ifStackEntry": ifStackEntry,
       "ifStackHigherLayer": ifStackHigherLayer,
       "ifStackLowerLayer": ifStackLowerLayer,
       "ifStackStatus": ifStackStatus,
       "ifTestTable": ifTestTable,
       "ifTestEntry": ifTestEntry,
       "ifTestId": ifTestId,
       "ifTestStatus": ifTestStatus,
       "ifTestType": ifTestType,
       "ifTestResult": ifTestResult,
       "ifTestCode": ifTestCode,
       "ifTestOwner": ifTestOwner,
       "ifRcvAddressTable": ifRcvAddressTable,
       "ifRcvAddressEntry": ifRcvAddressEntry,
       "ifRcvAddressAddress": ifRcvAddressAddress,
       "ifRcvAddressStatus": ifRcvAddressStatus,
       "ifRcvAddressType": ifRcvAddressType,
       "ifTableLastChange": ifTableLastChange,
       "ifStackLastChange": ifStackLastChange,
       "ifConformance": ifConformance,
       "ifGroups": ifGroups,
       "ifGeneralGroup": ifGeneralGroup,
       "ifFixedLengthGroup": ifFixedLengthGroup,
       "ifHCFixedLengthGroup": ifHCFixedLengthGroup,
       "ifPacketGroup": ifPacketGroup,
       "ifHCPacketGroup": ifHCPacketGroup,
       "ifVHCPacketGroup": ifVHCPacketGroup,
       "ifRcvAddressGroup": ifRcvAddressGroup,
       "ifTestGroup": ifTestGroup,
       "ifStackGroup": ifStackGroup,
       "ifGeneralInformationGroup": ifGeneralInformationGroup,
       "ifStackGroup2": ifStackGroup2,
       "ifOldObjectsGroup": ifOldObjectsGroup,
       "ifCounterDiscontinuityGroup": ifCounterDiscontinuityGroup,
       "linkUpDownNotificationsGroup": linkUpDownNotificationsGroup,
       "ifCompliances": ifCompliances,
       "ifCompliance": ifCompliance,
       "ifCompliance2": ifCompliance2,
       "ifCompliance3": ifCompliance3,
       "linkDown": linkDown,
       "linkUp": linkUp}
)
