# SNMP MIB module (RT1170-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://D:\olix\soft\SNMP_BROWSER\data\mibs\RT1170-AGENT-MIB.mib
# Produced by pysmi-2.0.0 at Sun Oct 18 16:21:49 2026
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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rt1170Agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 1)
)
if mibBuilder.loadTexts:
    rt1170Agent.setRevisions(
        ("2026-10-17 00:00",)
    )
if mibBuilder.loadTexts:
    rt1170Agent.setLastUpdated("202610170000Z")
if mibBuilder.loadTexts:
    rt1170Agent.setOrganization("Example")
if mibBuilder.loadTexts:
    rt1170Agent.setContactInfo("admin@example.com")
if mibBuilder.loadTexts:
    rt1170Agent.setDescription("Private objects of the PHYTEC phyCORE-i.MX RT1170 SNMPv3 agent. NOTE: enterprise number 26381 is the lwIP project's PEN, used as a placeholder. Replace it with your own IANA Private Enterprise Number (and APP_SNMP_ENTERPRISE_ID in app_config.h) before deployment.")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rt1170AgentNotifications_ObjectIdentity = ObjectIdentity
rt1170AgentNotifications = _Rt1170AgentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 1, 0)
)
_Rt1170AgentObjects_ObjectIdentity = ObjectIdentity
rt1170AgentObjects = _Rt1170AgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 1, 1)
)
_LedBlinkEnable_Type = TruthValue
_LedBlinkEnable_Object = MibScalar
ledBlinkEnable = _LedBlinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 26381, 1, 1, 1),
    _LedBlinkEnable_Type()
)
ledBlinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledBlinkEnable.setStatus("current")
if mibBuilder.loadTexts:
    ledBlinkEnable.setDescription("true: LED1 blinks; false: LED1 is off. Not persistent.")


class _LedBlinkPeriod_Type(Integer32):
    """Custom type ledBlinkPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_LedBlinkPeriod_Type.__name__ = "Integer32"
_LedBlinkPeriod_Object = MibScalar
ledBlinkPeriod = _LedBlinkPeriod_Object(
    (1, 3, 6, 1, 4, 1, 26381, 1, 1, 2),
    _LedBlinkPeriod_Type()
)
ledBlinkPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledBlinkPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ledBlinkPeriod.setUnits("milliseconds")
if mibBuilder.loadTexts:
    ledBlinkPeriod.setDescription("Full blink period of LED1 (on + off). Not persistent.")


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
    (1, 3, 6, 1, 4, 1, 26381, 1, 1, 3),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("current")
if mibBuilder.loadTexts:
    ledState.setDescription("Current state of LED1.")
_Rt1170AgentConformance_ObjectIdentity = ObjectIdentity
rt1170AgentConformance = _Rt1170AgentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 1, 2)
)
_Rt1170AgentGroups_ObjectIdentity = ObjectIdentity
rt1170AgentGroups = _Rt1170AgentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 1, 2, 1)
)
_Rt1170AgentCompliances_ObjectIdentity = ObjectIdentity
rt1170AgentCompliances = _Rt1170AgentCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26381, 1, 2, 2)
)

# Managed Objects groups

rt1170LedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 26381, 1, 2, 1, 1)
)
rt1170LedGroup.setObjects(
      *(("RT1170-AGENT-MIB", "ledBlinkEnable"),
        ("RT1170-AGENT-MIB", "ledBlinkPeriod"),
        ("RT1170-AGENT-MIB", "ledState"))
)
if mibBuilder.loadTexts:
    rt1170LedGroup.setStatus("current")
if mibBuilder.loadTexts:
    rt1170LedGroup.setDescription("LED control objects.")


# Notification objects

ledConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 26381, 1, 0, 1)
)
ledConfigChanged.setObjects(
      *(("RT1170-AGENT-MIB", "ledBlinkEnable"),
        ("RT1170-AGENT-MIB", "ledBlinkPeriod"))
)
if mibBuilder.loadTexts:
    ledConfigChanged.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    ledConfigChanged.setDescription("Sent (as SNMPv2c trap) after ledBlinkEnable or ledBlinkPeriod is changed, via SNMP or the web page.")


# Notifications groups

rt1170NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 26381, 1, 2, 1, 2)
)
rt1170NotificationGroup.setObjects(
    ("RT1170-AGENT-MIB", "ledConfigChanged")
)
if mibBuilder.loadTexts:
    rt1170NotificationGroup.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    rt1170NotificationGroup.setDescription("Notifications.")


# Agent capabilities


# Module compliance

rt1170AgentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 26381, 1, 2, 2, 1)
)
rt1170AgentCompliance.setObjects(
      *(("RT1170-AGENT-MIB", "rt1170LedGroup"),
        ("RT1170-AGENT-MIB", "rt1170NotificationGroup"))
)
if mibBuilder.loadTexts:
    rt1170AgentCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    rt1170AgentCompliance.setDescription("Compliance statement for the RT1170 agent.")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RT1170-AGENT-MIB",
    **{"rt1170Agent": rt1170Agent,
       "rt1170AgentNotifications": rt1170AgentNotifications,
       "ledConfigChanged": ledConfigChanged,
       "rt1170AgentObjects": rt1170AgentObjects,
       "ledBlinkEnable": ledBlinkEnable,
       "ledBlinkPeriod": ledBlinkPeriod,
       "ledState": ledState,
       "rt1170AgentConformance": rt1170AgentConformance,
       "rt1170AgentGroups": rt1170AgentGroups,
       "rt1170LedGroup": rt1170LedGroup,
       "rt1170NotificationGroup": rt1170NotificationGroup,
       "rt1170AgentCompliances": rt1170AgentCompliances,
       "rt1170AgentCompliance": rt1170AgentCompliance}
)
