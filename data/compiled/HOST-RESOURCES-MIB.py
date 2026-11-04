# SNMP MIB module (HOST-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://mibs.pysnmp.com/asn1/HOST-RESOURCES-MIB
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
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

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hostResourcesMibModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7, 1)
)
if mibBuilder.loadTexts:
    hostResourcesMibModule.setRevisions(
        ("2000-03-06 00:00",
         "1999-10-20 22:00")
    )
if mibBuilder.loadTexts:
    hostResourcesMibModule.setLastUpdated("200003060000Z")
if mibBuilder.loadTexts:
    hostResourcesMibModule.setOrganization("IETF Host Resources MIB Working Group")
if mibBuilder.loadTexts:
    hostResourcesMibModule.setContactInfo("Steve Waldbusser Postal: Lucent Technologies, Inc. 1213 Innsbruck Dr. Sunnyvale, CA 94089 USA Phone: 650-318-1251 Fax: 650-318-1633 Email: waldbusser@lucent.com In addition, the Host Resources MIB mailing list is dedicated to discussion of this MIB. To join the mailing list, send a request message to hostmib-request@andrew.cmu.edu. The mailing list address is hostmib@andrew.cmu.edu.")
if mibBuilder.loadTexts:
    hostResourcesMibModule.setDescription("This MIB is for use in managing host systems. The term `host' is construed to mean any computer that communicates with other similar computers attached to the internet and that is directly used by one or more human beings. Although this MIB does not necessarily apply to devices whose primary function is communications services (e.g., terminal servers, routers, bridges, monitoring equipment), such relevance is not explicitly precluded. This MIB instruments attributes common to all internet hosts including, for example, both personal computers and systems that run variants of Unix.")


# Types definitions


# TEXTUAL-CONVENTIONS



class KBytes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = "Storage size, expressed in units of 1024 bytes."


class ProductID(TextualConvention, ObjectIdentifier):
    status = "current"
    if mibBuilder.loadTexts:
        description = "This textual convention is intended to identify the manufacturer, model, and version of a specific hardware or software product. It is suggested that these OBJECT IDENTIFIERs are allocated such that all products from a particular manufacturer are registered under a subtree distinct to that manufacturer. In addition, all versions of a product should be registered under a subtree distinct to that product. With this strategy, a management station may uniquely determine the manufacturer and/or model of a product whose productID is unknown to the management station. Objects of this type may be useful for inventory purposes or for automatically detecting incompatibilities or version mismatches between various hardware and software components on a system. For example, the product ID for the ACME 4860 66MHz clock doubled processor might be: enterprises.acme.acmeProcessors.a4860DX2.MHz66 A software product might be registered as: enterprises.acme.acmeOperatingSystems.acmeDOS.six(6).one(1) "


class InternationalDisplayString(TextualConvention, OctetString):
    status = "current"
    if mibBuilder.loadTexts:
        description = "This data type is used to model textual information in some character set. A network management station should use a local algorithm to determine which character set is in use and how it should be displayed. Note that this character set may be encoded with more than one octet per symbol, but will most often be NVT ASCII. When a size clause is specified for an object of this type, the size refers to the length in octets, not the number of symbols."


# MIB Managed Objects in the order of their OIDs

_Host_ObjectIdentity = ObjectIdentity
host = _Host_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25)
)
_HrSystem_ObjectIdentity = ObjectIdentity
hrSystem = _HrSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 1)
)
_HrSystemUptime_Type = TimeTicks
_HrSystemUptime_Object = MibScalar
hrSystemUptime = _HrSystemUptime_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 1),
    _HrSystemUptime_Type()
)
hrSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemUptime.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemUptime.setDescription("The amount of time since this host was last initialized. Note that this is different from sysUpTime in the SNMPv2-MIB [RFC1907] because sysUpTime is the uptime of the network management portion of the system.")
_HrSystemDate_Type = DateAndTime
_HrSystemDate_Object = MibScalar
hrSystemDate = _HrSystemDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 2),
    _HrSystemDate_Type()
)
hrSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemDate.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemDate.setDescription("The host's notion of the local date and time of day.")


class _HrSystemInitialLoadDevice_Type(Integer32):
    """Custom type hrSystemInitialLoadDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSystemInitialLoadDevice_Type.__name__ = "Integer32"
_HrSystemInitialLoadDevice_Object = MibScalar
hrSystemInitialLoadDevice = _HrSystemInitialLoadDevice_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 3),
    _HrSystemInitialLoadDevice_Type()
)
hrSystemInitialLoadDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemInitialLoadDevice.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemInitialLoadDevice.setDescription("The index of the hrDeviceEntry for the device from which this host is configured to load its initial operating system configuration (i.e., which operating system code and/or boot parameters). Note that writing to this object just changes the configuration that will be used the next time the operating system is loaded and does not actually cause the reload to occur.")


class _HrSystemInitialLoadParameters_Type(InternationalDisplayString):
    """Custom type hrSystemInitialLoadParameters based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrSystemInitialLoadParameters_Type.__name__ = "InternationalDisplayString"
_HrSystemInitialLoadParameters_Object = MibScalar
hrSystemInitialLoadParameters = _HrSystemInitialLoadParameters_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 4),
    _HrSystemInitialLoadParameters_Type()
)
hrSystemInitialLoadParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemInitialLoadParameters.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemInitialLoadParameters.setDescription("This object contains the parameters (e.g. a pathname and parameter) supplied to the load device when requesting the initial operating system configuration from that device. Note that writing to this object just changes the configuration that will be used the next time the operating system is loaded and does not actually cause the reload to occur.")
_HrSystemNumUsers_Type = Gauge32
_HrSystemNumUsers_Object = MibScalar
hrSystemNumUsers = _HrSystemNumUsers_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 5),
    _HrSystemNumUsers_Type()
)
hrSystemNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemNumUsers.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemNumUsers.setDescription("The number of user sessions for which this host is storing state information. A session is a collection of processes requiring a single act of user authentication and possibly subject to collective job control.")
_HrSystemProcesses_Type = Gauge32
_HrSystemProcesses_Object = MibScalar
hrSystemProcesses = _HrSystemProcesses_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 6),
    _HrSystemProcesses_Type()
)
hrSystemProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemProcesses.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemProcesses.setDescription("The number of process contexts currently loaded or running on this system.")


class _HrSystemMaxProcesses_Type(Integer32):
    """Custom type hrSystemMaxProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrSystemMaxProcesses_Type.__name__ = "Integer32"
_HrSystemMaxProcesses_Object = MibScalar
hrSystemMaxProcesses = _HrSystemMaxProcesses_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 7),
    _HrSystemMaxProcesses_Type()
)
hrSystemMaxProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemMaxProcesses.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemMaxProcesses.setDescription("The maximum number of process contexts this system can support. If there is no fixed maximum, the value should be zero. On systems that have a fixed maximum, this object can help diagnose failures that occur when this maximum is reached.")
_HrStorage_ObjectIdentity = ObjectIdentity
hrStorage = _HrStorage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2)
)
_HrStorageTypes_ObjectIdentity = ObjectIdentity
hrStorageTypes = _HrStorageTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1)
)
_HrMemorySize_Type = KBytes
_HrMemorySize_Object = MibScalar
hrMemorySize = _HrMemorySize_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 2),
    _HrMemorySize_Type()
)
hrMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hrMemorySize.setUnits("KBytes")
if mibBuilder.loadTexts:
    hrMemorySize.setDescription("The amount of physical read-write main memory, typically RAM, contained by the host.")
_HrStorageTable_Object = MibTable
hrStorageTable = _HrStorageTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3)
)
if mibBuilder.loadTexts:
    hrStorageTable.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageTable.setDescription("The (conceptual) table of logical storage areas on the host. An entry shall be placed in the storage table for each logical area of storage that is allocated and has fixed resource limits. The amount of storage represented in an entity is the amount actually usable by the requesting entity, and excludes loss due to formatting or file system reference information. These entries are associated with logical storage areas, as might be seen by an application, rather than physical storage entities which are typically seen by an operating system. Storage such as tapes and floppies without file systems on them are typically not allocated in chunks by the operating system to requesting applications, and therefore shouldn't appear in this table. Examples of valid storage for this table include disk partitions, file systems, ram (for some architectures this is further segmented into regular memory, extended memory, and so on), backing store for virtual memory (`swap space'). This table is intended to be a useful diagnostic for `out of memory' and `out of buffers' types of failures. In addition, it can be a useful performance monitoring tool for tracking memory, disk, or buffer usage.")
_HrStorageEntry_Object = MibTableRow
hrStorageEntry = _HrStorageEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1)
)
hrStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrStorageIndex"),
)
if mibBuilder.loadTexts:
    hrStorageEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageEntry.setDescription("A (conceptual) entry for one logical storage area on the host. As an example, an instance of the hrStorageType object might be named hrStorageType.3")


class _HrStorageIndex_Type(Integer32):
    """Custom type hrStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrStorageIndex_Type.__name__ = "Integer32"
_HrStorageIndex_Object = MibTableColumn
hrStorageIndex = _HrStorageIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 1),
    _HrStorageIndex_Type()
)
hrStorageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageIndex.setDescription("A unique value for each logical storage area contained by the host.")
_HrStorageType_Type = AutonomousType
_HrStorageType_Object = MibTableColumn
hrStorageType = _HrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 2),
    _HrStorageType_Type()
)
hrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageType.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageType.setDescription("The type of storage represented by this entry.")
_HrStorageDescr_Type = DisplayString
_HrStorageDescr_Object = MibTableColumn
hrStorageDescr = _HrStorageDescr_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 3),
    _HrStorageDescr_Type()
)
hrStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageDescr.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageDescr.setDescription("A description of the type and instance of the storage described by this entry.")


class _HrStorageAllocationUnits_Type(Integer32):
    """Custom type hrStorageAllocationUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrStorageAllocationUnits_Type.__name__ = "Integer32"
_HrStorageAllocationUnits_Object = MibTableColumn
hrStorageAllocationUnits = _HrStorageAllocationUnits_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 4),
    _HrStorageAllocationUnits_Type()
)
hrStorageAllocationUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageAllocationUnits.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageAllocationUnits.setUnits("Bytes")
if mibBuilder.loadTexts:
    hrStorageAllocationUnits.setDescription("The size, in bytes, of the data objects allocated from this pool. If this entry is monitoring sectors, blocks, buffers, or packets, for example, this number will commonly be greater than one. Otherwise this number will typically be one.")


class _HrStorageSize_Type(Integer32):
    """Custom type hrStorageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrStorageSize_Type.__name__ = "Integer32"
_HrStorageSize_Object = MibTableColumn
hrStorageSize = _HrStorageSize_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 5),
    _HrStorageSize_Type()
)
hrStorageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageSize.setDescription("The size of the storage represented by this entry, in units of hrStorageAllocationUnits. This object is writable to allow remote configuration of the size of the storage area in those cases where such an operation makes sense and is possible on the underlying system. For example, the amount of main memory allocated to a buffer pool might be modified or the amount of disk space allocated to virtual memory might be modified.")


class _HrStorageUsed_Type(Integer32):
    """Custom type hrStorageUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrStorageUsed_Type.__name__ = "Integer32"
_HrStorageUsed_Object = MibTableColumn
hrStorageUsed = _HrStorageUsed_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 6),
    _HrStorageUsed_Type()
)
hrStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageUsed.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageUsed.setDescription("The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.")
_HrStorageAllocationFailures_Type = Counter32
_HrStorageAllocationFailures_Object = MibTableColumn
hrStorageAllocationFailures = _HrStorageAllocationFailures_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 7),
    _HrStorageAllocationFailures_Type()
)
hrStorageAllocationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageAllocationFailures.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageAllocationFailures.setDescription("The number of requests for storage represented by this entry that could not be honored due to not enough storage. It should be noted that as this object has a SYNTAX of Counter32, that it does not have a defined initial value. However, it is recommended that this object be initialized to zero, even though management stations must not depend on such an initialization.")
_HrDevice_ObjectIdentity = ObjectIdentity
hrDevice = _HrDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3)
)
_HrDeviceTypes_ObjectIdentity = ObjectIdentity
hrDeviceTypes = _HrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1)
)
_HrDeviceTable_Object = MibTable
hrDeviceTable = _HrDeviceTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2)
)
if mibBuilder.loadTexts:
    hrDeviceTable.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceTable.setDescription("The (conceptual) table of devices contained by the host.")
_HrDeviceEntry_Object = MibTableRow
hrDeviceEntry = _HrDeviceEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1)
)
hrDeviceEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrDeviceEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceEntry.setDescription("A (conceptual) entry for one device contained by the host. As an example, an instance of the hrDeviceType object might be named hrDeviceType.3")


class _HrDeviceIndex_Type(Integer32):
    """Custom type hrDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrDeviceIndex_Type.__name__ = "Integer32"
_HrDeviceIndex_Object = MibTableColumn
hrDeviceIndex = _HrDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 1),
    _HrDeviceIndex_Type()
)
hrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceIndex.setDescription("A unique value for each device contained by the host. The value for each device must remain constant at least from one re-initialization of the agent to the next re-initialization.")
_HrDeviceType_Type = AutonomousType
_HrDeviceType_Object = MibTableColumn
hrDeviceType = _HrDeviceType_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 2),
    _HrDeviceType_Type()
)
hrDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceType.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceType.setDescription("An indication of the type of device. If this value is `hrDeviceProcessor { hrDeviceTypes 3 }' then an entry exists in the hrProcessorTable which corresponds to this device. If this value is `hrDeviceNetwork { hrDeviceTypes 4 }', then an entry exists in the hrNetworkTable which corresponds to this device. If this value is `hrDevicePrinter { hrDeviceTypes 5 }', then an entry exists in the hrPrinterTable which corresponds to this device. If this value is `hrDeviceDiskStorage { hrDeviceTypes 6 }', then an entry exists in the hrDiskStorageTable which corresponds to this device.")


class _HrDeviceDescr_Type(DisplayString):
    """Custom type hrDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HrDeviceDescr_Type.__name__ = "DisplayString"
_HrDeviceDescr_Object = MibTableColumn
hrDeviceDescr = _HrDeviceDescr_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 3),
    _HrDeviceDescr_Type()
)
hrDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceDescr.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceDescr.setDescription("A textual description of this device, including the device's manufacturer and revision, and optionally, its serial number.")
_HrDeviceID_Type = ProductID
_HrDeviceID_Object = MibTableColumn
hrDeviceID = _HrDeviceID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 4),
    _HrDeviceID_Type()
)
hrDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceID.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceID.setDescription("The product ID for this device.")


class _HrDeviceStatus_Type(Integer32):
    """Custom type hrDeviceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("running", 2),
          ("warning", 3),
          ("testing", 4),
          ("down", 5))
    )


_HrDeviceStatus_Type.__name__ = "Integer32"
_HrDeviceStatus_Object = MibTableColumn
hrDeviceStatus = _HrDeviceStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 5),
    _HrDeviceStatus_Type()
)
hrDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceStatus.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceStatus.setDescription("The current operational state of the device described by this row of the table. A value unknown(1) indicates that the current state of the device is unknown. running(2) indicates that the device is up and running and that no unusual error conditions are known. The warning(3) state indicates that agent has been informed of an unusual error condition by the operational software (e.g., a disk device driver) but that the device is still 'operational'. An example would be a high number of soft errors on a disk. A value of testing(4), indicates that the device is not available for use because it is in the testing state. The state of down(5) is used only when the agent has been informed that the device is not available for any use.")
_HrDeviceErrors_Type = Counter32
_HrDeviceErrors_Object = MibTableColumn
hrDeviceErrors = _HrDeviceErrors_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 6),
    _HrDeviceErrors_Type()
)
hrDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceErrors.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceErrors.setDescription("The number of errors detected on this device. It should be noted that as this object has a SYNTAX of Counter32, that it does not have a defined initial value. However, it is recommended that this object be initialized to zero, even though management stations must not depend on such an initialization.")
_HrProcessorTable_Object = MibTable
hrProcessorTable = _HrProcessorTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3)
)
if mibBuilder.loadTexts:
    hrProcessorTable.setStatus("current")
if mibBuilder.loadTexts:
    hrProcessorTable.setDescription("The (conceptual) table of processors contained by the host. Note that this table is potentially sparse: a (conceptual) entry exists only if the correspondent value of the hrDeviceType object is `hrDeviceProcessor'.")
_HrProcessorEntry_Object = MibTableRow
hrProcessorEntry = _HrProcessorEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1)
)
hrProcessorEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrProcessorEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrProcessorEntry.setDescription("A (conceptual) entry for one processor contained by the host. The hrDeviceIndex in the index represents the entry in the hrDeviceTable that corresponds to the hrProcessorEntry. As an example of how objects in this table are named, an instance of the hrProcessorFrwID object might be named hrProcessorFrwID.3")
_HrProcessorFrwID_Type = ProductID
_HrProcessorFrwID_Object = MibTableColumn
hrProcessorFrwID = _HrProcessorFrwID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1, 1),
    _HrProcessorFrwID_Type()
)
hrProcessorFrwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrProcessorFrwID.setStatus("current")
if mibBuilder.loadTexts:
    hrProcessorFrwID.setDescription("The product ID of the firmware associated with the processor.")


class _HrProcessorLoad_Type(Integer32):
    """Custom type hrProcessorLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HrProcessorLoad_Type.__name__ = "Integer32"
_HrProcessorLoad_Object = MibTableColumn
hrProcessorLoad = _HrProcessorLoad_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1, 2),
    _HrProcessorLoad_Type()
)
hrProcessorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrProcessorLoad.setStatus("current")
if mibBuilder.loadTexts:
    hrProcessorLoad.setDescription("The average, over the last minute, of the percentage of time that this processor was not idle. Implementations may approximate this one minute smoothing period if necessary.")
_HrNetworkTable_Object = MibTable
hrNetworkTable = _HrNetworkTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4)
)
if mibBuilder.loadTexts:
    hrNetworkTable.setStatus("current")
if mibBuilder.loadTexts:
    hrNetworkTable.setDescription("The (conceptual) table of network devices contained by the host. Note that this table is potentially sparse: a (conceptual) entry exists only if the correspondent value of the hrDeviceType object is `hrDeviceNetwork'.")
_HrNetworkEntry_Object = MibTableRow
hrNetworkEntry = _HrNetworkEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4, 1)
)
hrNetworkEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrNetworkEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrNetworkEntry.setDescription("A (conceptual) entry for one network device contained by the host. The hrDeviceIndex in the index represents the entry in the hrDeviceTable that corresponds to the hrNetworkEntry. As an example of how objects in this table are named, an instance of the hrNetworkIfIndex object might be named hrNetworkIfIndex.3")
_HrNetworkIfIndex_Type = InterfaceIndexOrZero
_HrNetworkIfIndex_Object = MibTableColumn
hrNetworkIfIndex = _HrNetworkIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4, 1, 1),
    _HrNetworkIfIndex_Type()
)
hrNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrNetworkIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrNetworkIfIndex.setDescription("The value of ifIndex which corresponds to this network device. If this device is not represented in the ifTable, then this value shall be zero.")
_HrPrinterTable_Object = MibTable
hrPrinterTable = _HrPrinterTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5)
)
if mibBuilder.loadTexts:
    hrPrinterTable.setStatus("current")
if mibBuilder.loadTexts:
    hrPrinterTable.setDescription("The (conceptual) table of printers local to the host. Note that this table is potentially sparse: a (conceptual) entry exists only if the correspondent value of the hrDeviceType object is `hrDevicePrinter'.")
_HrPrinterEntry_Object = MibTableRow
hrPrinterEntry = _HrPrinterEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1)
)
hrPrinterEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrPrinterEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrPrinterEntry.setDescription("A (conceptual) entry for one printer local to the host. The hrDeviceIndex in the index represents the entry in the hrDeviceTable that corresponds to the hrPrinterEntry. As an example of how objects in this table are named, an instance of the hrPrinterStatus object might be named hrPrinterStatus.3")


class _HrPrinterStatus_Type(Integer32):
    """Custom type hrPrinterStatus based on Integer32"""
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
          ("unknown", 2),
          ("idle", 3),
          ("printing", 4),
          ("warmup", 5))
    )


_HrPrinterStatus_Type.__name__ = "Integer32"
_HrPrinterStatus_Object = MibTableColumn
hrPrinterStatus = _HrPrinterStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1, 1),
    _HrPrinterStatus_Type()
)
hrPrinterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPrinterStatus.setStatus("current")
if mibBuilder.loadTexts:
    hrPrinterStatus.setDescription("The current status of this printer device.")
_HrPrinterDetectedErrorState_Type = OctetString
_HrPrinterDetectedErrorState_Object = MibTableColumn
hrPrinterDetectedErrorState = _HrPrinterDetectedErrorState_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1, 2),
    _HrPrinterDetectedErrorState_Type()
)
hrPrinterDetectedErrorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPrinterDetectedErrorState.setStatus("current")
if mibBuilder.loadTexts:
    hrPrinterDetectedErrorState.setDescription("This object represents any error conditions detected by the printer. The error conditions are encoded as bits in an octet string, with the following definitions: Condition Bit # lowPaper 0 noPaper 1 lowToner 2 noToner 3 doorOpen 4 jammed 5 offline 6 serviceRequested 7 inputTrayMissing 8 outputTrayMissing 9 markerSupplyMissing 10 outputNearFull 11 outputFull 12 inputTrayEmpty 13 overduePreventMaint 14 Bits are numbered starting with the most significant bit of the first byte being bit 0, the least significant bit of the first byte being bit 7, the most significant bit of the second byte being bit 8, and so on. A one bit encodes that the condition was detected, while a zero bit encodes that the condition was not detected. This object is useful for alerting an operator to specific warning or error conditions that may occur, especially those requiring human intervention.")
_HrDiskStorageTable_Object = MibTable
hrDiskStorageTable = _HrDiskStorageTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6)
)
if mibBuilder.loadTexts:
    hrDiskStorageTable.setStatus("current")
if mibBuilder.loadTexts:
    hrDiskStorageTable.setDescription("The (conceptual) table of long-term storage devices contained by the host. In particular, disk devices accessed remotely over a network are not included here. Note that this table is potentially sparse: a (conceptual) entry exists only if the correspondent value of the hrDeviceType object is `hrDeviceDiskStorage'.")
_HrDiskStorageEntry_Object = MibTableRow
hrDiskStorageEntry = _HrDiskStorageEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1)
)
hrDiskStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrDiskStorageEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrDiskStorageEntry.setDescription("A (conceptual) entry for one long-term storage device contained by the host. The hrDeviceIndex in the index represents the entry in the hrDeviceTable that corresponds to the hrDiskStorageEntry. As an example, an instance of the hrDiskStorageCapacity object might be named hrDiskStorageCapacity.3")


class _HrDiskStorageAccess_Type(Integer32):
    """Custom type hrDiskStorageAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readWrite", 1),
          ("readOnly", 2))
    )


_HrDiskStorageAccess_Type.__name__ = "Integer32"
_HrDiskStorageAccess_Object = MibTableColumn
hrDiskStorageAccess = _HrDiskStorageAccess_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 1),
    _HrDiskStorageAccess_Type()
)
hrDiskStorageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageAccess.setStatus("current")
if mibBuilder.loadTexts:
    hrDiskStorageAccess.setDescription("An indication if this long-term storage device is readable and writable or only readable. This should reflect the media type, any write-protect mechanism, and any device configuration that affects the entire device.")


class _HrDiskStorageMedia_Type(Integer32):
    """Custom type hrDiskStorageMedia based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("hardDisk", 3),
          ("floppyDisk", 4),
          ("opticalDiskROM", 5),
          ("opticalDiskWORM", 6),
          ("opticalDiskRW", 7),
          ("ramDisk", 8))
    )


_HrDiskStorageMedia_Type.__name__ = "Integer32"
_HrDiskStorageMedia_Object = MibTableColumn
hrDiskStorageMedia = _HrDiskStorageMedia_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 2),
    _HrDiskStorageMedia_Type()
)
hrDiskStorageMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageMedia.setStatus("current")
if mibBuilder.loadTexts:
    hrDiskStorageMedia.setDescription("An indication of the type of media used in this long- term storage device.")
_HrDiskStorageRemoveble_Type = TruthValue
_HrDiskStorageRemoveble_Object = MibTableColumn
hrDiskStorageRemoveble = _HrDiskStorageRemoveble_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 3),
    _HrDiskStorageRemoveble_Type()
)
hrDiskStorageRemoveble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageRemoveble.setStatus("current")
if mibBuilder.loadTexts:
    hrDiskStorageRemoveble.setDescription("Denotes whether or not the disk media may be removed from the drive.")
_HrDiskStorageCapacity_Type = KBytes
_HrDiskStorageCapacity_Object = MibTableColumn
hrDiskStorageCapacity = _HrDiskStorageCapacity_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 4),
    _HrDiskStorageCapacity_Type()
)
hrDiskStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hrDiskStorageCapacity.setUnits("KBytes")
if mibBuilder.loadTexts:
    hrDiskStorageCapacity.setDescription("The total size for this long-term storage device. If the media is removable and is currently removed, this value should be zero.")
_HrPartitionTable_Object = MibTable
hrPartitionTable = _HrPartitionTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7)
)
if mibBuilder.loadTexts:
    hrPartitionTable.setStatus("current")
if mibBuilder.loadTexts:
    hrPartitionTable.setDescription("The (conceptual) table of partitions for long-term storage devices contained by the host. In particular, partitions accessed remotely over a network are not included here.")
_HrPartitionEntry_Object = MibTableRow
hrPartitionEntry = _HrPartitionEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1)
)
hrPartitionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "HOST-RESOURCES-MIB", "hrPartitionIndex"),
)
if mibBuilder.loadTexts:
    hrPartitionEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrPartitionEntry.setDescription("A (conceptual) entry for one partition. The hrDeviceIndex in the index represents the entry in the hrDeviceTable that corresponds to the hrPartitionEntry. As an example of how objects in this table are named, an instance of the hrPartitionSize object might be named hrPartitionSize.3.1")


class _HrPartitionIndex_Type(Integer32):
    """Custom type hrPartitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrPartitionIndex_Type.__name__ = "Integer32"
_HrPartitionIndex_Object = MibTableColumn
hrPartitionIndex = _HrPartitionIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 1),
    _HrPartitionIndex_Type()
)
hrPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrPartitionIndex.setDescription("A unique value for each partition on this long-term storage device. The value for each long-term storage device must remain constant at least from one re- initialization of the agent to the next re- initialization.")


class _HrPartitionLabel_Type(InternationalDisplayString):
    """Custom type hrPartitionLabel based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrPartitionLabel_Type.__name__ = "InternationalDisplayString"
_HrPartitionLabel_Object = MibTableColumn
hrPartitionLabel = _HrPartitionLabel_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 2),
    _HrPartitionLabel_Type()
)
hrPartitionLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionLabel.setStatus("current")
if mibBuilder.loadTexts:
    hrPartitionLabel.setDescription("A textual description of this partition.")
_HrPartitionID_Type = OctetString
_HrPartitionID_Object = MibTableColumn
hrPartitionID = _HrPartitionID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 3),
    _HrPartitionID_Type()
)
hrPartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionID.setStatus("current")
if mibBuilder.loadTexts:
    hrPartitionID.setDescription("A descriptor which uniquely represents this partition to the responsible operating system. On some systems, this might take on a binary representation.")
_HrPartitionSize_Type = KBytes
_HrPartitionSize_Object = MibTableColumn
hrPartitionSize = _HrPartitionSize_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 4),
    _HrPartitionSize_Type()
)
hrPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    hrPartitionSize.setUnits("KBytes")
if mibBuilder.loadTexts:
    hrPartitionSize.setDescription("The size of this partition.")


class _HrPartitionFSIndex_Type(Integer32):
    """Custom type hrPartitionFSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrPartitionFSIndex_Type.__name__ = "Integer32"
_HrPartitionFSIndex_Object = MibTableColumn
hrPartitionFSIndex = _HrPartitionFSIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 5),
    _HrPartitionFSIndex_Type()
)
hrPartitionFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionFSIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrPartitionFSIndex.setDescription("The index of the file system mounted on this partition. If no file system is mounted on this partition, then this value shall be zero. Note that multiple partitions may point to one file system, denoting that that file system resides on those partitions. Multiple file systems may not reside on one partition.")
_HrFSTable_Object = MibTable
hrFSTable = _HrFSTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8)
)
if mibBuilder.loadTexts:
    hrFSTable.setStatus("current")
if mibBuilder.loadTexts:
    hrFSTable.setDescription("The (conceptual) table of file systems local to this host or remotely mounted from a file server. File systems that are in only one user's environment on a multi-user system will not be included in this table.")
_HrFSEntry_Object = MibTableRow
hrFSEntry = _HrFSEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1)
)
hrFSEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrFSIndex"),
)
if mibBuilder.loadTexts:
    hrFSEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrFSEntry.setDescription("A (conceptual) entry for one file system local to this host or remotely mounted from a file server. File systems that are in only one user's environment on a multi-user system will not be included in this table. As an example of how objects in this table are named, an instance of the hrFSMountPoint object might be named hrFSMountPoint.3")


class _HrFSIndex_Type(Integer32):
    """Custom type hrFSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrFSIndex_Type.__name__ = "Integer32"
_HrFSIndex_Object = MibTableColumn
hrFSIndex = _HrFSIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 1),
    _HrFSIndex_Type()
)
hrFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrFSIndex.setDescription("A unique value for each file system local to this host. The value for each file system must remain constant at least from one re-initialization of the agent to the next re-initialization.")


class _HrFSMountPoint_Type(InternationalDisplayString):
    """Custom type hrFSMountPoint based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrFSMountPoint_Type.__name__ = "InternationalDisplayString"
_HrFSMountPoint_Object = MibTableColumn
hrFSMountPoint = _HrFSMountPoint_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 2),
    _HrFSMountPoint_Type()
)
hrFSMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSMountPoint.setStatus("current")
if mibBuilder.loadTexts:
    hrFSMountPoint.setDescription("The path name of the root of this file system.")


class _HrFSRemoteMountPoint_Type(InternationalDisplayString):
    """Custom type hrFSRemoteMountPoint based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrFSRemoteMountPoint_Type.__name__ = "InternationalDisplayString"
_HrFSRemoteMountPoint_Object = MibTableColumn
hrFSRemoteMountPoint = _HrFSRemoteMountPoint_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 3),
    _HrFSRemoteMountPoint_Type()
)
hrFSRemoteMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSRemoteMountPoint.setStatus("current")
if mibBuilder.loadTexts:
    hrFSRemoteMountPoint.setDescription("A description of the name and/or address of the server that this file system is mounted from. This may also include parameters such as the mount point on the remote file system. If this is not a remote file system, this string should have a length of zero.")
_HrFSType_Type = AutonomousType
_HrFSType_Object = MibTableColumn
hrFSType = _HrFSType_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 4),
    _HrFSType_Type()
)
hrFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSType.setStatus("current")
if mibBuilder.loadTexts:
    hrFSType.setDescription("The value of this object identifies the type of this file system.")


class _HrFSAccess_Type(Integer32):
    """Custom type hrFSAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readWrite", 1),
          ("readOnly", 2))
    )


_HrFSAccess_Type.__name__ = "Integer32"
_HrFSAccess_Object = MibTableColumn
hrFSAccess = _HrFSAccess_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 5),
    _HrFSAccess_Type()
)
hrFSAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSAccess.setStatus("current")
if mibBuilder.loadTexts:
    hrFSAccess.setDescription("An indication if this file system is logically configured by the operating system to be readable and writable or only readable. This does not represent any local access-control policy, except one that is applied to the file system as a whole.")
_HrFSBootable_Type = TruthValue
_HrFSBootable_Object = MibTableColumn
hrFSBootable = _HrFSBootable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 6),
    _HrFSBootable_Type()
)
hrFSBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSBootable.setStatus("current")
if mibBuilder.loadTexts:
    hrFSBootable.setDescription("A flag indicating whether this file system is bootable.")


class _HrFSStorageIndex_Type(Integer32):
    """Custom type hrFSStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrFSStorageIndex_Type.__name__ = "Integer32"
_HrFSStorageIndex_Object = MibTableColumn
hrFSStorageIndex = _HrFSStorageIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 7),
    _HrFSStorageIndex_Type()
)
hrFSStorageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSStorageIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrFSStorageIndex.setDescription("The index of the hrStorageEntry that represents information about this file system. If there is no such information available, then this value shall be zero. The relevant storage entry will be useful in tracking the percent usage of this file system and diagnosing errors that may occur when it runs out of space.")
_HrFSLastFullBackupDate_Type = DateAndTime
_HrFSLastFullBackupDate_Object = MibTableColumn
hrFSLastFullBackupDate = _HrFSLastFullBackupDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 8),
    _HrFSLastFullBackupDate_Type()
)
hrFSLastFullBackupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrFSLastFullBackupDate.setStatus("current")
if mibBuilder.loadTexts:
    hrFSLastFullBackupDate.setDescription("The last date at which this complete file system was copied to another storage device for backup. This information is useful for ensuring that backups are being performed regularly. If this information is not known, then this variable shall have the value corresponding to January 1, year 0000, 00:00:00.0, which is encoded as (hex)'00 00 01 01 00 00 00 00'.")
_HrFSLastPartialBackupDate_Type = DateAndTime
_HrFSLastPartialBackupDate_Object = MibTableColumn
hrFSLastPartialBackupDate = _HrFSLastPartialBackupDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 9),
    _HrFSLastPartialBackupDate_Type()
)
hrFSLastPartialBackupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrFSLastPartialBackupDate.setStatus("current")
if mibBuilder.loadTexts:
    hrFSLastPartialBackupDate.setDescription("The last date at which a portion of this file system was copied to another storage device for backup. This information is useful for ensuring that backups are being performed regularly. If this information is not known, then this variable shall have the value corresponding to January 1, year 0000, 00:00:00.0, which is encoded as (hex)'00 00 01 01 00 00 00 00'.")
_HrFSTypes_ObjectIdentity = ObjectIdentity
hrFSTypes = _HrFSTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9)
)
_HrSWRun_ObjectIdentity = ObjectIdentity
hrSWRun = _HrSWRun_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 4)
)


class _HrSWOSIndex_Type(Integer32):
    """Custom type hrSWOSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSWOSIndex_Type.__name__ = "Integer32"
_HrSWOSIndex_Object = MibScalar
hrSWOSIndex = _HrSWOSIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 1),
    _HrSWOSIndex_Type()
)
hrSWOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWOSIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrSWOSIndex.setDescription("The value of the hrSWRunIndex for the hrSWRunEntry that represents the primary operating system running on this host. This object is useful for quickly and uniquely identifying that primary operating system.")
_HrSWRunTable_Object = MibTable
hrSWRunTable = _HrSWRunTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2)
)
if mibBuilder.loadTexts:
    hrSWRunTable.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunTable.setDescription("The (conceptual) table of software running on the host.")
_HrSWRunEntry_Object = MibTableRow
hrSWRunEntry = _HrSWRunEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1)
)
hrSWRunEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrSWRunIndex"),
)
if mibBuilder.loadTexts:
    hrSWRunEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunEntry.setDescription("A (conceptual) entry for one piece of software running on the host Note that because the installed software table only contains information for software stored locally on this host, not every piece of running software will be found in the installed software table. This is true of software that was loaded and run from a non-local source, such as a network-mounted file system. As an example of how objects in this table are named, an instance of the hrSWRunName object might be named hrSWRunName.1287")


class _HrSWRunIndex_Type(Integer32):
    """Custom type hrSWRunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSWRunIndex_Type.__name__ = "Integer32"
_HrSWRunIndex_Object = MibTableColumn
hrSWRunIndex = _HrSWRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 1),
    _HrSWRunIndex_Type()
)
hrSWRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunIndex.setDescription("A unique value for each piece of software running on the host. Wherever possible, this should be the system's native, unique identification number.")


class _HrSWRunName_Type(InternationalDisplayString):
    """Custom type hrSWRunName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HrSWRunName_Type.__name__ = "InternationalDisplayString"
_HrSWRunName_Object = MibTableColumn
hrSWRunName = _HrSWRunName_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 2),
    _HrSWRunName_Type()
)
hrSWRunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunName.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunName.setDescription("A textual description of this running piece of software, including the manufacturer, revision, and the name by which it is commonly known. If this software was installed locally, this should be the same string as used in the corresponding hrSWInstalledName.")
_HrSWRunID_Type = ProductID
_HrSWRunID_Object = MibTableColumn
hrSWRunID = _HrSWRunID_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 3),
    _HrSWRunID_Type()
)
hrSWRunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunID.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunID.setDescription("The product ID of this running piece of software.")


class _HrSWRunPath_Type(InternationalDisplayString):
    """Custom type hrSWRunPath based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrSWRunPath_Type.__name__ = "InternationalDisplayString"
_HrSWRunPath_Object = MibTableColumn
hrSWRunPath = _HrSWRunPath_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 4),
    _HrSWRunPath_Type()
)
hrSWRunPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunPath.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunPath.setDescription("A description of the location on long-term storage (e.g. a disk drive) from which this software was loaded.")


class _HrSWRunParameters_Type(InternationalDisplayString):
    """Custom type hrSWRunParameters based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrSWRunParameters_Type.__name__ = "InternationalDisplayString"
_HrSWRunParameters_Object = MibTableColumn
hrSWRunParameters = _HrSWRunParameters_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 5),
    _HrSWRunParameters_Type()
)
hrSWRunParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunParameters.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunParameters.setDescription("A description of the parameters supplied to this software when it was initially loaded.")


class _HrSWRunType_Type(Integer32):
    """Custom type hrSWRunType based on Integer32"""
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
        *(("unknown", 1),
          ("operatingSystem", 2),
          ("deviceDriver", 3),
          ("application", 4))
    )


_HrSWRunType_Type.__name__ = "Integer32"
_HrSWRunType_Object = MibTableColumn
hrSWRunType = _HrSWRunType_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 6),
    _HrSWRunType_Type()
)
hrSWRunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunType.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunType.setDescription("The type of this software.")


class _HrSWRunStatus_Type(Integer32):
    """Custom type hrSWRunStatus based on Integer32"""
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
        *(("running", 1),
          ("runnable", 2),
          ("notRunnable", 3),
          ("invalid", 4))
    )


_HrSWRunStatus_Type.__name__ = "Integer32"
_HrSWRunStatus_Object = MibTableColumn
hrSWRunStatus = _HrSWRunStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 7),
    _HrSWRunStatus_Type()
)
hrSWRunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSWRunStatus.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunStatus.setDescription("The status of this running piece of software. Setting this value to invalid(4) shall cause this software to stop running and to be unloaded. Sets to other values are not valid.")
_HrSWRunPerf_ObjectIdentity = ObjectIdentity
hrSWRunPerf = _HrSWRunPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 5)
)
_HrSWRunPerfTable_Object = MibTable
hrSWRunPerfTable = _HrSWRunPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1)
)
if mibBuilder.loadTexts:
    hrSWRunPerfTable.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunPerfTable.setDescription("The (conceptual) table of running software performance metrics.")
_HrSWRunPerfEntry_Object = MibTableRow
hrSWRunPerfEntry = _HrSWRunPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hrSWRunPerfEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunPerfEntry.setDescription("A (conceptual) entry containing software performance metrics. As an example, an instance of the hrSWRunPerfCPU object might be named hrSWRunPerfCPU.1287")


class _HrSWRunPerfCPU_Type(Integer32):
    """Custom type hrSWRunPerfCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrSWRunPerfCPU_Type.__name__ = "Integer32"
_HrSWRunPerfCPU_Object = MibTableColumn
hrSWRunPerfCPU = _HrSWRunPerfCPU_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1, 1, 1),
    _HrSWRunPerfCPU_Type()
)
hrSWRunPerfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunPerfCPU.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunPerfCPU.setDescription("The number of centi-seconds of the total system's CPU resources consumed by this process. Note that on a multi-processor system, this value may increment by more than one centi-second in one centi-second of real (wall clock) time.")
_HrSWRunPerfMem_Type = KBytes
_HrSWRunPerfMem_Object = MibTableColumn
hrSWRunPerfMem = _HrSWRunPerfMem_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1, 1, 2),
    _HrSWRunPerfMem_Type()
)
hrSWRunPerfMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunPerfMem.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunPerfMem.setUnits("KBytes")
if mibBuilder.loadTexts:
    hrSWRunPerfMem.setDescription("The total amount of real system memory allocated to this process.")
_HrSWInstalled_ObjectIdentity = ObjectIdentity
hrSWInstalled = _HrSWInstalled_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 6)
)
_HrSWInstalledLastChange_Type = TimeTicks
_HrSWInstalledLastChange_Object = MibScalar
hrSWInstalledLastChange = _HrSWInstalledLastChange_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 1),
    _HrSWInstalledLastChange_Type()
)
hrSWInstalledLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledLastChange.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledLastChange.setDescription("The value of sysUpTime when an entry in the hrSWInstalledTable was last added, renamed, or deleted. Because this table is likely to contain many entries, polling of this object allows a management station to determine when re-downloading of the table might be useful.")
_HrSWInstalledLastUpdateTime_Type = TimeTicks
_HrSWInstalledLastUpdateTime_Object = MibScalar
hrSWInstalledLastUpdateTime = _HrSWInstalledLastUpdateTime_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 2),
    _HrSWInstalledLastUpdateTime_Type()
)
hrSWInstalledLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledLastUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledLastUpdateTime.setDescription("The value of sysUpTime when the hrSWInstalledTable was last completely updated. Because caching of this data will be a popular implementation strategy, retrieval of this object allows a management station to obtain a guarantee that no data in this table is older than the indicated time.")
_HrSWInstalledTable_Object = MibTable
hrSWInstalledTable = _HrSWInstalledTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3)
)
if mibBuilder.loadTexts:
    hrSWInstalledTable.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledTable.setDescription("The (conceptual) table of software installed on this host.")
_HrSWInstalledEntry_Object = MibTableRow
hrSWInstalledEntry = _HrSWInstalledEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1)
)
hrSWInstalledEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrSWInstalledIndex"),
)
if mibBuilder.loadTexts:
    hrSWInstalledEntry.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledEntry.setDescription("A (conceptual) entry for a piece of software installed on this host. As an example of how objects in this table are named, an instance of the hrSWInstalledName object might be named hrSWInstalledName.96")


class _HrSWInstalledIndex_Type(Integer32):
    """Custom type hrSWInstalledIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSWInstalledIndex_Type.__name__ = "Integer32"
_HrSWInstalledIndex_Object = MibTableColumn
hrSWInstalledIndex = _HrSWInstalledIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 1),
    _HrSWInstalledIndex_Type()
)
hrSWInstalledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledIndex.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledIndex.setDescription("A unique value for each piece of software installed on the host. This value shall be in the range from 1 to the number of pieces of software installed on the host.")


class _HrSWInstalledName_Type(InternationalDisplayString):
    """Custom type hrSWInstalledName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HrSWInstalledName_Type.__name__ = "InternationalDisplayString"
_HrSWInstalledName_Object = MibTableColumn
hrSWInstalledName = _HrSWInstalledName_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 2),
    _HrSWInstalledName_Type()
)
hrSWInstalledName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledName.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledName.setDescription("A textual description of this installed piece of software, including the manufacturer, revision, the name by which it is commonly known, and optionally, its serial number.")
_HrSWInstalledID_Type = ProductID
_HrSWInstalledID_Object = MibTableColumn
hrSWInstalledID = _HrSWInstalledID_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 3),
    _HrSWInstalledID_Type()
)
hrSWInstalledID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledID.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledID.setDescription("The product ID of this installed piece of software.")


class _HrSWInstalledType_Type(Integer32):
    """Custom type hrSWInstalledType based on Integer32"""
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
        *(("unknown", 1),
          ("operatingSystem", 2),
          ("deviceDriver", 3),
          ("application", 4))
    )


_HrSWInstalledType_Type.__name__ = "Integer32"
_HrSWInstalledType_Object = MibTableColumn
hrSWInstalledType = _HrSWInstalledType_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 4),
    _HrSWInstalledType_Type()
)
hrSWInstalledType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledType.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledType.setDescription("The type of this software.")
_HrSWInstalledDate_Type = DateAndTime
_HrSWInstalledDate_Object = MibTableColumn
hrSWInstalledDate = _HrSWInstalledDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 5),
    _HrSWInstalledDate_Type()
)
hrSWInstalledDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledDate.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledDate.setDescription("The last-modification date of this application as it would appear in a directory listing. If this information is not known, then this variable shall have the value corresponding to January 1, year 0000, 00:00:00.0, which is encoded as (hex)'00 00 01 01 00 00 00 00'.")
_HrMIBAdminInfo_ObjectIdentity = ObjectIdentity
hrMIBAdminInfo = _HrMIBAdminInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7)
)
_HrMIBCompliances_ObjectIdentity = ObjectIdentity
hrMIBCompliances = _HrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7, 2)
)
_HrMIBGroups_ObjectIdentity = ObjectIdentity
hrMIBGroups = _HrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7, 3)
)
hrSWRunEntry.registerAugmentions(
    ("HOST-RESOURCES-MIB",
     "hrSWRunPerfEntry")
)
hrSWRunPerfEntry.setIndexNames(*hrSWRunEntry.getIndexNames())

# Managed Objects groups

hrSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 3, 1)
)
hrSystemGroup.setObjects(
      *(("HOST-RESOURCES-MIB", "hrSystemUptime"),
        ("HOST-RESOURCES-MIB", "hrSystemDate"),
        ("HOST-RESOURCES-MIB", "hrSystemInitialLoadDevice"),
        ("HOST-RESOURCES-MIB", "hrSystemInitialLoadParameters"),
        ("HOST-RESOURCES-MIB", "hrSystemNumUsers"),
        ("HOST-RESOURCES-MIB", "hrSystemProcesses"),
        ("HOST-RESOURCES-MIB", "hrSystemMaxProcesses"))
)
if mibBuilder.loadTexts:
    hrSystemGroup.setStatus("current")
if mibBuilder.loadTexts:
    hrSystemGroup.setDescription("The Host Resources System Group.")

hrStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 3, 2)
)
hrStorageGroup.setObjects(
      *(("HOST-RESOURCES-MIB", "hrMemorySize"),
        ("HOST-RESOURCES-MIB", "hrStorageIndex"),
        ("HOST-RESOURCES-MIB", "hrStorageType"),
        ("HOST-RESOURCES-MIB", "hrStorageDescr"),
        ("HOST-RESOURCES-MIB", "hrStorageAllocationUnits"),
        ("HOST-RESOURCES-MIB", "hrStorageSize"),
        ("HOST-RESOURCES-MIB", "hrStorageUsed"),
        ("HOST-RESOURCES-MIB", "hrStorageAllocationFailures"))
)
if mibBuilder.loadTexts:
    hrStorageGroup.setStatus("current")
if mibBuilder.loadTexts:
    hrStorageGroup.setDescription("The Host Resources Storage Group.")

hrDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 3, 3)
)
hrDeviceGroup.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("HOST-RESOURCES-MIB", "hrDeviceType"),
        ("HOST-RESOURCES-MIB", "hrDeviceDescr"),
        ("HOST-RESOURCES-MIB", "hrDeviceID"),
        ("HOST-RESOURCES-MIB", "hrDeviceStatus"),
        ("HOST-RESOURCES-MIB", "hrDeviceErrors"),
        ("HOST-RESOURCES-MIB", "hrProcessorFrwID"),
        ("HOST-RESOURCES-MIB", "hrProcessorLoad"),
        ("HOST-RESOURCES-MIB", "hrNetworkIfIndex"),
        ("HOST-RESOURCES-MIB", "hrPrinterStatus"),
        ("HOST-RESOURCES-MIB", "hrPrinterDetectedErrorState"),
        ("HOST-RESOURCES-MIB", "hrDiskStorageAccess"),
        ("HOST-RESOURCES-MIB", "hrDiskStorageMedia"),
        ("HOST-RESOURCES-MIB", "hrDiskStorageRemoveble"),
        ("HOST-RESOURCES-MIB", "hrDiskStorageCapacity"),
        ("HOST-RESOURCES-MIB", "hrPartitionIndex"),
        ("HOST-RESOURCES-MIB", "hrPartitionLabel"),
        ("HOST-RESOURCES-MIB", "hrPartitionID"),
        ("HOST-RESOURCES-MIB", "hrPartitionSize"),
        ("HOST-RESOURCES-MIB", "hrPartitionFSIndex"),
        ("HOST-RESOURCES-MIB", "hrFSIndex"),
        ("HOST-RESOURCES-MIB", "hrFSMountPoint"),
        ("HOST-RESOURCES-MIB", "hrFSRemoteMountPoint"),
        ("HOST-RESOURCES-MIB", "hrFSType"),
        ("HOST-RESOURCES-MIB", "hrFSAccess"),
        ("HOST-RESOURCES-MIB", "hrFSBootable"),
        ("HOST-RESOURCES-MIB", "hrFSStorageIndex"),
        ("HOST-RESOURCES-MIB", "hrFSLastFullBackupDate"),
        ("HOST-RESOURCES-MIB", "hrFSLastPartialBackupDate"))
)
if mibBuilder.loadTexts:
    hrDeviceGroup.setStatus("current")
if mibBuilder.loadTexts:
    hrDeviceGroup.setDescription("The Host Resources Device Group.")

hrSWRunGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 3, 4)
)
hrSWRunGroup.setObjects(
      *(("HOST-RESOURCES-MIB", "hrSWOSIndex"),
        ("HOST-RESOURCES-MIB", "hrSWRunIndex"),
        ("HOST-RESOURCES-MIB", "hrSWRunName"),
        ("HOST-RESOURCES-MIB", "hrSWRunID"),
        ("HOST-RESOURCES-MIB", "hrSWRunPath"),
        ("HOST-RESOURCES-MIB", "hrSWRunParameters"),
        ("HOST-RESOURCES-MIB", "hrSWRunType"),
        ("HOST-RESOURCES-MIB", "hrSWRunStatus"))
)
if mibBuilder.loadTexts:
    hrSWRunGroup.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunGroup.setDescription("The Host Resources Running Software Group.")

hrSWRunPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 3, 5)
)
hrSWRunPerfGroup.setObjects(
      *(("HOST-RESOURCES-MIB", "hrSWRunPerfCPU"),
        ("HOST-RESOURCES-MIB", "hrSWRunPerfMem"))
)
if mibBuilder.loadTexts:
    hrSWRunPerfGroup.setStatus("current")
if mibBuilder.loadTexts:
    hrSWRunPerfGroup.setDescription("The Host Resources Running Software Performance Group.")

hrSWInstalledGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 3, 6)
)
hrSWInstalledGroup.setObjects(
      *(("HOST-RESOURCES-MIB", "hrSWInstalledLastChange"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledLastUpdateTime"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledIndex"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledName"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledID"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledType"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledDate"))
)
if mibBuilder.loadTexts:
    hrSWInstalledGroup.setStatus("current")
if mibBuilder.loadTexts:
    hrSWInstalledGroup.setDescription("The Host Resources Installed Software Group.")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 25, 7, 2, 1)
)
hrMIBCompliance.setObjects(
      *(("HOST-RESOURCES-MIB", "hrSystemGroup"),
        ("HOST-RESOURCES-MIB", "hrStorageGroup"),
        ("HOST-RESOURCES-MIB", "hrDeviceGroup"),
        ("HOST-RESOURCES-MIB", "hrSWRunGroup"),
        ("HOST-RESOURCES-MIB", "hrSWRunPerfGroup"),
        ("HOST-RESOURCES-MIB", "hrSWInstalledGroup"))
)
if mibBuilder.loadTexts:
    hrMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    hrMIBCompliance.setDescription("The requirements for conformance to the Host Resources MIB.")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HOST-RESOURCES-MIB",
    **{"KBytes": KBytes,
       "ProductID": ProductID,
       "InternationalDisplayString": InternationalDisplayString,
       "host": host,
       "hrSystem": hrSystem,
       "hrSystemUptime": hrSystemUptime,
       "hrSystemDate": hrSystemDate,
       "hrSystemInitialLoadDevice": hrSystemInitialLoadDevice,
       "hrSystemInitialLoadParameters": hrSystemInitialLoadParameters,
       "hrSystemNumUsers": hrSystemNumUsers,
       "hrSystemProcesses": hrSystemProcesses,
       "hrSystemMaxProcesses": hrSystemMaxProcesses,
       "hrStorage": hrStorage,
       "hrStorageTypes": hrStorageTypes,
       "hrMemorySize": hrMemorySize,
       "hrStorageTable": hrStorageTable,
       "hrStorageEntry": hrStorageEntry,
       "hrStorageIndex": hrStorageIndex,
       "hrStorageType": hrStorageType,
       "hrStorageDescr": hrStorageDescr,
       "hrStorageAllocationUnits": hrStorageAllocationUnits,
       "hrStorageSize": hrStorageSize,
       "hrStorageUsed": hrStorageUsed,
       "hrStorageAllocationFailures": hrStorageAllocationFailures,
       "hrDevice": hrDevice,
       "hrDeviceTypes": hrDeviceTypes,
       "hrDeviceTable": hrDeviceTable,
       "hrDeviceEntry": hrDeviceEntry,
       "hrDeviceIndex": hrDeviceIndex,
       "hrDeviceType": hrDeviceType,
       "hrDeviceDescr": hrDeviceDescr,
       "hrDeviceID": hrDeviceID,
       "hrDeviceStatus": hrDeviceStatus,
       "hrDeviceErrors": hrDeviceErrors,
       "hrProcessorTable": hrProcessorTable,
       "hrProcessorEntry": hrProcessorEntry,
       "hrProcessorFrwID": hrProcessorFrwID,
       "hrProcessorLoad": hrProcessorLoad,
       "hrNetworkTable": hrNetworkTable,
       "hrNetworkEntry": hrNetworkEntry,
       "hrNetworkIfIndex": hrNetworkIfIndex,
       "hrPrinterTable": hrPrinterTable,
       "hrPrinterEntry": hrPrinterEntry,
       "hrPrinterStatus": hrPrinterStatus,
       "hrPrinterDetectedErrorState": hrPrinterDetectedErrorState,
       "hrDiskStorageTable": hrDiskStorageTable,
       "hrDiskStorageEntry": hrDiskStorageEntry,
       "hrDiskStorageAccess": hrDiskStorageAccess,
       "hrDiskStorageMedia": hrDiskStorageMedia,
       "hrDiskStorageRemoveble": hrDiskStorageRemoveble,
       "hrDiskStorageCapacity": hrDiskStorageCapacity,
       "hrPartitionTable": hrPartitionTable,
       "hrPartitionEntry": hrPartitionEntry,
       "hrPartitionIndex": hrPartitionIndex,
       "hrPartitionLabel": hrPartitionLabel,
       "hrPartitionID": hrPartitionID,
       "hrPartitionSize": hrPartitionSize,
       "hrPartitionFSIndex": hrPartitionFSIndex,
       "hrFSTable": hrFSTable,
       "hrFSEntry": hrFSEntry,
       "hrFSIndex": hrFSIndex,
       "hrFSMountPoint": hrFSMountPoint,
       "hrFSRemoteMountPoint": hrFSRemoteMountPoint,
       "hrFSType": hrFSType,
       "hrFSAccess": hrFSAccess,
       "hrFSBootable": hrFSBootable,
       "hrFSStorageIndex": hrFSStorageIndex,
       "hrFSLastFullBackupDate": hrFSLastFullBackupDate,
       "hrFSLastPartialBackupDate": hrFSLastPartialBackupDate,
       "hrFSTypes": hrFSTypes,
       "hrSWRun": hrSWRun,
       "hrSWOSIndex": hrSWOSIndex,
       "hrSWRunTable": hrSWRunTable,
       "hrSWRunEntry": hrSWRunEntry,
       "hrSWRunIndex": hrSWRunIndex,
       "hrSWRunName": hrSWRunName,
       "hrSWRunID": hrSWRunID,
       "hrSWRunPath": hrSWRunPath,
       "hrSWRunParameters": hrSWRunParameters,
       "hrSWRunType": hrSWRunType,
       "hrSWRunStatus": hrSWRunStatus,
       "hrSWRunPerf": hrSWRunPerf,
       "hrSWRunPerfTable": hrSWRunPerfTable,
       "hrSWRunPerfEntry": hrSWRunPerfEntry,
       "hrSWRunPerfCPU": hrSWRunPerfCPU,
       "hrSWRunPerfMem": hrSWRunPerfMem,
       "hrSWInstalled": hrSWInstalled,
       "hrSWInstalledLastChange": hrSWInstalledLastChange,
       "hrSWInstalledLastUpdateTime": hrSWInstalledLastUpdateTime,
       "hrSWInstalledTable": hrSWInstalledTable,
       "hrSWInstalledEntry": hrSWInstalledEntry,
       "hrSWInstalledIndex": hrSWInstalledIndex,
       "hrSWInstalledName": hrSWInstalledName,
       "hrSWInstalledID": hrSWInstalledID,
       "hrSWInstalledType": hrSWInstalledType,
       "hrSWInstalledDate": hrSWInstalledDate,
       "hrMIBAdminInfo": hrMIBAdminInfo,
       "hostResourcesMibModule": hostResourcesMibModule,
       "hrMIBCompliances": hrMIBCompliances,
       "hrMIBCompliance": hrMIBCompliance,
       "hrMIBGroups": hrMIBGroups,
       "hrSystemGroup": hrSystemGroup,
       "hrStorageGroup": hrStorageGroup,
       "hrDeviceGroup": hrDeviceGroup,
       "hrSWRunGroup": hrSWRunGroup,
       "hrSWRunPerfGroup": hrSWRunPerfGroup,
       "hrSWInstalledGroup": hrSWInstalledGroup}
)
