# SNMP MIB module (UDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/UDP-MIB
# Produced by pysmi-2.0.0 at Sat Oct 17 14:25:42 2026
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
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
    "Counter32",
    "Counter64",
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

udpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 50)
)
if mibBuilder.loadTexts:
    udpMIB.setRevisions(
        ("2005-05-20 00:00",
         "1994-11-01 00:00",
         "1991-03-31 00:00")
    )
if mibBuilder.loadTexts:
    udpMIB.setLastUpdated("200505200000Z")
if mibBuilder.loadTexts:
    udpMIB.setOrganization("IETF IPv6 Working Group http://www.ietf.org/html.charters/ipv6-charter.html")
if mibBuilder.loadTexts:
    udpMIB.setContactInfo("Bill Fenner (editor) AT&T Labs -- Research 75 Willow Rd. Menlo Park, CA 94025 Phone: +1 650 330-7893 Email: <fenner@research.att.com> John Flick (editor) Hewlett-Packard Company 8000 Foothills Blvd. M/S 5557 Roseville, CA 95747 Phone: +1 916 785 4018 Email: <john.flick@hp.com> Send comments to <ipv6@ietf.org>")
if mibBuilder.loadTexts:
    udpMIB.setDescription("The MIB module for managing UDP implementations. Copyright (C) The Internet Society (2005). This version of this MIB module is part of RFC 4113; see the RFC itself for full legal notices.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7)
)
_UdpInDatagrams_Type = Counter32
_UdpInDatagrams_Object = MibScalar
udpInDatagrams = _UdpInDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 7, 1),
    _UdpInDatagrams_Type()
)
udpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpInDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    udpInDatagrams.setDescription("The total number of UDP datagrams delivered to UDP users. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.")
_UdpNoPorts_Type = Counter32
_UdpNoPorts_Object = MibScalar
udpNoPorts = _UdpNoPorts_Object(
    (1, 3, 6, 1, 2, 1, 7, 2),
    _UdpNoPorts_Type()
)
udpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpNoPorts.setStatus("current")
if mibBuilder.loadTexts:
    udpNoPorts.setDescription("The total number of received UDP datagrams for which there was no application at the destination port. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.")
_UdpInErrors_Type = Counter32
_UdpInErrors_Object = MibScalar
udpInErrors = _UdpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 7, 3),
    _UdpInErrors_Type()
)
udpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpInErrors.setStatus("current")
if mibBuilder.loadTexts:
    udpInErrors.setDescription("The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.")
_UdpOutDatagrams_Type = Counter32
_UdpOutDatagrams_Object = MibScalar
udpOutDatagrams = _UdpOutDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 7, 4),
    _UdpOutDatagrams_Type()
)
udpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpOutDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    udpOutDatagrams.setDescription("The total number of UDP datagrams sent from this entity. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.")
_UdpTable_Object = MibTable
udpTable = _UdpTable_Object(
    (1, 3, 6, 1, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    udpTable.setStatus("deprecated")
if mibBuilder.loadTexts:
    udpTable.setDescription("A table containing IPv4-specific UDP listener information. It contains information about all local IPv4 UDP end-points on which an application is currently accepting datagrams. This table has been deprecated in favor of the version neutral udpEndpointTable.")
_UdpEntry_Object = MibTableRow
udpEntry = _UdpEntry_Object(
    (1, 3, 6, 1, 2, 1, 7, 5, 1)
)
udpEntry.setIndexNames(
    (0, "UDP-MIB", "udpLocalAddress"),
    (0, "UDP-MIB", "udpLocalPort"),
)
if mibBuilder.loadTexts:
    udpEntry.setStatus("deprecated")
if mibBuilder.loadTexts:
    udpEntry.setDescription("Information about a particular current UDP listener.")
_UdpLocalAddress_Type = IpAddress
_UdpLocalAddress_Object = MibTableColumn
udpLocalAddress = _UdpLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 7, 5, 1, 1),
    _UdpLocalAddress_Type()
)
udpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpLocalAddress.setStatus("deprecated")
if mibBuilder.loadTexts:
    udpLocalAddress.setDescription("The local IP address for this UDP listener. In the case of a UDP listener that is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used.")


class _UdpLocalPort_Type(Integer32):
    """Custom type udpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UdpLocalPort_Type.__name__ = "Integer32"
_UdpLocalPort_Object = MibTableColumn
udpLocalPort = _UdpLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 7, 5, 1, 2),
    _UdpLocalPort_Type()
)
udpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpLocalPort.setStatus("deprecated")
if mibBuilder.loadTexts:
    udpLocalPort.setDescription("The local port number for this UDP listener.")
_UdpEndpointTable_Object = MibTable
udpEndpointTable = _UdpEndpointTable_Object(
    (1, 3, 6, 1, 2, 1, 7, 7)
)
if mibBuilder.loadTexts:
    udpEndpointTable.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointTable.setDescription("A table containing information about this entity's UDP endpoints on which a local application is currently accepting or sending datagrams. The address type in this table represents the address type used for the communication, irrespective of the higher-layer abstraction. For example, an application using IPv6 'sockets' to communicate via IPv4 between ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would use InetAddressType ipv4(1). Unlike the udpTable in RFC 2013, this table also allows the representation of an application that completely specifies both local and remote addresses and ports. A listening application is represented in three possible ways: 1) An application that is willing to accept both IPv4 and IPv6 datagrams is represented by a udpEndpointLocalAddressType of unknown(0) and a udpEndpointLocalAddress of ''h (a zero-length octet-string). 2) An application that is willing to accept only IPv4 or only IPv6 datagrams is represented by a udpEndpointLocalAddressType of the appropriate address type and a udpEndpointLocalAddress of '0.0.0.0' or '::' respectively. 3) An application that is listening for datagrams only for a specific IP address but from any remote system is represented by a udpEndpointLocalAddressType of the appropriate address type, with udpEndpointLocalAddress specifying the local address. In all cases where the remote is a wildcard, the udpEndpointRemoteAddressType is unknown(0), the udpEndpointRemoteAddress is ''h (a zero-length octet-string), and the udpEndpointRemotePort is 0. If the operating system is demultiplexing UDP packets by remote address and port, or if the application has 'connected' the socket specifying a default remote address and port, the udpEndpointRemote* values should be used to reflect this.")
_UdpEndpointEntry_Object = MibTableRow
udpEndpointEntry = _UdpEndpointEntry_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1)
)
udpEndpointEntry.setIndexNames(
    (0, "UDP-MIB", "udpEndpointLocalAddressType"),
    (0, "UDP-MIB", "udpEndpointLocalAddress"),
    (0, "UDP-MIB", "udpEndpointLocalPort"),
    (0, "UDP-MIB", "udpEndpointRemoteAddressType"),
    (0, "UDP-MIB", "udpEndpointRemoteAddress"),
    (0, "UDP-MIB", "udpEndpointRemotePort"),
    (0, "UDP-MIB", "udpEndpointInstance"),
)
if mibBuilder.loadTexts:
    udpEndpointEntry.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointEntry.setDescription("Information about a particular current UDP endpoint. Implementers need to be aware that if the total number of elements (octets or sub-identifiers) in udpEndpointLocalAddress and udpEndpointRemoteAddress exceeds 111, then OIDs of column instances in this table will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
_UdpEndpointLocalAddressType_Type = InetAddressType
_UdpEndpointLocalAddressType_Object = MibTableColumn
udpEndpointLocalAddressType = _UdpEndpointLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 1),
    _UdpEndpointLocalAddressType_Type()
)
udpEndpointLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEndpointLocalAddressType.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointLocalAddressType.setDescription("The address type of udpEndpointLocalAddress. Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all local IP addresses are accepted.")
_UdpEndpointLocalAddress_Type = InetAddress
_UdpEndpointLocalAddress_Object = MibTableColumn
udpEndpointLocalAddress = _UdpEndpointLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 2),
    _UdpEndpointLocalAddress_Type()
)
udpEndpointLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEndpointLocalAddress.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointLocalAddress.setDescription("The local IP address for this UDP endpoint. The value of this object can be represented in three possible ways, depending on the characteristics of the listening application: 1. For an application that is willing to accept both IPv4 and IPv6 datagrams, the value of this object must be ''h (a zero-length octet-string), with the value of the corresponding instance of the udpEndpointLocalAddressType object being unknown(0). 2. For an application that is willing to accept only IPv4 or only IPv6 datagrams, the value of this object must be '0.0.0.0' or '::', respectively, while the corresponding instance of the udpEndpointLocalAddressType object represents the appropriate address type. 3. For an application that is listening for data destined only to a specific IP address, the value of this object is the specific IP address for which this node is receiving packets, with the corresponding instance of the udpEndpointLocalAddressType object representing the appropriate address type. As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
_UdpEndpointLocalPort_Type = InetPortNumber
_UdpEndpointLocalPort_Object = MibTableColumn
udpEndpointLocalPort = _UdpEndpointLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 3),
    _UdpEndpointLocalPort_Type()
)
udpEndpointLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEndpointLocalPort.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointLocalPort.setDescription("The local port number for this UDP endpoint.")
_UdpEndpointRemoteAddressType_Type = InetAddressType
_UdpEndpointRemoteAddressType_Object = MibTableColumn
udpEndpointRemoteAddressType = _UdpEndpointRemoteAddressType_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 4),
    _UdpEndpointRemoteAddressType_Type()
)
udpEndpointRemoteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEndpointRemoteAddressType.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointRemoteAddressType.setDescription("The address type of udpEndpointRemoteAddress. Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all remote IP addresses are accepted. Also, note that some combinations of udpEndpointLocalAdressType and udpEndpointRemoteAddressType are not supported. In particular, if the value of this object is not unknown(0), it is expected to always refer to the same IP version as udpEndpointLocalAddressType.")
_UdpEndpointRemoteAddress_Type = InetAddress
_UdpEndpointRemoteAddress_Object = MibTableColumn
udpEndpointRemoteAddress = _UdpEndpointRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 5),
    _UdpEndpointRemoteAddress_Type()
)
udpEndpointRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEndpointRemoteAddress.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointRemoteAddress.setDescription("The remote IP address for this UDP endpoint. If datagrams from any remote system are to be accepted, this value is ''h (a zero-length octet-string). Otherwise, it has the type described by udpEndpointRemoteAddressType and is the address of the remote system from which datagrams are to be accepted (or to which all datagrams will be sent). As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
_UdpEndpointRemotePort_Type = InetPortNumber
_UdpEndpointRemotePort_Object = MibTableColumn
udpEndpointRemotePort = _UdpEndpointRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 6),
    _UdpEndpointRemotePort_Type()
)
udpEndpointRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEndpointRemotePort.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointRemotePort.setDescription("The remote port number for this UDP endpoint. If datagrams from any remote system are to be accepted, this value is zero.")


class _UdpEndpointInstance_Type(Unsigned32):
    """Custom type udpEndpointInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_UdpEndpointInstance_Type.__name__ = "Unsigned32"
_UdpEndpointInstance_Object = MibTableColumn
udpEndpointInstance = _UdpEndpointInstance_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 7),
    _UdpEndpointInstance_Type()
)
udpEndpointInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    udpEndpointInstance.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointInstance.setDescription("The instance of this tuple. This object is used to distinguish among multiple processes 'connected' to the same UDP endpoint. For example, on a system implementing the BSD sockets interface, this would be used to support the SO_REUSEADDR and SO_REUSEPORT socket options.")
_UdpEndpointProcess_Type = Unsigned32
_UdpEndpointProcess_Object = MibTableColumn
udpEndpointProcess = _UdpEndpointProcess_Object(
    (1, 3, 6, 1, 2, 1, 7, 7, 1, 8),
    _UdpEndpointProcess_Type()
)
udpEndpointProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpEndpointProcess.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointProcess.setDescription("The system's process ID for the process associated with this endpoint, or zero if there is no such process. This value is expected to be the same as HOST-RESOURCES-MIB::hrSWRunIndex or SYSAPPL-MIB:: sysApplElmtRunIndex for some row in the appropriate tables.")
_UdpHCInDatagrams_Type = Counter64
_UdpHCInDatagrams_Object = MibScalar
udpHCInDatagrams = _UdpHCInDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 7, 8),
    _UdpHCInDatagrams_Type()
)
udpHCInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpHCInDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    udpHCInDatagrams.setDescription("The total number of UDP datagrams delivered to UDP users, for devices that can receive more than 1 million UDP datagrams per second. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.")
_UdpHCOutDatagrams_Type = Counter64
_UdpHCOutDatagrams_Object = MibScalar
udpHCOutDatagrams = _UdpHCOutDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 7, 9),
    _UdpHCOutDatagrams_Type()
)
udpHCOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpHCOutDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    udpHCOutDatagrams.setDescription("The total number of UDP datagrams sent from this entity, for devices that can transmit more than 1 million UDP datagrams per second. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime.")
_UdpMIBConformance_ObjectIdentity = ObjectIdentity
udpMIBConformance = _UdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 50, 2)
)
_UdpMIBCompliances_ObjectIdentity = ObjectIdentity
udpMIBCompliances = _UdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 50, 2, 1)
)
_UdpMIBGroups_ObjectIdentity = ObjectIdentity
udpMIBGroups = _UdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 50, 2, 2)
)

# Managed Objects groups

udpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 50, 2, 2, 1)
)
udpGroup.setObjects(
      *(("UDP-MIB", "udpInDatagrams"),
        ("UDP-MIB", "udpNoPorts"),
        ("UDP-MIB", "udpInErrors"),
        ("UDP-MIB", "udpOutDatagrams"),
        ("UDP-MIB", "udpLocalAddress"),
        ("UDP-MIB", "udpLocalPort"))
)
if mibBuilder.loadTexts:
    udpGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    udpGroup.setDescription("The deprecated group of objects providing for management of UDP over IPv4.")

udpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 50, 2, 2, 2)
)
udpBaseGroup.setObjects(
      *(("UDP-MIB", "udpInDatagrams"),
        ("UDP-MIB", "udpNoPorts"),
        ("UDP-MIB", "udpInErrors"),
        ("UDP-MIB", "udpOutDatagrams"))
)
if mibBuilder.loadTexts:
    udpBaseGroup.setStatus("current")
if mibBuilder.loadTexts:
    udpBaseGroup.setDescription("The group of objects providing for counters of UDP statistics.")

udpHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 50, 2, 2, 3)
)
udpHCGroup.setObjects(
      *(("UDP-MIB", "udpHCInDatagrams"),
        ("UDP-MIB", "udpHCOutDatagrams"))
)
if mibBuilder.loadTexts:
    udpHCGroup.setStatus("current")
if mibBuilder.loadTexts:
    udpHCGroup.setDescription("The group of objects providing for counters of high speed UDP implementations.")

udpEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 50, 2, 2, 4)
)
udpEndpointGroup.setObjects(
    ("UDP-MIB", "udpEndpointProcess")
)
if mibBuilder.loadTexts:
    udpEndpointGroup.setStatus("current")
if mibBuilder.loadTexts:
    udpEndpointGroup.setDescription("The group of objects providing for the IP version independent management of UDP 'endpoints'.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

udpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 50, 2, 1, 1)
)
udpMIBCompliance.setObjects(
    ("UDP-MIB", "udpGroup")
)
if mibBuilder.loadTexts:
    udpMIBCompliance.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    udpMIBCompliance.setDescription("The compliance statement for IPv4-only systems that implement UDP. For IP version independence, this compliance statement is deprecated in favor of udpMIBCompliance2. However, agents are still encouraged to implement these objects in order to interoperate with the deployed base of managers.")

udpMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 50, 2, 1, 2)
)
udpMIBCompliance2.setObjects(
      *(("UDP-MIB", "udpBaseGroup"),
        ("UDP-MIB", "udpEndpointGroup"),
        ("UDP-MIB", "udpHCGroup"))
)
if mibBuilder.loadTexts:
    udpMIBCompliance2.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    udpMIBCompliance2.setDescription("The compliance statement for systems that implement UDP. There are a number of INDEX objects that cannot be represented in the form of OBJECT clauses in SMIv2, but for which we have the following compliance requirements, expressed in OBJECT clause form in this description clause: -- OBJECT udpEndpointLocalAddressType -- SYNTAX InetAddressType { unknown(0), ipv4(1), -- ipv6(2), ipv4z(3), -- ipv6z(4) } -- DESCRIPTION -- Support for dns(5) is not required. -- OBJECT udpEndpointLocalAddress -- SYNTAX InetAddress (SIZE(0|4|8|16|20)) -- DESCRIPTION -- Support is only required for zero-length -- octet-strings, and for scoped and unscoped -- IPv4 and IPv6 addresses. -- OBJECT udpEndpointRemoteAddressType -- SYNTAX InetAddressType { unknown(0), ipv4(1), -- ipv6(2), ipv4z(3), -- ipv6z(4) } -- DESCRIPTION -- Support for dns(5) is not required. -- OBJECT udpEndpointRemoteAddress -- SYNTAX InetAddress (SIZE(0|4|8|16|20)) -- DESCRIPTION -- Support is only required for zero-length -- octet-strings, and for scoped and unscoped -- IPv4 and IPv6 addresses. ")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UDP-MIB",
    **{"udp": udp,
       "udpInDatagrams": udpInDatagrams,
       "udpNoPorts": udpNoPorts,
       "udpInErrors": udpInErrors,
       "udpOutDatagrams": udpOutDatagrams,
       "udpTable": udpTable,
       "udpEntry": udpEntry,
       "udpLocalAddress": udpLocalAddress,
       "udpLocalPort": udpLocalPort,
       "udpEndpointTable": udpEndpointTable,
       "udpEndpointEntry": udpEndpointEntry,
       "udpEndpointLocalAddressType": udpEndpointLocalAddressType,
       "udpEndpointLocalAddress": udpEndpointLocalAddress,
       "udpEndpointLocalPort": udpEndpointLocalPort,
       "udpEndpointRemoteAddressType": udpEndpointRemoteAddressType,
       "udpEndpointRemoteAddress": udpEndpointRemoteAddress,
       "udpEndpointRemotePort": udpEndpointRemotePort,
       "udpEndpointInstance": udpEndpointInstance,
       "udpEndpointProcess": udpEndpointProcess,
       "udpHCInDatagrams": udpHCInDatagrams,
       "udpHCOutDatagrams": udpHCOutDatagrams,
       "udpMIB": udpMIB,
       "udpMIBConformance": udpMIBConformance,
       "udpMIBCompliances": udpMIBCompliances,
       "udpMIBCompliance": udpMIBCompliance,
       "udpMIBCompliance2": udpMIBCompliance2,
       "udpMIBGroups": udpMIBGroups,
       "udpGroup": udpGroup,
       "udpBaseGroup": udpBaseGroup,
       "udpHCGroup": udpHCGroup,
       "udpEndpointGroup": udpEndpointGroup}
)
