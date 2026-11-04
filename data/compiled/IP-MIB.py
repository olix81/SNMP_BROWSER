# SNMP MIB module (IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/IP-MIB
# Produced by pysmi-2.0.0 at Sat Oct 17 14:25:40 2026
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

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
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ipMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 48)
)
if mibBuilder.loadTexts:
    ipMIB.setRevisions(
        ("2006-02-02 00:00",
         "1994-11-01 00:00",
         "1991-03-31 00:00")
    )
if mibBuilder.loadTexts:
    ipMIB.setLastUpdated("200602020000Z")
if mibBuilder.loadTexts:
    ipMIB.setOrganization("IETF IPv6 MIB Revision Team")
if mibBuilder.loadTexts:
    ipMIB.setContactInfo("Editor: Shawn A. Routhier Interworking Labs 108 Whispering Pines Dr. Suite 235 Scotts Valley, CA 95066 USA EMail: <sar@iwl.com>")
if mibBuilder.loadTexts:
    ipMIB.setDescription("The MIB module for managing IP and ICMP implementations, but excluding their management of IP routes. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4293; see the RFC itself for full legal notices.")


# Types definitions


# TEXTUAL-CONVENTIONS



class IpAddressOriginTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("manual", 2),
          ("dhcp", 4),
          ("linklayer", 5),
          ("random", 6))
    )

    if mibBuilder.loadTexts:
        description = "The origin of the address. manual(2) indicates that the address was manually configured to a specified address, e.g., by user configuration. dhcp(4) indicates an address that was assigned to this system by a DHCP server. linklayer(5) indicates an address created by IPv6 stateless auto-configuration. random(6) indicates an address chosen by the system at random, e.g., an IPv4 address within 169.254/16, or an RFC 3041 privacy address."


class IpAddressStatusTC(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("preferred", 1),
          ("deprecated", 2),
          ("invalid", 3),
          ("inaccessible", 4),
          ("unknown", 5),
          ("tentative", 6),
          ("duplicate", 7),
          ("optimistic", 8))
    )

    if mibBuilder.loadTexts:
        description = "The status of an address. Most of the states correspond to states from the IPv6 Stateless Address Autoconfiguration protocol. The preferred(1) state indicates that this is a valid address that can appear as the destination or source address of a packet. The deprecated(2) state indicates that this is a valid but deprecated address that should no longer be used as a source address in new communications, but packets addressed to such an address are processed as expected. The invalid(3) state indicates that this isn't a valid address and it shouldn't appear as the destination or source address of a packet. The inaccessible(4) state indicates that the address is not accessible because the interface to which this address is assigned is not operational. The unknown(5) state indicates that the status cannot be determined for some reason. The tentative(6) state indicates that the uniqueness of the address on the link is being verified. Addresses in this state should not be used for general communication and should only be used to determine the uniqueness of the address. The duplicate(7) state indicates the address has been determined to be non-unique on the link and so must not be used. The optimistic(8) state indicates the address is available for use, subject to restrictions, while its uniqueness on a link is being verified. In the absence of other information, an IPv4 address is always preferred(1)."
    if mibBuilder.loadTexts:
        reference = "RFC 2462"


class IpAddressPrefixOriginTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("manual", 2),
          ("wellknown", 3),
          ("dhcp", 4),
          ("routeradv", 5))
    )

    if mibBuilder.loadTexts:
        description = "The origin of this prefix. manual(2) indicates a prefix that was manually configured. wellknown(3) indicates a well-known prefix, e.g., 169.254/16 for IPv4 auto-configuration or fe80::/10 for IPv6 link-local addresses. Well known prefixes may be assigned by IANA, the address registries, or by specification in a standards track RFC. dhcp(4) indicates a prefix that was assigned by a DHCP server. routeradv(5) indicates a prefix learned from a router advertisement. Note: while IpAddressOriginTC and IpAddressPrefixOriginTC are similar, they are not identical. The first defines how an address was created, while the second defines how a prefix was found."


class Ipv6AddressIfIdentifierTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )

    if mibBuilder.loadTexts:
        description = "This data type is used to model IPv6 address interface identifiers. This is a binary string of up to 8 octets in network byte-order."


# MIB Managed Objects in the order of their OIDs

_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)


class _IpForwarding_Type(Integer32):
    """Custom type ipForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_IpForwarding_Type.__name__ = "Integer32"
_IpForwarding_Object = MibScalar
ipForwarding = _IpForwarding_Object(
    (1, 3, 6, 1, 2, 1, 4, 1),
    _IpForwarding_Type()
)
ipForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwarding.setStatus("current")
if mibBuilder.loadTexts:
    ipForwarding.setDescription("The indication of whether this entity is acting as an IPv4 router in respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv4 routers forward datagrams. IPv4 hosts do not (except those source-routed via the host). When this object is written, the entity should save the change to non-volatile storage and restore the object from non-volatile storage upon re-initialization of the system. Note: a stronger requirement is not used because this object was previously defined.")


class _IpDefaultTTL_Type(Integer32):
    """Custom type ipDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpDefaultTTL_Type.__name__ = "Integer32"
_IpDefaultTTL_Object = MibScalar
ipDefaultTTL = _IpDefaultTTL_Object(
    (1, 3, 6, 1, 2, 1, 4, 2),
    _IpDefaultTTL_Type()
)
ipDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultTTL.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultTTL.setDescription("The default value inserted into the Time-To-Live field of the IPv4 header of datagrams originated at this entity, whenever a TTL value is not supplied by the transport layer protocol. When this object is written, the entity should save the change to non-volatile storage and restore the object from non-volatile storage upon re-initialization of the system. Note: a stronger requirement is not used because this object was previously defined.")
_IpInReceives_Type = Counter32
_IpInReceives_Object = MibScalar
ipInReceives = _IpInReceives_Object(
    (1, 3, 6, 1, 2, 1, 4, 3),
    _IpInReceives_Type()
)
ipInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInReceives.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipInReceives.setDescription("The total number of input datagrams received from interfaces, including those received in error. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsInRecieves.")
_IpInHdrErrors_Type = Counter32
_IpInHdrErrors_Object = MibScalar
ipInHdrErrors = _IpInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 4),
    _IpInHdrErrors_Type()
)
ipInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInHdrErrors.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipInHdrErrors.setDescription("The number of input datagrams discarded due to errors in their IPv4 headers, including bad checksums, version number mismatch, other format errors, time-to-live exceeded, errors discovered in processing their IPv4 options, etc. This object has been deprecated as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsInHdrErrors.")
_IpInAddrErrors_Type = Counter32
_IpInAddrErrors_Object = MibScalar
ipInAddrErrors = _IpInAddrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 5),
    _IpInAddrErrors_Type()
)
ipInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInAddrErrors.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipInAddrErrors.setDescription("The number of input datagrams discarded because the IPv4 address in their IPv4 header's destination field was not a valid address to be received at this entity. This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E). For entities which are not IPv4 routers, and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsInAddrErrors.")
_IpForwDatagrams_Type = Counter32
_IpForwDatagrams_Object = MibScalar
ipForwDatagrams = _IpForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 6),
    _IpForwDatagrams_Type()
)
ipForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwDatagrams.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipForwDatagrams.setDescription("The number of input datagrams for which this entity was not their final IPv4 destination, as a result of which an attempt was made to find a route to forward them to that final destination. In entities which do not act as IPv4 routers, this counter will include only those packets which were Source-Routed via this entity, and the Source-Route option processing was successful. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsInForwDatagrams.")
_IpInUnknownProtos_Type = Counter32
_IpInUnknownProtos_Object = MibScalar
ipInUnknownProtos = _IpInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 4, 7),
    _IpInUnknownProtos_Type()
)
ipInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInUnknownProtos.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipInUnknownProtos.setDescription("The number of locally-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsInUnknownProtos.")
_IpInDiscards_Type = Counter32
_IpInDiscards_Object = MibScalar
ipInDiscards = _IpInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 8),
    _IpInDiscards_Type()
)
ipInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInDiscards.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipInDiscards.setDescription("The number of input IPv4 datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space). Note that this counter does not include any datagrams discarded while awaiting re-assembly. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsInDiscards.")
_IpInDelivers_Type = Counter32
_IpInDelivers_Object = MibScalar
ipInDelivers = _IpInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 4, 9),
    _IpInDelivers_Type()
)
ipInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInDelivers.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipInDelivers.setDescription("The total number of input datagrams successfully delivered to IPv4 user-protocols (including ICMP). This object has been deprecated as a new IP version neutral table has been added. It is loosely replaced by ipSystemStatsIndelivers.")
_IpOutRequests_Type = Counter32
_IpOutRequests_Object = MibScalar
ipOutRequests = _IpOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 4, 10),
    _IpOutRequests_Type()
)
ipOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRequests.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipOutRequests.setDescription("The total number of IPv4 datagrams which local IPv4 user protocols (including ICMP) supplied to IPv4 in requests for transmission. Note that this counter does not include any datagrams counted in ipForwDatagrams. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsOutRequests.")
_IpOutDiscards_Type = Counter32
_IpOutDiscards_Object = MibScalar
ipOutDiscards = _IpOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 11),
    _IpOutDiscards_Type()
)
ipOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutDiscards.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipOutDiscards.setDescription("The number of output IPv4 datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space). Note that this counter would include datagrams counted in ipForwDatagrams if any such packets met this (discretionary) discard criterion. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsOutDiscards.")
_IpOutNoRoutes_Type = Counter32
_IpOutNoRoutes_Object = MibScalar
ipOutNoRoutes = _IpOutNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 12),
    _IpOutNoRoutes_Type()
)
ipOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutNoRoutes.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipOutNoRoutes.setDescription("The number of IPv4 datagrams discarded because no route could be found to transmit them to their destination. Note that this counter includes any packets counted in ipForwDatagrams which meet this `no-route' criterion. Note that this includes any datagrams which a host cannot route because all of its default routers are down. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsOutNoRoutes.")
_IpReasmTimeout_Type = Integer32
_IpReasmTimeout_Object = MibScalar
ipReasmTimeout = _IpReasmTimeout_Object(
    (1, 3, 6, 1, 2, 1, 4, 13),
    _IpReasmTimeout_Type()
)
ipReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ipReasmTimeout.setUnits("seconds")
if mibBuilder.loadTexts:
    ipReasmTimeout.setDescription("The maximum number of seconds that received fragments are held while they are awaiting reassembly at this entity.")
_IpReasmReqds_Type = Counter32
_IpReasmReqds_Object = MibScalar
ipReasmReqds = _IpReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 4, 14),
    _IpReasmReqds_Type()
)
ipReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmReqds.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipReasmReqds.setDescription("The number of IPv4 fragments received which needed to be reassembled at this entity. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsReasmReqds.")
_IpReasmOKs_Type = Counter32
_IpReasmOKs_Object = MibScalar
ipReasmOKs = _IpReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 15),
    _IpReasmOKs_Type()
)
ipReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmOKs.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipReasmOKs.setDescription("The number of IPv4 datagrams successfully re-assembled. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsReasmOKs.")
_IpReasmFails_Type = Counter32
_IpReasmFails_Object = MibScalar
ipReasmFails = _IpReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 16),
    _IpReasmFails_Type()
)
ipReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmFails.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipReasmFails.setDescription("The number of failures detected by the IPv4 re-assembly algorithm (for whatever reason: timed out, errors, etc). Note that this is not necessarily a count of discarded IPv4 fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsReasmFails.")
_IpFragOKs_Type = Counter32
_IpFragOKs_Object = MibScalar
ipFragOKs = _IpFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 17),
    _IpFragOKs_Type()
)
ipFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragOKs.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipFragOKs.setDescription("The number of IPv4 datagrams that have been successfully fragmented at this entity. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsOutFragOKs.")
_IpFragFails_Type = Counter32
_IpFragFails_Object = MibScalar
ipFragFails = _IpFragFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 18),
    _IpFragFails_Type()
)
ipFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragFails.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipFragFails.setDescription("The number of IPv4 datagrams that have been discarded because they needed to be fragmented at this entity but could not be, e.g., because their Don't Fragment flag was set. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by ipSystemStatsOutFragFails.")
_IpFragCreates_Type = Counter32
_IpFragCreates_Object = MibScalar
ipFragCreates = _IpFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 4, 19),
    _IpFragCreates_Type()
)
ipFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragCreates.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipFragCreates.setDescription("The number of IPv4 datagram fragments that have been generated as a result of fragmentation at this entity. This object has been deprecated as a new IP version neutral table has been added. It is loosely replaced by ipSystemStatsOutFragCreates.")
_IpAddrTable_Object = MibTable
ipAddrTable = _IpAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 20)
)
if mibBuilder.loadTexts:
    ipAddrTable.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipAddrTable.setDescription("The table of addressing information relevant to this entity's IPv4 addresses. This table has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by the ipAddressTable although several objects that weren't deemed useful weren't carried forward while another (ipAdEntReasmMaxSize) was moved to the ipv4InterfaceTable.")
_IpAddrEntry_Object = MibTableRow
ipAddrEntry = _IpAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1)
)
ipAddrEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
)
if mibBuilder.loadTexts:
    ipAddrEntry.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipAddrEntry.setDescription("The addressing information for one of this entity's IPv4 addresses.")
_IpAdEntAddr_Type = IpAddress
_IpAdEntAddr_Object = MibTableColumn
ipAdEntAddr = _IpAdEntAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 1),
    _IpAdEntAddr_Type()
)
ipAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntAddr.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipAdEntAddr.setDescription("The IPv4 address to which this entry's addressing information pertains.")


class _IpAdEntIfIndex_Type(Integer32):
    """Custom type ipAdEntIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpAdEntIfIndex_Type.__name__ = "Integer32"
_IpAdEntIfIndex_Object = MibTableColumn
ipAdEntIfIndex = _IpAdEntIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 2),
    _IpAdEntIfIndex_Type()
)
ipAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntIfIndex.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipAdEntIfIndex.setDescription("The index value which uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")
_IpAdEntNetMask_Type = IpAddress
_IpAdEntNetMask_Object = MibTableColumn
ipAdEntNetMask = _IpAdEntNetMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 3),
    _IpAdEntNetMask_Type()
)
ipAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntNetMask.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipAdEntNetMask.setDescription("The subnet mask associated with the IPv4 address of this entry. The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0.")


class _IpAdEntBcastAddr_Type(Integer32):
    """Custom type ipAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IpAdEntBcastAddr_Type.__name__ = "Integer32"
_IpAdEntBcastAddr_Object = MibTableColumn
ipAdEntBcastAddr = _IpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 4),
    _IpAdEntBcastAddr_Type()
)
ipAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntBcastAddr.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipAdEntBcastAddr.setDescription("The value of the least-significant bit in the IPv4 broadcast address used for sending datagrams on the (logical) interface associated with the IPv4 address of this entry. For example, when the Internet standard all-ones broadcast address is used, the value will be 1. This value applies to both the subnet and network broadcast addresses used by the entity on this (logical) interface.")


class _IpAdEntReasmMaxSize_Type(Integer32):
    """Custom type ipAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_IpAdEntReasmMaxSize_Object = MibTableColumn
ipAdEntReasmMaxSize = _IpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 5),
    _IpAdEntReasmMaxSize_Type()
)
ipAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntReasmMaxSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipAdEntReasmMaxSize.setDescription("The size of the largest IPv4 datagram which this entity can re-assemble from incoming IPv4 fragmented datagrams received on this interface.")
_IpNetToMediaTable_Object = MibTable
ipNetToMediaTable = _IpNetToMediaTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 22)
)
if mibBuilder.loadTexts:
    ipNetToMediaTable.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipNetToMediaTable.setDescription("The IPv4 Address Translation table used for mapping from IPv4 addresses to physical addresses. This table has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by the ipNetToPhysicalTable.")
_IpNetToMediaEntry_Object = MibTableRow
ipNetToMediaEntry = _IpNetToMediaEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1)
)
ipNetToMediaEntry.setIndexNames(
    (0, "IP-MIB", "ipNetToMediaIfIndex"),
    (0, "IP-MIB", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    ipNetToMediaEntry.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipNetToMediaEntry.setDescription("Each entry contains one IpAddress to `physical' address equivalence.")


class _IpNetToMediaIfIndex_Type(Integer32):
    """Custom type ipNetToMediaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpNetToMediaIfIndex_Type.__name__ = "Integer32"
_IpNetToMediaIfIndex_Object = MibTableColumn
ipNetToMediaIfIndex = _IpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 1),
    _IpNetToMediaIfIndex_Type()
)
ipNetToMediaIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToMediaIfIndex.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipNetToMediaIfIndex.setDescription("The interface on which this entry's equivalence is effective. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex. This object predates the rule limiting index objects to a max access value of 'not-accessible' and so continues to use a value of 'read-create'.")


class _IpNetToMediaPhysAddress_Type(PhysAddress):
    """Custom type ipNetToMediaPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_IpNetToMediaPhysAddress_Type.__name__ = "PhysAddress"
_IpNetToMediaPhysAddress_Object = MibTableColumn
ipNetToMediaPhysAddress = _IpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 2),
    _IpNetToMediaPhysAddress_Type()
)
ipNetToMediaPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToMediaPhysAddress.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipNetToMediaPhysAddress.setDescription("The media-dependent `physical' address. This object should return 0 when this entry is in the 'incomplete' state. As the entries in this table are typically not persistent when this object is written the entity should not save the change to non-volatile storage. Note: a stronger requirement is not used because this object was previously defined.")
_IpNetToMediaNetAddress_Type = IpAddress
_IpNetToMediaNetAddress_Object = MibTableColumn
ipNetToMediaNetAddress = _IpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 3),
    _IpNetToMediaNetAddress_Type()
)
ipNetToMediaNetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToMediaNetAddress.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipNetToMediaNetAddress.setDescription("The IpAddress corresponding to the media-dependent `physical' address. This object predates the rule limiting index objects to a max access value of 'not-accessible' and so continues to use a value of 'read-create'.")


class _IpNetToMediaType_Type(Integer32):
    """Custom type ipNetToMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4))
    )


_IpNetToMediaType_Type.__name__ = "Integer32"
_IpNetToMediaType_Object = MibTableColumn
ipNetToMediaType = _IpNetToMediaType_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 4),
    _IpNetToMediaType_Type()
)
ipNetToMediaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToMediaType.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipNetToMediaType.setDescription("The type of mapping. Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToMediaTable. That is, it effectively dis-associates the interface identified with said entry from the mapping identified with said entry. It is an implementation- specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipNetToMediaType object. As the entries in this table are typically not persistent when this object is written the entity should not save the change to non-volatile storage. Note: a stronger requirement is not used because this object was previously defined.")
_IpRoutingDiscards_Type = Counter32
_IpRoutingDiscards_Object = MibScalar
ipRoutingDiscards = _IpRoutingDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 23),
    _IpRoutingDiscards_Type()
)
ipRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutingDiscards.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipRoutingDiscards.setDescription("The number of routing entries which were chosen to be discarded even though they are valid. One possible reason for discarding such an entry could be to free-up buffer space for other routing entries. This object was defined in pre-IPv6 versions of the IP MIB. It was implicitly IPv4 only, but the original specifications did not indicate this protocol restriction. In order to clarify the specifications, this object has been deprecated and a similar, but more thoroughly clarified, object has been added to the IP-FORWARD-MIB.")


class _Ipv6IpForwarding_Type(Integer32):
    """Custom type ipv6IpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_Ipv6IpForwarding_Type.__name__ = "Integer32"
_Ipv6IpForwarding_Object = MibScalar
ipv6IpForwarding = _Ipv6IpForwarding_Object(
    (1, 3, 6, 1, 2, 1, 4, 25),
    _Ipv6IpForwarding_Type()
)
ipv6IpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IpForwarding.setStatus("current")
if mibBuilder.loadTexts:
    ipv6IpForwarding.setDescription("The indication of whether this entity is acting as an IPv6 router on any interface in respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams. IPv6 hosts do not (except those source-routed via the host). When this object is written, the entity SHOULD save the change to non-volatile storage and restore the object from non-volatile storage upon re-initialization of the system.")


class _Ipv6IpDefaultHopLimit_Type(Integer32):
    """Custom type ipv6IpDefaultHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ipv6IpDefaultHopLimit_Type.__name__ = "Integer32"
_Ipv6IpDefaultHopLimit_Object = MibScalar
ipv6IpDefaultHopLimit = _Ipv6IpDefaultHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 4, 26),
    _Ipv6IpDefaultHopLimit_Type()
)
ipv6IpDefaultHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IpDefaultHopLimit.setStatus("current")
if mibBuilder.loadTexts:
    ipv6IpDefaultHopLimit.setReference("RFC 2461 Section 6.3.2")
if mibBuilder.loadTexts:
    ipv6IpDefaultHopLimit.setDescription("The default value inserted into the Hop Limit field of the IPv6 header of datagrams originated at this entity whenever a Hop Limit value is not supplied by the transport layer protocol. When this object is written, the entity SHOULD save the change to non-volatile storage and restore the object from non-volatile storage upon re-initialization of the system.")
_Ipv4InterfaceTableLastChange_Type = TimeStamp
_Ipv4InterfaceTableLastChange_Object = MibScalar
ipv4InterfaceTableLastChange = _Ipv4InterfaceTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 4, 27),
    _Ipv4InterfaceTableLastChange_Type()
)
ipv4InterfaceTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4InterfaceTableLastChange.setStatus("current")
if mibBuilder.loadTexts:
    ipv4InterfaceTableLastChange.setDescription("The value of sysUpTime on the most recent occasion at which a row in the ipv4InterfaceTable was added or deleted, or when an ipv4InterfaceReasmMaxSize or an ipv4InterfaceEnableStatus object was modified. If new objects are added to the ipv4InterfaceTable that require the ipv4InterfaceTableLastChange to be updated when they are modified, they must specify that requirement in their description clause.")
_Ipv4InterfaceTable_Object = MibTable
ipv4InterfaceTable = _Ipv4InterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 28)
)
if mibBuilder.loadTexts:
    ipv4InterfaceTable.setStatus("current")
if mibBuilder.loadTexts:
    ipv4InterfaceTable.setDescription("The table containing per-interface IPv4-specific information.")
_Ipv4InterfaceEntry_Object = MibTableRow
ipv4InterfaceEntry = _Ipv4InterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 28, 1)
)
ipv4InterfaceEntry.setIndexNames(
    (0, "IP-MIB", "ipv4InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipv4InterfaceEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipv4InterfaceEntry.setDescription("An entry containing IPv4-specific information for a specific interface.")
_Ipv4InterfaceIfIndex_Type = InterfaceIndex
_Ipv4InterfaceIfIndex_Object = MibTableColumn
ipv4InterfaceIfIndex = _Ipv4InterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 28, 1, 1),
    _Ipv4InterfaceIfIndex_Type()
)
ipv4InterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv4InterfaceIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipv4InterfaceIfIndex.setDescription("The index value that uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")


class _Ipv4InterfaceReasmMaxSize_Type(Integer32):
    """Custom type ipv4InterfaceReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv4InterfaceReasmMaxSize_Type.__name__ = "Integer32"
_Ipv4InterfaceReasmMaxSize_Object = MibTableColumn
ipv4InterfaceReasmMaxSize = _Ipv4InterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 2, 1, 4, 28, 1, 2),
    _Ipv4InterfaceReasmMaxSize_Type()
)
ipv4InterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4InterfaceReasmMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    ipv4InterfaceReasmMaxSize.setDescription("The size of the largest IPv4 datagram that this entity can re-assemble from incoming IPv4 fragmented datagrams received on this interface.")


class _Ipv4InterfaceEnableStatus_Type(Integer32):
    """Custom type ipv4InterfaceEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Ipv4InterfaceEnableStatus_Type.__name__ = "Integer32"
_Ipv4InterfaceEnableStatus_Object = MibTableColumn
ipv4InterfaceEnableStatus = _Ipv4InterfaceEnableStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 28, 1, 3),
    _Ipv4InterfaceEnableStatus_Type()
)
ipv4InterfaceEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4InterfaceEnableStatus.setStatus("current")
if mibBuilder.loadTexts:
    ipv4InterfaceEnableStatus.setDescription("The indication of whether IPv4 is enabled (up) or disabled (down) on this interface. This object does not affect the state of the interface itself, only its connection to an IPv4 stack. The IF-MIB should be used to control the state of the interface.")


class _Ipv4InterfaceRetransmitTime_Type(Unsigned32):
    """Custom type ipv4InterfaceRetransmitTime based on Unsigned32"""
    defaultValue = 1000


_Ipv4InterfaceRetransmitTime_Type.__name__ = "Unsigned32"
_Ipv4InterfaceRetransmitTime_Object = MibTableColumn
ipv4InterfaceRetransmitTime = _Ipv4InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 28, 1, 4),
    _Ipv4InterfaceRetransmitTime_Type()
)
ipv4InterfaceRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    ipv4InterfaceRetransmitTime.setUnits("milliseconds")
if mibBuilder.loadTexts:
    ipv4InterfaceRetransmitTime.setReference("RFC 1122")
if mibBuilder.loadTexts:
    ipv4InterfaceRetransmitTime.setDescription("The time between retransmissions of ARP requests to a neighbor when resolving the address or when probing the reachability of a neighbor.")
_Ipv6InterfaceTableLastChange_Type = TimeStamp
_Ipv6InterfaceTableLastChange_Object = MibScalar
ipv6InterfaceTableLastChange = _Ipv6InterfaceTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 4, 29),
    _Ipv6InterfaceTableLastChange_Type()
)
ipv6InterfaceTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InterfaceTableLastChange.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceTableLastChange.setDescription("The value of sysUpTime on the most recent occasion at which a row in the ipv6InterfaceTable was added or deleted or when an ipv6InterfaceReasmMaxSize, ipv6InterfaceIdentifier, ipv6InterfaceEnableStatus, ipv6InterfaceReachableTime, ipv6InterfaceRetransmitTime, or ipv6InterfaceForwarding object was modified. If new objects are added to the ipv6InterfaceTable that require the ipv6InterfaceTableLastChange to be updated when they are modified, they must specify that requirement in their description clause.")
_Ipv6InterfaceTable_Object = MibTable
ipv6InterfaceTable = _Ipv6InterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 30)
)
if mibBuilder.loadTexts:
    ipv6InterfaceTable.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceTable.setDescription("The table containing per-interface IPv6-specific information.")
_Ipv6InterfaceEntry_Object = MibTableRow
ipv6InterfaceEntry = _Ipv6InterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1)
)
ipv6InterfaceEntry.setIndexNames(
    (0, "IP-MIB", "ipv6InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6InterfaceEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceEntry.setDescription("An entry containing IPv6-specific information for a given interface.")
_Ipv6InterfaceIfIndex_Type = InterfaceIndex
_Ipv6InterfaceIfIndex_Object = MibTableColumn
ipv6InterfaceIfIndex = _Ipv6InterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1, 1),
    _Ipv6InterfaceIfIndex_Type()
)
ipv6InterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6InterfaceIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceIfIndex.setDescription("The index value that uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")


class _Ipv6InterfaceReasmMaxSize_Type(Unsigned32):
    """Custom type ipv6InterfaceReasmMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 65535),
    )


_Ipv6InterfaceReasmMaxSize_Type.__name__ = "Unsigned32"
_Ipv6InterfaceReasmMaxSize_Object = MibTableColumn
ipv6InterfaceReasmMaxSize = _Ipv6InterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1, 2),
    _Ipv6InterfaceReasmMaxSize_Type()
)
ipv6InterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InterfaceReasmMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceReasmMaxSize.setUnits("octets")
if mibBuilder.loadTexts:
    ipv6InterfaceReasmMaxSize.setDescription("The size of the largest IPv6 datagram that this entity can re-assemble from incoming IPv6 fragmented datagrams received on this interface.")
_Ipv6InterfaceIdentifier_Type = Ipv6AddressIfIdentifierTC
_Ipv6InterfaceIdentifier_Object = MibTableColumn
ipv6InterfaceIdentifier = _Ipv6InterfaceIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1, 3),
    _Ipv6InterfaceIdentifier_Type()
)
ipv6InterfaceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InterfaceIdentifier.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceIdentifier.setDescription("The Interface Identifier for this interface. The Interface Identifier is combined with an address prefix to form an interface address. By default, the Interface Identifier is auto-configured according to the rules of the link type to which this interface is attached. A zero length identifier may be used where appropriate. One possible example is a loopback interface.")


class _Ipv6InterfaceEnableStatus_Type(Integer32):
    """Custom type ipv6InterfaceEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_Ipv6InterfaceEnableStatus_Type.__name__ = "Integer32"
_Ipv6InterfaceEnableStatus_Object = MibTableColumn
ipv6InterfaceEnableStatus = _Ipv6InterfaceEnableStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1, 5),
    _Ipv6InterfaceEnableStatus_Type()
)
ipv6InterfaceEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6InterfaceEnableStatus.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceEnableStatus.setDescription("The indication of whether IPv6 is enabled (up) or disabled (down) on this interface. This object does not affect the state of the interface itself, only its connection to an IPv6 stack. The IF-MIB should be used to control the state of the interface. When this object is written, the entity SHOULD save the change to non-volatile storage and restore the object from non-volatile storage upon re-initialization of the system.")
_Ipv6InterfaceReachableTime_Type = Unsigned32
_Ipv6InterfaceReachableTime_Object = MibTableColumn
ipv6InterfaceReachableTime = _Ipv6InterfaceReachableTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1, 6),
    _Ipv6InterfaceReachableTime_Type()
)
ipv6InterfaceReachableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InterfaceReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceReachableTime.setUnits("milliseconds")
if mibBuilder.loadTexts:
    ipv6InterfaceReachableTime.setReference("RFC 2461, Section 6.3.2")
if mibBuilder.loadTexts:
    ipv6InterfaceReachableTime.setDescription("The time a neighbor is considered reachable after receiving a reachability confirmation.")
_Ipv6InterfaceRetransmitTime_Type = Unsigned32
_Ipv6InterfaceRetransmitTime_Object = MibTableColumn
ipv6InterfaceRetransmitTime = _Ipv6InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1, 7),
    _Ipv6InterfaceRetransmitTime_Type()
)
ipv6InterfaceRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceRetransmitTime.setUnits("milliseconds")
if mibBuilder.loadTexts:
    ipv6InterfaceRetransmitTime.setReference("RFC 2461, Section 6.3.2")
if mibBuilder.loadTexts:
    ipv6InterfaceRetransmitTime.setDescription("The time between retransmissions of Neighbor Solicitation messages to a neighbor when resolving the address or when probing the reachability of a neighbor.")


class _Ipv6InterfaceForwarding_Type(Integer32):
    """Custom type ipv6InterfaceForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_Ipv6InterfaceForwarding_Type.__name__ = "Integer32"
_Ipv6InterfaceForwarding_Object = MibTableColumn
ipv6InterfaceForwarding = _Ipv6InterfaceForwarding_Object(
    (1, 3, 6, 1, 2, 1, 4, 30, 1, 8),
    _Ipv6InterfaceForwarding_Type()
)
ipv6InterfaceForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6InterfaceForwarding.setStatus("current")
if mibBuilder.loadTexts:
    ipv6InterfaceForwarding.setDescription("The indication of whether this entity is acting as an IPv6 router on this interface with respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams. IPv6 hosts do not (except those source-routed via the host). This object is constrained by ipv6IpForwarding and is ignored if ipv6IpForwarding is set to notForwarding. Those systems that do not provide per-interface control of the forwarding function should set this object to forwarding for all interfaces and allow the ipv6IpForwarding object to control the forwarding capability. When this object is written, the entity SHOULD save the change to non-volatile storage and restore the object from non-volatile storage upon re-initialization of the system.")
_IpTrafficStats_ObjectIdentity = ObjectIdentity
ipTrafficStats = _IpTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 31)
)
_IpSystemStatsTable_Object = MibTable
ipSystemStatsTable = _IpSystemStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1)
)
if mibBuilder.loadTexts:
    ipSystemStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsTable.setDescription("The table containing system wide, IP version specific traffic statistics. This table and the ipIfStatsTable contain similar objects whose difference is in their granularity. Where this table contains system wide traffic statistics, the ipIfStatsTable contains the same statistics but counted on a per-interface basis.")
_IpSystemStatsEntry_Object = MibTableRow
ipSystemStatsEntry = _IpSystemStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1)
)
ipSystemStatsEntry.setIndexNames(
    (0, "IP-MIB", "ipSystemStatsIPVersion"),
)
if mibBuilder.loadTexts:
    ipSystemStatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsEntry.setDescription("A statistics entry containing system-wide objects for a particular IP version.")
_IpSystemStatsIPVersion_Type = InetVersion
_IpSystemStatsIPVersion_Object = MibTableColumn
ipSystemStatsIPVersion = _IpSystemStatsIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 1),
    _IpSystemStatsIPVersion_Type()
)
ipSystemStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSystemStatsIPVersion.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsIPVersion.setDescription("The IP version of this row.")
_IpSystemStatsInReceives_Type = Counter32
_IpSystemStatsInReceives_Object = MibTableColumn
ipSystemStatsInReceives = _IpSystemStatsInReceives_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 3),
    _IpSystemStatsInReceives_Type()
)
ipSystemStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInReceives.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInReceives.setDescription("The total number of input IP datagrams received, including those received in error. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCInReceives_Type = Counter64
_IpSystemStatsHCInReceives_Object = MibTableColumn
ipSystemStatsHCInReceives = _IpSystemStatsHCInReceives_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 4),
    _IpSystemStatsHCInReceives_Type()
)
ipSystemStatsHCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCInReceives.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCInReceives.setDescription("The total number of input IP datagrams received, including those received in error. This object counts the same datagrams as ipSystemStatsInReceives, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInOctets_Type = Counter32
_IpSystemStatsInOctets_Object = MibTableColumn
ipSystemStatsInOctets = _IpSystemStatsInOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 5),
    _IpSystemStatsInOctets_Type()
)
ipSystemStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInOctets.setDescription("The total number of octets received in input IP datagrams, including those received in error. Octets from datagrams counted in ipSystemStatsInReceives MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCInOctets_Type = Counter64
_IpSystemStatsHCInOctets_Object = MibTableColumn
ipSystemStatsHCInOctets = _IpSystemStatsHCInOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 6),
    _IpSystemStatsHCInOctets_Type()
)
ipSystemStatsHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCInOctets.setDescription("The total number of octets received in input IP datagrams, including those received in error. This object counts the same octets as ipSystemStatsInOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInHdrErrors_Type = Counter32
_IpSystemStatsInHdrErrors_Object = MibTableColumn
ipSystemStatsInHdrErrors = _IpSystemStatsInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 7),
    _IpSystemStatsInHdrErrors_Type()
)
ipSystemStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInHdrErrors.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInHdrErrors.setDescription("The number of input IP datagrams discarded due to errors in their IP headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IP options, etc. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInNoRoutes_Type = Counter32
_IpSystemStatsInNoRoutes_Object = MibTableColumn
ipSystemStatsInNoRoutes = _IpSystemStatsInNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 8),
    _IpSystemStatsInNoRoutes_Type()
)
ipSystemStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInNoRoutes.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInNoRoutes.setDescription("The number of input IP datagrams discarded because no route could be found to transmit them to their destination. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInAddrErrors_Type = Counter32
_IpSystemStatsInAddrErrors_Object = MibTableColumn
ipSystemStatsInAddrErrors = _IpSystemStatsInAddrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 9),
    _IpSystemStatsInAddrErrors_Type()
)
ipSystemStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInAddrErrors.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInAddrErrors.setDescription("The number of input IP datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity. This count includes invalid addresses (e.g., ::0). For entities that are not IP routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInUnknownProtos_Type = Counter32
_IpSystemStatsInUnknownProtos_Object = MibTableColumn
ipSystemStatsInUnknownProtos = _IpSystemStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 10),
    _IpSystemStatsInUnknownProtos_Type()
)
ipSystemStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInUnknownProtos.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInUnknownProtos.setDescription("The number of locally-addressed IP datagrams received successfully but discarded because of an unknown or unsupported protocol. When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented. This interface might not be the same as the input interface for some of the datagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInTruncatedPkts_Type = Counter32
_IpSystemStatsInTruncatedPkts_Object = MibTableColumn
ipSystemStatsInTruncatedPkts = _IpSystemStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 11),
    _IpSystemStatsInTruncatedPkts_Type()
)
ipSystemStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInTruncatedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInTruncatedPkts.setDescription("The number of input IP datagrams discarded because the datagram frame didn't carry enough data. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInForwDatagrams_Type = Counter32
_IpSystemStatsInForwDatagrams_Object = MibTableColumn
ipSystemStatsInForwDatagrams = _IpSystemStatsInForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 12),
    _IpSystemStatsInForwDatagrams_Type()
)
ipSystemStatsInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInForwDatagrams.setDescription("The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination. In entities that do not act as IP routers, this counter will include only those datagrams that were Source-Routed via this entity, and the Source-Route processing was successful. When tracking interface statistics, the counter of the incoming interface is incremented for each datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCInForwDatagrams_Type = Counter64
_IpSystemStatsHCInForwDatagrams_Object = MibTableColumn
ipSystemStatsHCInForwDatagrams = _IpSystemStatsHCInForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 13),
    _IpSystemStatsHCInForwDatagrams_Type()
)
ipSystemStatsHCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCInForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCInForwDatagrams.setDescription("The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination. This object counts the same packets as ipSystemStatsInForwDatagrams, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsReasmReqds_Type = Counter32
_IpSystemStatsReasmReqds_Object = MibTableColumn
ipSystemStatsReasmReqds = _IpSystemStatsReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 14),
    _IpSystemStatsReasmReqds_Type()
)
ipSystemStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsReasmReqds.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsReasmReqds.setDescription("The number of IP fragments received that needed to be reassembled at this interface. When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented. This interface might not be the same as the input interface for some of the fragments. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsReasmOKs_Type = Counter32
_IpSystemStatsReasmOKs_Object = MibTableColumn
ipSystemStatsReasmOKs = _IpSystemStatsReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 15),
    _IpSystemStatsReasmOKs_Type()
)
ipSystemStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsReasmOKs.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsReasmOKs.setDescription("The number of IP datagrams successfully reassembled. When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented. This interface might not be the same as the input interface for some of the datagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsReasmFails_Type = Counter32
_IpSystemStatsReasmFails_Object = MibTableColumn
ipSystemStatsReasmFails = _IpSystemStatsReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 16),
    _IpSystemStatsReasmFails_Type()
)
ipSystemStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsReasmFails.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsReasmFails.setDescription("The number of failures detected by the IP re-assembly algorithm (for whatever reason: timed out, errors, etc.). Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received. When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented. This interface might not be the same as the input interface for some of the fragments. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInDiscards_Type = Counter32
_IpSystemStatsInDiscards_Object = MibTableColumn
ipSystemStatsInDiscards = _IpSystemStatsInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 17),
    _IpSystemStatsInDiscards_Type()
)
ipSystemStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInDiscards.setDescription("The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space). Note that this counter does not include any datagrams discarded while awaiting re-assembly. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInDelivers_Type = Counter32
_IpSystemStatsInDelivers_Object = MibTableColumn
ipSystemStatsInDelivers = _IpSystemStatsInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 18),
    _IpSystemStatsInDelivers_Type()
)
ipSystemStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInDelivers.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInDelivers.setDescription("The total number of datagrams successfully delivered to IP user-protocols (including ICMP). When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented. This interface might not be the same as the input interface for some of the datagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCInDelivers_Type = Counter64
_IpSystemStatsHCInDelivers_Object = MibTableColumn
ipSystemStatsHCInDelivers = _IpSystemStatsHCInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 19),
    _IpSystemStatsHCInDelivers_Type()
)
ipSystemStatsHCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCInDelivers.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCInDelivers.setDescription("The total number of datagrams successfully delivered to IP user-protocols (including ICMP). This object counts the same packets as ipSystemStatsInDelivers, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutRequests_Type = Counter32
_IpSystemStatsOutRequests_Object = MibTableColumn
ipSystemStatsOutRequests = _IpSystemStatsOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 20),
    _IpSystemStatsOutRequests_Type()
)
ipSystemStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutRequests.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutRequests.setDescription("The total number of IP datagrams that local IP user- protocols (including ICMP) supplied to IP in requests for transmission. Note that this counter does not include any datagrams counted in ipSystemStatsOutForwDatagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCOutRequests_Type = Counter64
_IpSystemStatsHCOutRequests_Object = MibTableColumn
ipSystemStatsHCOutRequests = _IpSystemStatsHCOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 21),
    _IpSystemStatsHCOutRequests_Type()
)
ipSystemStatsHCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutRequests.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutRequests.setDescription("The total number of IP datagrams that local IP user- protocols (including ICMP) supplied to IP in requests for transmission. This object counts the same packets as ipSystemStatsOutRequests, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutNoRoutes_Type = Counter32
_IpSystemStatsOutNoRoutes_Object = MibTableColumn
ipSystemStatsOutNoRoutes = _IpSystemStatsOutNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 22),
    _IpSystemStatsOutNoRoutes_Type()
)
ipSystemStatsOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutNoRoutes.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutNoRoutes.setDescription("The number of locally generated IP datagrams discarded because no route could be found to transmit them to their destination. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutForwDatagrams_Type = Counter32
_IpSystemStatsOutForwDatagrams_Object = MibTableColumn
ipSystemStatsOutForwDatagrams = _IpSystemStatsOutForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 23),
    _IpSystemStatsOutForwDatagrams_Type()
)
ipSystemStatsOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutForwDatagrams.setDescription("The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination. In entities that do not act as IP routers, this counter will include only those datagrams that were Source-Routed via this entity, and the Source-Route processing was successful. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully forwarded datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCOutForwDatagrams_Type = Counter64
_IpSystemStatsHCOutForwDatagrams_Object = MibTableColumn
ipSystemStatsHCOutForwDatagrams = _IpSystemStatsHCOutForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 24),
    _IpSystemStatsHCOutForwDatagrams_Type()
)
ipSystemStatsHCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutForwDatagrams.setDescription("The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination. This object counts the same packets as ipSystemStatsOutForwDatagrams, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutDiscards_Type = Counter32
_IpSystemStatsOutDiscards_Object = MibTableColumn
ipSystemStatsOutDiscards = _IpSystemStatsOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 25),
    _IpSystemStatsOutDiscards_Type()
)
ipSystemStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutDiscards.setDescription("The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space). Note that this counter would include datagrams counted in ipSystemStatsOutForwDatagrams if any such datagrams met this (discretionary) discard criterion. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutFragReqds_Type = Counter32
_IpSystemStatsOutFragReqds_Object = MibTableColumn
ipSystemStatsOutFragReqds = _IpSystemStatsOutFragReqds_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 26),
    _IpSystemStatsOutFragReqds_Type()
)
ipSystemStatsOutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragReqds.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragReqds.setDescription("The number of IP datagrams that would require fragmentation in order to be transmitted. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutFragOKs_Type = Counter32
_IpSystemStatsOutFragOKs_Object = MibTableColumn
ipSystemStatsOutFragOKs = _IpSystemStatsOutFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 27),
    _IpSystemStatsOutFragOKs_Type()
)
ipSystemStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragOKs.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragOKs.setDescription("The number of IP datagrams that have been successfully fragmented. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutFragFails_Type = Counter32
_IpSystemStatsOutFragFails_Object = MibTableColumn
ipSystemStatsOutFragFails = _IpSystemStatsOutFragFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 28),
    _IpSystemStatsOutFragFails_Type()
)
ipSystemStatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragFails.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragFails.setDescription("The number of IP datagrams that have been discarded because they needed to be fragmented but could not be. This includes IPv4 packets that have the DF bit set and IPv6 packets that are being forwarded and exceed the outgoing link MTU. When tracking interface statistics, the counter of the outgoing interface is incremented for an unsuccessfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutFragCreates_Type = Counter32
_IpSystemStatsOutFragCreates_Object = MibTableColumn
ipSystemStatsOutFragCreates = _IpSystemStatsOutFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 29),
    _IpSystemStatsOutFragCreates_Type()
)
ipSystemStatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragCreates.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutFragCreates.setDescription("The number of output datagram fragments that have been generated as a result of IP fragmentation. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutTransmits_Type = Counter32
_IpSystemStatsOutTransmits_Object = MibTableColumn
ipSystemStatsOutTransmits = _IpSystemStatsOutTransmits_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 30),
    _IpSystemStatsOutTransmits_Type()
)
ipSystemStatsOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutTransmits.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutTransmits.setDescription("The total number of IP datagrams that this entity supplied to the lower layers for transmission. This includes datagrams generated locally and those forwarded by this entity. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCOutTransmits_Type = Counter64
_IpSystemStatsHCOutTransmits_Object = MibTableColumn
ipSystemStatsHCOutTransmits = _IpSystemStatsHCOutTransmits_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 31),
    _IpSystemStatsHCOutTransmits_Type()
)
ipSystemStatsHCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutTransmits.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutTransmits.setDescription("The total number of IP datagrams that this entity supplied to the lower layers for transmission. This object counts the same datagrams as ipSystemStatsOutTransmits, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutOctets_Type = Counter32
_IpSystemStatsOutOctets_Object = MibTableColumn
ipSystemStatsOutOctets = _IpSystemStatsOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 32),
    _IpSystemStatsOutOctets_Type()
)
ipSystemStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutOctets.setDescription("The total number of octets in IP datagrams delivered to the lower layers for transmission. Octets from datagrams counted in ipSystemStatsOutTransmits MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCOutOctets_Type = Counter64
_IpSystemStatsHCOutOctets_Object = MibTableColumn
ipSystemStatsHCOutOctets = _IpSystemStatsHCOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 33),
    _IpSystemStatsHCOutOctets_Type()
)
ipSystemStatsHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutOctets.setDescription("The total number of octets in IP datagrams delivered to the lower layers for transmission. This objects counts the same octets as ipSystemStatsOutOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInMcastPkts_Type = Counter32
_IpSystemStatsInMcastPkts_Object = MibTableColumn
ipSystemStatsInMcastPkts = _IpSystemStatsInMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 34),
    _IpSystemStatsInMcastPkts_Type()
)
ipSystemStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInMcastPkts.setDescription("The number of IP multicast datagrams received. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCInMcastPkts_Type = Counter64
_IpSystemStatsHCInMcastPkts_Object = MibTableColumn
ipSystemStatsHCInMcastPkts = _IpSystemStatsHCInMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 35),
    _IpSystemStatsHCInMcastPkts_Type()
)
ipSystemStatsHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCInMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCInMcastPkts.setDescription("The number of IP multicast datagrams received. This object counts the same datagrams as ipSystemStatsInMcastPkts but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInMcastOctets_Type = Counter32
_IpSystemStatsInMcastOctets_Object = MibTableColumn
ipSystemStatsInMcastOctets = _IpSystemStatsInMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 36),
    _IpSystemStatsInMcastOctets_Type()
)
ipSystemStatsInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInMcastOctets.setDescription("The total number of octets received in IP multicast datagrams. Octets from datagrams counted in ipSystemStatsInMcastPkts MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCInMcastOctets_Type = Counter64
_IpSystemStatsHCInMcastOctets_Object = MibTableColumn
ipSystemStatsHCInMcastOctets = _IpSystemStatsHCInMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 37),
    _IpSystemStatsHCInMcastOctets_Type()
)
ipSystemStatsHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCInMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCInMcastOctets.setDescription("The total number of octets received in IP multicast datagrams. This object counts the same octets as ipSystemStatsInMcastOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutMcastPkts_Type = Counter32
_IpSystemStatsOutMcastPkts_Object = MibTableColumn
ipSystemStatsOutMcastPkts = _IpSystemStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 38),
    _IpSystemStatsOutMcastPkts_Type()
)
ipSystemStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutMcastPkts.setDescription("The number of IP multicast datagrams transmitted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCOutMcastPkts_Type = Counter64
_IpSystemStatsHCOutMcastPkts_Object = MibTableColumn
ipSystemStatsHCOutMcastPkts = _IpSystemStatsHCOutMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 39),
    _IpSystemStatsHCOutMcastPkts_Type()
)
ipSystemStatsHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutMcastPkts.setDescription("The number of IP multicast datagrams transmitted. This object counts the same datagrams as ipSystemStatsOutMcastPkts, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutMcastOctets_Type = Counter32
_IpSystemStatsOutMcastOctets_Object = MibTableColumn
ipSystemStatsOutMcastOctets = _IpSystemStatsOutMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 40),
    _IpSystemStatsOutMcastOctets_Type()
)
ipSystemStatsOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutMcastOctets.setDescription("The total number of octets transmitted in IP multicast datagrams. Octets from datagrams counted in ipSystemStatsOutMcastPkts MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCOutMcastOctets_Type = Counter64
_IpSystemStatsHCOutMcastOctets_Object = MibTableColumn
ipSystemStatsHCOutMcastOctets = _IpSystemStatsHCOutMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 41),
    _IpSystemStatsHCOutMcastOctets_Type()
)
ipSystemStatsHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutMcastOctets.setDescription("The total number of octets transmitted in IP multicast datagrams. This object counts the same octets as ipSystemStatsOutMcastOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsInBcastPkts_Type = Counter32
_IpSystemStatsInBcastPkts_Object = MibTableColumn
ipSystemStatsInBcastPkts = _IpSystemStatsInBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 42),
    _IpSystemStatsInBcastPkts_Type()
)
ipSystemStatsInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsInBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsInBcastPkts.setDescription("The number of IP broadcast datagrams received. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCInBcastPkts_Type = Counter64
_IpSystemStatsHCInBcastPkts_Object = MibTableColumn
ipSystemStatsHCInBcastPkts = _IpSystemStatsHCInBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 43),
    _IpSystemStatsHCInBcastPkts_Type()
)
ipSystemStatsHCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCInBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCInBcastPkts.setDescription("The number of IP broadcast datagrams received. This object counts the same datagrams as ipSystemStatsInBcastPkts but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsOutBcastPkts_Type = Counter32
_IpSystemStatsOutBcastPkts_Object = MibTableColumn
ipSystemStatsOutBcastPkts = _IpSystemStatsOutBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 44),
    _IpSystemStatsOutBcastPkts_Type()
)
ipSystemStatsOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsOutBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsOutBcastPkts.setDescription("The number of IP broadcast datagrams transmitted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsHCOutBcastPkts_Type = Counter64
_IpSystemStatsHCOutBcastPkts_Object = MibTableColumn
ipSystemStatsHCOutBcastPkts = _IpSystemStatsHCOutBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 45),
    _IpSystemStatsHCOutBcastPkts_Type()
)
ipSystemStatsHCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOutBcastPkts.setDescription("The number of IP broadcast datagrams transmitted. This object counts the same datagrams as ipSystemStatsOutBcastPkts, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime.")
_IpSystemStatsDiscontinuityTime_Type = TimeStamp
_IpSystemStatsDiscontinuityTime_Object = MibTableColumn
ipSystemStatsDiscontinuityTime = _IpSystemStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 46),
    _IpSystemStatsDiscontinuityTime_Type()
)
ipSystemStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsDiscontinuityTime.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity. If no such discontinuities have occurred since the last re- initialization of the local management subsystem, then this object contains a zero value.")
_IpSystemStatsRefreshRate_Type = Unsigned32
_IpSystemStatsRefreshRate_Object = MibTableColumn
ipSystemStatsRefreshRate = _IpSystemStatsRefreshRate_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 1, 1, 47),
    _IpSystemStatsRefreshRate_Type()
)
ipSystemStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSystemStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsRefreshRate.setUnits("milli-seconds")
if mibBuilder.loadTexts:
    ipSystemStatsRefreshRate.setDescription("The minimum reasonable polling interval for this entry. This object provides an indication of the minimum amount of time required to update the counters in this entry.")
_IpIfStatsTableLastChange_Type = TimeStamp
_IpIfStatsTableLastChange_Object = MibScalar
ipIfStatsTableLastChange = _IpIfStatsTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 2),
    _IpIfStatsTableLastChange_Type()
)
ipIfStatsTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsTableLastChange.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsTableLastChange.setDescription("The value of sysUpTime on the most recent occasion at which a row in the ipIfStatsTable was added or deleted. If new objects are added to the ipIfStatsTable that require the ipIfStatsTableLastChange to be updated when they are modified, they must specify that requirement in their description clause.")
_IpIfStatsTable_Object = MibTable
ipIfStatsTable = _IpIfStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3)
)
if mibBuilder.loadTexts:
    ipIfStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsTable.setDescription("The table containing per-interface traffic statistics. This table and the ipSystemStatsTable contain similar objects whose difference is in their granularity. Where this table contains per-interface statistics, the ipSystemStatsTable contains the same statistics, but counted on a system wide basis.")
_IpIfStatsEntry_Object = MibTableRow
ipIfStatsEntry = _IpIfStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1)
)
ipIfStatsEntry.setIndexNames(
    (0, "IP-MIB", "ipIfStatsIPVersion"),
    (0, "IP-MIB", "ipIfStatsIfIndex"),
)
if mibBuilder.loadTexts:
    ipIfStatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsEntry.setDescription("An interface statistics entry containing objects for a particular interface and version of IP.")
_IpIfStatsIPVersion_Type = InetVersion
_IpIfStatsIPVersion_Object = MibTableColumn
ipIfStatsIPVersion = _IpIfStatsIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 1),
    _IpIfStatsIPVersion_Type()
)
ipIfStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipIfStatsIPVersion.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsIPVersion.setDescription("The IP version of this row.")
_IpIfStatsIfIndex_Type = InterfaceIndex
_IpIfStatsIfIndex_Object = MibTableColumn
ipIfStatsIfIndex = _IpIfStatsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 2),
    _IpIfStatsIfIndex_Type()
)
ipIfStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipIfStatsIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsIfIndex.setDescription("The index value that uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")
_IpIfStatsInReceives_Type = Counter32
_IpIfStatsInReceives_Object = MibTableColumn
ipIfStatsInReceives = _IpIfStatsInReceives_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 3),
    _IpIfStatsInReceives_Type()
)
ipIfStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInReceives.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInReceives.setDescription("The total number of input IP datagrams received, including those received in error. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCInReceives_Type = Counter64
_IpIfStatsHCInReceives_Object = MibTableColumn
ipIfStatsHCInReceives = _IpIfStatsHCInReceives_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 4),
    _IpIfStatsHCInReceives_Type()
)
ipIfStatsHCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCInReceives.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCInReceives.setDescription("The total number of input IP datagrams received, including those received in error. This object counts the same datagrams as ipIfStatsInReceives, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInOctets_Type = Counter32
_IpIfStatsInOctets_Object = MibTableColumn
ipIfStatsInOctets = _IpIfStatsInOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 5),
    _IpIfStatsInOctets_Type()
)
ipIfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInOctets.setDescription("The total number of octets received in input IP datagrams, including those received in error. Octets from datagrams counted in ipIfStatsInReceives MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCInOctets_Type = Counter64
_IpIfStatsHCInOctets_Object = MibTableColumn
ipIfStatsHCInOctets = _IpIfStatsHCInOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 6),
    _IpIfStatsHCInOctets_Type()
)
ipIfStatsHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCInOctets.setDescription("The total number of octets received in input IP datagrams, including those received in error. This object counts the same octets as ipIfStatsInOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInHdrErrors_Type = Counter32
_IpIfStatsInHdrErrors_Object = MibTableColumn
ipIfStatsInHdrErrors = _IpIfStatsInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 7),
    _IpIfStatsInHdrErrors_Type()
)
ipIfStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInHdrErrors.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInHdrErrors.setDescription("The number of input IP datagrams discarded due to errors in their IP headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IP options, etc. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInNoRoutes_Type = Counter32
_IpIfStatsInNoRoutes_Object = MibTableColumn
ipIfStatsInNoRoutes = _IpIfStatsInNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 8),
    _IpIfStatsInNoRoutes_Type()
)
ipIfStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInNoRoutes.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInNoRoutes.setDescription("The number of input IP datagrams discarded because no route could be found to transmit them to their destination. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInAddrErrors_Type = Counter32
_IpIfStatsInAddrErrors_Object = MibTableColumn
ipIfStatsInAddrErrors = _IpIfStatsInAddrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 9),
    _IpIfStatsInAddrErrors_Type()
)
ipIfStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInAddrErrors.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInAddrErrors.setDescription("The number of input IP datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity. This count includes invalid addresses (e.g., ::0). For entities that are not IP routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInUnknownProtos_Type = Counter32
_IpIfStatsInUnknownProtos_Object = MibTableColumn
ipIfStatsInUnknownProtos = _IpIfStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 10),
    _IpIfStatsInUnknownProtos_Type()
)
ipIfStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInUnknownProtos.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInUnknownProtos.setDescription("The number of locally-addressed IP datagrams received successfully but discarded because of an unknown or unsupported protocol. When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented. This interface might not be the same as the input interface for some of the datagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInTruncatedPkts_Type = Counter32
_IpIfStatsInTruncatedPkts_Object = MibTableColumn
ipIfStatsInTruncatedPkts = _IpIfStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 11),
    _IpIfStatsInTruncatedPkts_Type()
)
ipIfStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInTruncatedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInTruncatedPkts.setDescription("The number of input IP datagrams discarded because the datagram frame didn't carry enough data. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInForwDatagrams_Type = Counter32
_IpIfStatsInForwDatagrams_Object = MibTableColumn
ipIfStatsInForwDatagrams = _IpIfStatsInForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 12),
    _IpIfStatsInForwDatagrams_Type()
)
ipIfStatsInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInForwDatagrams.setDescription("The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination. In entities that do not act as IP routers, this counter will include only those datagrams that were Source-Routed via this entity, and the Source-Route processing was successful. When tracking interface statistics, the counter of the incoming interface is incremented for each datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCInForwDatagrams_Type = Counter64
_IpIfStatsHCInForwDatagrams_Object = MibTableColumn
ipIfStatsHCInForwDatagrams = _IpIfStatsHCInForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 13),
    _IpIfStatsHCInForwDatagrams_Type()
)
ipIfStatsHCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCInForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCInForwDatagrams.setDescription("The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination. This object counts the same packets as ipIfStatsInForwDatagrams, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsReasmReqds_Type = Counter32
_IpIfStatsReasmReqds_Object = MibTableColumn
ipIfStatsReasmReqds = _IpIfStatsReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 14),
    _IpIfStatsReasmReqds_Type()
)
ipIfStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsReasmReqds.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsReasmReqds.setDescription("The number of IP fragments received that needed to be reassembled at this interface. When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented. This interface might not be the same as the input interface for some of the fragments. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsReasmOKs_Type = Counter32
_IpIfStatsReasmOKs_Object = MibTableColumn
ipIfStatsReasmOKs = _IpIfStatsReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 15),
    _IpIfStatsReasmOKs_Type()
)
ipIfStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsReasmOKs.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsReasmOKs.setDescription("The number of IP datagrams successfully reassembled. When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented. This interface might not be the same as the input interface for some of the datagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsReasmFails_Type = Counter32
_IpIfStatsReasmFails_Object = MibTableColumn
ipIfStatsReasmFails = _IpIfStatsReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 16),
    _IpIfStatsReasmFails_Type()
)
ipIfStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsReasmFails.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsReasmFails.setDescription("The number of failures detected by the IP re-assembly algorithm (for whatever reason: timed out, errors, etc.). Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received. When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented. This interface might not be the same as the input interface for some of the fragments. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInDiscards_Type = Counter32
_IpIfStatsInDiscards_Object = MibTableColumn
ipIfStatsInDiscards = _IpIfStatsInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 17),
    _IpIfStatsInDiscards_Type()
)
ipIfStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInDiscards.setDescription("The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space). Note that this counter does not include any datagrams discarded while awaiting re-assembly. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInDelivers_Type = Counter32
_IpIfStatsInDelivers_Object = MibTableColumn
ipIfStatsInDelivers = _IpIfStatsInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 18),
    _IpIfStatsInDelivers_Type()
)
ipIfStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInDelivers.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInDelivers.setDescription("The total number of datagrams successfully delivered to IP user-protocols (including ICMP). When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented. This interface might not be the same as the input interface for some of the datagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCInDelivers_Type = Counter64
_IpIfStatsHCInDelivers_Object = MibTableColumn
ipIfStatsHCInDelivers = _IpIfStatsHCInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 19),
    _IpIfStatsHCInDelivers_Type()
)
ipIfStatsHCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCInDelivers.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCInDelivers.setDescription("The total number of datagrams successfully delivered to IP user-protocols (including ICMP). This object counts the same packets as ipIfStatsInDelivers, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutRequests_Type = Counter32
_IpIfStatsOutRequests_Object = MibTableColumn
ipIfStatsOutRequests = _IpIfStatsOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 20),
    _IpIfStatsOutRequests_Type()
)
ipIfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutRequests.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutRequests.setDescription("The total number of IP datagrams that local IP user- protocols (including ICMP) supplied to IP in requests for transmission. Note that this counter does not include any datagrams counted in ipIfStatsOutForwDatagrams. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCOutRequests_Type = Counter64
_IpIfStatsHCOutRequests_Object = MibTableColumn
ipIfStatsHCOutRequests = _IpIfStatsHCOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 21),
    _IpIfStatsHCOutRequests_Type()
)
ipIfStatsHCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCOutRequests.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOutRequests.setDescription("The total number of IP datagrams that local IP user- protocols (including ICMP) supplied to IP in requests for transmission. This object counts the same packets as ipIfStatsOutRequests, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutForwDatagrams_Type = Counter32
_IpIfStatsOutForwDatagrams_Object = MibTableColumn
ipIfStatsOutForwDatagrams = _IpIfStatsOutForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 23),
    _IpIfStatsOutForwDatagrams_Type()
)
ipIfStatsOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutForwDatagrams.setDescription("The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination. In entities that do not act as IP routers, this counter will include only those datagrams that were Source-Routed via this entity, and the Source-Route processing was successful. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully forwarded datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCOutForwDatagrams_Type = Counter64
_IpIfStatsHCOutForwDatagrams_Object = MibTableColumn
ipIfStatsHCOutForwDatagrams = _IpIfStatsHCOutForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 24),
    _IpIfStatsHCOutForwDatagrams_Type()
)
ipIfStatsHCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCOutForwDatagrams.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOutForwDatagrams.setDescription("The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination. This object counts the same packets as ipIfStatsOutForwDatagrams, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutDiscards_Type = Counter32
_IpIfStatsOutDiscards_Object = MibTableColumn
ipIfStatsOutDiscards = _IpIfStatsOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 25),
    _IpIfStatsOutDiscards_Type()
)
ipIfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutDiscards.setDescription("The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space). Note that this counter would include datagrams counted in ipIfStatsOutForwDatagrams if any such datagrams met this (discretionary) discard criterion. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutFragReqds_Type = Counter32
_IpIfStatsOutFragReqds_Object = MibTableColumn
ipIfStatsOutFragReqds = _IpIfStatsOutFragReqds_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 26),
    _IpIfStatsOutFragReqds_Type()
)
ipIfStatsOutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutFragReqds.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutFragReqds.setDescription("The number of IP datagrams that would require fragmentation in order to be transmitted. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutFragOKs_Type = Counter32
_IpIfStatsOutFragOKs_Object = MibTableColumn
ipIfStatsOutFragOKs = _IpIfStatsOutFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 27),
    _IpIfStatsOutFragOKs_Type()
)
ipIfStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutFragOKs.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutFragOKs.setDescription("The number of IP datagrams that have been successfully fragmented. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutFragFails_Type = Counter32
_IpIfStatsOutFragFails_Object = MibTableColumn
ipIfStatsOutFragFails = _IpIfStatsOutFragFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 28),
    _IpIfStatsOutFragFails_Type()
)
ipIfStatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutFragFails.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutFragFails.setDescription("The number of IP datagrams that have been discarded because they needed to be fragmented but could not be. This includes IPv4 packets that have the DF bit set and IPv6 packets that are being forwarded and exceed the outgoing link MTU. When tracking interface statistics, the counter of the outgoing interface is incremented for an unsuccessfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutFragCreates_Type = Counter32
_IpIfStatsOutFragCreates_Object = MibTableColumn
ipIfStatsOutFragCreates = _IpIfStatsOutFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 29),
    _IpIfStatsOutFragCreates_Type()
)
ipIfStatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutFragCreates.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutFragCreates.setDescription("The number of output datagram fragments that have been generated as a result of IP fragmentation. When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutTransmits_Type = Counter32
_IpIfStatsOutTransmits_Object = MibTableColumn
ipIfStatsOutTransmits = _IpIfStatsOutTransmits_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 30),
    _IpIfStatsOutTransmits_Type()
)
ipIfStatsOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutTransmits.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutTransmits.setDescription("The total number of IP datagrams that this entity supplied to the lower layers for transmission. This includes datagrams generated locally and those forwarded by this entity. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCOutTransmits_Type = Counter64
_IpIfStatsHCOutTransmits_Object = MibTableColumn
ipIfStatsHCOutTransmits = _IpIfStatsHCOutTransmits_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 31),
    _IpIfStatsHCOutTransmits_Type()
)
ipIfStatsHCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCOutTransmits.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOutTransmits.setDescription("The total number of IP datagrams that this entity supplied to the lower layers for transmission. This object counts the same datagrams as ipIfStatsOutTransmits, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutOctets_Type = Counter32
_IpIfStatsOutOctets_Object = MibTableColumn
ipIfStatsOutOctets = _IpIfStatsOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 32),
    _IpIfStatsOutOctets_Type()
)
ipIfStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutOctets.setDescription("The total number of octets in IP datagrams delivered to the lower layers for transmission. Octets from datagrams counted in ipIfStatsOutTransmits MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCOutOctets_Type = Counter64
_IpIfStatsHCOutOctets_Object = MibTableColumn
ipIfStatsHCOutOctets = _IpIfStatsHCOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 33),
    _IpIfStatsHCOutOctets_Type()
)
ipIfStatsHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOutOctets.setDescription("The total number of octets in IP datagrams delivered to the lower layers for transmission. This objects counts the same octets as ipIfStatsOutOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInMcastPkts_Type = Counter32
_IpIfStatsInMcastPkts_Object = MibTableColumn
ipIfStatsInMcastPkts = _IpIfStatsInMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 34),
    _IpIfStatsInMcastPkts_Type()
)
ipIfStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInMcastPkts.setDescription("The number of IP multicast datagrams received. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCInMcastPkts_Type = Counter64
_IpIfStatsHCInMcastPkts_Object = MibTableColumn
ipIfStatsHCInMcastPkts = _IpIfStatsHCInMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 35),
    _IpIfStatsHCInMcastPkts_Type()
)
ipIfStatsHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCInMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCInMcastPkts.setDescription("The number of IP multicast datagrams received. This object counts the same datagrams as ipIfStatsInMcastPkts, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInMcastOctets_Type = Counter32
_IpIfStatsInMcastOctets_Object = MibTableColumn
ipIfStatsInMcastOctets = _IpIfStatsInMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 36),
    _IpIfStatsInMcastOctets_Type()
)
ipIfStatsInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInMcastOctets.setDescription("The total number of octets received in IP multicast datagrams. Octets from datagrams counted in ipIfStatsInMcastPkts MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCInMcastOctets_Type = Counter64
_IpIfStatsHCInMcastOctets_Object = MibTableColumn
ipIfStatsHCInMcastOctets = _IpIfStatsHCInMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 37),
    _IpIfStatsHCInMcastOctets_Type()
)
ipIfStatsHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCInMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCInMcastOctets.setDescription("The total number of octets received in IP multicast datagrams. This object counts the same octets as ipIfStatsInMcastOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutMcastPkts_Type = Counter32
_IpIfStatsOutMcastPkts_Object = MibTableColumn
ipIfStatsOutMcastPkts = _IpIfStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 38),
    _IpIfStatsOutMcastPkts_Type()
)
ipIfStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutMcastPkts.setDescription("The number of IP multicast datagrams transmitted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCOutMcastPkts_Type = Counter64
_IpIfStatsHCOutMcastPkts_Object = MibTableColumn
ipIfStatsHCOutMcastPkts = _IpIfStatsHCOutMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 39),
    _IpIfStatsHCOutMcastPkts_Type()
)
ipIfStatsHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCOutMcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOutMcastPkts.setDescription("The number of IP multicast datagrams transmitted. This object counts the same datagrams as ipIfStatsOutMcastPkts, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutMcastOctets_Type = Counter32
_IpIfStatsOutMcastOctets_Object = MibTableColumn
ipIfStatsOutMcastOctets = _IpIfStatsOutMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 40),
    _IpIfStatsOutMcastOctets_Type()
)
ipIfStatsOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutMcastOctets.setDescription("The total number of octets transmitted in IP multicast datagrams. Octets from datagrams counted in ipIfStatsOutMcastPkts MUST be counted here. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCOutMcastOctets_Type = Counter64
_IpIfStatsHCOutMcastOctets_Object = MibTableColumn
ipIfStatsHCOutMcastOctets = _IpIfStatsHCOutMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 41),
    _IpIfStatsHCOutMcastOctets_Type()
)
ipIfStatsHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCOutMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOutMcastOctets.setDescription("The total number of octets transmitted in IP multicast datagrams. This object counts the same octets as ipIfStatsOutMcastOctets, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsInBcastPkts_Type = Counter32
_IpIfStatsInBcastPkts_Object = MibTableColumn
ipIfStatsInBcastPkts = _IpIfStatsInBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 42),
    _IpIfStatsInBcastPkts_Type()
)
ipIfStatsInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsInBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsInBcastPkts.setDescription("The number of IP broadcast datagrams received. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCInBcastPkts_Type = Counter64
_IpIfStatsHCInBcastPkts_Object = MibTableColumn
ipIfStatsHCInBcastPkts = _IpIfStatsHCInBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 43),
    _IpIfStatsHCInBcastPkts_Type()
)
ipIfStatsHCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCInBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCInBcastPkts.setDescription("The number of IP broadcast datagrams received. This object counts the same datagrams as ipIfStatsInBcastPkts, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsOutBcastPkts_Type = Counter32
_IpIfStatsOutBcastPkts_Object = MibTableColumn
ipIfStatsOutBcastPkts = _IpIfStatsOutBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 44),
    _IpIfStatsOutBcastPkts_Type()
)
ipIfStatsOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsOutBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsOutBcastPkts.setDescription("The number of IP broadcast datagrams transmitted. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsHCOutBcastPkts_Type = Counter64
_IpIfStatsHCOutBcastPkts_Object = MibTableColumn
ipIfStatsHCOutBcastPkts = _IpIfStatsHCOutBcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 45),
    _IpIfStatsHCOutBcastPkts_Type()
)
ipIfStatsHCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsHCOutBcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOutBcastPkts.setDescription("The number of IP broadcast datagrams transmitted. This object counts the same datagrams as ipIfStatsOutBcastPkts, but allows for larger values. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime.")
_IpIfStatsDiscontinuityTime_Type = TimeStamp
_IpIfStatsDiscontinuityTime_Object = MibTableColumn
ipIfStatsDiscontinuityTime = _IpIfStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 46),
    _IpIfStatsDiscontinuityTime_Type()
)
ipIfStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsDiscontinuityTime.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity. If no such discontinuities have occurred since the last re- initialization of the local management subsystem, then this object contains a zero value.")
_IpIfStatsRefreshRate_Type = Unsigned32
_IpIfStatsRefreshRate_Object = MibTableColumn
ipIfStatsRefreshRate = _IpIfStatsRefreshRate_Object(
    (1, 3, 6, 1, 2, 1, 4, 31, 3, 1, 47),
    _IpIfStatsRefreshRate_Type()
)
ipIfStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsRefreshRate.setUnits("milli-seconds")
if mibBuilder.loadTexts:
    ipIfStatsRefreshRate.setDescription("The minimum reasonable polling interval for this entry. This object provides an indication of the minimum amount of time required to update the counters in this entry.")
_IpAddressPrefixTable_Object = MibTable
ipAddressPrefixTable = _IpAddressPrefixTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 32)
)
if mibBuilder.loadTexts:
    ipAddressPrefixTable.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixTable.setDescription("This table allows the user to determine the source of an IP address or set of IP addresses, and allows other tables to share the information via pointer rather than by copying. For example, when the node configures both a unicast and anycast address for a prefix, the ipAddressPrefix objects for those addresses will point to a single row in this table. This table primarily provides support for IPv6 prefixes, and several of the objects are less meaningful for IPv4. The table continues to allow IPv4 addresses to allow future flexibility. In order to promote a common configuration, this document includes suggestions for default values for IPv4 prefixes. Each of these values may be overridden if an object is meaningful to the node. All prefixes used by this entity should be included in this table independent of how the entity learned the prefix. (This table isn't limited to prefixes learned from router advertisements.)")
_IpAddressPrefixEntry_Object = MibTableRow
ipAddressPrefixEntry = _IpAddressPrefixEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1)
)
ipAddressPrefixEntry.setIndexNames(
    (0, "IP-MIB", "ipAddressPrefixIfIndex"),
    (0, "IP-MIB", "ipAddressPrefixType"),
    (0, "IP-MIB", "ipAddressPrefixPrefix"),
    (0, "IP-MIB", "ipAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    ipAddressPrefixEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixEntry.setDescription("An entry in the ipAddressPrefixTable.")
_IpAddressPrefixIfIndex_Type = InterfaceIndex
_IpAddressPrefixIfIndex_Object = MibTableColumn
ipAddressPrefixIfIndex = _IpAddressPrefixIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 1),
    _IpAddressPrefixIfIndex_Type()
)
ipAddressPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressPrefixIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixIfIndex.setDescription("The index value that uniquely identifies the interface on which this prefix is configured. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")
_IpAddressPrefixType_Type = InetAddressType
_IpAddressPrefixType_Object = MibTableColumn
ipAddressPrefixType = _IpAddressPrefixType_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 2),
    _IpAddressPrefixType_Type()
)
ipAddressPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressPrefixType.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixType.setDescription("The address type of ipAddressPrefix.")
_IpAddressPrefixPrefix_Type = InetAddress
_IpAddressPrefixPrefix_Object = MibTableColumn
ipAddressPrefixPrefix = _IpAddressPrefixPrefix_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 3),
    _IpAddressPrefixPrefix_Type()
)
ipAddressPrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressPrefixPrefix.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixPrefix.setDescription("The address prefix. The address type of this object is specified in ipAddressPrefixType. The length of this object is the standard length for objects of that type (4 or 16 bytes). Any bits after ipAddressPrefixLength must be zero. Implementors need to be aware that, if the size of ipAddressPrefixPrefix exceeds 114 octets, then OIDS of instances of columns in this row will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
_IpAddressPrefixLength_Type = InetAddressPrefixLength
_IpAddressPrefixLength_Object = MibTableColumn
ipAddressPrefixLength = _IpAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 4),
    _IpAddressPrefixLength_Type()
)
ipAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixLength.setDescription("The prefix length associated with this prefix. The value 0 has no special meaning for this object. It simply refers to address '::/0'.")
_IpAddressPrefixOrigin_Type = IpAddressPrefixOriginTC
_IpAddressPrefixOrigin_Object = MibTableColumn
ipAddressPrefixOrigin = _IpAddressPrefixOrigin_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 5),
    _IpAddressPrefixOrigin_Type()
)
ipAddressPrefixOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPrefixOrigin.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixOrigin.setDescription("The origin of this prefix.")
_IpAddressPrefixOnLinkFlag_Type = TruthValue
_IpAddressPrefixOnLinkFlag_Object = MibTableColumn
ipAddressPrefixOnLinkFlag = _IpAddressPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 6),
    _IpAddressPrefixOnLinkFlag_Type()
)
ipAddressPrefixOnLinkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPrefixOnLinkFlag.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixOnLinkFlag.setReference("For IPv6 RFC 2461, especially sections 2 and 4.6.2 and RFC 2462")
if mibBuilder.loadTexts:
    ipAddressPrefixOnLinkFlag.setDescription("This object has the value 'true(1)', if this prefix can be used for on-link determination; otherwise, the value is 'false(2)'. The default for IPv4 prefixes is 'true(1)'.")
_IpAddressPrefixAutonomousFlag_Type = TruthValue
_IpAddressPrefixAutonomousFlag_Object = MibTableColumn
ipAddressPrefixAutonomousFlag = _IpAddressPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 7),
    _IpAddressPrefixAutonomousFlag_Type()
)
ipAddressPrefixAutonomousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPrefixAutonomousFlag.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixAutonomousFlag.setReference("For IPv6 RFC 2461, especially sections 2 and 4.6.2 and RFC 2462")
if mibBuilder.loadTexts:
    ipAddressPrefixAutonomousFlag.setDescription("Autonomous address configuration flag. When true(1), indicates that this prefix can be used for autonomous address configuration (i.e., can be used to form a local interface address). If false(2), it is not used to auto- configure a local interface address. The default for IPv4 prefixes is 'false(2)'.")
_IpAddressPrefixAdvPreferredLifetime_Type = Unsigned32
_IpAddressPrefixAdvPreferredLifetime_Object = MibTableColumn
ipAddressPrefixAdvPreferredLifetime = _IpAddressPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 8),
    _IpAddressPrefixAdvPreferredLifetime_Type()
)
ipAddressPrefixAdvPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvPreferredLifetime.setUnits("seconds")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvPreferredLifetime.setReference("For IPv6 RFC 2461, especially sections 2 and 4.6.2 and RFC 2462")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvPreferredLifetime.setDescription("The remaining length of time, in seconds, that this prefix will continue to be preferred, i.e., time until deprecation. A value of 4,294,967,295 represents infinity. The address generated from a deprecated prefix should no longer be used as a source address in new communications, but packets received on such an interface are processed as expected. The default for IPv4 prefixes is 4,294,967,295 (infinity).")
_IpAddressPrefixAdvValidLifetime_Type = Unsigned32
_IpAddressPrefixAdvValidLifetime_Object = MibTableColumn
ipAddressPrefixAdvValidLifetime = _IpAddressPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 2, 1, 4, 32, 1, 9),
    _IpAddressPrefixAdvValidLifetime_Type()
)
ipAddressPrefixAdvValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvValidLifetime.setUnits("seconds")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvValidLifetime.setReference("For IPv6 RFC 2461, especially sections 2 and 4.6.2 and RFC 2462")
if mibBuilder.loadTexts:
    ipAddressPrefixAdvValidLifetime.setDescription("The remaining length of time, in seconds, that this prefix will continue to be valid, i.e., time until invalidation. A value of 4,294,967,295 represents infinity. The address generated from an invalidated prefix should not appear as the destination or source address of a packet. The default for IPv4 prefixes is 4,294,967,295 (infinity).")
_IpAddressSpinLock_Type = TestAndIncr
_IpAddressSpinLock_Object = MibScalar
ipAddressSpinLock = _IpAddressSpinLock_Object(
    (1, 3, 6, 1, 2, 1, 4, 33),
    _IpAddressSpinLock_Type()
)
ipAddressSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressSpinLock.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressSpinLock.setDescription("An advisory lock used to allow cooperating SNMP managers to coordinate their use of the set operation in creating or modifying rows within this table. In order to use this lock to coordinate the use of set operations, managers should first retrieve ipAddressTableSpinLock. They should then determine the appropriate row to create or modify. Finally, they should issue the appropriate set command, including the retrieved value of ipAddressSpinLock. If another manager has altered the table in the meantime, then the value of ipAddressSpinLock will have changed, and the creation will fail as it will be specifying an incorrect value for ipAddressSpinLock. It is suggested, but not required, that the ipAddressSpinLock be the first var bind for each set of objects representing a 'row' in a PDU.")
_IpAddressTable_Object = MibTable
ipAddressTable = _IpAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 34)
)
if mibBuilder.loadTexts:
    ipAddressTable.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressTable.setDescription("This table contains addressing information relevant to the entity's interfaces. This table does not contain multicast address information. Tables for such information should be contained in multicast specific MIBs, such as RFC 3019. While this table is writable, the user will note that several objects, such as ipAddressOrigin, are not. The intention in allowing a user to write to this table is to allow them to add or remove any entry that isn't permanent. The user should be allowed to modify objects and entries when that would not cause inconsistencies within the table. Allowing write access to objects, such as ipAddressOrigin, could allow a user to insert an entry and then label it incorrectly. Note well: When including IPv6 link-local addresses in this table, the entry must use an InetAddressType of 'ipv6z' in order to differentiate between the possible interfaces.")
_IpAddressEntry_Object = MibTableRow
ipAddressEntry = _IpAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1)
)
ipAddressEntry.setIndexNames(
    (0, "IP-MIB", "ipAddressAddrType"),
    (0, "IP-MIB", "ipAddressAddr"),
)
if mibBuilder.loadTexts:
    ipAddressEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressEntry.setDescription("An address mapping for a particular interface.")
_IpAddressAddrType_Type = InetAddressType
_IpAddressAddrType_Object = MibTableColumn
ipAddressAddrType = _IpAddressAddrType_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 1),
    _IpAddressAddrType_Type()
)
ipAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressAddrType.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressAddrType.setDescription("The address type of ipAddressAddr.")
_IpAddressAddr_Type = InetAddress
_IpAddressAddr_Object = MibTableColumn
ipAddressAddr = _IpAddressAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 2),
    _IpAddressAddr_Type()
)
ipAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressAddr.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressAddr.setDescription("The IP address to which this entry's addressing information pertains. The address type of this object is specified in ipAddressAddrType. Implementors need to be aware that if the size of ipAddressAddr exceeds 116 octets, then OIDS of instances of columns in this row will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
_IpAddressIfIndex_Type = InterfaceIndex
_IpAddressIfIndex_Object = MibTableColumn
ipAddressIfIndex = _IpAddressIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 3),
    _IpAddressIfIndex_Type()
)
ipAddressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressIfIndex.setDescription("The index value that uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")


class _IpAddressType_Type(Integer32):
    """Custom type ipAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("anycast", 2),
          ("broadcast", 3))
    )


_IpAddressType_Type.__name__ = "Integer32"
_IpAddressType_Object = MibTableColumn
ipAddressType = _IpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 4),
    _IpAddressType_Type()
)
ipAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressType.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressType.setDescription("The type of address. broadcast(3) is not a valid value for IPv6 addresses (RFC 3513).")


class _IpAddressPrefix_Type(RowPointer):
    """Custom type ipAddressPrefix based on RowPointer"""
    defaultValue = (0, 0)


_IpAddressPrefix_Type.__name__ = "RowPointer"
_IpAddressPrefix_Object = MibTableColumn
ipAddressPrefix = _IpAddressPrefix_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 5),
    _IpAddressPrefix_Type()
)
ipAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPrefix.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefix.setDescription("A pointer to the row in the prefix table to which this address belongs. May be { 0 0 } if there is no such row.")
_IpAddressOrigin_Type = IpAddressOriginTC
_IpAddressOrigin_Object = MibTableColumn
ipAddressOrigin = _IpAddressOrigin_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 6),
    _IpAddressOrigin_Type()
)
ipAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressOrigin.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressOrigin.setDescription("The origin of the address.")


class _IpAddressStatus_Type(IpAddressStatusTC):
    """Custom type ipAddressStatus based on IpAddressStatusTC"""
    defaultValue = 1


_IpAddressStatus_Type.__name__ = "IpAddressStatusTC"
_IpAddressStatus_Object = MibTableColumn
ipAddressStatus = _IpAddressStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 7),
    _IpAddressStatus_Type()
)
ipAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressStatus.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressStatus.setDescription("The status of the address, describing if the address can be used for communication. In the absence of other information, an IPv4 address is always preferred(1).")
_IpAddressCreated_Type = TimeStamp
_IpAddressCreated_Object = MibTableColumn
ipAddressCreated = _IpAddressCreated_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 8),
    _IpAddressCreated_Type()
)
ipAddressCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressCreated.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressCreated.setDescription("The value of sysUpTime at the time this entry was created. If this entry was created prior to the last re- initialization of the local network management subsystem, then this object contains a zero value.")
_IpAddressLastChanged_Type = TimeStamp
_IpAddressLastChanged_Object = MibTableColumn
ipAddressLastChanged = _IpAddressLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 9),
    _IpAddressLastChanged_Type()
)
ipAddressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressLastChanged.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressLastChanged.setDescription("The value of sysUpTime at the time this entry was last updated. If this entry was updated prior to the last re- initialization of the local network management subsystem, then this object contains a zero value.")
_IpAddressRowStatus_Type = RowStatus
_IpAddressRowStatus_Object = MibTableColumn
ipAddressRowStatus = _IpAddressRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 10),
    _IpAddressRowStatus_Type()
)
ipAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressRowStatus.setDescription("The status of this conceptual row. The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified. The value of this object has no effect on whether other objects in this conceptual row can be modified. A conceptual row can not be made active until the ipAddressIfIndex has been set to a valid index.")


class _IpAddressStorageType_Type(StorageType):
    """Custom type ipAddressStorageType based on StorageType"""
    defaultValue = 2


_IpAddressStorageType_Type.__name__ = "StorageType"
_IpAddressStorageType_Object = MibTableColumn
ipAddressStorageType = _IpAddressStorageType_Object(
    (1, 3, 6, 1, 2, 1, 4, 34, 1, 11),
    _IpAddressStorageType_Type()
)
ipAddressStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressStorageType.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressStorageType.setDescription("The storage type for this conceptual row. If this object has a value of 'permanent', then no other objects are required to be able to be modified.")
_IpNetToPhysicalTable_Object = MibTable
ipNetToPhysicalTable = _IpNetToPhysicalTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 35)
)
if mibBuilder.loadTexts:
    ipNetToPhysicalTable.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalTable.setReference("RFC 826 and RFC 2461")
if mibBuilder.loadTexts:
    ipNetToPhysicalTable.setDescription("The IP Address Translation table used for mapping from IP addresses to physical addresses. The Address Translation tables contain the IP address to 'physical' address equivalences. Some interfaces do not use translation tables for determining address equivalences (e.g., DDN-X.25 has an algorithmic method); if all interfaces are of this type, then the Address Translation table is empty, i.e., has zero entries. While many protocols may be used to populate this table, ARP and Neighbor Discovery are the most likely options.")
_IpNetToPhysicalEntry_Object = MibTableRow
ipNetToPhysicalEntry = _IpNetToPhysicalEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1)
)
ipNetToPhysicalEntry.setIndexNames(
    (0, "IP-MIB", "ipNetToPhysicalIfIndex"),
    (0, "IP-MIB", "ipNetToPhysicalNetAddressType"),
    (0, "IP-MIB", "ipNetToPhysicalNetAddress"),
)
if mibBuilder.loadTexts:
    ipNetToPhysicalEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalEntry.setDescription("Each entry contains one IP address to `physical' address equivalence.")
_IpNetToPhysicalIfIndex_Type = InterfaceIndex
_IpNetToPhysicalIfIndex_Object = MibTableColumn
ipNetToPhysicalIfIndex = _IpNetToPhysicalIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 1),
    _IpNetToPhysicalIfIndex_Type()
)
ipNetToPhysicalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNetToPhysicalIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalIfIndex.setDescription("The index value that uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")
_IpNetToPhysicalNetAddressType_Type = InetAddressType
_IpNetToPhysicalNetAddressType_Object = MibTableColumn
ipNetToPhysicalNetAddressType = _IpNetToPhysicalNetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 2),
    _IpNetToPhysicalNetAddressType_Type()
)
ipNetToPhysicalNetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNetToPhysicalNetAddressType.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalNetAddressType.setDescription("The type of ipNetToPhysicalNetAddress.")
_IpNetToPhysicalNetAddress_Type = InetAddress
_IpNetToPhysicalNetAddress_Object = MibTableColumn
ipNetToPhysicalNetAddress = _IpNetToPhysicalNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 3),
    _IpNetToPhysicalNetAddress_Type()
)
ipNetToPhysicalNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNetToPhysicalNetAddress.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalNetAddress.setDescription("The IP Address corresponding to the media-dependent `physical' address. The address type of this object is specified in ipNetToPhysicalAddressType. Implementors need to be aware that if the size of ipNetToPhysicalNetAddress exceeds 115 octets, then OIDS of instances of columns in this row will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")


class _IpNetToPhysicalPhysAddress_Type(PhysAddress):
    """Custom type ipNetToPhysicalPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_IpNetToPhysicalPhysAddress_Type.__name__ = "PhysAddress"
_IpNetToPhysicalPhysAddress_Object = MibTableColumn
ipNetToPhysicalPhysAddress = _IpNetToPhysicalPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 4),
    _IpNetToPhysicalPhysAddress_Type()
)
ipNetToPhysicalPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToPhysicalPhysAddress.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalPhysAddress.setDescription("The media-dependent `physical' address. As the entries in this table are typically not persistent when this object is written the entity SHOULD NOT save the change to non-volatile storage.")
_IpNetToPhysicalLastUpdated_Type = TimeStamp
_IpNetToPhysicalLastUpdated_Object = MibTableColumn
ipNetToPhysicalLastUpdated = _IpNetToPhysicalLastUpdated_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 5),
    _IpNetToPhysicalLastUpdated_Type()
)
ipNetToPhysicalLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNetToPhysicalLastUpdated.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalLastUpdated.setDescription("The value of sysUpTime at the time this entry was last updated. If this entry was updated prior to the last re- initialization of the local network management subsystem, then this object contains a zero value.")


class _IpNetToPhysicalType_Type(Integer32):
    """Custom type ipNetToPhysicalType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4),
          ("local", 5))
    )


_IpNetToPhysicalType_Type.__name__ = "Integer32"
_IpNetToPhysicalType_Object = MibTableColumn
ipNetToPhysicalType = _IpNetToPhysicalType_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 6),
    _IpNetToPhysicalType_Type()
)
ipNetToPhysicalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToPhysicalType.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalType.setDescription("The type of mapping. Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToPhysicalTable. That is, it effectively dis- associates the interface identified with said entry from the mapping identified with said entry. It is an implementation-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipNetToPhysicalType object. The 'dynamic(3)' type indicates that the IP address to physical addresses mapping has been dynamically resolved using e.g., IPv4 ARP or the IPv6 Neighbor Discovery protocol. The 'static(4)' type indicates that the mapping has been statically configured. Both of these refer to entries that provide mappings for other entities addresses. The 'local(5)' type indicates that the mapping is provided for an entity's own interface address. As the entries in this table are typically not persistent when this object is written the entity SHOULD NOT save the change to non-volatile storage.")


class _IpNetToPhysicalState_Type(Integer32):
    """Custom type ipNetToPhysicalState based on Integer32"""
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
        *(("reachable", 1),
          ("stale", 2),
          ("delay", 3),
          ("probe", 4),
          ("invalid", 5),
          ("unknown", 6),
          ("incomplete", 7))
    )


_IpNetToPhysicalState_Type.__name__ = "Integer32"
_IpNetToPhysicalState_Object = MibTableColumn
ipNetToPhysicalState = _IpNetToPhysicalState_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 7),
    _IpNetToPhysicalState_Type()
)
ipNetToPhysicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNetToPhysicalState.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalState.setReference("RFC 2461")
if mibBuilder.loadTexts:
    ipNetToPhysicalState.setDescription("The Neighbor Unreachability Detection state for the interface when the address mapping in this entry is used. If Neighbor Unreachability Detection is not in use (e.g. for IPv4), this object is always unknown(6).")
_IpNetToPhysicalRowStatus_Type = RowStatus
_IpNetToPhysicalRowStatus_Object = MibTableColumn
ipNetToPhysicalRowStatus = _IpNetToPhysicalRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 35, 1, 8),
    _IpNetToPhysicalRowStatus_Type()
)
ipNetToPhysicalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNetToPhysicalRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalRowStatus.setDescription("The status of this conceptual row. The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified. The value of this object has no effect on whether other objects in this conceptual row can be modified. A conceptual row can not be made active until the ipNetToPhysicalPhysAddress object has been set. Note that if the ipNetToPhysicalType is set to 'invalid', the managed node may delete the entry independent of the state of this object.")
_Ipv6ScopeZoneIndexTable_Object = MibTable
ipv6ScopeZoneIndexTable = _Ipv6ScopeZoneIndexTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 36)
)
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexTable.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexTable.setReference("Section 2.7 of RFC 4291")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexTable.setDescription("The table used to describe IPv6 unicast and multicast scope zones. For those objects that have names rather than numbers, the names were chosen to coincide with the names used in the IPv6 address architecture document. ")
_Ipv6ScopeZoneIndexEntry_Object = MibTableRow
ipv6ScopeZoneIndexEntry = _Ipv6ScopeZoneIndexEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1)
)
ipv6ScopeZoneIndexEntry.setIndexNames(
    (0, "IP-MIB", "ipv6ScopeZoneIndexIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexEntry.setDescription("Each entry contains the list of scope identifiers on a given interface.")
_Ipv6ScopeZoneIndexIfIndex_Type = InterfaceIndex
_Ipv6ScopeZoneIndexIfIndex_Object = MibTableColumn
ipv6ScopeZoneIndexIfIndex = _Ipv6ScopeZoneIndexIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 1),
    _Ipv6ScopeZoneIndexIfIndex_Type()
)
ipv6ScopeZoneIndexIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexIfIndex.setDescription("The index value that uniquely identifies the interface to which these scopes belong. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")
_Ipv6ScopeZoneIndexLinkLocal_Type = InetZoneIndex
_Ipv6ScopeZoneIndexLinkLocal_Object = MibTableColumn
ipv6ScopeZoneIndexLinkLocal = _Ipv6ScopeZoneIndexLinkLocal_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 2),
    _Ipv6ScopeZoneIndexLinkLocal_Type()
)
ipv6ScopeZoneIndexLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexLinkLocal.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexLinkLocal.setDescription("The zone index for the link-local scope on this interface.")
_Ipv6ScopeZoneIndex3_Type = InetZoneIndex
_Ipv6ScopeZoneIndex3_Object = MibTableColumn
ipv6ScopeZoneIndex3 = _Ipv6ScopeZoneIndex3_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 3),
    _Ipv6ScopeZoneIndex3_Type()
)
ipv6ScopeZoneIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex3.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex3.setDescription("The zone index for scope 3 on this interface.")
_Ipv6ScopeZoneIndexAdminLocal_Type = InetZoneIndex
_Ipv6ScopeZoneIndexAdminLocal_Object = MibTableColumn
ipv6ScopeZoneIndexAdminLocal = _Ipv6ScopeZoneIndexAdminLocal_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 4),
    _Ipv6ScopeZoneIndexAdminLocal_Type()
)
ipv6ScopeZoneIndexAdminLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexAdminLocal.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexAdminLocal.setDescription("The zone index for the admin-local scope on this interface.")
_Ipv6ScopeZoneIndexSiteLocal_Type = InetZoneIndex
_Ipv6ScopeZoneIndexSiteLocal_Object = MibTableColumn
ipv6ScopeZoneIndexSiteLocal = _Ipv6ScopeZoneIndexSiteLocal_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 5),
    _Ipv6ScopeZoneIndexSiteLocal_Type()
)
ipv6ScopeZoneIndexSiteLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexSiteLocal.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexSiteLocal.setDescription("The zone index for the site-local scope on this interface.")
_Ipv6ScopeZoneIndex6_Type = InetZoneIndex
_Ipv6ScopeZoneIndex6_Object = MibTableColumn
ipv6ScopeZoneIndex6 = _Ipv6ScopeZoneIndex6_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 6),
    _Ipv6ScopeZoneIndex6_Type()
)
ipv6ScopeZoneIndex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex6.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex6.setDescription("The zone index for scope 6 on this interface.")
_Ipv6ScopeZoneIndex7_Type = InetZoneIndex
_Ipv6ScopeZoneIndex7_Object = MibTableColumn
ipv6ScopeZoneIndex7 = _Ipv6ScopeZoneIndex7_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 7),
    _Ipv6ScopeZoneIndex7_Type()
)
ipv6ScopeZoneIndex7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex7.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex7.setDescription("The zone index for scope 7 on this interface.")
_Ipv6ScopeZoneIndexOrganizationLocal_Type = InetZoneIndex
_Ipv6ScopeZoneIndexOrganizationLocal_Object = MibTableColumn
ipv6ScopeZoneIndexOrganizationLocal = _Ipv6ScopeZoneIndexOrganizationLocal_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 8),
    _Ipv6ScopeZoneIndexOrganizationLocal_Type()
)
ipv6ScopeZoneIndexOrganizationLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexOrganizationLocal.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexOrganizationLocal.setDescription("The zone index for the organization-local scope on this interface.")
_Ipv6ScopeZoneIndex9_Type = InetZoneIndex
_Ipv6ScopeZoneIndex9_Object = MibTableColumn
ipv6ScopeZoneIndex9 = _Ipv6ScopeZoneIndex9_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 9),
    _Ipv6ScopeZoneIndex9_Type()
)
ipv6ScopeZoneIndex9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex9.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndex9.setDescription("The zone index for scope 9 on this interface.")
_Ipv6ScopeZoneIndexA_Type = InetZoneIndex
_Ipv6ScopeZoneIndexA_Object = MibTableColumn
ipv6ScopeZoneIndexA = _Ipv6ScopeZoneIndexA_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 10),
    _Ipv6ScopeZoneIndexA_Type()
)
ipv6ScopeZoneIndexA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexA.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexA.setDescription("The zone index for scope A on this interface.")
_Ipv6ScopeZoneIndexB_Type = InetZoneIndex
_Ipv6ScopeZoneIndexB_Object = MibTableColumn
ipv6ScopeZoneIndexB = _Ipv6ScopeZoneIndexB_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 11),
    _Ipv6ScopeZoneIndexB_Type()
)
ipv6ScopeZoneIndexB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexB.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexB.setDescription("The zone index for scope B on this interface.")
_Ipv6ScopeZoneIndexC_Type = InetZoneIndex
_Ipv6ScopeZoneIndexC_Object = MibTableColumn
ipv6ScopeZoneIndexC = _Ipv6ScopeZoneIndexC_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 12),
    _Ipv6ScopeZoneIndexC_Type()
)
ipv6ScopeZoneIndexC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexC.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexC.setDescription("The zone index for scope C on this interface.")
_Ipv6ScopeZoneIndexD_Type = InetZoneIndex
_Ipv6ScopeZoneIndexD_Object = MibTableColumn
ipv6ScopeZoneIndexD = _Ipv6ScopeZoneIndexD_Object(
    (1, 3, 6, 1, 2, 1, 4, 36, 1, 13),
    _Ipv6ScopeZoneIndexD_Type()
)
ipv6ScopeZoneIndexD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexD.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeZoneIndexD.setDescription("The zone index for scope D on this interface.")
_IpDefaultRouterTable_Object = MibTable
ipDefaultRouterTable = _IpDefaultRouterTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 37)
)
if mibBuilder.loadTexts:
    ipDefaultRouterTable.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterTable.setDescription("The table used to describe the default routers known to this entity.")
_IpDefaultRouterEntry_Object = MibTableRow
ipDefaultRouterEntry = _IpDefaultRouterEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 37, 1)
)
ipDefaultRouterEntry.setIndexNames(
    (0, "IP-MIB", "ipDefaultRouterAddressType"),
    (0, "IP-MIB", "ipDefaultRouterAddress"),
    (0, "IP-MIB", "ipDefaultRouterIfIndex"),
)
if mibBuilder.loadTexts:
    ipDefaultRouterEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterEntry.setDescription("Each entry contains information about a default router known to this entity.")
_IpDefaultRouterAddressType_Type = InetAddressType
_IpDefaultRouterAddressType_Object = MibTableColumn
ipDefaultRouterAddressType = _IpDefaultRouterAddressType_Object(
    (1, 3, 6, 1, 2, 1, 4, 37, 1, 1),
    _IpDefaultRouterAddressType_Type()
)
ipDefaultRouterAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDefaultRouterAddressType.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterAddressType.setDescription("The address type for this row.")
_IpDefaultRouterAddress_Type = InetAddress
_IpDefaultRouterAddress_Object = MibTableColumn
ipDefaultRouterAddress = _IpDefaultRouterAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 37, 1, 2),
    _IpDefaultRouterAddress_Type()
)
ipDefaultRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDefaultRouterAddress.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterAddress.setDescription("The IP address of the default router represented by this row. The address type of this object is specified in ipDefaultRouterAddressType. Implementers need to be aware that if the size of ipDefaultRouterAddress exceeds 115 octets, then OIDS of instances of columns in this row will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
_IpDefaultRouterIfIndex_Type = InterfaceIndex
_IpDefaultRouterIfIndex_Object = MibTableColumn
ipDefaultRouterIfIndex = _IpDefaultRouterIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 37, 1, 3),
    _IpDefaultRouterIfIndex_Type()
)
ipDefaultRouterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDefaultRouterIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterIfIndex.setDescription("The index value that uniquely identifies the interface by which the router can be reached. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")


class _IpDefaultRouterLifetime_Type(Unsigned32):
    """Custom type ipDefaultRouterLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpDefaultRouterLifetime_Type.__name__ = "Unsigned32"
_IpDefaultRouterLifetime_Object = MibTableColumn
ipDefaultRouterLifetime = _IpDefaultRouterLifetime_Object(
    (1, 3, 6, 1, 2, 1, 4, 37, 1, 4),
    _IpDefaultRouterLifetime_Type()
)
ipDefaultRouterLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDefaultRouterLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterLifetime.setUnits("seconds")
if mibBuilder.loadTexts:
    ipDefaultRouterLifetime.setReference("For IPv6 RFC 2462 sections 4.2 and 6.3.4")
if mibBuilder.loadTexts:
    ipDefaultRouterLifetime.setDescription("The remaining length of time, in seconds, that this router will continue to be useful as a default router. A value of zero indicates that it is no longer useful as a default router. It is left to the implementer of the MIB as to whether a router with a lifetime of zero is removed from the list. For IPv6, this value should be extracted from the router advertisement messages.")


class _IpDefaultRouterPreference_Type(Integer32):
    """Custom type ipDefaultRouterPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reserved", -2),
          ("low", -1),
          ("medium", 0),
          ("high", 1))
    )


_IpDefaultRouterPreference_Type.__name__ = "Integer32"
_IpDefaultRouterPreference_Object = MibTableColumn
ipDefaultRouterPreference = _IpDefaultRouterPreference_Object(
    (1, 3, 6, 1, 2, 1, 4, 37, 1, 5),
    _IpDefaultRouterPreference_Type()
)
ipDefaultRouterPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDefaultRouterPreference.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterPreference.setReference("RFC 4291, section 2.1")
if mibBuilder.loadTexts:
    ipDefaultRouterPreference.setDescription("An indication of preference given to this router as a default router as described in he Default Router Preferences document. Treating the value as a 2 bit signed integer allows for simple arithmetic comparisons. For IPv4 routers or IPv6 routers that are not using the updated router advertisement format, this object is set to medium (0).")
_Ipv6RouterAdvertSpinLock_Type = TestAndIncr
_Ipv6RouterAdvertSpinLock_Object = MibScalar
ipv6RouterAdvertSpinLock = _Ipv6RouterAdvertSpinLock_Object(
    (1, 3, 6, 1, 2, 1, 4, 38),
    _Ipv6RouterAdvertSpinLock_Type()
)
ipv6RouterAdvertSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6RouterAdvertSpinLock.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertSpinLock.setDescription("An advisory lock used to allow cooperating SNMP managers to coordinate their use of the set operation in creating or modifying rows within this table. In order to use this lock to coordinate the use of set operations, managers should first retrieve ipv6RouterAdvertSpinLock. They should then determine the appropriate row to create or modify. Finally, they should issue the appropriate set command including the retrieved value of ipv6RouterAdvertSpinLock. If another manager has altered the table in the meantime, then the value of ipv6RouterAdvertSpinLock will have changed and the creation will fail as it will be specifying an incorrect value for ipv6RouterAdvertSpinLock. It is suggested, but not required, that the ipv6RouterAdvertSpinLock be the first var bind for each set of objects representing a 'row' in a PDU.")
_Ipv6RouterAdvertTable_Object = MibTable
ipv6RouterAdvertTable = _Ipv6RouterAdvertTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 39)
)
if mibBuilder.loadTexts:
    ipv6RouterAdvertTable.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertTable.setDescription("The table containing information used to construct router advertisements.")
_Ipv6RouterAdvertEntry_Object = MibTableRow
ipv6RouterAdvertEntry = _Ipv6RouterAdvertEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1)
)
ipv6RouterAdvertEntry.setIndexNames(
    (0, "IP-MIB", "ipv6RouterAdvertIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6RouterAdvertEntry.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertEntry.setDescription("An entry containing information used to construct router advertisements. Information in this table is persistent, and when this object is written, the entity SHOULD save the change to non-volatile storage.")
_Ipv6RouterAdvertIfIndex_Type = InterfaceIndex
_Ipv6RouterAdvertIfIndex_Object = MibTableColumn
ipv6RouterAdvertIfIndex = _Ipv6RouterAdvertIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 1),
    _Ipv6RouterAdvertIfIndex_Type()
)
ipv6RouterAdvertIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6RouterAdvertIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertIfIndex.setDescription("The index value that uniquely identifies the interface on which router advertisements constructed with this information will be transmitted. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")


class _Ipv6RouterAdvertSendAdverts_Type(TruthValue):
    """Custom type ipv6RouterAdvertSendAdverts based on TruthValue"""
    defaultValue = 2


_Ipv6RouterAdvertSendAdverts_Type.__name__ = "TruthValue"
_Ipv6RouterAdvertSendAdverts_Object = MibTableColumn
ipv6RouterAdvertSendAdverts = _Ipv6RouterAdvertSendAdverts_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 2),
    _Ipv6RouterAdvertSendAdverts_Type()
)
ipv6RouterAdvertSendAdverts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertSendAdverts.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertSendAdverts.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertSendAdverts.setDescription("A flag indicating whether the router sends periodic router advertisements and responds to router solicitations on this interface.")


class _Ipv6RouterAdvertMaxInterval_Type(Unsigned32):
    """Custom type ipv6RouterAdvertMaxInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_Ipv6RouterAdvertMaxInterval_Type.__name__ = "Unsigned32"
_Ipv6RouterAdvertMaxInterval_Object = MibTableColumn
ipv6RouterAdvertMaxInterval = _Ipv6RouterAdvertMaxInterval_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 3),
    _Ipv6RouterAdvertMaxInterval_Type()
)
ipv6RouterAdvertMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMaxInterval.setUnits("seconds")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMaxInterval.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMaxInterval.setDescription("The maximum time allowed between sending unsolicited router advertisements from this interface.")


class _Ipv6RouterAdvertMinInterval_Type(Unsigned32):
    """Custom type ipv6RouterAdvertMinInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1350),
    )


_Ipv6RouterAdvertMinInterval_Type.__name__ = "Unsigned32"
_Ipv6RouterAdvertMinInterval_Object = MibTableColumn
ipv6RouterAdvertMinInterval = _Ipv6RouterAdvertMinInterval_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 4),
    _Ipv6RouterAdvertMinInterval_Type()
)
ipv6RouterAdvertMinInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMinInterval.setUnits("seconds")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMinInterval.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertMinInterval.setDescription("The minimum time allowed between sending unsolicited router advertisements from this interface. The default is 0.33 * ipv6RouterAdvertMaxInterval, however, in the case of a low value for ipv6RouterAdvertMaxInterval, the minimum value for this object is restricted to 3.")


class _Ipv6RouterAdvertManagedFlag_Type(TruthValue):
    """Custom type ipv6RouterAdvertManagedFlag based on TruthValue"""
    defaultValue = 2


_Ipv6RouterAdvertManagedFlag_Type.__name__ = "TruthValue"
_Ipv6RouterAdvertManagedFlag_Object = MibTableColumn
ipv6RouterAdvertManagedFlag = _Ipv6RouterAdvertManagedFlag_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 5),
    _Ipv6RouterAdvertManagedFlag_Type()
)
ipv6RouterAdvertManagedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertManagedFlag.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertManagedFlag.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertManagedFlag.setDescription("The true/false value to be placed into the 'managed address configuration' flag field in router advertisements sent from this interface.")


class _Ipv6RouterAdvertOtherConfigFlag_Type(TruthValue):
    """Custom type ipv6RouterAdvertOtherConfigFlag based on TruthValue"""
    defaultValue = 2


_Ipv6RouterAdvertOtherConfigFlag_Type.__name__ = "TruthValue"
_Ipv6RouterAdvertOtherConfigFlag_Object = MibTableColumn
ipv6RouterAdvertOtherConfigFlag = _Ipv6RouterAdvertOtherConfigFlag_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 6),
    _Ipv6RouterAdvertOtherConfigFlag_Type()
)
ipv6RouterAdvertOtherConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertOtherConfigFlag.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertOtherConfigFlag.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertOtherConfigFlag.setDescription("The true/false value to be placed into the 'other stateful configuration' flag field in router advertisements sent from this interface.")


class _Ipv6RouterAdvertLinkMTU_Type(Unsigned32):
    """Custom type ipv6RouterAdvertLinkMTU based on Unsigned32"""
    defaultValue = 0


_Ipv6RouterAdvertLinkMTU_Type.__name__ = "Unsigned32"
_Ipv6RouterAdvertLinkMTU_Object = MibTableColumn
ipv6RouterAdvertLinkMTU = _Ipv6RouterAdvertLinkMTU_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 7),
    _Ipv6RouterAdvertLinkMTU_Type()
)
ipv6RouterAdvertLinkMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertLinkMTU.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertLinkMTU.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertLinkMTU.setDescription("The value to be placed in MTU options sent by the router on this interface. A value of zero indicates that no MTU options are sent.")


class _Ipv6RouterAdvertReachableTime_Type(Unsigned32):
    """Custom type ipv6RouterAdvertReachableTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_Ipv6RouterAdvertReachableTime_Type.__name__ = "Unsigned32"
_Ipv6RouterAdvertReachableTime_Object = MibTableColumn
ipv6RouterAdvertReachableTime = _Ipv6RouterAdvertReachableTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 8),
    _Ipv6RouterAdvertReachableTime_Type()
)
ipv6RouterAdvertReachableTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertReachableTime.setUnits("milliseconds")
if mibBuilder.loadTexts:
    ipv6RouterAdvertReachableTime.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertReachableTime.setDescription("The value to be placed in the reachable time field in router advertisement messages sent from this interface. A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for reachable time.")


class _Ipv6RouterAdvertRetransmitTime_Type(Unsigned32):
    """Custom type ipv6RouterAdvertRetransmitTime based on Unsigned32"""
    defaultValue = 0


_Ipv6RouterAdvertRetransmitTime_Type.__name__ = "Unsigned32"
_Ipv6RouterAdvertRetransmitTime_Object = MibTableColumn
ipv6RouterAdvertRetransmitTime = _Ipv6RouterAdvertRetransmitTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 9),
    _Ipv6RouterAdvertRetransmitTime_Type()
)
ipv6RouterAdvertRetransmitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertRetransmitTime.setUnits("milliseconds")
if mibBuilder.loadTexts:
    ipv6RouterAdvertRetransmitTime.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertRetransmitTime.setDescription("The value to be placed in the retransmit timer field in router advertisements sent from this interface. A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for retrans time.")


class _Ipv6RouterAdvertCurHopLimit_Type(Unsigned32):
    """Custom type ipv6RouterAdvertCurHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ipv6RouterAdvertCurHopLimit_Type.__name__ = "Unsigned32"
_Ipv6RouterAdvertCurHopLimit_Object = MibTableColumn
ipv6RouterAdvertCurHopLimit = _Ipv6RouterAdvertCurHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 10),
    _Ipv6RouterAdvertCurHopLimit_Type()
)
ipv6RouterAdvertCurHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertCurHopLimit.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertCurHopLimit.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertCurHopLimit.setDescription("The default value to be placed in the current hop limit field in router advertisements sent from this interface. The value should be set to the current diameter of the Internet. A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for curHopLimit. The default should be set to the value specified in the IANA web pages (www.iana.org) at the time of implementation.")


class _Ipv6RouterAdvertDefaultLifetime_Type(Unsigned32):
    """Custom type ipv6RouterAdvertDefaultLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 9000),
    )


_Ipv6RouterAdvertDefaultLifetime_Type.__name__ = "Unsigned32"
_Ipv6RouterAdvertDefaultLifetime_Object = MibTableColumn
ipv6RouterAdvertDefaultLifetime = _Ipv6RouterAdvertDefaultLifetime_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 11),
    _Ipv6RouterAdvertDefaultLifetime_Type()
)
ipv6RouterAdvertDefaultLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertDefaultLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertDefaultLifetime.setUnits("seconds")
if mibBuilder.loadTexts:
    ipv6RouterAdvertDefaultLifetime.setReference("RFC 2461 Section 6.2.1")
if mibBuilder.loadTexts:
    ipv6RouterAdvertDefaultLifetime.setDescription("The value to be placed in the router lifetime field of router advertisements sent from this interface. This value MUST be either 0 or between ipv6RouterAdvertMaxInterval and 9000 seconds. A value of zero indicates that the router is not to be used as a default router. The default is 3 * ipv6RouterAdvertMaxInterval.")
_Ipv6RouterAdvertRowStatus_Type = RowStatus
_Ipv6RouterAdvertRowStatus_Object = MibTableColumn
ipv6RouterAdvertRowStatus = _Ipv6RouterAdvertRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 39, 1, 12),
    _Ipv6RouterAdvertRowStatus_Type()
)
ipv6RouterAdvertRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6RouterAdvertRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertRowStatus.setDescription("The status of this conceptual row. As all objects in this conceptual row have default values, a row can be created and made active by setting this object appropriately. The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified. The value of this object has no effect on whether other objects in this conceptual row can be modified.")
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5)
)
_IcmpInMsgs_Type = Counter32
_IcmpInMsgs_Object = MibScalar
icmpInMsgs = _IcmpInMsgs_Object(
    (1, 3, 6, 1, 2, 1, 5, 1),
    _IcmpInMsgs_Type()
)
icmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInMsgs.setDescription("The total number of ICMP messages which the entity received. Note that this counter includes all those counted by icmpInErrors. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by icmpStatsInMsgs.")
_IcmpInErrors_Type = Counter32
_IcmpInErrors_Object = MibScalar
icmpInErrors = _IcmpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 5, 2),
    _IcmpInErrors_Type()
)
icmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInErrors.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInErrors.setDescription("The number of ICMP messages which the entity received but determined as having ICMP-specific errors (bad ICMP checksums, bad length, etc.). This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by icmpStatsInErrors.")
_IcmpInDestUnreachs_Type = Counter32
_IcmpInDestUnreachs_Object = MibScalar
icmpInDestUnreachs = _IcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 2, 1, 5, 3),
    _IcmpInDestUnreachs_Type()
)
icmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInDestUnreachs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInDestUnreachs.setDescription("The number of ICMP Destination Unreachable messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInTimeExcds_Type = Counter32
_IcmpInTimeExcds_Object = MibScalar
icmpInTimeExcds = _IcmpInTimeExcds_Object(
    (1, 3, 6, 1, 2, 1, 5, 4),
    _IcmpInTimeExcds_Type()
)
icmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInTimeExcds.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInTimeExcds.setDescription("The number of ICMP Time Exceeded messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInParmProbs_Type = Counter32
_IcmpInParmProbs_Object = MibScalar
icmpInParmProbs = _IcmpInParmProbs_Object(
    (1, 3, 6, 1, 2, 1, 5, 5),
    _IcmpInParmProbs_Type()
)
icmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInParmProbs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInParmProbs.setDescription("The number of ICMP Parameter Problem messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInSrcQuenchs_Type = Counter32
_IcmpInSrcQuenchs_Object = MibScalar
icmpInSrcQuenchs = _IcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 2, 1, 5, 6),
    _IcmpInSrcQuenchs_Type()
)
icmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInSrcQuenchs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInSrcQuenchs.setDescription("The number of ICMP Source Quench messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInRedirects_Type = Counter32
_IcmpInRedirects_Object = MibScalar
icmpInRedirects = _IcmpInRedirects_Object(
    (1, 3, 6, 1, 2, 1, 5, 7),
    _IcmpInRedirects_Type()
)
icmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInRedirects.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInRedirects.setDescription("The number of ICMP Redirect messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInEchos_Type = Counter32
_IcmpInEchos_Object = MibScalar
icmpInEchos = _IcmpInEchos_Object(
    (1, 3, 6, 1, 2, 1, 5, 8),
    _IcmpInEchos_Type()
)
icmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInEchos.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInEchos.setDescription("The number of ICMP Echo (request) messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInEchoReps_Type = Counter32
_IcmpInEchoReps_Object = MibScalar
icmpInEchoReps = _IcmpInEchoReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 9),
    _IcmpInEchoReps_Type()
)
icmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInEchoReps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInEchoReps.setDescription("The number of ICMP Echo Reply messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInTimestamps_Type = Counter32
_IcmpInTimestamps_Object = MibScalar
icmpInTimestamps = _IcmpInTimestamps_Object(
    (1, 3, 6, 1, 2, 1, 5, 10),
    _IcmpInTimestamps_Type()
)
icmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInTimestamps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInTimestamps.setDescription("The number of ICMP Timestamp (request) messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInTimestampReps_Type = Counter32
_IcmpInTimestampReps_Object = MibScalar
icmpInTimestampReps = _IcmpInTimestampReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 11),
    _IcmpInTimestampReps_Type()
)
icmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInTimestampReps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInTimestampReps.setDescription("The number of ICMP Timestamp Reply messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInAddrMasks_Type = Counter32
_IcmpInAddrMasks_Object = MibScalar
icmpInAddrMasks = _IcmpInAddrMasks_Object(
    (1, 3, 6, 1, 2, 1, 5, 12),
    _IcmpInAddrMasks_Type()
)
icmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInAddrMasks.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInAddrMasks.setDescription("The number of ICMP Address Mask Request messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpInAddrMaskReps_Type = Counter32
_IcmpInAddrMaskReps_Object = MibScalar
icmpInAddrMaskReps = _IcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 13),
    _IcmpInAddrMaskReps_Type()
)
icmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInAddrMaskReps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpInAddrMaskReps.setDescription("The number of ICMP Address Mask Reply messages received. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutMsgs_Type = Counter32
_IcmpOutMsgs_Object = MibScalar
icmpOutMsgs = _IcmpOutMsgs_Object(
    (1, 3, 6, 1, 2, 1, 5, 14),
    _IcmpOutMsgs_Type()
)
icmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutMsgs.setDescription("The total number of ICMP messages which this entity attempted to send. Note that this counter includes all those counted by icmpOutErrors. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by icmpStatsOutMsgs.")
_IcmpOutErrors_Type = Counter32
_IcmpOutErrors_Object = MibScalar
icmpOutErrors = _IcmpOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 5, 15),
    _IcmpOutErrors_Type()
)
icmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutErrors.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutErrors.setDescription("The number of ICMP messages which this entity did not send due to problems discovered within ICMP, such as a lack of buffers. This value should not include errors discovered outside the ICMP layer, such as the inability of IP to route the resultant datagram. In some implementations, there may be no types of error which contribute to this counter's value. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by icmpStatsOutErrors.")
_IcmpOutDestUnreachs_Type = Counter32
_IcmpOutDestUnreachs_Object = MibScalar
icmpOutDestUnreachs = _IcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 2, 1, 5, 16),
    _IcmpOutDestUnreachs_Type()
)
icmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutDestUnreachs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutDestUnreachs.setDescription("The number of ICMP Destination Unreachable messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutTimeExcds_Type = Counter32
_IcmpOutTimeExcds_Object = MibScalar
icmpOutTimeExcds = _IcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 2, 1, 5, 17),
    _IcmpOutTimeExcds_Type()
)
icmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutTimeExcds.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutTimeExcds.setDescription("The number of ICMP Time Exceeded messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutParmProbs_Type = Counter32
_IcmpOutParmProbs_Object = MibScalar
icmpOutParmProbs = _IcmpOutParmProbs_Object(
    (1, 3, 6, 1, 2, 1, 5, 18),
    _IcmpOutParmProbs_Type()
)
icmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutParmProbs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutParmProbs.setDescription("The number of ICMP Parameter Problem messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutSrcQuenchs_Type = Counter32
_IcmpOutSrcQuenchs_Object = MibScalar
icmpOutSrcQuenchs = _IcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 2, 1, 5, 19),
    _IcmpOutSrcQuenchs_Type()
)
icmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutSrcQuenchs.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutSrcQuenchs.setDescription("The number of ICMP Source Quench messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutRedirects_Type = Counter32
_IcmpOutRedirects_Object = MibScalar
icmpOutRedirects = _IcmpOutRedirects_Object(
    (1, 3, 6, 1, 2, 1, 5, 20),
    _IcmpOutRedirects_Type()
)
icmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutRedirects.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutRedirects.setDescription("The number of ICMP Redirect messages sent. For a host, this object will always be zero, since hosts do not send redirects. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutEchos_Type = Counter32
_IcmpOutEchos_Object = MibScalar
icmpOutEchos = _IcmpOutEchos_Object(
    (1, 3, 6, 1, 2, 1, 5, 21),
    _IcmpOutEchos_Type()
)
icmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutEchos.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutEchos.setDescription("The number of ICMP Echo (request) messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutEchoReps_Type = Counter32
_IcmpOutEchoReps_Object = MibScalar
icmpOutEchoReps = _IcmpOutEchoReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 22),
    _IcmpOutEchoReps_Type()
)
icmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutEchoReps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutEchoReps.setDescription("The number of ICMP Echo Reply messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutTimestamps_Type = Counter32
_IcmpOutTimestamps_Object = MibScalar
icmpOutTimestamps = _IcmpOutTimestamps_Object(
    (1, 3, 6, 1, 2, 1, 5, 23),
    _IcmpOutTimestamps_Type()
)
icmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutTimestamps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutTimestamps.setDescription("The number of ICMP Timestamp (request) messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutTimestampReps_Type = Counter32
_IcmpOutTimestampReps_Object = MibScalar
icmpOutTimestampReps = _IcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 24),
    _IcmpOutTimestampReps_Type()
)
icmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutTimestampReps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutTimestampReps.setDescription("The number of ICMP Timestamp Reply messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutAddrMasks_Type = Counter32
_IcmpOutAddrMasks_Object = MibScalar
icmpOutAddrMasks = _IcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 2, 1, 5, 25),
    _IcmpOutAddrMasks_Type()
)
icmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutAddrMasks.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutAddrMasks.setDescription("The number of ICMP Address Mask Request messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpOutAddrMaskReps_Type = Counter32
_IcmpOutAddrMaskReps_Object = MibScalar
icmpOutAddrMaskReps = _IcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 26),
    _IcmpOutAddrMaskReps_Type()
)
icmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutAddrMaskReps.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpOutAddrMaskReps.setDescription("The number of ICMP Address Mask Reply messages sent. This object has been deprecated, as a new IP version-neutral table has been added. It is loosely replaced by a column in the icmpMsgStatsTable.")
_IcmpStatsTable_Object = MibTable
icmpStatsTable = _IcmpStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 5, 29)
)
if mibBuilder.loadTexts:
    icmpStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsTable.setDescription("The table of generic system-wide ICMP counters.")
_IcmpStatsEntry_Object = MibTableRow
icmpStatsEntry = _IcmpStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 5, 29, 1)
)
icmpStatsEntry.setIndexNames(
    (0, "IP-MIB", "icmpStatsIPVersion"),
)
if mibBuilder.loadTexts:
    icmpStatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsEntry.setDescription("A conceptual row in the icmpStatsTable.")
_IcmpStatsIPVersion_Type = InetVersion
_IcmpStatsIPVersion_Object = MibTableColumn
icmpStatsIPVersion = _IcmpStatsIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 5, 29, 1, 1),
    _IcmpStatsIPVersion_Type()
)
icmpStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icmpStatsIPVersion.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsIPVersion.setDescription("The IP version of the statistics.")
_IcmpStatsInMsgs_Type = Counter32
_IcmpStatsInMsgs_Object = MibTableColumn
icmpStatsInMsgs = _IcmpStatsInMsgs_Object(
    (1, 3, 6, 1, 2, 1, 5, 29, 1, 2),
    _IcmpStatsInMsgs_Type()
)
icmpStatsInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpStatsInMsgs.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsInMsgs.setDescription("The total number of ICMP messages that the entity received. Note that this counter includes all those counted by icmpStatsInErrors.")
_IcmpStatsInErrors_Type = Counter32
_IcmpStatsInErrors_Object = MibTableColumn
icmpStatsInErrors = _IcmpStatsInErrors_Object(
    (1, 3, 6, 1, 2, 1, 5, 29, 1, 3),
    _IcmpStatsInErrors_Type()
)
icmpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpStatsInErrors.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsInErrors.setDescription("The number of ICMP messages that the entity received but determined as having ICMP-specific errors (bad ICMP checksums, bad length, etc.).")
_IcmpStatsOutMsgs_Type = Counter32
_IcmpStatsOutMsgs_Object = MibTableColumn
icmpStatsOutMsgs = _IcmpStatsOutMsgs_Object(
    (1, 3, 6, 1, 2, 1, 5, 29, 1, 4),
    _IcmpStatsOutMsgs_Type()
)
icmpStatsOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpStatsOutMsgs.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsOutMsgs.setDescription("The total number of ICMP messages that the entity attempted to send. Note that this counter includes all those counted by icmpStatsOutErrors.")
_IcmpStatsOutErrors_Type = Counter32
_IcmpStatsOutErrors_Object = MibTableColumn
icmpStatsOutErrors = _IcmpStatsOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 5, 29, 1, 5),
    _IcmpStatsOutErrors_Type()
)
icmpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpStatsOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsOutErrors.setDescription("The number of ICMP messages that this entity did not send due to problems discovered within ICMP, such as a lack of buffers. This value should not include errors discovered outside the ICMP layer, such as the inability of IP to route the resultant datagram. In some implementations, there may be no types of error that contribute to this counter's value.")
_IcmpMsgStatsTable_Object = MibTable
icmpMsgStatsTable = _IcmpMsgStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 5, 30)
)
if mibBuilder.loadTexts:
    icmpMsgStatsTable.setStatus("current")
if mibBuilder.loadTexts:
    icmpMsgStatsTable.setDescription("The table of system-wide per-version, per-message type ICMP counters.")
_IcmpMsgStatsEntry_Object = MibTableRow
icmpMsgStatsEntry = _IcmpMsgStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 5, 30, 1)
)
icmpMsgStatsEntry.setIndexNames(
    (0, "IP-MIB", "icmpMsgStatsIPVersion"),
    (0, "IP-MIB", "icmpMsgStatsType"),
)
if mibBuilder.loadTexts:
    icmpMsgStatsEntry.setStatus("current")
if mibBuilder.loadTexts:
    icmpMsgStatsEntry.setDescription("A conceptual row in the icmpMsgStatsTable. The system should track each ICMP type value, even if that ICMP type is not supported by the system. However, a given row need not be instantiated unless a message of that type has been processed, i.e., the row for icmpMsgStatsType=X MAY be instantiated before but MUST be instantiated after the first message with Type=X is received or transmitted. After receiving or transmitting any succeeding messages with Type=X, the relevant counter must be incremented.")
_IcmpMsgStatsIPVersion_Type = InetVersion
_IcmpMsgStatsIPVersion_Object = MibTableColumn
icmpMsgStatsIPVersion = _IcmpMsgStatsIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 5, 30, 1, 1),
    _IcmpMsgStatsIPVersion_Type()
)
icmpMsgStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icmpMsgStatsIPVersion.setStatus("current")
if mibBuilder.loadTexts:
    icmpMsgStatsIPVersion.setDescription("The IP version of the statistics.")


class _IcmpMsgStatsType_Type(Integer32):
    """Custom type icmpMsgStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IcmpMsgStatsType_Type.__name__ = "Integer32"
_IcmpMsgStatsType_Object = MibTableColumn
icmpMsgStatsType = _IcmpMsgStatsType_Object(
    (1, 3, 6, 1, 2, 1, 5, 30, 1, 2),
    _IcmpMsgStatsType_Type()
)
icmpMsgStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icmpMsgStatsType.setStatus("current")
if mibBuilder.loadTexts:
    icmpMsgStatsType.setReference("http://www.iana.org/assignments/icmp-parameters and http://www.iana.org/assignments/icmpv6-parameters")
if mibBuilder.loadTexts:
    icmpMsgStatsType.setDescription("The ICMP type field of the message type being counted by this row. Note that ICMP message types are scoped by the address type in use.")
_IcmpMsgStatsInPkts_Type = Counter32
_IcmpMsgStatsInPkts_Object = MibTableColumn
icmpMsgStatsInPkts = _IcmpMsgStatsInPkts_Object(
    (1, 3, 6, 1, 2, 1, 5, 30, 1, 3),
    _IcmpMsgStatsInPkts_Type()
)
icmpMsgStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpMsgStatsInPkts.setStatus("current")
if mibBuilder.loadTexts:
    icmpMsgStatsInPkts.setDescription("The number of input packets for this AF and type.")
_IcmpMsgStatsOutPkts_Type = Counter32
_IcmpMsgStatsOutPkts_Object = MibTableColumn
icmpMsgStatsOutPkts = _IcmpMsgStatsOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 5, 30, 1, 4),
    _IcmpMsgStatsOutPkts_Type()
)
icmpMsgStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpMsgStatsOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    icmpMsgStatsOutPkts.setDescription("The number of output packets for this AF and type.")
_IpMIBConformance_ObjectIdentity = ObjectIdentity
ipMIBConformance = _IpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 48, 2)
)
_IpMIBCompliances_ObjectIdentity = ObjectIdentity
ipMIBCompliances = _IpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 48, 2, 1)
)
_IpMIBGroups_ObjectIdentity = ObjectIdentity
ipMIBGroups = _IpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 48, 2, 2)
)

# Managed Objects groups

ipGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 1)
)
ipGroup.setObjects(
      *(("IP-MIB", "ipForwarding"),
        ("IP-MIB", "ipDefaultTTL"),
        ("IP-MIB", "ipInReceives"),
        ("IP-MIB", "ipInHdrErrors"),
        ("IP-MIB", "ipInAddrErrors"),
        ("IP-MIB", "ipForwDatagrams"),
        ("IP-MIB", "ipInUnknownProtos"),
        ("IP-MIB", "ipInDiscards"),
        ("IP-MIB", "ipInDelivers"),
        ("IP-MIB", "ipOutRequests"),
        ("IP-MIB", "ipOutDiscards"),
        ("IP-MIB", "ipOutNoRoutes"),
        ("IP-MIB", "ipReasmTimeout"),
        ("IP-MIB", "ipReasmReqds"),
        ("IP-MIB", "ipReasmOKs"),
        ("IP-MIB", "ipReasmFails"),
        ("IP-MIB", "ipFragOKs"),
        ("IP-MIB", "ipFragFails"),
        ("IP-MIB", "ipFragCreates"),
        ("IP-MIB", "ipAdEntAddr"),
        ("IP-MIB", "ipAdEntIfIndex"),
        ("IP-MIB", "ipAdEntNetMask"),
        ("IP-MIB", "ipAdEntBcastAddr"),
        ("IP-MIB", "ipAdEntReasmMaxSize"),
        ("IP-MIB", "ipNetToMediaIfIndex"),
        ("IP-MIB", "ipNetToMediaPhysAddress"),
        ("IP-MIB", "ipNetToMediaNetAddress"),
        ("IP-MIB", "ipNetToMediaType"),
        ("IP-MIB", "ipRoutingDiscards"))
)
if mibBuilder.loadTexts:
    ipGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    ipGroup.setDescription("The ip group of objects providing for basic management of IP entities, exclusive of the management of IP routes. As part of the version independence, this group has been deprecated. ")

icmpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 2)
)
icmpGroup.setObjects(
      *(("IP-MIB", "icmpInMsgs"),
        ("IP-MIB", "icmpInErrors"),
        ("IP-MIB", "icmpInDestUnreachs"),
        ("IP-MIB", "icmpInTimeExcds"),
        ("IP-MIB", "icmpInParmProbs"),
        ("IP-MIB", "icmpInSrcQuenchs"),
        ("IP-MIB", "icmpInRedirects"),
        ("IP-MIB", "icmpInEchos"),
        ("IP-MIB", "icmpInEchoReps"),
        ("IP-MIB", "icmpInTimestamps"),
        ("IP-MIB", "icmpInTimestampReps"),
        ("IP-MIB", "icmpInAddrMasks"),
        ("IP-MIB", "icmpInAddrMaskReps"),
        ("IP-MIB", "icmpOutMsgs"),
        ("IP-MIB", "icmpOutErrors"),
        ("IP-MIB", "icmpOutDestUnreachs"),
        ("IP-MIB", "icmpOutTimeExcds"),
        ("IP-MIB", "icmpOutParmProbs"),
        ("IP-MIB", "icmpOutSrcQuenchs"),
        ("IP-MIB", "icmpOutRedirects"),
        ("IP-MIB", "icmpOutEchos"),
        ("IP-MIB", "icmpOutEchoReps"),
        ("IP-MIB", "icmpOutTimestamps"),
        ("IP-MIB", "icmpOutTimestampReps"),
        ("IP-MIB", "icmpOutAddrMasks"),
        ("IP-MIB", "icmpOutAddrMaskReps"))
)
if mibBuilder.loadTexts:
    icmpGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    icmpGroup.setDescription("The icmp group of objects providing ICMP statistics. As part of the version independence, this group has been deprecated. ")

ipv4GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 3)
)
ipv4GeneralGroup.setObjects(
      *(("IP-MIB", "ipForwarding"),
        ("IP-MIB", "ipDefaultTTL"),
        ("IP-MIB", "ipReasmTimeout"))
)
if mibBuilder.loadTexts:
    ipv4GeneralGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv4GeneralGroup.setDescription("The group of IPv4-specific objects for basic management of IPv4 entities.")

ipv4IfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 4)
)
ipv4IfGroup.setObjects(
      *(("IP-MIB", "ipv4InterfaceReasmMaxSize"),
        ("IP-MIB", "ipv4InterfaceEnableStatus"),
        ("IP-MIB", "ipv4InterfaceRetransmitTime"))
)
if mibBuilder.loadTexts:
    ipv4IfGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv4IfGroup.setDescription("The group of IPv4-specific objects for basic management of IPv4 interfaces.")

ipv6GeneralGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 5)
)
ipv6GeneralGroup2.setObjects(
      *(("IP-MIB", "ipv6IpForwarding"),
        ("IP-MIB", "ipv6IpDefaultHopLimit"))
)
if mibBuilder.loadTexts:
    ipv6GeneralGroup2.setStatus("current")
if mibBuilder.loadTexts:
    ipv6GeneralGroup2.setDescription("The IPv6 group of objects providing for basic management of IPv6 entities.")

ipv6IfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 6)
)
ipv6IfGroup.setObjects(
      *(("IP-MIB", "ipv6InterfaceReasmMaxSize"),
        ("IP-MIB", "ipv6InterfaceIdentifier"),
        ("IP-MIB", "ipv6InterfaceEnableStatus"),
        ("IP-MIB", "ipv6InterfaceReachableTime"),
        ("IP-MIB", "ipv6InterfaceRetransmitTime"),
        ("IP-MIB", "ipv6InterfaceForwarding"))
)
if mibBuilder.loadTexts:
    ipv6IfGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv6IfGroup.setDescription("The group of IPv6-specific objects for basic management of IPv6 interfaces.")

ipLastChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 7)
)
ipLastChangeGroup.setObjects(
      *(("IP-MIB", "ipv4InterfaceTableLastChange"),
        ("IP-MIB", "ipv6InterfaceTableLastChange"),
        ("IP-MIB", "ipIfStatsTableLastChange"))
)
if mibBuilder.loadTexts:
    ipLastChangeGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipLastChangeGroup.setDescription("The last change objects associated with this MIB. These objects are optional for all agents. They SHOULD be implemented on agents where it is possible to determine the proper values. Where it is not possible to determine the proper values, for example when the tables are split amongst several sub-agents using AgentX, the agent MUST NOT implement these objects to return an incorrect or static value.")

ipSystemStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 8)
)
ipSystemStatsGroup.setObjects(
      *(("IP-MIB", "ipSystemStatsInReceives"),
        ("IP-MIB", "ipSystemStatsInOctets"),
        ("IP-MIB", "ipSystemStatsInHdrErrors"),
        ("IP-MIB", "ipSystemStatsInNoRoutes"),
        ("IP-MIB", "ipSystemStatsInAddrErrors"),
        ("IP-MIB", "ipSystemStatsInUnknownProtos"),
        ("IP-MIB", "ipSystemStatsInTruncatedPkts"),
        ("IP-MIB", "ipSystemStatsInForwDatagrams"),
        ("IP-MIB", "ipSystemStatsReasmReqds"),
        ("IP-MIB", "ipSystemStatsReasmOKs"),
        ("IP-MIB", "ipSystemStatsReasmFails"),
        ("IP-MIB", "ipSystemStatsInDiscards"),
        ("IP-MIB", "ipSystemStatsInDelivers"),
        ("IP-MIB", "ipSystemStatsOutRequests"),
        ("IP-MIB", "ipSystemStatsOutNoRoutes"),
        ("IP-MIB", "ipSystemStatsOutForwDatagrams"),
        ("IP-MIB", "ipSystemStatsOutDiscards"),
        ("IP-MIB", "ipSystemStatsOutFragReqds"),
        ("IP-MIB", "ipSystemStatsOutFragOKs"),
        ("IP-MIB", "ipSystemStatsOutFragFails"),
        ("IP-MIB", "ipSystemStatsOutFragCreates"),
        ("IP-MIB", "ipSystemStatsOutTransmits"),
        ("IP-MIB", "ipSystemStatsOutOctets"),
        ("IP-MIB", "ipSystemStatsInMcastPkts"),
        ("IP-MIB", "ipSystemStatsInMcastOctets"),
        ("IP-MIB", "ipSystemStatsOutMcastPkts"),
        ("IP-MIB", "ipSystemStatsOutMcastOctets"),
        ("IP-MIB", "ipSystemStatsDiscontinuityTime"),
        ("IP-MIB", "ipSystemStatsRefreshRate"))
)
if mibBuilder.loadTexts:
    ipSystemStatsGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsGroup.setDescription("IP system wide statistics.")

ipv4SystemStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 9)
)
ipv4SystemStatsGroup.setObjects(
      *(("IP-MIB", "ipSystemStatsInBcastPkts"),
        ("IP-MIB", "ipSystemStatsOutBcastPkts"))
)
if mibBuilder.loadTexts:
    ipv4SystemStatsGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv4SystemStatsGroup.setDescription("IPv4 only system wide statistics.")

ipSystemStatsHCOctetGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 10)
)
ipSystemStatsHCOctetGroup.setObjects(
      *(("IP-MIB", "ipSystemStatsHCInOctets"),
        ("IP-MIB", "ipSystemStatsHCOutOctets"),
        ("IP-MIB", "ipSystemStatsHCInMcastOctets"),
        ("IP-MIB", "ipSystemStatsHCOutMcastOctets"))
)
if mibBuilder.loadTexts:
    ipSystemStatsHCOctetGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCOctetGroup.setDescription("IP system wide statistics for systems that may overflow the standard octet counters within 1 hour.")

ipSystemStatsHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 11)
)
ipSystemStatsHCPacketGroup.setObjects(
      *(("IP-MIB", "ipSystemStatsHCInReceives"),
        ("IP-MIB", "ipSystemStatsHCInForwDatagrams"),
        ("IP-MIB", "ipSystemStatsHCInDelivers"),
        ("IP-MIB", "ipSystemStatsHCOutRequests"),
        ("IP-MIB", "ipSystemStatsHCOutForwDatagrams"),
        ("IP-MIB", "ipSystemStatsHCOutTransmits"),
        ("IP-MIB", "ipSystemStatsHCInMcastPkts"),
        ("IP-MIB", "ipSystemStatsHCOutMcastPkts"))
)
if mibBuilder.loadTexts:
    ipSystemStatsHCPacketGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipSystemStatsHCPacketGroup.setDescription("IP system wide statistics for systems that may overflow the standard packet counters within 1 hour.")

ipv4SystemStatsHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 12)
)
ipv4SystemStatsHCPacketGroup.setObjects(
      *(("IP-MIB", "ipSystemStatsHCInBcastPkts"),
        ("IP-MIB", "ipSystemStatsHCOutBcastPkts"))
)
if mibBuilder.loadTexts:
    ipv4SystemStatsHCPacketGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv4SystemStatsHCPacketGroup.setDescription("IPv4 only system wide statistics for systems that may overflow the standard packet counters within 1 hour.")

ipIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 13)
)
ipIfStatsGroup.setObjects(
      *(("IP-MIB", "ipIfStatsInReceives"),
        ("IP-MIB", "ipIfStatsInOctets"),
        ("IP-MIB", "ipIfStatsInHdrErrors"),
        ("IP-MIB", "ipIfStatsInNoRoutes"),
        ("IP-MIB", "ipIfStatsInAddrErrors"),
        ("IP-MIB", "ipIfStatsInUnknownProtos"),
        ("IP-MIB", "ipIfStatsInTruncatedPkts"),
        ("IP-MIB", "ipIfStatsInForwDatagrams"),
        ("IP-MIB", "ipIfStatsReasmReqds"),
        ("IP-MIB", "ipIfStatsReasmOKs"),
        ("IP-MIB", "ipIfStatsReasmFails"),
        ("IP-MIB", "ipIfStatsInDiscards"),
        ("IP-MIB", "ipIfStatsInDelivers"),
        ("IP-MIB", "ipIfStatsOutRequests"),
        ("IP-MIB", "ipIfStatsOutForwDatagrams"),
        ("IP-MIB", "ipIfStatsOutDiscards"),
        ("IP-MIB", "ipIfStatsOutFragReqds"),
        ("IP-MIB", "ipIfStatsOutFragOKs"),
        ("IP-MIB", "ipIfStatsOutFragFails"),
        ("IP-MIB", "ipIfStatsOutFragCreates"),
        ("IP-MIB", "ipIfStatsOutTransmits"),
        ("IP-MIB", "ipIfStatsOutOctets"),
        ("IP-MIB", "ipIfStatsInMcastPkts"),
        ("IP-MIB", "ipIfStatsInMcastOctets"),
        ("IP-MIB", "ipIfStatsOutMcastPkts"),
        ("IP-MIB", "ipIfStatsOutMcastOctets"),
        ("IP-MIB", "ipIfStatsDiscontinuityTime"),
        ("IP-MIB", "ipIfStatsRefreshRate"))
)
if mibBuilder.loadTexts:
    ipIfStatsGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsGroup.setDescription("IP per-interface statistics.")

ipv4IfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 14)
)
ipv4IfStatsGroup.setObjects(
      *(("IP-MIB", "ipIfStatsInBcastPkts"),
        ("IP-MIB", "ipIfStatsOutBcastPkts"))
)
if mibBuilder.loadTexts:
    ipv4IfStatsGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv4IfStatsGroup.setDescription("IPv4 only per-interface statistics.")

ipIfStatsHCOctetGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 15)
)
ipIfStatsHCOctetGroup.setObjects(
      *(("IP-MIB", "ipIfStatsHCInOctets"),
        ("IP-MIB", "ipIfStatsHCOutOctets"),
        ("IP-MIB", "ipIfStatsHCInMcastOctets"),
        ("IP-MIB", "ipIfStatsHCOutMcastOctets"))
)
if mibBuilder.loadTexts:
    ipIfStatsHCOctetGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCOctetGroup.setDescription("IP per-interfaces statistics for systems that include interfaces that may overflow the standard octet counters within 1 hour.")

ipIfStatsHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 16)
)
ipIfStatsHCPacketGroup.setObjects(
      *(("IP-MIB", "ipIfStatsHCInReceives"),
        ("IP-MIB", "ipIfStatsHCInForwDatagrams"),
        ("IP-MIB", "ipIfStatsHCInDelivers"),
        ("IP-MIB", "ipIfStatsHCOutRequests"),
        ("IP-MIB", "ipIfStatsHCOutForwDatagrams"),
        ("IP-MIB", "ipIfStatsHCOutTransmits"),
        ("IP-MIB", "ipIfStatsHCInMcastPkts"),
        ("IP-MIB", "ipIfStatsHCOutMcastPkts"))
)
if mibBuilder.loadTexts:
    ipIfStatsHCPacketGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipIfStatsHCPacketGroup.setDescription("IP per-interfaces statistics for systems that include interfaces that may overflow the standard packet counters within 1 hour.")

ipv4IfStatsHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 17)
)
ipv4IfStatsHCPacketGroup.setObjects(
      *(("IP-MIB", "ipIfStatsHCInBcastPkts"),
        ("IP-MIB", "ipIfStatsHCOutBcastPkts"))
)
if mibBuilder.loadTexts:
    ipv4IfStatsHCPacketGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv4IfStatsHCPacketGroup.setDescription("IPv4 only per-interface statistics for systems that include interfaces that may overflow the standard packet counters within 1 hour.")

ipAddressPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 18)
)
ipAddressPrefixGroup.setObjects(
      *(("IP-MIB", "ipAddressPrefixOrigin"),
        ("IP-MIB", "ipAddressPrefixOnLinkFlag"),
        ("IP-MIB", "ipAddressPrefixAutonomousFlag"),
        ("IP-MIB", "ipAddressPrefixAdvPreferredLifetime"),
        ("IP-MIB", "ipAddressPrefixAdvValidLifetime"))
)
if mibBuilder.loadTexts:
    ipAddressPrefixGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressPrefixGroup.setDescription("The group of objects for providing information about address prefixes used by this node.")

ipAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 19)
)
ipAddressGroup.setObjects(
      *(("IP-MIB", "ipAddressSpinLock"),
        ("IP-MIB", "ipAddressIfIndex"),
        ("IP-MIB", "ipAddressType"),
        ("IP-MIB", "ipAddressPrefix"),
        ("IP-MIB", "ipAddressOrigin"),
        ("IP-MIB", "ipAddressStatus"),
        ("IP-MIB", "ipAddressCreated"),
        ("IP-MIB", "ipAddressLastChanged"),
        ("IP-MIB", "ipAddressRowStatus"),
        ("IP-MIB", "ipAddressStorageType"))
)
if mibBuilder.loadTexts:
    ipAddressGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressGroup.setDescription("The group of objects for providing information about the addresses relevant to this entity's interfaces.")

ipNetToPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 20)
)
ipNetToPhysicalGroup.setObjects(
      *(("IP-MIB", "ipNetToPhysicalPhysAddress"),
        ("IP-MIB", "ipNetToPhysicalLastUpdated"),
        ("IP-MIB", "ipNetToPhysicalType"),
        ("IP-MIB", "ipNetToPhysicalState"),
        ("IP-MIB", "ipNetToPhysicalRowStatus"))
)
if mibBuilder.loadTexts:
    ipNetToPhysicalGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipNetToPhysicalGroup.setDescription("The group of objects for providing information about the mappings of network address to physical address known to this node.")

ipv6ScopeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 21)
)
ipv6ScopeGroup.setObjects(
      *(("IP-MIB", "ipv6ScopeZoneIndexLinkLocal"),
        ("IP-MIB", "ipv6ScopeZoneIndex3"),
        ("IP-MIB", "ipv6ScopeZoneIndexAdminLocal"),
        ("IP-MIB", "ipv6ScopeZoneIndexSiteLocal"),
        ("IP-MIB", "ipv6ScopeZoneIndex6"),
        ("IP-MIB", "ipv6ScopeZoneIndex7"),
        ("IP-MIB", "ipv6ScopeZoneIndexOrganizationLocal"),
        ("IP-MIB", "ipv6ScopeZoneIndex9"),
        ("IP-MIB", "ipv6ScopeZoneIndexA"),
        ("IP-MIB", "ipv6ScopeZoneIndexB"),
        ("IP-MIB", "ipv6ScopeZoneIndexC"),
        ("IP-MIB", "ipv6ScopeZoneIndexD"))
)
if mibBuilder.loadTexts:
    ipv6ScopeGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv6ScopeGroup.setDescription("The group of objects for managing IPv6 scope zones.")

ipDefaultRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 22)
)
ipDefaultRouterGroup.setObjects(
      *(("IP-MIB", "ipDefaultRouterLifetime"),
        ("IP-MIB", "ipDefaultRouterPreference"))
)
if mibBuilder.loadTexts:
    ipDefaultRouterGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipDefaultRouterGroup.setDescription("The group of objects for providing information about default routers known to this node.")

ipv6RouterAdvertGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 23)
)
ipv6RouterAdvertGroup.setObjects(
      *(("IP-MIB", "ipv6RouterAdvertSpinLock"),
        ("IP-MIB", "ipv6RouterAdvertSendAdverts"),
        ("IP-MIB", "ipv6RouterAdvertMaxInterval"),
        ("IP-MIB", "ipv6RouterAdvertMinInterval"),
        ("IP-MIB", "ipv6RouterAdvertManagedFlag"),
        ("IP-MIB", "ipv6RouterAdvertOtherConfigFlag"),
        ("IP-MIB", "ipv6RouterAdvertLinkMTU"),
        ("IP-MIB", "ipv6RouterAdvertReachableTime"),
        ("IP-MIB", "ipv6RouterAdvertRetransmitTime"),
        ("IP-MIB", "ipv6RouterAdvertCurHopLimit"),
        ("IP-MIB", "ipv6RouterAdvertDefaultLifetime"),
        ("IP-MIB", "ipv6RouterAdvertRowStatus"))
)
if mibBuilder.loadTexts:
    ipv6RouterAdvertGroup.setStatus("current")
if mibBuilder.loadTexts:
    ipv6RouterAdvertGroup.setDescription("The group of objects for controlling information advertised by IPv6 routers.")

icmpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 48, 2, 2, 24)
)
icmpStatsGroup.setObjects(
      *(("IP-MIB", "icmpStatsInMsgs"),
        ("IP-MIB", "icmpStatsInErrors"),
        ("IP-MIB", "icmpStatsOutMsgs"),
        ("IP-MIB", "icmpStatsOutErrors"),
        ("IP-MIB", "icmpMsgStatsInPkts"),
        ("IP-MIB", "icmpMsgStatsOutPkts"))
)
if mibBuilder.loadTexts:
    icmpStatsGroup.setStatus("current")
if mibBuilder.loadTexts:
    icmpStatsGroup.setDescription("The group of objects providing ICMP statistics.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 48, 2, 1, 1)
)
ipMIBCompliance.setObjects(
      *(("IP-MIB", "ipGroup"),
        ("IP-MIB", "icmpGroup"))
)
if mibBuilder.loadTexts:
    ipMIBCompliance.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    ipMIBCompliance.setDescription("The compliance statement for systems that implement only IPv4. For version-independence, this compliance statement is deprecated in favor of ipMIBCompliance2.")

ipMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 48, 2, 1, 2)
)
ipMIBCompliance2.setObjects(
      *(("IP-MIB", "ipSystemStatsGroup"),
        ("IP-MIB", "ipAddressGroup"),
        ("IP-MIB", "ipNetToPhysicalGroup"),
        ("IP-MIB", "ipDefaultRouterGroup"),
        ("IP-MIB", "icmpStatsGroup"),
        ("IP-MIB", "ipSystemStatsHCOctetGroup"),
        ("IP-MIB", "ipSystemStatsHCPacketGroup"),
        ("IP-MIB", "ipIfStatsGroup"),
        ("IP-MIB", "ipIfStatsHCOctetGroup"),
        ("IP-MIB", "ipIfStatsHCPacketGroup"),
        ("IP-MIB", "ipv4GeneralGroup"),
        ("IP-MIB", "ipv4IfGroup"),
        ("IP-MIB", "ipv4SystemStatsGroup"),
        ("IP-MIB", "ipv4SystemStatsHCPacketGroup"),
        ("IP-MIB", "ipv4IfStatsGroup"),
        ("IP-MIB", "ipv4IfStatsHCPacketGroup"),
        ("IP-MIB", "ipv6GeneralGroup2"),
        ("IP-MIB", "ipv6IfGroup"),
        ("IP-MIB", "ipAddressPrefixGroup"),
        ("IP-MIB", "ipv6ScopeGroup"),
        ("IP-MIB", "ipv6RouterAdvertGroup"),
        ("IP-MIB", "ipLastChangeGroup"))
)
if mibBuilder.loadTexts:
    ipMIBCompliance2.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ipMIBCompliance2.setDescription("The compliance statement for systems that implement IP - either IPv4 or IPv6. There are a number of INDEX objects that cannot be represented in the form of OBJECT clauses in SMIv2, but for which we have the following compliance requirements, expressed in OBJECT clause form in this description clause: -- OBJECT ipSystemStatsIPVersion -- SYNTAX InetVersion {ipv4(1), ipv6(2)} -- DESCRIPTION -- This MIB requires support for only IPv4 and IPv6 -- versions. -- -- OBJECT ipIfStatsIPVersion -- SYNTAX InetVersion {ipv4(1), ipv6(2)} -- DESCRIPTION -- This MIB requires support for only IPv4 and IPv6 -- versions. -- -- OBJECT icmpStatsIPVersion -- SYNTAX InetVersion {ipv4(1), ipv6(2)} -- DESCRIPTION -- This MIB requires support for only IPv4 and IPv6 -- versions. -- -- OBJECT icmpMsgStatsIPVersion -- SYNTAX InetVersion {ipv4(1), ipv6(2)} -- DESCRIPTION -- This MIB requires support for only IPv4 and IPv6 -- versions. -- -- OBJECT ipAddressPrefixType -- SYNTAX InetAddressType {ipv4(1), ipv6(2)} -- DESCRIPTION -- This MIB requires support for only global IPv4 and -- IPv6 address types. -- -- OBJECT ipAddressPrefixPrefix -- SYNTAX InetAddress (Size(4 | 16)) -- DESCRIPTION -- This MIB requires support for only global IPv4 and -- IPv6 addresses and so the size can be either 4 or -- 16 bytes. -- -- OBJECT ipAddressAddrType -- SYNTAX InetAddressType {ipv4(1), ipv6(2), -- ipv4z(3), ipv6z(4)} -- DESCRIPTION -- This MIB requires support for only global and -- non-global IPv4 and IPv6 address types. -- -- OBJECT ipAddressAddr -- SYNTAX InetAddress (Size(4 | 8 | 16 | 20)) -- DESCRIPTION -- This MIB requires support for only global and -- non-global IPv4 and IPv6 addresses and so the size -- can be 4, 8, 16, or 20 bytes. -- -- OBJECT ipNetToPhysicalNetAddressType -- SYNTAX InetAddressType {ipv4(1), ipv6(2), -- ipv4z(3), ipv6z(4)} -- DESCRIPTION -- This MIB requires support for only global and -- non-global IPv4 and IPv6 address types. -- -- OBJECT ipNetToPhysicalNetAddress -- SYNTAX InetAddress (Size(4 | 8 | 16 | 20)) -- DESCRIPTION -- This MIB requires support for only global and -- non-global IPv4 and IPv6 addresses and so the size -- can be 4, 8, 16, or 20 bytes. -- -- OBJECT ipDefaultRouterAddressType -- SYNTAX InetAddressType {ipv4(1), ipv6(2), -- ipv4z(3), ipv6z(4)} -- DESCRIPTION -- This MIB requires support for only global and -- non-global IPv4 and IPv6 address types. -- -- OBJECT ipDefaultRouterAddress -- SYNTAX InetAddress (Size(4 | 8 | 16 | 20)) -- DESCRIPTION -- This MIB requires support for only global and -- non-global IPv4 and IPv6 addresses and so the size -- can be 4, 8, 16, or 20 bytes.")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-MIB",
    **{"IpAddressOriginTC": IpAddressOriginTC,
       "IpAddressStatusTC": IpAddressStatusTC,
       "IpAddressPrefixOriginTC": IpAddressPrefixOriginTC,
       "Ipv6AddressIfIdentifierTC": Ipv6AddressIfIdentifierTC,
       "ip": ip,
       "ipForwarding": ipForwarding,
       "ipDefaultTTL": ipDefaultTTL,
       "ipInReceives": ipInReceives,
       "ipInHdrErrors": ipInHdrErrors,
       "ipInAddrErrors": ipInAddrErrors,
       "ipForwDatagrams": ipForwDatagrams,
       "ipInUnknownProtos": ipInUnknownProtos,
       "ipInDiscards": ipInDiscards,
       "ipInDelivers": ipInDelivers,
       "ipOutRequests": ipOutRequests,
       "ipOutDiscards": ipOutDiscards,
       "ipOutNoRoutes": ipOutNoRoutes,
       "ipReasmTimeout": ipReasmTimeout,
       "ipReasmReqds": ipReasmReqds,
       "ipReasmOKs": ipReasmOKs,
       "ipReasmFails": ipReasmFails,
       "ipFragOKs": ipFragOKs,
       "ipFragFails": ipFragFails,
       "ipFragCreates": ipFragCreates,
       "ipAddrTable": ipAddrTable,
       "ipAddrEntry": ipAddrEntry,
       "ipAdEntAddr": ipAdEntAddr,
       "ipAdEntIfIndex": ipAdEntIfIndex,
       "ipAdEntNetMask": ipAdEntNetMask,
       "ipAdEntBcastAddr": ipAdEntBcastAddr,
       "ipAdEntReasmMaxSize": ipAdEntReasmMaxSize,
       "ipNetToMediaTable": ipNetToMediaTable,
       "ipNetToMediaEntry": ipNetToMediaEntry,
       "ipNetToMediaIfIndex": ipNetToMediaIfIndex,
       "ipNetToMediaPhysAddress": ipNetToMediaPhysAddress,
       "ipNetToMediaNetAddress": ipNetToMediaNetAddress,
       "ipNetToMediaType": ipNetToMediaType,
       "ipRoutingDiscards": ipRoutingDiscards,
       "ipv6IpForwarding": ipv6IpForwarding,
       "ipv6IpDefaultHopLimit": ipv6IpDefaultHopLimit,
       "ipv4InterfaceTableLastChange": ipv4InterfaceTableLastChange,
       "ipv4InterfaceTable": ipv4InterfaceTable,
       "ipv4InterfaceEntry": ipv4InterfaceEntry,
       "ipv4InterfaceIfIndex": ipv4InterfaceIfIndex,
       "ipv4InterfaceReasmMaxSize": ipv4InterfaceReasmMaxSize,
       "ipv4InterfaceEnableStatus": ipv4InterfaceEnableStatus,
       "ipv4InterfaceRetransmitTime": ipv4InterfaceRetransmitTime,
       "ipv6InterfaceTableLastChange": ipv6InterfaceTableLastChange,
       "ipv6InterfaceTable": ipv6InterfaceTable,
       "ipv6InterfaceEntry": ipv6InterfaceEntry,
       "ipv6InterfaceIfIndex": ipv6InterfaceIfIndex,
       "ipv6InterfaceReasmMaxSize": ipv6InterfaceReasmMaxSize,
       "ipv6InterfaceIdentifier": ipv6InterfaceIdentifier,
       "ipv6InterfaceEnableStatus": ipv6InterfaceEnableStatus,
       "ipv6InterfaceReachableTime": ipv6InterfaceReachableTime,
       "ipv6InterfaceRetransmitTime": ipv6InterfaceRetransmitTime,
       "ipv6InterfaceForwarding": ipv6InterfaceForwarding,
       "ipTrafficStats": ipTrafficStats,
       "ipSystemStatsTable": ipSystemStatsTable,
       "ipSystemStatsEntry": ipSystemStatsEntry,
       "ipSystemStatsIPVersion": ipSystemStatsIPVersion,
       "ipSystemStatsInReceives": ipSystemStatsInReceives,
       "ipSystemStatsHCInReceives": ipSystemStatsHCInReceives,
       "ipSystemStatsInOctets": ipSystemStatsInOctets,
       "ipSystemStatsHCInOctets": ipSystemStatsHCInOctets,
       "ipSystemStatsInHdrErrors": ipSystemStatsInHdrErrors,
       "ipSystemStatsInNoRoutes": ipSystemStatsInNoRoutes,
       "ipSystemStatsInAddrErrors": ipSystemStatsInAddrErrors,
       "ipSystemStatsInUnknownProtos": ipSystemStatsInUnknownProtos,
       "ipSystemStatsInTruncatedPkts": ipSystemStatsInTruncatedPkts,
       "ipSystemStatsInForwDatagrams": ipSystemStatsInForwDatagrams,
       "ipSystemStatsHCInForwDatagrams": ipSystemStatsHCInForwDatagrams,
       "ipSystemStatsReasmReqds": ipSystemStatsReasmReqds,
       "ipSystemStatsReasmOKs": ipSystemStatsReasmOKs,
       "ipSystemStatsReasmFails": ipSystemStatsReasmFails,
       "ipSystemStatsInDiscards": ipSystemStatsInDiscards,
       "ipSystemStatsInDelivers": ipSystemStatsInDelivers,
       "ipSystemStatsHCInDelivers": ipSystemStatsHCInDelivers,
       "ipSystemStatsOutRequests": ipSystemStatsOutRequests,
       "ipSystemStatsHCOutRequests": ipSystemStatsHCOutRequests,
       "ipSystemStatsOutNoRoutes": ipSystemStatsOutNoRoutes,
       "ipSystemStatsOutForwDatagrams": ipSystemStatsOutForwDatagrams,
       "ipSystemStatsHCOutForwDatagrams": ipSystemStatsHCOutForwDatagrams,
       "ipSystemStatsOutDiscards": ipSystemStatsOutDiscards,
       "ipSystemStatsOutFragReqds": ipSystemStatsOutFragReqds,
       "ipSystemStatsOutFragOKs": ipSystemStatsOutFragOKs,
       "ipSystemStatsOutFragFails": ipSystemStatsOutFragFails,
       "ipSystemStatsOutFragCreates": ipSystemStatsOutFragCreates,
       "ipSystemStatsOutTransmits": ipSystemStatsOutTransmits,
       "ipSystemStatsHCOutTransmits": ipSystemStatsHCOutTransmits,
       "ipSystemStatsOutOctets": ipSystemStatsOutOctets,
       "ipSystemStatsHCOutOctets": ipSystemStatsHCOutOctets,
       "ipSystemStatsInMcastPkts": ipSystemStatsInMcastPkts,
       "ipSystemStatsHCInMcastPkts": ipSystemStatsHCInMcastPkts,
       "ipSystemStatsInMcastOctets": ipSystemStatsInMcastOctets,
       "ipSystemStatsHCInMcastOctets": ipSystemStatsHCInMcastOctets,
       "ipSystemStatsOutMcastPkts": ipSystemStatsOutMcastPkts,
       "ipSystemStatsHCOutMcastPkts": ipSystemStatsHCOutMcastPkts,
       "ipSystemStatsOutMcastOctets": ipSystemStatsOutMcastOctets,
       "ipSystemStatsHCOutMcastOctets": ipSystemStatsHCOutMcastOctets,
       "ipSystemStatsInBcastPkts": ipSystemStatsInBcastPkts,
       "ipSystemStatsHCInBcastPkts": ipSystemStatsHCInBcastPkts,
       "ipSystemStatsOutBcastPkts": ipSystemStatsOutBcastPkts,
       "ipSystemStatsHCOutBcastPkts": ipSystemStatsHCOutBcastPkts,
       "ipSystemStatsDiscontinuityTime": ipSystemStatsDiscontinuityTime,
       "ipSystemStatsRefreshRate": ipSystemStatsRefreshRate,
       "ipIfStatsTableLastChange": ipIfStatsTableLastChange,
       "ipIfStatsTable": ipIfStatsTable,
       "ipIfStatsEntry": ipIfStatsEntry,
       "ipIfStatsIPVersion": ipIfStatsIPVersion,
       "ipIfStatsIfIndex": ipIfStatsIfIndex,
       "ipIfStatsInReceives": ipIfStatsInReceives,
       "ipIfStatsHCInReceives": ipIfStatsHCInReceives,
       "ipIfStatsInOctets": ipIfStatsInOctets,
       "ipIfStatsHCInOctets": ipIfStatsHCInOctets,
       "ipIfStatsInHdrErrors": ipIfStatsInHdrErrors,
       "ipIfStatsInNoRoutes": ipIfStatsInNoRoutes,
       "ipIfStatsInAddrErrors": ipIfStatsInAddrErrors,
       "ipIfStatsInUnknownProtos": ipIfStatsInUnknownProtos,
       "ipIfStatsInTruncatedPkts": ipIfStatsInTruncatedPkts,
       "ipIfStatsInForwDatagrams": ipIfStatsInForwDatagrams,
       "ipIfStatsHCInForwDatagrams": ipIfStatsHCInForwDatagrams,
       "ipIfStatsReasmReqds": ipIfStatsReasmReqds,
       "ipIfStatsReasmOKs": ipIfStatsReasmOKs,
       "ipIfStatsReasmFails": ipIfStatsReasmFails,
       "ipIfStatsInDiscards": ipIfStatsInDiscards,
       "ipIfStatsInDelivers": ipIfStatsInDelivers,
       "ipIfStatsHCInDelivers": ipIfStatsHCInDelivers,
       "ipIfStatsOutRequests": ipIfStatsOutRequests,
       "ipIfStatsHCOutRequests": ipIfStatsHCOutRequests,
       "ipIfStatsOutForwDatagrams": ipIfStatsOutForwDatagrams,
       "ipIfStatsHCOutForwDatagrams": ipIfStatsHCOutForwDatagrams,
       "ipIfStatsOutDiscards": ipIfStatsOutDiscards,
       "ipIfStatsOutFragReqds": ipIfStatsOutFragReqds,
       "ipIfStatsOutFragOKs": ipIfStatsOutFragOKs,
       "ipIfStatsOutFragFails": ipIfStatsOutFragFails,
       "ipIfStatsOutFragCreates": ipIfStatsOutFragCreates,
       "ipIfStatsOutTransmits": ipIfStatsOutTransmits,
       "ipIfStatsHCOutTransmits": ipIfStatsHCOutTransmits,
       "ipIfStatsOutOctets": ipIfStatsOutOctets,
       "ipIfStatsHCOutOctets": ipIfStatsHCOutOctets,
       "ipIfStatsInMcastPkts": ipIfStatsInMcastPkts,
       "ipIfStatsHCInMcastPkts": ipIfStatsHCInMcastPkts,
       "ipIfStatsInMcastOctets": ipIfStatsInMcastOctets,
       "ipIfStatsHCInMcastOctets": ipIfStatsHCInMcastOctets,
       "ipIfStatsOutMcastPkts": ipIfStatsOutMcastPkts,
       "ipIfStatsHCOutMcastPkts": ipIfStatsHCOutMcastPkts,
       "ipIfStatsOutMcastOctets": ipIfStatsOutMcastOctets,
       "ipIfStatsHCOutMcastOctets": ipIfStatsHCOutMcastOctets,
       "ipIfStatsInBcastPkts": ipIfStatsInBcastPkts,
       "ipIfStatsHCInBcastPkts": ipIfStatsHCInBcastPkts,
       "ipIfStatsOutBcastPkts": ipIfStatsOutBcastPkts,
       "ipIfStatsHCOutBcastPkts": ipIfStatsHCOutBcastPkts,
       "ipIfStatsDiscontinuityTime": ipIfStatsDiscontinuityTime,
       "ipIfStatsRefreshRate": ipIfStatsRefreshRate,
       "ipAddressPrefixTable": ipAddressPrefixTable,
       "ipAddressPrefixEntry": ipAddressPrefixEntry,
       "ipAddressPrefixIfIndex": ipAddressPrefixIfIndex,
       "ipAddressPrefixType": ipAddressPrefixType,
       "ipAddressPrefixPrefix": ipAddressPrefixPrefix,
       "ipAddressPrefixLength": ipAddressPrefixLength,
       "ipAddressPrefixOrigin": ipAddressPrefixOrigin,
       "ipAddressPrefixOnLinkFlag": ipAddressPrefixOnLinkFlag,
       "ipAddressPrefixAutonomousFlag": ipAddressPrefixAutonomousFlag,
       "ipAddressPrefixAdvPreferredLifetime": ipAddressPrefixAdvPreferredLifetime,
       "ipAddressPrefixAdvValidLifetime": ipAddressPrefixAdvValidLifetime,
       "ipAddressSpinLock": ipAddressSpinLock,
       "ipAddressTable": ipAddressTable,
       "ipAddressEntry": ipAddressEntry,
       "ipAddressAddrType": ipAddressAddrType,
       "ipAddressAddr": ipAddressAddr,
       "ipAddressIfIndex": ipAddressIfIndex,
       "ipAddressType": ipAddressType,
       "ipAddressPrefix": ipAddressPrefix,
       "ipAddressOrigin": ipAddressOrigin,
       "ipAddressStatus": ipAddressStatus,
       "ipAddressCreated": ipAddressCreated,
       "ipAddressLastChanged": ipAddressLastChanged,
       "ipAddressRowStatus": ipAddressRowStatus,
       "ipAddressStorageType": ipAddressStorageType,
       "ipNetToPhysicalTable": ipNetToPhysicalTable,
       "ipNetToPhysicalEntry": ipNetToPhysicalEntry,
       "ipNetToPhysicalIfIndex": ipNetToPhysicalIfIndex,
       "ipNetToPhysicalNetAddressType": ipNetToPhysicalNetAddressType,
       "ipNetToPhysicalNetAddress": ipNetToPhysicalNetAddress,
       "ipNetToPhysicalPhysAddress": ipNetToPhysicalPhysAddress,
       "ipNetToPhysicalLastUpdated": ipNetToPhysicalLastUpdated,
       "ipNetToPhysicalType": ipNetToPhysicalType,
       "ipNetToPhysicalState": ipNetToPhysicalState,
       "ipNetToPhysicalRowStatus": ipNetToPhysicalRowStatus,
       "ipv6ScopeZoneIndexTable": ipv6ScopeZoneIndexTable,
       "ipv6ScopeZoneIndexEntry": ipv6ScopeZoneIndexEntry,
       "ipv6ScopeZoneIndexIfIndex": ipv6ScopeZoneIndexIfIndex,
       "ipv6ScopeZoneIndexLinkLocal": ipv6ScopeZoneIndexLinkLocal,
       "ipv6ScopeZoneIndex3": ipv6ScopeZoneIndex3,
       "ipv6ScopeZoneIndexAdminLocal": ipv6ScopeZoneIndexAdminLocal,
       "ipv6ScopeZoneIndexSiteLocal": ipv6ScopeZoneIndexSiteLocal,
       "ipv6ScopeZoneIndex6": ipv6ScopeZoneIndex6,
       "ipv6ScopeZoneIndex7": ipv6ScopeZoneIndex7,
       "ipv6ScopeZoneIndexOrganizationLocal": ipv6ScopeZoneIndexOrganizationLocal,
       "ipv6ScopeZoneIndex9": ipv6ScopeZoneIndex9,
       "ipv6ScopeZoneIndexA": ipv6ScopeZoneIndexA,
       "ipv6ScopeZoneIndexB": ipv6ScopeZoneIndexB,
       "ipv6ScopeZoneIndexC": ipv6ScopeZoneIndexC,
       "ipv6ScopeZoneIndexD": ipv6ScopeZoneIndexD,
       "ipDefaultRouterTable": ipDefaultRouterTable,
       "ipDefaultRouterEntry": ipDefaultRouterEntry,
       "ipDefaultRouterAddressType": ipDefaultRouterAddressType,
       "ipDefaultRouterAddress": ipDefaultRouterAddress,
       "ipDefaultRouterIfIndex": ipDefaultRouterIfIndex,
       "ipDefaultRouterLifetime": ipDefaultRouterLifetime,
       "ipDefaultRouterPreference": ipDefaultRouterPreference,
       "ipv6RouterAdvertSpinLock": ipv6RouterAdvertSpinLock,
       "ipv6RouterAdvertTable": ipv6RouterAdvertTable,
       "ipv6RouterAdvertEntry": ipv6RouterAdvertEntry,
       "ipv6RouterAdvertIfIndex": ipv6RouterAdvertIfIndex,
       "ipv6RouterAdvertSendAdverts": ipv6RouterAdvertSendAdverts,
       "ipv6RouterAdvertMaxInterval": ipv6RouterAdvertMaxInterval,
       "ipv6RouterAdvertMinInterval": ipv6RouterAdvertMinInterval,
       "ipv6RouterAdvertManagedFlag": ipv6RouterAdvertManagedFlag,
       "ipv6RouterAdvertOtherConfigFlag": ipv6RouterAdvertOtherConfigFlag,
       "ipv6RouterAdvertLinkMTU": ipv6RouterAdvertLinkMTU,
       "ipv6RouterAdvertReachableTime": ipv6RouterAdvertReachableTime,
       "ipv6RouterAdvertRetransmitTime": ipv6RouterAdvertRetransmitTime,
       "ipv6RouterAdvertCurHopLimit": ipv6RouterAdvertCurHopLimit,
       "ipv6RouterAdvertDefaultLifetime": ipv6RouterAdvertDefaultLifetime,
       "ipv6RouterAdvertRowStatus": ipv6RouterAdvertRowStatus,
       "icmp": icmp,
       "icmpInMsgs": icmpInMsgs,
       "icmpInErrors": icmpInErrors,
       "icmpInDestUnreachs": icmpInDestUnreachs,
       "icmpInTimeExcds": icmpInTimeExcds,
       "icmpInParmProbs": icmpInParmProbs,
       "icmpInSrcQuenchs": icmpInSrcQuenchs,
       "icmpInRedirects": icmpInRedirects,
       "icmpInEchos": icmpInEchos,
       "icmpInEchoReps": icmpInEchoReps,
       "icmpInTimestamps": icmpInTimestamps,
       "icmpInTimestampReps": icmpInTimestampReps,
       "icmpInAddrMasks": icmpInAddrMasks,
       "icmpInAddrMaskReps": icmpInAddrMaskReps,
       "icmpOutMsgs": icmpOutMsgs,
       "icmpOutErrors": icmpOutErrors,
       "icmpOutDestUnreachs": icmpOutDestUnreachs,
       "icmpOutTimeExcds": icmpOutTimeExcds,
       "icmpOutParmProbs": icmpOutParmProbs,
       "icmpOutSrcQuenchs": icmpOutSrcQuenchs,
       "icmpOutRedirects": icmpOutRedirects,
       "icmpOutEchos": icmpOutEchos,
       "icmpOutEchoReps": icmpOutEchoReps,
       "icmpOutTimestamps": icmpOutTimestamps,
       "icmpOutTimestampReps": icmpOutTimestampReps,
       "icmpOutAddrMasks": icmpOutAddrMasks,
       "icmpOutAddrMaskReps": icmpOutAddrMaskReps,
       "icmpStatsTable": icmpStatsTable,
       "icmpStatsEntry": icmpStatsEntry,
       "icmpStatsIPVersion": icmpStatsIPVersion,
       "icmpStatsInMsgs": icmpStatsInMsgs,
       "icmpStatsInErrors": icmpStatsInErrors,
       "icmpStatsOutMsgs": icmpStatsOutMsgs,
       "icmpStatsOutErrors": icmpStatsOutErrors,
       "icmpMsgStatsTable": icmpMsgStatsTable,
       "icmpMsgStatsEntry": icmpMsgStatsEntry,
       "icmpMsgStatsIPVersion": icmpMsgStatsIPVersion,
       "icmpMsgStatsType": icmpMsgStatsType,
       "icmpMsgStatsInPkts": icmpMsgStatsInPkts,
       "icmpMsgStatsOutPkts": icmpMsgStatsOutPkts,
       "ipMIB": ipMIB,
       "ipMIBConformance": ipMIBConformance,
       "ipMIBCompliances": ipMIBCompliances,
       "ipMIBCompliance": ipMIBCompliance,
       "ipMIBCompliance2": ipMIBCompliance2,
       "ipMIBGroups": ipMIBGroups,
       "ipGroup": ipGroup,
       "icmpGroup": icmpGroup,
       "ipv4GeneralGroup": ipv4GeneralGroup,
       "ipv4IfGroup": ipv4IfGroup,
       "ipv6GeneralGroup2": ipv6GeneralGroup2,
       "ipv6IfGroup": ipv6IfGroup,
       "ipLastChangeGroup": ipLastChangeGroup,
       "ipSystemStatsGroup": ipSystemStatsGroup,
       "ipv4SystemStatsGroup": ipv4SystemStatsGroup,
       "ipSystemStatsHCOctetGroup": ipSystemStatsHCOctetGroup,
       "ipSystemStatsHCPacketGroup": ipSystemStatsHCPacketGroup,
       "ipv4SystemStatsHCPacketGroup": ipv4SystemStatsHCPacketGroup,
       "ipIfStatsGroup": ipIfStatsGroup,
       "ipv4IfStatsGroup": ipv4IfStatsGroup,
       "ipIfStatsHCOctetGroup": ipIfStatsHCOctetGroup,
       "ipIfStatsHCPacketGroup": ipIfStatsHCPacketGroup,
       "ipv4IfStatsHCPacketGroup": ipv4IfStatsHCPacketGroup,
       "ipAddressPrefixGroup": ipAddressPrefixGroup,
       "ipAddressGroup": ipAddressGroup,
       "ipNetToPhysicalGroup": ipNetToPhysicalGroup,
       "ipv6ScopeGroup": ipv6ScopeGroup,
       "ipDefaultRouterGroup": ipDefaultRouterGroup,
       "ipv6RouterAdvertGroup": ipv6RouterAdvertGroup,
       "icmpStatsGroup": icmpStatsGroup}
)
