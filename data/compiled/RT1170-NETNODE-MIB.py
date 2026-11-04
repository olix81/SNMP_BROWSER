# SNMP MIB module (RT1170-NETNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://D:\olix\soft\SNMP_BROWSER\data\mibs\RT1170-NETNODE-MIB.mib
# Produced by pysmi-2.0.0 at Sun Oct 18 16:21:47 2026
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
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
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rt1170NetNode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2)
)
if mibBuilder.loadTexts:
    rt1170NetNode.setRevisions(
        ("2026-10-18 00:00",)
    )
if mibBuilder.loadTexts:
    rt1170NetNode.setLastUpdated("202610180000Z")
if mibBuilder.loadTexts:
    rt1170NetNode.setOrganization("Example")
if mibBuilder.loadTexts:
    rt1170NetNode.setContactInfo("admin@example.com")
if mibBuilder.loadTexts:
    rt1170NetNode.setDescription("Second product built on the PHYTEC phyCORE-i.MX RT1170 SNMPv3 agent: LED control plus the state of the Ethernet interface. NOTE: enterprise number 26381 is the lwIP project's PEN, used as a placeholder. Replace it with your own IANA Private Enterprise Number (and APP_SNMP_ENTERPRISE_ID in app_config.h) before deployment.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rt1170NetNodeNotifications_ObjectIdentity = ObjectIdentity
rt1170NetNodeNotifications = _Rt1170NetNodeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2, 0)
)
_Rt1170NetNodeObjects_ObjectIdentity = ObjectIdentity
rt1170NetNodeObjects = _Rt1170NetNodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1)
)
_Led_ObjectIdentity = ObjectIdentity
led = _Led_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 1)
)
_LedBlinkEnable_Type = TruthValue
_LedBlinkEnable_Object = MibScalar
ledBlinkEnable = _LedBlinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 1, 1),
    _LedBlinkEnable_Type()
)
ledBlinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledBlinkEnable.setStatus("current")
if mibBuilder.loadTexts:
    ledBlinkEnable.setDescription("true: LED1 blinks; false: LED1 is off. Stored in the EEPROM.")


class _LedBlinkPeriod_Type(Integer32):
    """Custom type ledBlinkPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_LedBlinkPeriod_Type.__name__ = "Integer32"
_LedBlinkPeriod_Object = MibScalar
ledBlinkPeriod = _LedBlinkPeriod_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 1, 2),
    _LedBlinkPeriod_Type()
)
ledBlinkPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledBlinkPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ledBlinkPeriod.setUnits("milliseconds")
if mibBuilder.loadTexts:
    ledBlinkPeriod.setDescription("Full blink period of LED1 (on + off). Stored in the EEPROM.")


class _LedState_Type(Integer32):
    """Custom type ledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LedState_Type.__name__ = "Integer32"
_LedState_Object = MibScalar
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 1, 3),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("current")
if mibBuilder.loadTexts:
    ledState.setDescription("Current state of LED1.")
_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2)
)


class _NetHostname_Type(DisplayString):
    """Custom type netHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NetHostname_Type.__name__ = "DisplayString"
_NetHostname_Object = MibScalar
netHostname = _NetHostname_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 1),
    _NetHostname_Type()
)
netHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netHostname.setStatus("current")
if mibBuilder.loadTexts:
    netHostname.setDescription("Host name of the device (letters, digits and '-', not at the start or end). Sent to the DHCP server (option 12) and reported as sysName. Stored in the EEPROM.")
_NetMacAddress_Type = MacAddress
_NetMacAddress_Object = MibScalar
netMacAddress = _NetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 2),
    _NetMacAddress_Type()
)
netMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMacAddress.setStatus("current")
if mibBuilder.loadTexts:
    netMacAddress.setDescription("MAC address of the Ethernet interface.")
_NetDhcpEnable_Type = TruthValue
_NetDhcpEnable_Object = MibScalar
netDhcpEnable = _NetDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 3),
    _NetDhcpEnable_Type()
)
netDhcpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netDhcpEnable.setStatus("current")
if mibBuilder.loadTexts:
    netDhcpEnable.setDescription("true: the address is obtained with DHCP; false: static.")
_NetIpAddress_Type = IpAddress
_NetIpAddress_Object = MibScalar
netIpAddress = _NetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 4),
    _NetIpAddress_Type()
)
netIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIpAddress.setStatus("current")
if mibBuilder.loadTexts:
    netIpAddress.setDescription("Current IPv4 address (0.0.0.0 while DHCP has no lease).")
_NetSubnetMask_Type = IpAddress
_NetSubnetMask_Object = MibScalar
netSubnetMask = _NetSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 5),
    _NetSubnetMask_Type()
)
netSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSubnetMask.setStatus("current")
if mibBuilder.loadTexts:
    netSubnetMask.setDescription("Current IPv4 subnet mask.")
_NetGateway_Type = IpAddress
_NetGateway_Object = MibScalar
netGateway = _NetGateway_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 6),
    _NetGateway_Type()
)
netGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netGateway.setStatus("current")
if mibBuilder.loadTexts:
    netGateway.setDescription("Current IPv4 default gateway.")


class _NetLinkStatus_Type(Integer32):
    """Custom type netLinkStatus based on Integer32"""
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


_NetLinkStatus_Type.__name__ = "Integer32"
_NetLinkStatus_Object = MibScalar
netLinkStatus = _NetLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 7),
    _NetLinkStatus_Type()
)
netLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLinkStatus.setStatus("current")
if mibBuilder.loadTexts:
    netLinkStatus.setDescription("State of the Ethernet link.")
_NetLinkSpeed_Type = Gauge32
_NetLinkSpeed_Object = MibScalar
netLinkSpeed = _NetLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26381, 2, 1, 2, 8),
    _NetLinkSpeed_Type()
)
netLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLinkSpeed.setStatus("current")
if mibBuilder.loadTexts:
    netLinkSpeed.setUnits("Mbit/s")
if mibBuilder.loadTexts:
    netLinkSpeed.setDescription("Negotiated link speed: 10, 100 or 1000; 0 while the link is down.")
_Rt1170NetNodeConformance_ObjectIdentity = ObjectIdentity
rt1170NetNodeConformance = _Rt1170NetNodeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2, 2)
)
_Rt1170NetNodeGroups_ObjectIdentity = ObjectIdentity
rt1170NetNodeGroups = _Rt1170NetNodeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2, 2, 1)
)
_Rt1170NetNodeCompliances_ObjectIdentity = ObjectIdentity
rt1170NetNodeCompliances = _Rt1170NetNodeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 2, 2, 2)
)

# Managed Objects groups

rt1170NetNodeLedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26381, 2, 2, 1, 1)
)
rt1170NetNodeLedGroup.setObjects(
      *(("RT1170-NETNODE-MIB", "ledBlinkEnable"),
        ("RT1170-NETNODE-MIB", "ledBlinkPeriod"),
        ("RT1170-NETNODE-MIB", "ledState"))
)
if mibBuilder.loadTexts:
    rt1170NetNodeLedGroup.setStatus("current")
if mibBuilder.loadTexts:
    rt1170NetNodeLedGroup.setDescription("LED control objects.")

rt1170NetNodeNetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26381, 2, 2, 1, 2)
)
rt1170NetNodeNetGroup.setObjects(
      *(("RT1170-NETNODE-MIB", "netHostname"),
        ("RT1170-NETNODE-MIB", "netMacAddress"),
        ("RT1170-NETNODE-MIB", "netDhcpEnable"),
        ("RT1170-NETNODE-MIB", "netIpAddress"),
        ("RT1170-NETNODE-MIB", "netSubnetMask"),
        ("RT1170-NETNODE-MIB", "netGateway"),
        ("RT1170-NETNODE-MIB", "netLinkStatus"),
        ("RT1170-NETNODE-MIB", "netLinkSpeed"))
)
if mibBuilder.loadTexts:
    rt1170NetNodeNetGroup.setStatus("current")
if mibBuilder.loadTexts:
    rt1170NetNodeNetGroup.setDescription("Network interface objects.")


# Notification objects

ledConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 26381, 2, 0, 1)
)
ledConfigChanged.setObjects(
      *(("RT1170-NETNODE-MIB", "ledBlinkEnable"),
        ("RT1170-NETNODE-MIB", "ledBlinkPeriod"))
)
if mibBuilder.loadTexts:
    ledConfigChanged.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ledConfigChanged.setDescription("Sent after ledBlinkEnable or ledBlinkPeriod is changed, via SNMP or the web page.")

netLinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 26381, 2, 0, 2)
)
netLinkChanged.setObjects(
      *(("RT1170-NETNODE-MIB", "netLinkStatus"),
        ("RT1170-NETNODE-MIB", "netLinkSpeed"))
)
if mibBuilder.loadTexts:
    netLinkChanged.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    netLinkChanged.setDescription("Sent when the Ethernet link goes up or down. With a single interface the link-down trap cannot leave the device: only the link-up one reaches the manager.")


# Notifications groups

rt1170NetNodeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 26381, 2, 2, 1, 3)
)
rt1170NetNodeNotificationGroup.setObjects(
      *(("RT1170-NETNODE-MIB", "ledConfigChanged"),
        ("RT1170-NETNODE-MIB", "netLinkChanged"))
)
if mibBuilder.loadTexts:
    rt1170NetNodeNotificationGroup.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    rt1170NetNodeNotificationGroup.setDescription("Notifications.")


# Agent capabilities


# Module compliance

rt1170NetNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 26381, 2, 2, 2, 1)
)
rt1170NetNodeCompliance.setObjects(
      *(("RT1170-NETNODE-MIB", "rt1170NetNodeLedGroup"),
        ("RT1170-NETNODE-MIB", "rt1170NetNodeNetGroup"),
        ("RT1170-NETNODE-MIB", "rt1170NetNodeNotificationGroup"))
)
if mibBuilder.loadTexts:
    rt1170NetNodeCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    rt1170NetNodeCompliance.setDescription("Compliance statement for the RT1170 network node.")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RT1170-NETNODE-MIB",
    **{"rt1170NetNode": rt1170NetNode,
       "rt1170NetNodeNotifications": rt1170NetNodeNotifications,
       "ledConfigChanged": ledConfigChanged,
       "netLinkChanged": netLinkChanged,
       "rt1170NetNodeObjects": rt1170NetNodeObjects,
       "led": led,
       "ledBlinkEnable": ledBlinkEnable,
       "ledBlinkPeriod": ledBlinkPeriod,
       "ledState": ledState,
       "net": net,
       "netHostname": netHostname,
       "netMacAddress": netMacAddress,
       "netDhcpEnable": netDhcpEnable,
       "netIpAddress": netIpAddress,
       "netSubnetMask": netSubnetMask,
       "netGateway": netGateway,
       "netLinkStatus": netLinkStatus,
       "netLinkSpeed": netLinkSpeed,
       "rt1170NetNodeConformance": rt1170NetNodeConformance,
       "rt1170NetNodeGroups": rt1170NetNodeGroups,
       "rt1170NetNodeLedGroup": rt1170NetNodeLedGroup,
       "rt1170NetNodeNetGroup": rt1170NetNodeNetGroup,
       "rt1170NetNodeNotificationGroup": rt1170NetNodeNotificationGroup,
       "rt1170NetNodeCompliances": rt1170NetNodeCompliances,
       "rt1170NetNodeCompliance": rt1170NetNodeCompliance}
)
