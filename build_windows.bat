@echo off
rem Crea dist\SNMPBrowser\SNMPBrowser.exe su Windows.
cd /d "%~dp0"
python -m pip install -r requirements.txt pyinstaller || exit /b 1
python -m PyInstaller --noconfirm --clean SNMPBrowser.spec || exit /b 1
echo.
echo Fatto: dist\SNMPBrowser\SNMPBrowser.exe  (distribuire tutta la cartella dist\SNMPBrowser)
