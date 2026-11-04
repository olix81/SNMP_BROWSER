@echo off
cd /d "%~dp0"
python -c "import pysnmp, pysmi, cryptography" 2>nul || python -m pip install -r requirements.txt
start "" pythonw snmp_browser.py
