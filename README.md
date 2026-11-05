# SNMP MIB Browser

MIB browser con interfaccia grafica (Tkinter) che supporta SNMP **v1, v2c e v3**.

## Avvio

```
pip install -r requirements.txt
python snmp_browser.py
```
oppure doppio clic su `run.bat` (installa le dipendenze se mancano).

## Funzioni

- **SNMPv3 (USM)**: noAuthNoPriv / authNoPriv / authPriv
  - autenticazione: MD5, SHA, SHA-224, SHA-256, SHA-384, SHA-512
  - privacy: DES, 3DES, AES-128, AES-192, AES-256, AES-192/256 "Cisco" (Blumenthal)
  - context name, context engine ID, security engine ID (opzionali: di norma scoperta automatica)
- Operazioni: Get, GetNext, GetBulk, Walk (con GetBulk su v2c/v3), Set, vista Tabella
- Albero MIB con descrizione, sintassi, valori enumerati, accesso, indici; oggetti scrivibili in grassetto
- Valori formattati secondo la MIB (enum `up(1)`, MAC address, TimeTicks, OID risolti in nomi)
- Caricamento di file MIB (`File → Carica file MIB…`) o per nome; le dipendenze mancanti
  vengono scaricate da mibs.pysnmp.com (disattivabile da Opzioni)
- Esportazione dei risultati in CSV, copia negli appunti, ricerca nell'albero

Il campo OID accetta OID numerici (`1.3.6.1.2.1.1.1.0`), nomi (`sysDescr.0`) o nomi qualificati
(`IF-MIB::ifDescr.2`). Il Get su un nodo scalare aggiunge automaticamente `.0`.

## Ricezione trap

`Trap → Ricevitore trap…` (Ctrl+T) riceve trap **v1, v2c, v3** e **inform v2c/v3** (con risposta automatica).

- Porta predefinita 162 (configurabile); se è occupata, di solito è il servizio Windows "SNMP Trap".
- Community accettate separate da virgola; campo vuoto = qualsiasi.
- Utenti v3 (`Utenti v3…`): lasciando vuoto l'engine ID del mittente, l'utente vale per qualsiasi
  dispositivo e l'engine ID viene appreso dal primo pacchetto ricevuto. Per gli inform v3 il dispositivo
  usa l'engine ID del ricevitore, mostrato nella finestra (resta uguale tra i riavvii).
- Le trap scartate compaiono in rosso con il motivo (community errata, utente sconosciuto,
  password auth/priv errate, …).
- Trap e variabili sono decodificate con le MIB caricate; esportazione CSV; opzione di avvio automatico.
- Chiudere la finestra non ferma la ricezione: le nuove trap vengono segnalate nella barra di stato.

`python test_trap_sender.py [host] [porta]` invia trap/inform di prova di tutte le versioni
(utente v3 `trapuser`, SHA/AES-128, password `authkey1`/`privkey1`).

## MIB non conformi

All'importazione di un file MIB ne viene creata una copia corretta, perché il compilatore
richiede le regole SMI che molte MIB in uso non rispettano. Gli OID non cambiano, quindi la MIB resta
valida per i dispositivi che usano l'originale (che non viene modificato):
- oggetti, nodi, notifiche ed etichette enum con l'iniziale minuscola (`UPSStatus` → `upsStatus`)
- tipi e TEXTUAL-CONVENTION con l'iniziale maiuscola (`myString` → `MyString`)
- parole chiave nella forma canonica (`Read-Only`, `Current`, `integer32`, `Sequence Of`)
- riferimenti e IMPORTS scritti con capitalizzazione diversa dal simbolo/modulo reale
- `_` nei nomi sostituito da `-`

Le correzioni vengono mostrate dopo il caricamento ed elencate in testa al file in `data/mibs/`.
Sono supportate anche le MIB SMIv1 (`FROM RFC-1212` / `RFC-1215`, `TRAP-TYPE`).

## Dati

Tutto viene salvato in `data/` accanto al programma:
- `data/mibs/` file MIB sorgenti importati (versione corretta)
- `data/mibs_original/` copia dei file originali
- `data/mibs_cache/` MIB scaricate da mibs.pysnmp.com (per compilare anche offline)
- `data/compiled/` MIB compilate (cache)
- `data/settings.json` ultima configurazione (le password v3 solo se abilitato in Opzioni)

Con l'eseguibile la cartella dati è:
- Windows: `data\` accanto a `SNMPBrowser.exe`
- macOS: `~/Library/Application Support/SNMPBrowser/`

## Eseguibile

Va creato sul sistema di destinazione (niente cross-compilazione):
- **Windows**: `build_windows.bat` → `dist\SNMPBrowser\SNMPBrowser.exe` (distribuire tutta la cartella)
- **macOS**: `chmod +x build_mac.sh && ./build_mac.sh` → `dist/SNMPBrowser.app`
  (serve Python da python.org, oppure Homebrew + `brew install python-tk`).
  App non firmata: al primo avvio tasto destro → Apri, oppure
  `xattr -dr com.apple.quarantine SNMPBrowser.app`.
- **GitHub Actions** (`.github/workflows/build.yml`): a ogni push su `main` crea gli zip per
  Windows, macOS Apple Silicon e macOS Intel (scheda *Actions* → run → *Artifacts*).
  Con un tag `v*` (es. `git tag v1.0.0 && git push --tags`) li allega anche a una Release.

## Agent di test

`python test_agent.py` avvia un agent locale su `127.0.0.1:1161` con community `public`/`private`
e diversi utenti v3 (password `authkey1` / `privkey1`): vedi l'intestazione del file.
