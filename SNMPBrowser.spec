# -*- mode: python ; coding: utf-8 -*-
# Build:  python -m PyInstaller --noconfirm SNMPBrowser.spec
# Funziona sia su Windows (dist/SNMPBrowser/SNMPBrowser.exe) sia su macOS (dist/SNMPBrowser.app).
import re
import sys
from PyInstaller.utils.hooks import collect_all

VERSION = re.search(r'^__version__ = "([^"]+)"', open("snmp_browser.py", encoding="utf-8").read(), re.M).group(1)

datas, binaries, hiddenimports = [], [], []
for pkg in ("pysnmp", "pysmi"):
    d, b, h = collect_all(pkg)
    datas += d
    binaries += b
    hiddenimports += h

# MIB incluse nel pacchetto (settings.json escluso di proposito: contiene host e credenziali)
datas += [
    ("data/mibs", "data/mibs"),
    ("data/mibs_stubs", "data/mibs_stubs"),
    ("data/compiled/*.py", "data/compiled"),
]

a = Analysis(
    ["snmp_browser.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SNMPBrowser",
    console=False,
    upx=False,
    argv_emulation=False,
    target_arch=None,  # su Mac: "universal2" richiede un Python universal2
)

coll = COLLECT(exe, a.binaries, a.datas, name="SNMPBrowser", upx=False)

if sys.platform == "darwin":
    app = BUNDLE(
        coll,
        name="SNMPBrowser.app",
        bundle_identifier="com.olix.snmpbrowser",
        info_plist={
            "CFBundleDisplayName": "SNMP MIB Browser",
            "CFBundleShortVersionString": VERSION,
            "CFBundleVersion": VERSION,
            "NSHighResolutionCapable": True,
        },
    )
