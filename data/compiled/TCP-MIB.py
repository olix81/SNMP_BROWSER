# SNMP MIB module (TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/TCP-MIB
# Produced by pysmi-2.0.0 at Sat Oct 17 14:25:41 2026
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
 Gauge32,
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
    "Gauge32",
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

tcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 49)
)
if mibBuilder.loadTexts:
    tcpMIB.setRevisions(
        ("2005-02-18 00:00",
         "1994-11-01 00:00",
         "1991-03-31 00:00")
    )
if mibBuilder.loadTexts:
    tcpMIB.setLastUpdated("200502180000Z")
if mibBuilder.loadTexts:
    tcpMIB.setOrganization("IETF IPv6 MIB Revision Team http://www.ietf.org/html.charters/ipv6-charter.html")
if mibBuilder.loadTexts:
    tcpMIB.setContactInfo("Rajiv Raghunarayan (editor) Cisco Systems Inc. 170 West Tasman Drive San Jose, CA 95134 Phone: +1 408 853 9612 Email: <raraghun@cisco.com> Send comments to <ipv6@ietf.org>")
if mibBuilder.loadTexts:
    tcpMIB.setDescription("The MIB module for managing TCP implementations. Copyright (C) The Internet Society (2005). This version of this MIB module is a part of RFC 4022; see the RFC itself for full legal notices.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)


class _TcpRtoAlgorithm_Type(Integer32):
    """Custom type tcpRtoAlgorithm based on Integer32"""
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
          ("constant", 2),
          ("rsre", 3),
          ("vanj", 4),
          ("rfc2988", 5))
    )


_TcpRtoAlgorithm_Type.__name__ = "Integer32"
_TcpRtoAlgorithm_Object = MibScalar
tcpRtoAlgorithm = _TcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 6, 1),
    _TcpRtoAlgorithm_Type()
)
tcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRtoAlgorithm.setStatus("current")
if mibBuilder.loadTexts:
    tcpRtoAlgorithm.setDescription("The algorithm used to determine the timeout value used for retransmitting unacknowledged octets.")


class _TcpRtoMin_Type(Integer32):
    """Custom type tcpRtoMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TcpRtoMin_Type.__name__ = "Integer32"
_TcpRtoMin_Object = MibScalar
tcpRtoMin = _TcpRtoMin_Object(
    (1, 3, 6, 1, 2, 1, 6, 2),
    _TcpRtoMin_Type()
)
tcpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    tcpRtoMin.setUnits("milliseconds")
if mibBuilder.loadTexts:
    tcpRtoMin.setDescription("The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides a minimum value.")


class _TcpRtoMax_Type(Integer32):
    """Custom type tcpRtoMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TcpRtoMax_Type.__name__ = "Integer32"
_TcpRtoMax_Object = MibScalar
tcpRtoMax = _TcpRtoMax_Object(
    (1, 3, 6, 1, 2, 1, 6, 3),
    _TcpRtoMax_Type()
)
tcpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    tcpRtoMax.setUnits("milliseconds")
if mibBuilder.loadTexts:
    tcpRtoMax.setDescription("The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides an upper bound (as part of an adaptive backoff algorithm).")


class _TcpMaxConn_Type(Integer32):
    """Custom type tcpMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_TcpMaxConn_Type.__name__ = "Integer32"
_TcpMaxConn_Object = MibScalar
tcpMaxConn = _TcpMaxConn_Object(
    (1, 3, 6, 1, 2, 1, 6, 4),
    _TcpMaxConn_Type()
)
tcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpMaxConn.setStatus("current")
if mibBuilder.loadTexts:
    tcpMaxConn.setDescription("The limit on the total number of TCP connections the entity can support. In entities where the maximum number of connections is dynamic, this object should contain the value -1.")
_TcpActiveOpens_Type = Counter32
_TcpActiveOpens_Object = MibScalar
tcpActiveOpens = _TcpActiveOpens_Object(
    (1, 3, 6, 1, 2, 1, 6, 5),
    _TcpActiveOpens_Type()
)
tcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpActiveOpens.setStatus("current")
if mibBuilder.loadTexts:
    tcpActiveOpens.setDescription("The number of times that TCP connections have made a direct transition to the SYN-SENT state from the CLOSED state. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpPassiveOpens_Type = Counter32
_TcpPassiveOpens_Object = MibScalar
tcpPassiveOpens = _TcpPassiveOpens_Object(
    (1, 3, 6, 1, 2, 1, 6, 6),
    _TcpPassiveOpens_Type()
)
tcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpPassiveOpens.setStatus("current")
if mibBuilder.loadTexts:
    tcpPassiveOpens.setDescription("The number of times TCP connections have made a direct transition to the SYN-RCVD state from the LISTEN state. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpAttemptFails_Type = Counter32
_TcpAttemptFails_Object = MibScalar
tcpAttemptFails = _TcpAttemptFails_Object(
    (1, 3, 6, 1, 2, 1, 6, 7),
    _TcpAttemptFails_Type()
)
tcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpAttemptFails.setStatus("current")
if mibBuilder.loadTexts:
    tcpAttemptFails.setDescription("The number of times that TCP connections have made a direct transition to the CLOSED state from either the SYN-SENT state or the SYN-RCVD state, plus the number of times that TCP connections have made a direct transition to the LISTEN state from the SYN-RCVD state. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpEstabResets_Type = Counter32
_TcpEstabResets_Object = MibScalar
tcpEstabResets = _TcpEstabResets_Object(
    (1, 3, 6, 1, 2, 1, 6, 8),
    _TcpEstabResets_Type()
)
tcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEstabResets.setStatus("current")
if mibBuilder.loadTexts:
    tcpEstabResets.setDescription("The number of times that TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE-WAIT state. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpCurrEstab_Type = Gauge32
_TcpCurrEstab_Object = MibScalar
tcpCurrEstab = _TcpCurrEstab_Object(
    (1, 3, 6, 1, 2, 1, 6, 9),
    _TcpCurrEstab_Type()
)
tcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurrEstab.setStatus("current")
if mibBuilder.loadTexts:
    tcpCurrEstab.setDescription("The number of TCP connections for which the current state is either ESTABLISHED or CLOSE-WAIT.")
_TcpInSegs_Type = Counter32
_TcpInSegs_Object = MibScalar
tcpInSegs = _TcpInSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 10),
    _TcpInSegs_Type()
)
tcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInSegs.setStatus("current")
if mibBuilder.loadTexts:
    tcpInSegs.setDescription("The total number of segments received, including those received in error. This count includes segments received on currently established connections. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpOutSegs_Type = Counter32
_TcpOutSegs_Object = MibScalar
tcpOutSegs = _TcpOutSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 11),
    _TcpOutSegs_Type()
)
tcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOutSegs.setStatus("current")
if mibBuilder.loadTexts:
    tcpOutSegs.setDescription("The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpRetransSegs_Type = Counter32
_TcpRetransSegs_Object = MibScalar
tcpRetransSegs = _TcpRetransSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 12),
    _TcpRetransSegs_Type()
)
tcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRetransSegs.setStatus("current")
if mibBuilder.loadTexts:
    tcpRetransSegs.setDescription("The total number of segments retransmitted; that is, the number of TCP segments transmitted containing one or more previously transmitted octets. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpConnTable_Object = MibTable
tcpConnTable = _TcpConnTable_Object(
    (1, 3, 6, 1, 2, 1, 6, 13)
)
if mibBuilder.loadTexts:
    tcpConnTable.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpConnTable.setDescription("A table containing information about existing IPv4-specific TCP connections or listeners. This table has been deprecated in favor of the version neutral tcpConnectionTable.")
_TcpConnEntry_Object = MibTableRow
tcpConnEntry = _TcpConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1)
)
tcpConnEntry.setIndexNames(
    (0, "TCP-MIB", "tcpConnLocalAddress"),
    (0, "TCP-MIB", "tcpConnLocalPort"),
    (0, "TCP-MIB", "tcpConnRemAddress"),
    (0, "TCP-MIB", "tcpConnRemPort"),
)
if mibBuilder.loadTexts:
    tcpConnEntry.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpConnEntry.setDescription("A conceptual row of the tcpConnTable containing information about a particular current IPv4 TCP connection. Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state.")


class _TcpConnState_Type(Integer32):
    """Custom type tcpConnState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("listen", 2),
          ("synSent", 3),
          ("synReceived", 4),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("closeWait", 8),
          ("lastAck", 9),
          ("closing", 10),
          ("timeWait", 11),
          ("deleteTCB", 12))
    )


_TcpConnState_Type.__name__ = "Integer32"
_TcpConnState_Object = MibTableColumn
tcpConnState = _TcpConnState_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 1),
    _TcpConnState_Type()
)
tcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpConnState.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpConnState.setDescription("The state of this TCP connection. The only value that may be set by a management station is deleteTCB(12). Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value. If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection. As an implementation-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably).")
_TcpConnLocalAddress_Type = IpAddress
_TcpConnLocalAddress_Object = MibTableColumn
tcpConnLocalAddress = _TcpConnLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 2),
    _TcpConnLocalAddress_Type()
)
tcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnLocalAddress.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpConnLocalAddress.setDescription("The local IP address for this TCP connection. In the case of a connection in the listen state willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used.")


class _TcpConnLocalPort_Type(Integer32):
    """Custom type tcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpConnLocalPort_Type.__name__ = "Integer32"
_TcpConnLocalPort_Object = MibTableColumn
tcpConnLocalPort = _TcpConnLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 3),
    _TcpConnLocalPort_Type()
)
tcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnLocalPort.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpConnLocalPort.setDescription("The local port number for this TCP connection.")
_TcpConnRemAddress_Type = IpAddress
_TcpConnRemAddress_Object = MibTableColumn
tcpConnRemAddress = _TcpConnRemAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 4),
    _TcpConnRemAddress_Type()
)
tcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnRemAddress.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpConnRemAddress.setDescription("The remote IP address for this TCP connection.")


class _TcpConnRemPort_Type(Integer32):
    """Custom type tcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpConnRemPort_Type.__name__ = "Integer32"
_TcpConnRemPort_Object = MibTableColumn
tcpConnRemPort = _TcpConnRemPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 5),
    _TcpConnRemPort_Type()
)
tcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnRemPort.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpConnRemPort.setDescription("The remote port number for this TCP connection.")
_TcpInErrs_Type = Counter32
_TcpInErrs_Object = MibScalar
tcpInErrs = _TcpInErrs_Object(
    (1, 3, 6, 1, 2, 1, 6, 14),
    _TcpInErrs_Type()
)
tcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInErrs.setStatus("current")
if mibBuilder.loadTexts:
    tcpInErrs.setDescription("The total number of segments received in error (e.g., bad TCP checksums). Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpOutRsts_Type = Counter32
_TcpOutRsts_Object = MibScalar
tcpOutRsts = _TcpOutRsts_Object(
    (1, 3, 6, 1, 2, 1, 6, 15),
    _TcpOutRsts_Type()
)
tcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOutRsts.setStatus("current")
if mibBuilder.loadTexts:
    tcpOutRsts.setDescription("The number of TCP segments sent containing the RST flag. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpHCInSegs_Type = Counter64
_TcpHCInSegs_Object = MibScalar
tcpHCInSegs = _TcpHCInSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 17),
    _TcpHCInSegs_Type()
)
tcpHCInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpHCInSegs.setStatus("current")
if mibBuilder.loadTexts:
    tcpHCInSegs.setDescription("The total number of segments received, including those received in error. This count includes segments received on currently established connections. This object is the 64-bit equivalent of tcpInSegs. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpHCOutSegs_Type = Counter64
_TcpHCOutSegs_Object = MibScalar
tcpHCOutSegs = _TcpHCOutSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 18),
    _TcpHCOutSegs_Type()
)
tcpHCOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpHCOutSegs.setStatus("current")
if mibBuilder.loadTexts:
    tcpHCOutSegs.setDescription("The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets. This object is the 64-bit equivalent of tcpOutSegs. Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime.")
_TcpConnectionTable_Object = MibTable
tcpConnectionTable = _TcpConnectionTable_Object(
    (1, 3, 6, 1, 2, 1, 6, 19)
)
if mibBuilder.loadTexts:
    tcpConnectionTable.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionTable.setDescription("A table containing information about existing TCP connections. Note that unlike earlier TCP MIBs, there is a separate table for connections in the LISTEN state.")
_TcpConnectionEntry_Object = MibTableRow
tcpConnectionEntry = _TcpConnectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1)
)
tcpConnectionEntry.setIndexNames(
    (0, "TCP-MIB", "tcpConnectionLocalAddressType"),
    (0, "TCP-MIB", "tcpConnectionLocalAddress"),
    (0, "TCP-MIB", "tcpConnectionLocalPort"),
    (0, "TCP-MIB", "tcpConnectionRemAddressType"),
    (0, "TCP-MIB", "tcpConnectionRemAddress"),
    (0, "TCP-MIB", "tcpConnectionRemPort"),
)
if mibBuilder.loadTexts:
    tcpConnectionEntry.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionEntry.setDescription("A conceptual row of the tcpConnectionTable containing information about a particular current TCP connection. Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state.")
_TcpConnectionLocalAddressType_Type = InetAddressType
_TcpConnectionLocalAddressType_Object = MibTableColumn
tcpConnectionLocalAddressType = _TcpConnectionLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 1),
    _TcpConnectionLocalAddressType_Type()
)
tcpConnectionLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpConnectionLocalAddressType.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionLocalAddressType.setDescription("The address type of tcpConnectionLocalAddress.")
_TcpConnectionLocalAddress_Type = InetAddress
_TcpConnectionLocalAddress_Object = MibTableColumn
tcpConnectionLocalAddress = _TcpConnectionLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 2),
    _TcpConnectionLocalAddress_Type()
)
tcpConnectionLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpConnectionLocalAddress.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionLocalAddress.setDescription("The local IP address for this TCP connection. The type of this address is determined by the value of tcpConnectionLocalAddressType. As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.")
_TcpConnectionLocalPort_Type = InetPortNumber
_TcpConnectionLocalPort_Object = MibTableColumn
tcpConnectionLocalPort = _TcpConnectionLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 3),
    _TcpConnectionLocalPort_Type()
)
tcpConnectionLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpConnectionLocalPort.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionLocalPort.setDescription("The local port number for this TCP connection.")
_TcpConnectionRemAddressType_Type = InetAddressType
_TcpConnectionRemAddressType_Object = MibTableColumn
tcpConnectionRemAddressType = _TcpConnectionRemAddressType_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 4),
    _TcpConnectionRemAddressType_Type()
)
tcpConnectionRemAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpConnectionRemAddressType.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionRemAddressType.setDescription("The address type of tcpConnectionRemAddress.")
_TcpConnectionRemAddress_Type = InetAddress
_TcpConnectionRemAddress_Object = MibTableColumn
tcpConnectionRemAddress = _TcpConnectionRemAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 5),
    _TcpConnectionRemAddress_Type()
)
tcpConnectionRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpConnectionRemAddress.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionRemAddress.setDescription("The remote IP address for this TCP connection. The type of this address is determined by the value of tcpConnectionRemAddressType. As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.")
_TcpConnectionRemPort_Type = InetPortNumber
_TcpConnectionRemPort_Object = MibTableColumn
tcpConnectionRemPort = _TcpConnectionRemPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 6),
    _TcpConnectionRemPort_Type()
)
tcpConnectionRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpConnectionRemPort.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionRemPort.setDescription("The remote port number for this TCP connection.")


class _TcpConnectionState_Type(Integer32):
    """Custom type tcpConnectionState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("listen", 2),
          ("synSent", 3),
          ("synReceived", 4),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("closeWait", 8),
          ("lastAck", 9),
          ("closing", 10),
          ("timeWait", 11),
          ("deleteTCB", 12))
    )


_TcpConnectionState_Type.__name__ = "Integer32"
_TcpConnectionState_Object = MibTableColumn
tcpConnectionState = _TcpConnectionState_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 7),
    _TcpConnectionState_Type()
)
tcpConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpConnectionState.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionState.setDescription("The state of this TCP connection. The value listen(2) is included only for parallelism to the old tcpConnTable and should not be used. A connection in LISTEN state should be present in the tcpListenerTable. The only value that may be set by a management station is deleteTCB(12). Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value. If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection. As an implementation-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably).")
_TcpConnectionProcess_Type = Unsigned32
_TcpConnectionProcess_Object = MibTableColumn
tcpConnectionProcess = _TcpConnectionProcess_Object(
    (1, 3, 6, 1, 2, 1, 6, 19, 1, 8),
    _TcpConnectionProcess_Type()
)
tcpConnectionProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnectionProcess.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionProcess.setDescription("The system's process ID for the process associated with this connection, or zero if there is no such process. This value is expected to be the same as HOST-RESOURCES-MIB:: hrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some row in the appropriate tables.")
_TcpListenerTable_Object = MibTable
tcpListenerTable = _TcpListenerTable_Object(
    (1, 3, 6, 1, 2, 1, 6, 20)
)
if mibBuilder.loadTexts:
    tcpListenerTable.setStatus("current")
if mibBuilder.loadTexts:
    tcpListenerTable.setDescription("A table containing information about TCP listeners. A listening application can be represented in three possible ways: 1. An application that is willing to accept both IPv4 and IPv6 datagrams is represented by a tcpListenerLocalAddressType of unknown (0) and a tcpListenerLocalAddress of ''h (a zero-length octet-string). 2. An application that is willing to accept only IPv4 or IPv6 datagrams is represented by a tcpListenerLocalAddressType of the appropriate address type and a tcpListenerLocalAddress of '0.0.0.0' or '::' respectively. 3. An application that is listening for data destined only to a specific IP address, but from any remote system, is represented by a tcpListenerLocalAddressType of an appropriate address type, with tcpListenerLocalAddress as the specific local address. NOTE: The address type in this table represents the address type used for the communication, irrespective of the higher-layer abstraction. For example, an application using IPv6 'sockets' to communicate via IPv4 between ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would use InetAddressType ipv4(1)).")
_TcpListenerEntry_Object = MibTableRow
tcpListenerEntry = _TcpListenerEntry_Object(
    (1, 3, 6, 1, 2, 1, 6, 20, 1)
)
tcpListenerEntry.setIndexNames(
    (0, "TCP-MIB", "tcpListenerLocalAddressType"),
    (0, "TCP-MIB", "tcpListenerLocalAddress"),
    (0, "TCP-MIB", "tcpListenerLocalPort"),
)
if mibBuilder.loadTexts:
    tcpListenerEntry.setStatus("current")
if mibBuilder.loadTexts:
    tcpListenerEntry.setDescription("A conceptual row of the tcpListenerTable containing information about a particular TCP listener.")
_TcpListenerLocalAddressType_Type = InetAddressType
_TcpListenerLocalAddressType_Object = MibTableColumn
tcpListenerLocalAddressType = _TcpListenerLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 6, 20, 1, 1),
    _TcpListenerLocalAddressType_Type()
)
tcpListenerLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpListenerLocalAddressType.setStatus("current")
if mibBuilder.loadTexts:
    tcpListenerLocalAddressType.setDescription("The address type of tcpListenerLocalAddress. The value should be unknown (0) if connection initiations to all local IP addresses are accepted.")
_TcpListenerLocalAddress_Type = InetAddress
_TcpListenerLocalAddress_Object = MibTableColumn
tcpListenerLocalAddress = _TcpListenerLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 20, 1, 2),
    _TcpListenerLocalAddress_Type()
)
tcpListenerLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpListenerLocalAddress.setStatus("current")
if mibBuilder.loadTexts:
    tcpListenerLocalAddress.setDescription("The local IP address for this TCP connection. The value of this object can be represented in three possible ways, depending on the characteristics of the listening application: 1. For an application willing to accept both IPv4 and IPv6 datagrams, the value of this object must be ''h (a zero-length octet-string), with the value of the corresponding tcpListenerLocalAddressType object being unknown (0). 2. For an application willing to accept only IPv4 or IPv6 datagrams, the value of this object must be '0.0.0.0' or '::' respectively, with tcpListenerLocalAddressType representing the appropriate address type. 3. For an application which is listening for data destined only to a specific IP address, the value of this object is the specific local address, with tcpListenerLocalAddressType representing the appropriate address type. As this object is used in the index for the tcpListenerTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed, using SNMPv1, SNMPv2c, or SNMPv3.")
_TcpListenerLocalPort_Type = InetPortNumber
_TcpListenerLocalPort_Object = MibTableColumn
tcpListenerLocalPort = _TcpListenerLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 20, 1, 3),
    _TcpListenerLocalPort_Type()
)
tcpListenerLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpListenerLocalPort.setStatus("current")
if mibBuilder.loadTexts:
    tcpListenerLocalPort.setDescription("The local port number for this TCP connection.")
_TcpListenerProcess_Type = Unsigned32
_TcpListenerProcess_Object = MibTableColumn
tcpListenerProcess = _TcpListenerProcess_Object(
    (1, 3, 6, 1, 2, 1, 6, 20, 1, 4),
    _TcpListenerProcess_Type()
)
tcpListenerProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpListenerProcess.setStatus("current")
if mibBuilder.loadTexts:
    tcpListenerProcess.setDescription("The system's process ID for the process associated with this listener, or zero if there is no such process. This value is expected to be the same as HOST-RESOURCES-MIB:: hrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some row in the appropriate tables.")
_TcpMIBConformance_ObjectIdentity = ObjectIdentity
tcpMIBConformance = _TcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 49, 2)
)
_TcpMIBCompliances_ObjectIdentity = ObjectIdentity
tcpMIBCompliances = _TcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 49, 2, 1)
)
_TcpMIBGroups_ObjectIdentity = ObjectIdentity
tcpMIBGroups = _TcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 49, 2, 2)
)

# Managed Objects groups

tcpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 49, 2, 2, 1)
)
tcpGroup.setObjects(
      *(("TCP-MIB", "tcpRtoAlgorithm"),
        ("TCP-MIB", "tcpRtoMin"),
        ("TCP-MIB", "tcpRtoMax"),
        ("TCP-MIB", "tcpMaxConn"),
        ("TCP-MIB", "tcpActiveOpens"),
        ("TCP-MIB", "tcpPassiveOpens"),
        ("TCP-MIB", "tcpAttemptFails"),
        ("TCP-MIB", "tcpEstabResets"),
        ("TCP-MIB", "tcpCurrEstab"),
        ("TCP-MIB", "tcpInSegs"),
        ("TCP-MIB", "tcpOutSegs"),
        ("TCP-MIB", "tcpRetransSegs"),
        ("TCP-MIB", "tcpConnState"),
        ("TCP-MIB", "tcpConnLocalAddress"),
        ("TCP-MIB", "tcpConnLocalPort"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("TCP-MIB", "tcpConnRemPort"),
        ("TCP-MIB", "tcpInErrs"),
        ("TCP-MIB", "tcpOutRsts"))
)
if mibBuilder.loadTexts:
    tcpGroup.setStatus("deprecated")
if mibBuilder.loadTexts:
    tcpGroup.setDescription("The tcp group of objects providing for management of TCP entities.")

tcpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 49, 2, 2, 2)
)
tcpBaseGroup.setObjects(
      *(("TCP-MIB", "tcpRtoAlgorithm"),
        ("TCP-MIB", "tcpRtoMin"),
        ("TCP-MIB", "tcpRtoMax"),
        ("TCP-MIB", "tcpMaxConn"),
        ("TCP-MIB", "tcpActiveOpens"),
        ("TCP-MIB", "tcpPassiveOpens"),
        ("TCP-MIB", "tcpAttemptFails"),
        ("TCP-MIB", "tcpEstabResets"),
        ("TCP-MIB", "tcpCurrEstab"),
        ("TCP-MIB", "tcpInSegs"),
        ("TCP-MIB", "tcpOutSegs"),
        ("TCP-MIB", "tcpRetransSegs"),
        ("TCP-MIB", "tcpInErrs"),
        ("TCP-MIB", "tcpOutRsts"))
)
if mibBuilder.loadTexts:
    tcpBaseGroup.setStatus("current")
if mibBuilder.loadTexts:
    tcpBaseGroup.setDescription("The group of counters common to TCP entities.")

tcpConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 49, 2, 2, 3)
)
tcpConnectionGroup.setObjects(
      *(("TCP-MIB", "tcpConnectionState"),
        ("TCP-MIB", "tcpConnectionProcess"))
)
if mibBuilder.loadTexts:
    tcpConnectionGroup.setStatus("current")
if mibBuilder.loadTexts:
    tcpConnectionGroup.setDescription("The group provides general information about TCP connections.")

tcpListenerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 49, 2, 2, 4)
)
tcpListenerGroup.setObjects(
    ("TCP-MIB", "tcpListenerProcess")
)
if mibBuilder.loadTexts:
    tcpListenerGroup.setStatus("current")
if mibBuilder.loadTexts:
    tcpListenerGroup.setDescription("This group has objects providing general information about TCP listeners.")

tcpHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 49, 2, 2, 5)
)
tcpHCGroup.setObjects(
      *(("TCP-MIB", "tcpHCInSegs"),
        ("TCP-MIB", "tcpHCOutSegs"))
)
if mibBuilder.loadTexts:
    tcpHCGroup.setStatus("current")
if mibBuilder.loadTexts:
    tcpHCGroup.setDescription("The group of objects providing for counters of high speed TCP implementations.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 49, 2, 1, 1)
)
tcpMIBCompliance.setObjects(
    ("TCP-MIB", "tcpGroup")
)
if mibBuilder.loadTexts:
    tcpMIBCompliance.setStatus(
        "deprecated"
    )
if mibBuilder.loadTexts:
    tcpMIBCompliance.setDescription("The compliance statement for IPv4-only systems that implement TCP. In order to be IP version independent, this compliance statement is deprecated in favor of tcpMIBCompliance2. However, agents are still encouraged to implement these objects in order to interoperate with the deployed base of managers.")

tcpMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 49, 2, 1, 2)
)
tcpMIBCompliance2.setObjects(
      *(("TCP-MIB", "tcpBaseGroup"),
        ("TCP-MIB", "tcpConnectionGroup"),
        ("TCP-MIB", "tcpListenerGroup"),
        ("TCP-MIB", "tcpHCGroup"))
)
if mibBuilder.loadTexts:
    tcpMIBCompliance2.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    tcpMIBCompliance2.setDescription("The compliance statement for systems that implement TCP. A number of INDEX objects cannot be represented in the form of OBJECT clauses in SMIv2 but have the following compliance requirements, expressed in OBJECT clause form in this description clause: -- OBJECT tcpConnectionLocalAddressType -- SYNTAX InetAddressType { ipv4(1), ipv6(2) } -- DESCRIPTION -- This MIB requires support for only global IPv4 -- and IPv6 address types. -- -- OBJECT tcpConnectionRemAddressType -- SYNTAX InetAddressType { ipv4(1), ipv6(2) } -- DESCRIPTION -- This MIB requires support for only global IPv4 -- and IPv6 address types. -- -- OBJECT tcpListenerLocalAddressType -- SYNTAX InetAddressType { unknown(0), ipv4(1), -- ipv6(2) } -- DESCRIPTION -- This MIB requires support for only global IPv4 -- and IPv6 address types. The type unknown also -- needs to be supported to identify a special -- case in the listener table: a listen using -- both IPv4 and IPv6 addresses on the device. -- ")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TCP-MIB",
    **{"tcp": tcp,
       "tcpRtoAlgorithm": tcpRtoAlgorithm,
       "tcpRtoMin": tcpRtoMin,
       "tcpRtoMax": tcpRtoMax,
       "tcpMaxConn": tcpMaxConn,
       "tcpActiveOpens": tcpActiveOpens,
       "tcpPassiveOpens": tcpPassiveOpens,
       "tcpAttemptFails": tcpAttemptFails,
       "tcpEstabResets": tcpEstabResets,
       "tcpCurrEstab": tcpCurrEstab,
       "tcpInSegs": tcpInSegs,
       "tcpOutSegs": tcpOutSegs,
       "tcpRetransSegs": tcpRetransSegs,
       "tcpConnTable": tcpConnTable,
       "tcpConnEntry": tcpConnEntry,
       "tcpConnState": tcpConnState,
       "tcpConnLocalAddress": tcpConnLocalAddress,
       "tcpConnLocalPort": tcpConnLocalPort,
       "tcpConnRemAddress": tcpConnRemAddress,
       "tcpConnRemPort": tcpConnRemPort,
       "tcpInErrs": tcpInErrs,
       "tcpOutRsts": tcpOutRsts,
       "tcpHCInSegs": tcpHCInSegs,
       "tcpHCOutSegs": tcpHCOutSegs,
       "tcpConnectionTable": tcpConnectionTable,
       "tcpConnectionEntry": tcpConnectionEntry,
       "tcpConnectionLocalAddressType": tcpConnectionLocalAddressType,
       "tcpConnectionLocalAddress": tcpConnectionLocalAddress,
       "tcpConnectionLocalPort": tcpConnectionLocalPort,
       "tcpConnectionRemAddressType": tcpConnectionRemAddressType,
       "tcpConnectionRemAddress": tcpConnectionRemAddress,
       "tcpConnectionRemPort": tcpConnectionRemPort,
       "tcpConnectionState": tcpConnectionState,
       "tcpConnectionProcess": tcpConnectionProcess,
       "tcpListenerTable": tcpListenerTable,
       "tcpListenerEntry": tcpListenerEntry,
       "tcpListenerLocalAddressType": tcpListenerLocalAddressType,
       "tcpListenerLocalAddress": tcpListenerLocalAddress,
       "tcpListenerLocalPort": tcpListenerLocalPort,
       "tcpListenerProcess": tcpListenerProcess,
       "tcpMIB": tcpMIB,
       "tcpMIBConformance": tcpMIBConformance,
       "tcpMIBCompliances": tcpMIBCompliances,
       "tcpMIBCompliance": tcpMIBCompliance,
       "tcpMIBCompliance2": tcpMIBCompliance2,
       "tcpMIBGroups": tcpMIBGroups,
       "tcpGroup": tcpGroup,
       "tcpBaseGroup": tcpBaseGroup,
       "tcpConnectionGroup": tcpConnectionGroup,
       "tcpListenerGroup": tcpListenerGroup,
       "tcpHCGroup": tcpHCGroup}
)
