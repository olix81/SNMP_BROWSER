#!/usr/bin/env bash
# Crea dist/SNMPBrowser.app su macOS.
# Uso:  chmod +x build_mac.sh && ./build_mac.sh
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
"$PY" -c "import tkinter" 2>/dev/null || {
    echo "tkinter non disponibile: installa Python da python.org oppure 'brew install python-tk'"; exit 1; }

[ -d venv ] || "$PY" -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt pyinstaller

python -m PyInstaller --noconfirm --clean SNMPBrowser.spec

# rimuove la quarantena così l'app si apre senza l'avviso di Gatekeeper su questo Mac
xattr -dr com.apple.quarantine dist/SNMPBrowser.app 2>/dev/null || true

echo
echo "Fatto: dist/SNMPBrowser.app  (dati utente in ~/Library/Application Support/SNMPBrowser)"
