"""SNMP MIB Browser con supporto SNMP v1 / v2c / v3.

Avvio:  python snmp_browser.py
"""

import csv
import json
import queue
import sys
import threading
import time
import tkinter as tk
from dataclasses import fields
from pathlib import Path
from tkinter import ttk, filedialog, messagebox, simpledialog

from snmp_core import (AgentConfig, SnmpClient, Cancelled, VERSIONS, SECURITY_LEVELS,
                       AUTH_PROTOCOLS, PRIV_PROTOCOLS)
from mib_store import MibStore, DEFAULT_MIBS, oid_str
from trap_receiver import TrapReceiver, TrapUser, ReceiverConfig, new_engine_id

APP_NAME = "SNMP MIB Browser"
__version__ = "1.0.0"  # unica fonte della versione (letta anche da SNMPBrowser.spec)
FROZEN = getattr(sys, "frozen", False)  # True quando gira come eseguibile PyInstaller


def _data_dir() -> Path:
    if not FROZEN:
        return Path(__file__).resolve().parent / "data"
    if sys.platform == "darwin":
        # dentro il bundle .app non si deve scrivere
        return Path.home() / "Library" / "Application Support" / "SNMPBrowser"
    if sys.platform == "win32":
        return Path(sys.executable).resolve().parent / "data"  # versione "portable"
    return Path.home() / ".local" / "share" / "SNMPBrowser"


def _seed_data_dir(dest: Path):
    """Al primo avvio dell'eseguibile copia le MIB incluse nel pacchetto nella cartella dati."""
    if not FROZEN:
        return
    import shutil
    bundled = Path(getattr(sys, "_MEIPASS", Path(sys.executable).parent)) / "data"
    if not bundled.is_dir() or bundled.resolve() == dest.resolve():
        return
    for src in bundled.rglob("*"):
        if src.is_file():
            target = dest / src.relative_to(bundled)
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, target)


DATA_DIR = _data_dir()
_seed_data_dir(DATA_DIR)
SETTINGS_FILE = DATA_DIR / "settings.json"

TREE_COLORS = {
    "scalar": "#0b5cad", "column": "#127a3a", "table": "#b35900", "row": "#b35900",
    "notification": "#8a2be2", "group": "#777777", "module": "#777777", "virtual": "#888888",
}


def load_settings():
    try:
        return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_settings(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    SETTINGS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def one_line(text):
    return text.replace("\r\n", "\n").replace("\n", " ↵ ")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.settings = load_settings()
        self.geometry(self.settings.get("geometry", "1280x800"))
        self.minsize(900, 560)

        self.client = SnmpClient()
        self.mibs = MibStore(DATA_DIR, use_remote=self.settings.get("remote_mibs", True))
        self.ui_queue = queue.Queue()
        self.busy = False
        self.stop_event = None
        self.result_rows = []  # (nome, oid, valore, tipo)
        self.tree_order = []   # iid in ordine di visualizzazione, per la ricerca
        self._suppress_oid_update = False
        self._modules_refresh = None

        self.v_remote = tk.BooleanVar(value=self.settings.get("remote_mibs", True))
        self.v_use_bulk = tk.BooleanVar(value=self.settings.get("walk_bulk", True))
        self.v_save_secrets = tk.BooleanVar(value=self.settings.get("save_secrets", False))
        self.v_clear = tk.BooleanVar(value=self.settings.get("clear_results", True))

        self._build_menu()
        self._build_agent_panel()
        self._build_ops_bar()
        self._build_main()
        self._build_status()
        self._apply_config(AgentConfig.from_dict(self.settings.get("agent")))
        self.v_oid.set(self.settings.get("last_oid", "1.3.6.1.2.1.1"))

        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.after(40, self._poll_queue)
        self.load_mibs_async(self.settings.get("mibs") or list(DEFAULT_MIBS), initial=True)
        self.trap_window = None
        if self.settings.get("trap_receiver", {}).get("autostart"):
            self.after(300, lambda: self.show_traps(start=True, focus=False))

    # ================================================================ UI

    def _build_menu(self):
        m = tk.Menu(self)
        f = tk.Menu(m, tearoff=False)
        f.add_command(label="Carica file MIB…", command=self.load_mib_files, accelerator="Ctrl+O")
        f.add_command(label="Carica MIB per nome…", command=self.load_mib_by_name)
        f.add_command(label="Moduli caricati…", command=self.show_modules)
        f.add_separator()
        f.add_command(label="Esporta risultati CSV…", command=self.export_csv, accelerator="Ctrl+S")
        f.add_separator()
        f.add_command(label="Esci", command=self._on_close)
        m.add_cascade(label="File", menu=f)

        o = tk.Menu(m, tearoff=False)
        o.add_checkbutton(label="Scarica le MIB mancanti da mibs.pysnmp.com (al riavvio)", variable=self.v_remote)
        o.add_checkbutton(label="Usa GetBulk per il Walk (v2c/v3)", variable=self.v_use_bulk)
        o.add_checkbutton(label="Pulisci i risultati a ogni operazione", variable=self.v_clear)
        o.add_checkbutton(label="Ricorda le password v3 (salvate in chiaro)", variable=self.v_save_secrets)
        m.add_cascade(label="Opzioni", menu=o)

        t = tk.Menu(m, tearoff=False)
        t.add_command(label="Ricevitore trap…", command=self.show_traps, accelerator="Ctrl+T")
        m.add_cascade(label="Trap", menu=t)

        h = tk.Menu(m, tearoff=False)
        h.add_command(label="Informazioni", command=self.show_about)
        m.add_cascade(label="Aiuto", menu=h)
        self.config(menu=m)
        self.bind("<Control-o>", lambda e: self.load_mib_files())
        self.bind("<Control-s>", lambda e: self.export_csv())
        self.bind("<Control-t>", lambda e: self.show_traps())

    def _build_agent_panel(self):
        self.vars = {f.name: tk.StringVar() for f in fields(AgentConfig)}
        v = self.vars
        box = ttk.LabelFrame(self, text="Agent", padding=(8, 4))
        box.pack(fill="x", padx=6, pady=(6, 2))

        r0 = ttk.Frame(box)
        r0.pack(fill="x")
        ttk.Label(r0, text="Host:").pack(side="left")
        self.host_combo = ttk.Combobox(r0, textvariable=v["host"], width=24,
                                       values=self.settings.get("host_history", []))
        self.host_combo.pack(side="left", padx=(2, 10))
        for label, key, w in (("Porta:", "port", 6), ("Timeout (s):", "timeout", 5),
                              ("Tentativi:", "retries", 4), ("Max-repetitions:", "max_repetitions", 5)):
            ttk.Label(r0, text=label).pack(side="left")
            ttk.Entry(r0, textvariable=v[key], width=w).pack(side="left", padx=(2, 10))
        ttk.Label(r0, text="Versione:").pack(side="left")
        cb = ttk.Combobox(r0, textvariable=v["version"], values=VERSIONS, state="readonly", width=5)
        cb.pack(side="left", padx=2)
        cb.bind("<<ComboboxSelected>>", lambda e: self._update_version_panel())

        # v1/v2c
        self.comm_frame = ttk.Frame(box)
        ttk.Label(self.comm_frame, text="Community lettura:").pack(side="left")
        ttk.Entry(self.comm_frame, textvariable=v["read_community"], width=18).pack(side="left", padx=(2, 10))
        ttk.Label(self.comm_frame, text="Community scrittura:").pack(side="left")
        ttk.Entry(self.comm_frame, textvariable=v["write_community"], width=18).pack(side="left", padx=2)

        # v3
        self.v3_frame = ttk.Frame(box)
        g = self.v3_frame
        self.v_show_pw = tk.BooleanVar(value=False)
        ttk.Label(g, text="Utente:").grid(row=0, column=0, sticky="e")
        ttk.Entry(g, textvariable=v["user"], width=18).grid(row=0, column=1, sticky="w", padx=(2, 10))
        ttk.Label(g, text="Livello:").grid(row=0, column=2, sticky="e")
        lvl = ttk.Combobox(g, textvariable=v["security_level"], values=SECURITY_LEVELS, state="readonly", width=13)
        lvl.grid(row=0, column=3, sticky="w", padx=(2, 10))
        lvl.bind("<<ComboboxSelected>>", lambda e: self._update_v3_state())
        ttk.Label(g, text="Context name:").grid(row=0, column=4, sticky="e")
        ttk.Entry(g, textvariable=v["context_name"], width=16).grid(row=0, column=5, sticky="w", padx=(2, 10))
        ttk.Label(g, text="Context engine ID (hex):").grid(row=0, column=6, sticky="e")
        ttk.Entry(g, textvariable=v["context_engine_id"], width=24).grid(row=0, column=7, sticky="w", padx=2)

        ttk.Label(g, text="Autenticazione:").grid(row=1, column=0, sticky="e", pady=(3, 0))
        self.auth_proto = ttk.Combobox(g, textvariable=v["auth_protocol"], values=list(AUTH_PROTOCOLS),
                                       state="readonly", width=10)
        self.auth_proto.grid(row=1, column=1, sticky="w", padx=(2, 10), pady=(3, 0))
        ttk.Label(g, text="Password auth:").grid(row=1, column=2, sticky="e", pady=(3, 0))
        self.auth_pw = ttk.Entry(g, textvariable=v["auth_password"], width=16, show="•")
        self.auth_pw.grid(row=1, column=3, sticky="w", padx=(2, 10), pady=(3, 0))
        ttk.Label(g, text="Privacy:").grid(row=1, column=4, sticky="e", pady=(3, 0))
        self.priv_proto = ttk.Combobox(g, textvariable=v["priv_protocol"], values=list(PRIV_PROTOCOLS),
                                       state="readonly", width=14)
        self.priv_proto.grid(row=1, column=5, sticky="w", padx=(2, 10), pady=(3, 0))
        ttk.Label(g, text="Password priv:").grid(row=1, column=6, sticky="e", pady=(3, 0))
        self.priv_pw = ttk.Entry(g, textvariable=v["priv_password"], width=16, show="•")
        self.priv_pw.grid(row=1, column=7, sticky="w", padx=2, pady=(3, 0))
        ttk.Checkbutton(g, text="Mostra", variable=self.v_show_pw,
                        command=self._toggle_pw).grid(row=1, column=8, sticky="w", padx=4, pady=(3, 0))
        ttk.Label(g, text="Security engine ID (hex, opz.):").grid(row=2, column=6, sticky="e", pady=(3, 0))
        ttk.Entry(g, textvariable=v["security_engine_id"], width=24).grid(row=2, column=7, sticky="w", padx=2,
                                                                         pady=(3, 0))
        ttk.Label(g, text="Lasciare vuoti gli engine ID per la scoperta automatica.",
                  foreground="#777").grid(row=2, column=0, columnspan=6, sticky="w", pady=(3, 0))

    def _build_ops_bar(self):
        bar = ttk.Frame(self, padding=(6, 4))
        bar.pack(fill="x")
        ttk.Label(bar, text="OID:").pack(side="left")
        self.v_oid = tk.StringVar()
        e = ttk.Entry(bar, textvariable=self.v_oid, width=46)
        e.pack(side="left", padx=(2, 8), fill="x", expand=True)
        e.bind("<Return>", lambda ev: self.do_get())
        self.op_buttons = []
        for text, cmd in (("Get", self.do_get), ("GetNext", self.do_get_next), ("GetBulk", self.do_get_bulk),
                          ("Walk", self.do_walk), ("Set…", self.do_set), ("Tabella", self.do_table)):
            b = ttk.Button(bar, text=text, command=cmd, width=9)
            b.pack(side="left", padx=1)
            self.op_buttons.append(b)
        self.stop_btn = ttk.Button(bar, text="Stop", command=self.do_stop, width=7, state="disabled")
        self.stop_btn.pack(side="left", padx=(8, 1))
        ttk.Button(bar, text="Pulisci", command=self.clear_results, width=8).pack(side="left", padx=1)

    def _build_main(self):
        pw = ttk.PanedWindow(self, orient="horizontal")
        pw.pack(fill="both", expand=True, padx=6, pady=2)

        # --- albero MIB
        left = ttk.Frame(pw)
        sf = ttk.Frame(left)
        sf.pack(fill="x", pady=(0, 3))
        self.v_search = tk.StringVar()
        se = ttk.Entry(sf, textvariable=self.v_search)
        se.pack(side="left", fill="x", expand=True)
        se.bind("<Return>", lambda e: self.find_next())
        ttk.Button(sf, text="Trova", command=self.find_next, width=7).pack(side="left", padx=(3, 0))
        tf = ttk.Frame(left)
        tf.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(tf, show="tree", selectmode="browse")
        ys = ttk.Scrollbar(tf, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=ys.set)
        self.tree.pack(side="left", fill="both", expand=True)
        ys.pack(side="right", fill="y")
        self.tree.column("#0", width=320)
        for kind, color in TREE_COLORS.items():
            self.tree.tag_configure(kind, foreground=color)
        self.tree.tag_configure("writable", font=("Segoe UI", 9, "bold"))
        self.tree.bind("<<TreeviewSelect>>", self._on_tree_select)
        self.tree.bind("<Double-1>", self._on_tree_double)
        self.tree.bind("<Button-3>", self._on_tree_menu)
        pw.add(left, weight=1)

        # --- risultati + dettagli
        right = ttk.PanedWindow(pw, orient="vertical")
        rf = ttk.Frame(right)
        cols = ("name", "oid", "value", "type")
        self.results = ttk.Treeview(rf, columns=cols, show="headings", selectmode="extended")
        for c, t, w in zip(cols, ("Nome", "OID", "Valore", "Tipo"), (230, 190, 380, 140)):
            self.results.heading(c, text=t)
            self.results.column(c, width=w, stretch=(c == "value"))
        rys = ttk.Scrollbar(rf, orient="vertical", command=self.results.yview)
        rxs = ttk.Scrollbar(rf, orient="horizontal", command=self.results.xview)
        self.results.configure(yscrollcommand=rys.set, xscrollcommand=rxs.set)
        self.results.grid(row=0, column=0, sticky="nsew")
        rys.grid(row=0, column=1, sticky="ns")
        rxs.grid(row=1, column=0, sticky="ew")
        rf.rowconfigure(0, weight=1)
        rf.columnconfigure(0, weight=1)
        self.results.tag_configure("error", foreground="#b00020")
        self.results.bind("<Double-1>", self._on_result_double)
        self.results.bind("<Button-3>", self._on_result_menu)
        self.results.bind("<Control-c>", lambda e: self._copy_results("row"))
        right.add(rf, weight=3)

        df = ttk.LabelFrame(right, text="Dettagli", padding=4)
        self.details = tk.Text(df, height=9, wrap="word", relief="flat", font=("Segoe UI", 9),
                               background=self.cget("background"))
        dys = ttk.Scrollbar(df, orient="vertical", command=self.details.yview)
        self.details.configure(yscrollcommand=dys.set, state="disabled")
        self.details.tag_configure("key", font=("Segoe UI", 9, "bold"))
        self.details.pack(side="left", fill="both", expand=True)
        dys.pack(side="right", fill="y")
        right.add(df, weight=1)
        pw.add(right, weight=3)

    def _build_status(self):
        sb = ttk.Frame(self, padding=(6, 2))
        sb.pack(fill="x", side="bottom")
        self.v_status = tk.StringVar(value="Pronto")
        ttk.Label(sb, textvariable=self.v_status, anchor="w").pack(side="left", fill="x", expand=True)
        self.progress = ttk.Progressbar(sb, mode="indeterminate", length=140)
        self.progress.pack(side="right")

    # ============================================================ config

    def _apply_config(self, cfg):
        for f in fields(AgentConfig):
            self.vars[f.name].set(str(getattr(cfg, f.name)))
        self._update_version_panel()

    def read_config(self):
        kw = {}
        for f in fields(AgentConfig):
            raw = self.vars[f.name].get().strip() if "password" not in f.name else self.vars[f.name].get()
            default = getattr(AgentConfig, f.name)
            try:
                kw[f.name] = type(default)(raw) if not isinstance(default, str) else raw
            except ValueError:
                raise ValueError(f"Valore non valido per '{f.name}': {raw!r}") from None
        cfg = AgentConfig(**kw)
        if not cfg.host:
            raise ValueError("Specificare l'host dell'agent")
        return cfg

    def _update_version_panel(self):
        if self.vars["version"].get() == "v3":
            self.comm_frame.pack_forget()
            self.v3_frame.pack(fill="x", pady=(4, 0))
        else:
            self.v3_frame.pack_forget()
            self.comm_frame.pack(fill="x", pady=(4, 0))
        self._update_v3_state()

    def _update_v3_state(self):
        lvl = self.vars["security_level"].get()
        auth = "normal" if lvl in ("authNoPriv", "authPriv") else "disabled"
        priv = "normal" if lvl == "authPriv" else "disabled"
        self.auth_proto.configure(state="readonly" if auth == "normal" else "disabled")
        self.auth_pw.configure(state=auth)
        self.priv_proto.configure(state="readonly" if priv == "normal" else "disabled")
        self.priv_pw.configure(state=priv)

    def _toggle_pw(self):
        show = "" if self.v_show_pw.get() else "•"
        self.auth_pw.configure(show=show)
        self.priv_pw.configure(show=show)

    def _remember_host(self, host):
        hist = [h for h in self.settings.get("host_history", []) if h != host]
        hist.insert(0, host)
        self.settings["host_history"] = hist[:15]
        self.host_combo.configure(values=self.settings["host_history"])

    # ========================================================= threading

    def call_soon(self, fn, *args):
        """Esegue fn nel thread della GUI (chiamabile da qualunque thread)."""
        self.ui_queue.put((fn, args))

    def _poll_queue(self):
        try:
            for _ in range(500):
                fn, args = self.ui_queue.get_nowait()
                try:
                    fn(*args)
                except Exception as exc:
                    self._status(f"Errore interno: {exc}")
        except queue.Empty:
            pass
        self.after(40, self._poll_queue)

    def _status(self, text):
        self.v_status.set(text)

    def _set_busy(self, text, stoppable=False):
        self.busy = True
        self._status(text)
        self.progress.start(12)
        self.stop_btn.configure(state="normal" if stoppable else "disabled")

    def _set_idle(self):
        self.busy = False
        self.progress.stop()
        self.stop_btn.configure(state="disabled")

    def _run(self, title, future, on_done):
        start = time.perf_counter()

        def done(f):
            try:
                res = f.result()
            except Cancelled:
                self.call_soon(self._status, f"{title}: interrotto dall'utente")
            except Exception as exc:
                self.call_soon(self._op_error, title, exc)
            else:
                self.call_soon(on_done, res, time.perf_counter() - start)
            finally:
                self.call_soon(self._set_idle)

        future.add_done_callback(done)

    def _op_error(self, title, exc):
        msg = str(exc) or exc.__class__.__name__
        self._status(f"{title}: errore — {one_line(msg)}")
        self._add_result_row(title, "", f"Errore: {one_line(msg)}", "", error=True)
        messagebox.showerror(title, msg, parent=self)

    # ========================================================= MIB

    def load_mibs_async(self, names, initial=False):
        self._set_busy(f"Caricamento MIB: {', '.join(names)}… (la prima volta può richiedere tempo)")

        def work():
            ok, errors = self.mibs.load(names)
            self.call_soon(self._mibs_loaded, ok, errors, initial)

        threading.Thread(target=work, daemon=True).start()

    def _mibs_loaded(self, ok, errors, initial):
        self._set_idle()
        self.rebuild_tree()
        if self._modules_refresh is not None:
            self._modules_refresh()
        self._status(f"MIB caricate: {len(self.mibs.loaded)} moduli, {len(self.mibs.nodes())} nodi"
                     + (f" — {len(errors)} errori" if errors else ""))
        if errors:
            text = "\n\n".join(f"{name}:\n{msg[:600]}" for name, msg in errors.items())
            messagebox.showwarning("Errori di caricamento MIB",
                                   f"Alcuni moduli non sono stati caricati:\n\n{text}", parent=self)
        if initial:
            self._select_oid(self.v_oid.get(), quiet=True)

    def load_mib_files(self):
        paths = filedialog.askopenfilenames(
            parent=self, title="Carica file MIB",
            filetypes=[("File MIB", "*.mib *.my *.txt *.smi *.mi2 *.asn *.asn1"), ("Tutti i file", "*.*")])
        if not paths:
            return
        modules, errors, fixes = [], [], []
        for p in paths:
            try:
                module, changes = self.mibs.import_file(p)
            except Exception as exc:
                errors.append(str(exc))
                continue
            modules.append(module)
            if changes:
                lines = [f"  riga {ln}: {old} → {new}" for ln, old, new in changes]
                if len(lines) > 25:
                    lines = lines[:25] + [f"  … e altre {len(lines) - 25}"]
                fixes.append(f"{module} ({Path(p).name}):\n" + "\n".join(lines))
        if errors:
            messagebox.showerror("Carica file MIB", "\n".join(errors), parent=self)
        if fixes:
            messagebox.showinfo(
                "MIB corrette",
                "Alcuni nomi non rispettano le regole SMI (maiuscole/minuscole, '_') e sono stati "
                "corretti in una copia della MIB. Gli OID non cambiano; il file originale non è "
                "stato modificato.\n\n" + "\n\n".join(fixes), parent=self)
        if modules:
            self.load_mibs_async(modules)

    def load_mib_by_name(self):
        name = simpledialog.askstring(
            "Carica MIB per nome",
            "Nomi dei moduli (separati da spazio o virgola), es.:\nCISCO-SMI  BRIDGE-MIB  LLDP-MIB\n\n"
            "Vengono cercati nella cartella data/mibs e, se abilitato, su mibs.pysnmp.com.",
            parent=self)
        if name:
            names = [n for n in name.replace(",", " ").split() if n]
            if names:
                self.load_mibs_async(names)

    def show_modules(self):
        win = tk.Toplevel(self)
        win.title("Moduli MIB caricati")
        win.geometry("420x420")
        win.transient(self)
        ttk.Label(win, text="Moduli richiesti (ricaricati all'avvio):", padding=6).pack(anchor="w")
        lb = tk.Listbox(win, selectmode="extended")
        lb.pack(fill="both", expand=True, padx=6)

        def refresh():
            lb.delete(0, "end")
            for m in sorted(self.mibs.loaded):
                lb.insert("end", m)

        def remove():
            for i in lb.curselection():
                self.mibs.unload(lb.get(i))
            refresh()
            self.rebuild_tree()

        refresh()
        self._modules_refresh = refresh
        win.bind("<Destroy>", lambda e: setattr(self, "_modules_refresh", None) if e.widget is win else None)
        bf = ttk.Frame(win, padding=6)
        bf.pack(fill="x")
        ttk.Button(bf, text="Aggiungi file…", command=self.load_mib_files).pack(side="left")
        ttk.Button(bf, text="Aggiungi per nome…", command=self.load_mib_by_name).pack(side="left", padx=4)
        ttk.Button(bf, text="Rimuovi", command=remove).pack(side="left")
        ttk.Button(bf, text="Chiudi", command=win.destroy).pack(side="right")
        ttk.Label(win, text=f"Cartella sorgenti MIB: {self.mibs.src_dir}", foreground="#777",
                  padding=(6, 0, 6, 6), wraplength=400).pack(anchor="w")

    def rebuild_tree(self):
        sel = self.tree.selection()
        open_items = {iid for iid in self.tree_order if self.tree.item(iid, "open")} if self.tree_order else None
        self.tree.delete(*self.tree.get_children())
        nodes = self.mibs.nodes()
        self.tree_order = []
        for oid in sorted(nodes):
            n = nodes[oid]
            iid = oid_str(oid)
            parent = oid_str(oid[:-1]) if len(oid) > 1 else ""
            tags = [n.kind]
            if n.kind in ("scalar", "column") and n.obj is not None:
                try:
                    if str(n.obj.getMaxAccess()) in ("read-write", "read-create"):
                        tags.append("writable")
                except Exception:
                    pass
            self.tree.insert(parent, "end", iid=iid, text=n.label, tags=tags)
            self.tree_order.append(iid)
        if open_items is None:
            open_items = {"1", "1.3", "1.3.6", "1.3.6.1", "1.3.6.1.2", "1.3.6.1.2.1", "1.3.6.1.4", "1.3.6.1.6"}
        for iid in open_items:
            if self.tree.exists(iid):
                self.tree.item(iid, open=True)
        if sel and self.tree.exists(sel[0]):
            self.tree.selection_set(sel[0])
            self.tree.see(sel[0])

    def _select_oid(self, text, quiet=False):
        try:
            oid = self.mibs.resolve(text)
        except ValueError:
            return
        node, _ = self.mibs.best_node(oid)
        if node is not None and self.tree.exists(oid_str(node.oid)):
            iid = oid_str(node.oid)
            if self.tree.selection() == (iid,):  # nessun evento di selezione verrebbe generato
                self.tree.see(iid)
                return
            self._suppress_oid_update = quiet
            self.tree.selection_set(iid)
            self.tree.see(iid)

    def find_next(self):
        text = self.v_search.get().strip().lower()
        if not text or not self.tree_order:
            return
        sel = self.tree.selection()
        start = self.tree_order.index(sel[0]) + 1 if sel and sel[0] in self.tree_order else 0
        n = len(self.tree_order)
        for k in range(n):
            iid = self.tree_order[(start + k) % n]
            if text in self.tree.item(iid, "text").lower() or text == iid:
                self.tree.selection_set(iid)
                self.tree.see(iid)
                return
        self._status(f"'{text}' non trovato")

    def _on_tree_select(self, _event=None):
        sel = self.tree.selection()
        if not sel:
            return
        oid = tuple(int(x) for x in sel[0].split("."))
        if not getattr(self, "_suppress_oid_update", False):
            self.v_oid.set(sel[0])
        self._suppress_oid_update = False
        self.show_details(self.mibs.describe(oid))

    def _on_tree_double(self, event):
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        node = self.mibs.node(tuple(int(x) for x in iid.split(".")))
        if node is None:
            return
        if node.kind == "scalar":
            self.do_get()
            return "break"
        if node.kind in ("table", "row"):
            self.do_table()
            return "break"
        if node.kind == "column":
            self.do_walk()
            return "break"

    def _on_tree_menu(self, event):
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        self.tree.selection_set(iid)
        m = tk.Menu(self, tearoff=False)
        m.add_command(label="Get", command=self.do_get)
        m.add_command(label="GetNext", command=self.do_get_next)
        m.add_command(label="Walk", command=self.do_walk)
        m.add_command(label="Set…", command=self.do_set)
        m.add_command(label="Vista tabella", command=self.do_table)
        m.add_separator()
        m.add_command(label="Copia OID", command=lambda: self._clip(iid))
        m.add_command(label="Copia nome", command=lambda: self._clip(self.mibs.name_of(
            tuple(int(x) for x in iid.split(".")))))
        m.tk_popup(event.x_root, event.y_root)

    def show_details(self, items):
        t = self.details
        t.configure(state="normal")
        t.delete("1.0", "end")
        for k, v in items:
            t.insert("end", f"{k}: ", "key")
            t.insert("end", f"{v}\n")
        t.configure(state="disabled")

    # ========================================================= risultati

    def clear_results(self):
        self.results.delete(*self.results.get_children())
        self.result_rows.clear()

    def _add_result_row(self, name, oid, value, type_name, error=False):
        self.result_rows.append((name, oid, value, type_name))
        iid = self.results.insert("", "end", values=(name, oid, one_line(value), type_name),
                                  tags=("error",) if error else ())
        return iid

    def _add_varbinds(self, rows):
        last = None
        for oid, value in rows:
            text, type_name = self.mibs.format_value(oid, value)
            last = self._add_result_row(self.mibs.name_of(oid), oid_str(oid), text, type_name)
        if last:
            self.results.see(last)

    def _selected_result(self):
        sel = self.results.selection()
        if not sel:
            return None
        idx = self.results.index(sel[0])
        return self.result_rows[idx] if idx < len(self.result_rows) else None

    def _on_result_double(self, event):
        if not self.results.identify_row(event.y):
            return
        row = self._selected_result()
        if not row or not row[1]:
            return
        self._select_oid(row[1], quiet=True)
        oid = tuple(int(x) for x in row[1].split("."))
        node, suffix = self.mibs.best_node(oid)
        info = [("Istanza", row[0]), ("OID", row[1]), ("Valore", row[2]), ("Tipo", row[3])]
        if node is not None:
            info += [i for i in self.mibs.describe(node.oid) if i[0] not in ("OID",)]
        self.show_details(info)

    def _on_result_menu(self, event):
        iid = self.results.identify_row(event.y)
        if not iid:
            return
        if iid not in self.results.selection():
            self.results.selection_set(iid)
        m = tk.Menu(self, tearoff=False)
        m.add_command(label="Copia valore", command=lambda: self._copy_results("value"))
        m.add_command(label="Copia OID", command=lambda: self._copy_results("oid"))
        m.add_command(label="Copia riga", command=lambda: self._copy_results("row"))
        m.add_separator()
        m.add_command(label="Set su questo OID…", command=self._set_from_result)
        m.add_command(label="Get di nuovo", command=self._get_from_result)
        m.tk_popup(event.x_root, event.y_root)

    def _copy_results(self, what):
        lines = []
        for iid in self.results.selection():
            idx = self.results.index(iid)
            name, oid, value, typ = self.result_rows[idx]
            lines.append({"value": value, "oid": oid}.get(what, f"{name}\t{oid}\t{value}\t{typ}"))
        if lines:
            self._clip("\n".join(lines))

    def _clip(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        self._status("Copiato negli appunti")

    def _set_from_result(self):
        row = self._selected_result()
        if row and row[1]:
            self.v_oid.set(row[1])
            self.do_set(initial_value=row[2])

    def _get_from_result(self):
        row = self._selected_result()
        if row and row[1]:
            self.v_oid.set(row[1])
            self.do_get()

    def export_csv(self):
        if not self.result_rows:
            messagebox.showinfo("Esporta", "Nessun risultato da esportare", parent=self)
            return
        path = filedialog.asksaveasfilename(parent=self, defaultextension=".csv",
                                            filetypes=[("CSV", "*.csv")], initialfile="snmp_risultati.csv")
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh, delimiter=";")
            w.writerow(["Nome", "OID", "Valore", "Tipo"])
            w.writerows(self.result_rows)
        self._status(f"Esportati {len(self.result_rows)} risultati in {path}")

    # ========================================================= operazioni

    def _prepare(self, title, for_get=False):
        if self.busy:
            self._status("Operazione in corso: attendere o premere Stop")
            return None
        try:
            cfg = self.read_config()
            text = self.v_oid.get().strip()
            if not text:
                raise ValueError("Specificare un OID")
            oid = self.mibs.resolve(text)
        except ValueError as exc:
            messagebox.showerror(title, str(exc), parent=self)
            return None
        if for_get:
            node = self.mibs.node(oid)
            if node is not None and node.kind == "scalar":
                oid = oid + (0,)
        self._remember_host(cfg.host)
        if self.v_clear.get():
            self.clear_results()
        return cfg, oid

    def _target_desc(self, cfg):
        sec = f"{cfg.user}/{cfg.security_level}" if cfg.version == "v3" else cfg.read_community
        return f"{cfg.host}:{cfg.port} {cfg.version} ({sec})"

    def do_get(self):
        p = self._prepare("Get", for_get=True)
        if not p:
            return
        cfg, oid = p
        self._set_busy(f"Get {oid_str(oid)} da {self._target_desc(cfg)}…")
        self._run("Get", self.client.get(cfg, [oid]),
                  lambda rows, dt: (self._add_varbinds(rows), self._status(f"Get completato in {dt * 1000:.0f} ms")))

    def do_get_next(self):
        p = self._prepare("GetNext")
        if not p:
            return
        cfg, oid = p

        def done(rows, dt):
            self._add_varbinds(rows)
            if rows:
                self.v_oid.set(oid_str(rows[0][0]))  # GetNext ripetuti avanzano nella MIB
            self._status(f"GetNext completato in {dt * 1000:.0f} ms")

        self._set_busy(f"GetNext {oid_str(oid)}…")
        self._run("GetNext", self.client.get_next(cfg, [oid]), done)

    def do_get_bulk(self):
        p = self._prepare("GetBulk")
        if not p:
            return
        cfg, oid = p
        self._set_busy(f"GetBulk {oid_str(oid)} (max-repetitions {cfg.max_repetitions})…")
        self._run("GetBulk", self.client.get_bulk(cfg, [oid], 0, cfg.max_repetitions),
                  lambda rows, dt: (self._add_varbinds(rows),
                                    self._status(f"GetBulk: {len(rows)} valori in {dt * 1000:.0f} ms")))

    def do_walk(self):
        p = self._prepare("Walk")
        if not p:
            return
        cfg, oid = p
        self.stop_event = threading.Event()
        counter = [0]

        def on_rows(rows):
            counter[0] += len(rows)
            self.call_soon(self._add_varbinds, rows)
            self.call_soon(self._status, f"Walk {oid_str(oid)}: {counter[0]} valori…")

        def done(total, dt):
            self._status(f"Walk completato: {total} valori in {dt:.2f} s")
            if total == 0:
                self._add_result_row("(nessun valore)", oid_str(oid), "Nessun oggetto sotto questo OID", "")

        self._set_busy(f"Walk {oid_str(oid)} su {self._target_desc(cfg)}…", stoppable=True)
        self._run("Walk", self.client.walk(cfg, oid, on_rows, self.stop_event, self.v_use_bulk.get()), done)

    def do_stop(self):
        if self.stop_event is not None:
            self.stop_event.set()

    def do_set(self, initial_value=None):
        p = self._prepare("Set", for_get=True)
        if not p:
            return
        cfg, oid = p
        SetDialog(self, cfg, oid, initial_value)

    def do_table(self):
        try:
            cfg = self.read_config()
            oid = self.mibs.resolve(self.v_oid.get())
        except ValueError as exc:
            messagebox.showerror("Tabella", str(exc), parent=self)
            return
        row_oid, columns = self.mibs.table_columns(oid)
        if row_oid is None:
            messagebox.showinfo("Tabella", "Selezionare un nodo tabella, riga o colonna di una tabella SNMP.",
                                parent=self)
            return
        self._remember_host(cfg.host)
        TableView(self, cfg, row_oid, columns)

    # ========================================================= varie

    def show_about(self):
        messagebox.showinfo(
            "Informazioni",
            f"{APP_NAME}\n\nSNMP v1 / v2c / v3 (USM: MD5, SHA, SHA-2; DES, 3DES, AES-128/192/256)\n"
            f"Basato su pysnmp e pysmi.\n\nCartella dati: {DATA_DIR}", parent=self)

    def show_traps(self, start=False, focus=True):
        if self.trap_window is None:
            self.trap_window = TrapWindow(self)
            if "SNMP-COMMUNITY-MIB" not in self.mibs.builder.mibSymbols:  # nomi dei campi delle trap v1
                self.load_mibs_async(["SNMP-COMMUNITY-MIB"])
        w = self.trap_window
        if focus:
            w.deiconify()
            w.lift()
        else:
            w.withdraw()
        if start and not w.receiver.running:
            w.start(quiet=not focus)

    def _on_close(self):
        if self.trap_window is not None:
            self.trap_window.save_settings()
            self.trap_window.receiver.stop()
        try:
            cfg = self.read_config()
            self.settings["agent"] = cfg.to_dict(include_secrets=self.v_save_secrets.get())
        except ValueError:
            pass
        self.settings.update({
            "geometry": self.geometry(), "mibs": self.mibs.loaded, "last_oid": self.v_oid.get(),
            "remote_mibs": self.v_remote.get(), "walk_bulk": self.v_use_bulk.get(),
            "save_secrets": self.v_save_secrets.get(), "clear_results": self.v_clear.get(),
        })
        try:
            save_settings(self.settings)
        except Exception:
            pass
        self.destroy()


class SetDialog(tk.Toplevel):
    def __init__(self, app: App, cfg, oid, initial_value=None):
        super().__init__(app)
        self.app, self.cfg, self.oid = app, cfg, oid
        self.title("SNMP Set")
        self.transient(app)
        self.resizable(True, False)
        node, _ = app.mibs.best_node(oid)
        frm = ttk.Frame(self, padding=10)
        frm.pack(fill="both", expand=True)
        frm.columnconfigure(1, weight=1)

        ttk.Label(frm, text="Oggetto:").grid(row=0, column=0, sticky="e", pady=2)
        ttk.Label(frm, text=app.mibs.name_of(oid)).grid(row=0, column=1, sticky="w", pady=2)
        ttk.Label(frm, text="OID:").grid(row=1, column=0, sticky="e", pady=2)
        self.v_oid = tk.StringVar(value=oid_str(oid))
        ttk.Entry(frm, textvariable=self.v_oid, width=50).grid(row=1, column=1, sticky="ew", pady=2)

        info = dict(app.mibs.describe(node.oid)) if node is not None else {}
        if info.get("Sintassi"):
            ttk.Label(frm, text="Sintassi MIB:").grid(row=2, column=0, sticky="e", pady=2)
            ttk.Label(frm, text=f"{info['Sintassi']}   accesso: {info.get('Accesso', '?')}",
                      foreground="#555").grid(row=2, column=1, sticky="w", pady=2)

        ttk.Label(frm, text="Tipo:").grid(row=3, column=0, sticky="e", pady=2)
        self.v_type = tk.StringVar(value=MibStore.SET_TYPES[0] if info.get("Sintassi") else "OCTET STRING")
        ttk.Combobox(frm, textvariable=self.v_type, values=MibStore.SET_TYPES, state="readonly",
                     width=22).grid(row=3, column=1, sticky="w", pady=2)

        ttk.Label(frm, text="Valore:").grid(row=4, column=0, sticky="e", pady=2)
        self.v_value = tk.StringVar(value=initial_value or "")
        enums = [v.strip() for v in info.get("Valori", "").split(",") if v.strip()]
        if enums:
            w = ttk.Combobox(frm, textvariable=self.v_value, values=enums, width=48)
        else:
            w = ttk.Entry(frm, textvariable=self.v_value, width=50)
        w.grid(row=4, column=1, sticky="ew", pady=2)
        w.focus_set()
        w.bind("<Return>", lambda e: self.send())
        ttk.Label(frm, text="Stringhe esadecimali: prefisso 0x (es. 0x0A1B2C). Community di scrittura per v1/v2c.",
                  foreground="#777").grid(row=5, column=0, columnspan=2, sticky="w", pady=(6, 0))

        bf = ttk.Frame(frm)
        bf.grid(row=6, column=0, columnspan=2, sticky="e", pady=(10, 0))
        ttk.Button(bf, text="Invia Set", command=self.send).pack(side="left", padx=4)
        ttk.Button(bf, text="Chiudi", command=self.destroy).pack(side="left")
        self.bind("<Escape>", lambda e: self.destroy())

    def send(self):
        app = self.app
        try:
            oid = app.mibs.resolve(self.v_oid.get())
            value = app.mibs.make_value(oid, self.v_type.get(), self.v_value.get())
        except Exception as exc:
            messagebox.showerror("Set", f"Valore non valido: {exc}", parent=self)
            return
        if app.busy:
            app._status("Operazione in corso: attendere")
            return
        app._set_busy(f"Set {oid_str(oid)}…")

        def done(rows, dt):
            app._add_varbinds(rows)
            app._status(f"Set completato in {dt * 1000:.0f} ms")
            if self.winfo_exists():
                self.destroy()

        app._run("Set", app.client.set(self.cfg, oid, value), done)


class TableView(tk.Toplevel):
    def __init__(self, app: App, cfg, row_oid, columns):
        super().__init__(app)
        self.app, self.cfg, self.row_oid, self.columns = app, cfg, tuple(row_oid), columns
        row_node = app.mibs.node(row_oid)
        table_node = app.mibs.node(row_oid[:-1])
        name = table_node.label if table_node else (row_node.label if row_node else oid_str(row_oid))
        self.title(f"Tabella {name} — {cfg.host}")
        self.geometry("1000x480")
        self.col_index = {c.oid[-1]: i for i, c in enumerate(columns)}
        self.rows = {}   # indice -> [valori]
        self.items = {}  # indice -> iid
        self.stop_event = None

        bar = ttk.Frame(self, padding=4)
        bar.pack(fill="x")
        self.refresh_btn = ttk.Button(bar, text="Aggiorna", command=self.refresh)
        self.refresh_btn.pack(side="left")
        ttk.Button(bar, text="Stop", command=lambda: self.stop_event and self.stop_event.set()).pack(side="left",
                                                                                                    padx=4)
        ttk.Button(bar, text="Esporta CSV…", command=self.export).pack(side="left")
        self.v_status = tk.StringVar()
        ttk.Label(bar, textvariable=self.v_status).pack(side="left", padx=10)

        frm = ttk.Frame(self)
        frm.pack(fill="both", expand=True)
        cols = ["_index"] + [c.label for c in columns]
        self.tv = ttk.Treeview(frm, columns=cols, show="headings")
        self.tv.heading("_index", text="Indice")
        self.tv.column("_index", width=140, stretch=False)
        for c in columns:
            self.tv.heading(c.label, text=c.label)
            self.tv.column(c.label, width=max(90, len(c.label) * 8), stretch=False)
        ys = ttk.Scrollbar(frm, orient="vertical", command=self.tv.yview)
        xs = ttk.Scrollbar(frm, orient="horizontal", command=self.tv.xview)
        self.tv.configure(yscrollcommand=ys.set, xscrollcommand=xs.set)
        self.tv.grid(row=0, column=0, sticky="nsew")
        ys.grid(row=0, column=1, sticky="ns")
        xs.grid(row=1, column=0, sticky="ew")
        frm.rowconfigure(0, weight=1)
        frm.columnconfigure(0, weight=1)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.refresh()

    def refresh(self):
        self.tv.delete(*self.tv.get_children())
        self.rows.clear()
        self.items.clear()
        self.stop_event = threading.Event()
        self.refresh_btn.configure(state="disabled")
        self.v_status.set("Lettura in corso…")
        n = len(self.row_oid)
        start = time.perf_counter()

        def on_rows(rows):
            self.app.call_soon(self._add, [(oid[n], oid[n + 1:], oid, val) for oid, val in rows if len(oid) > n + 1])

        def done(f):
            try:
                total = f.result()
                msg = f"{{rows}} righe ({total} valori) in {time.perf_counter() - start:.2f} s"
            except Cancelled:
                msg = "Interrotto"
            except Exception as exc:
                msg = f"Errore: {one_line(str(exc))}"
            self.app.call_soon(self._finished, msg)

        self.app.client.walk(self.cfg, self.row_oid, on_rows, self.stop_event,
                             self.app.v_use_bulk.get()).add_done_callback(done)

    def _add(self, items):
        if not self.winfo_exists():
            return
        width = len(self.columns)
        for col, index, oid, val in items:
            key = oid_str(index)
            vals = self.rows.setdefault(key, [""] * width)
            ci = self.col_index.get(col)
            if ci is None:
                continue
            vals[ci] = one_line(self.app.mibs.format_value(oid, val)[0])
            if key in self.items:
                self.tv.item(self.items[key], values=[key] + vals)
            else:
                self.items[key] = self.tv.insert("", "end", values=[key] + vals)
        self.v_status.set(f"{len(self.rows)} righe…")

    def _finished(self, msg):
        if self.winfo_exists():
            # le righe arrivano tramite la coda della GUI: il conteggio va fatto qui
            self.v_status.set(msg.replace("{rows}", str(len(self.rows))))
            self.refresh_btn.configure(state="normal")
            if msg.startswith("Errore"):
                messagebox.showerror("Tabella", msg, parent=self)

    def export(self):
        path = filedialog.asksaveasfilename(parent=self, defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh, delimiter=";")
            w.writerow(["Indice"] + [c.label for c in self.columns])
            for key, vals in self.rows.items():
                w.writerow([key] + vals)
        self.v_status.set(f"Esportato in {path}")

    def close(self):
        if self.stop_event is not None:
            self.stop_event.set()
        self.destroy()


class TrapWindow(tk.Toplevel):
    MAX_EVENTS = 5000

    def __init__(self, app: App):
        super().__init__(app)
        self.app = app
        self.title("Ricevitore trap SNMP")
        self.geometry("1100x640")
        self.protocol("WM_DELETE_WINDOW", self.withdraw)  # chiudere la finestra non ferma la ricezione
        s = app.settings.get("trap_receiver", {})
        if not s.get("engine_id"):
            s["engine_id"] = new_engine_id()  # stabile tra i riavvii: i dispositivi lo usano per gli inform v3
        app.settings["trap_receiver"] = s
        self.users = [TrapUser.from_dict(u) for u in app.settings.get("trap_users", [])]
        self.events = []  # TrapEvent oppure (ora, sorgente, motivo) per i messaggi scartati
        self.receiver = TrapReceiver(
            lambda ev: app.call_soon(self.add_event, ev),
            lambda src, why: app.call_soon(self.add_drop, src, why))

        self.v_addr = tk.StringVar(value=s.get("address", "0.0.0.0"))
        self.v_port = tk.StringVar(value=str(s.get("port", 162)))
        self.v_comm = tk.StringVar(value=s.get("communities", "public"))
        self.v_auto = tk.BooleanVar(value=s.get("autostart", False))
        self.v_follow = tk.BooleanVar(value=True)
        self.v_state = tk.StringVar(value="Fermo")

        top = ttk.Frame(self, padding=(8, 6))
        top.pack(fill="x")
        ttk.Label(top, text="Indirizzo:").pack(side="left")
        ttk.Entry(top, textvariable=self.v_addr, width=16).pack(side="left", padx=(2, 10))
        ttk.Label(top, text="Porta:").pack(side="left")
        ttk.Entry(top, textvariable=self.v_port, width=6).pack(side="left", padx=(2, 10))
        ttk.Label(top, text="Community (vuoto = qualsiasi):").pack(side="left")
        ttk.Entry(top, textvariable=self.v_comm, width=20).pack(side="left", padx=(2, 10))
        ttk.Button(top, text="Utenti v3…", command=self.edit_users).pack(side="left", padx=2)
        self.start_btn = ttk.Button(top, text="Avvia", command=self.toggle, width=8)
        self.start_btn.pack(side="left", padx=(10, 2))
        self.state_lbl = ttk.Label(top, textvariable=self.v_state, foreground="#b00020")
        self.state_lbl.pack(side="left", padx=6)
        ttk.Checkbutton(top, text="Avvia all'apertura del programma", variable=self.v_auto).pack(side="right")

        eng = ttk.Frame(self, padding=(8, 0, 8, 4))
        eng.pack(fill="x")
        ttk.Label(eng, text="Engine ID del ricevitore (per gli inform v3):").pack(side="left")
        self.v_engine = tk.StringVar(value=s["engine_id"])
        ttk.Entry(eng, textvariable=self.v_engine, width=36, state="readonly").pack(side="left", padx=4)
        ttk.Button(eng, text="Copia", command=lambda: app._clip(self.v_engine.get())).pack(side="left")
        self.v_users_info = tk.StringVar()
        ttk.Label(eng, textvariable=self.v_users_info, foreground="#555").pack(side="left", padx=12)
        self._update_users_info()

        pw = ttk.PanedWindow(self, orient="vertical")
        pw.pack(fill="both", expand=True, padx=8)

        lf = ttk.Frame(pw)
        cols = ("time", "source", "ver", "pdu", "sec", "trap")
        self.list = ttk.Treeview(lf, columns=cols, show="headings", selectmode="browse")
        for c, t, w in zip(cols, ("Ora", "Sorgente", "Ver.", "Tipo", "Sicurezza", "Trap"),
                           (140, 150, 45, 70, 200, 420)):
            self.list.heading(c, text=t)
            self.list.column(c, width=w, stretch=(c == "trap"))
        ys = ttk.Scrollbar(lf, orient="vertical", command=self.list.yview)
        self.list.configure(yscrollcommand=ys.set)
        self.list.pack(side="left", fill="both", expand=True)
        ys.pack(side="right", fill="y")
        self.list.tag_configure("drop", foreground="#b00020")
        self.list.tag_configure("inform", foreground="#0b5cad")
        self.list.bind("<<TreeviewSelect>>", self._on_select)
        pw.add(lf, weight=3)

        df = ttk.Frame(pw)
        self.v_title = tk.StringVar()
        ttk.Label(df, textvariable=self.v_title, wraplength=1050, justify="left",
                  padding=(0, 4)).pack(fill="x")
        vf = ttk.Frame(df)
        vf.pack(fill="both", expand=True)
        vcols = ("name", "value", "type")
        self.vb = ttk.Treeview(vf, columns=vcols, show="headings", height=7)
        for c, t, w in zip(vcols, ("Nome", "Valore", "Tipo"), (320, 520, 180)):
            self.vb.heading(c, text=t)
            self.vb.column(c, width=w, stretch=(c == "value"))
        vys = ttk.Scrollbar(vf, orient="vertical", command=self.vb.yview)
        self.vb.configure(yscrollcommand=vys.set)
        self.vb.pack(side="left", fill="both", expand=True)
        vys.pack(side="right", fill="y")
        pw.add(df, weight=2)

        bot = ttk.Frame(self, padding=(8, 4))
        bot.pack(fill="x")
        ttk.Button(bot, text="Pulisci", command=self.clear).pack(side="left")
        ttk.Button(bot, text="Esporta CSV…", command=self.export).pack(side="left", padx=4)
        ttk.Checkbutton(bot, text="Segui le nuove trap", variable=self.v_follow).pack(side="left", padx=8)
        self.v_count = tk.StringVar(value="0 trap")
        ttk.Label(bot, textvariable=self.v_count).pack(side="right")

    # --- configurazione ---------------------------------------------------------

    def _config(self):
        try:
            port = int(self.v_port.get())
        except ValueError:
            raise ValueError("Porta non valida") from None
        return ReceiverConfig(self.v_addr.get().strip() or "0.0.0.0", port, self.v_comm.get(),
                              self.v_engine.get())

    def save_settings(self):
        s = self.app.settings.setdefault("trap_receiver", {})
        s.update(address=self.v_addr.get().strip(), port=self.v_port.get().strip(),
                 communities=self.v_comm.get(), autostart=self.v_auto.get(), engine_id=self.v_engine.get())
        secrets = self.app.v_save_secrets.get()
        self.app.settings["trap_users"] = [u.to_dict(include_secrets=secrets) for u in self.users]

    def _update_users_info(self):
        n = len(self.users)
        self.v_users_info.set(f"{n} utent{'e' if n == 1 else 'i'} v3 configurat{'o' if n == 1 else 'i'}"
                              if n else "Nessun utente v3: le trap v3 verranno scartate")

    def edit_users(self):
        TrapUsersDialog(self)

    def users_changed(self):
        self._update_users_info()
        self.save_settings()
        if self.receiver.running:
            self.start()  # riavvio per applicare i nuovi utenti

    # --- avvio / arresto -----------------------------------------------------------

    def toggle(self):
        if self.receiver.running:
            self.stop()
        else:
            self.start()

    def start(self, quiet=False):
        missing = [u.name for u in self.users if u.security_level != "noAuthNoPriv" and not u.auth_password]
        try:
            cfg = self._config()
            self.receiver.start(cfg, self.users)
        except Exception as exc:
            self._set_state(False, "Errore")
            self.app._status(f"Ricevitore trap: {one_line(str(exc))}")
            if not quiet:
                messagebox.showerror("Ricevitore trap", str(exc), parent=self)
            return
        self.save_settings()
        where = f"{cfg.address}:{cfg.port}"
        self._set_state(True, f"In ascolto su {where}")
        self.app._status(f"Ricevitore trap in ascolto su {where}")
        if missing and not quiet:
            messagebox.showwarning("Ricevitore trap", "Utenti v3 senza password (non salvate): "
                                   + ", ".join(missing) + "\nReinserirle in 'Utenti v3…'.", parent=self)

    def stop(self):
        self.receiver.stop()
        self._set_state(False, "Fermo")
        self.app._status("Ricevitore trap fermato")

    def _set_state(self, running, text):
        self.v_state.set(("● " if running else "") + text)
        self.state_lbl.configure(foreground="#127a3a" if running else "#b00020")
        self.start_btn.configure(text="Ferma" if running else "Avvia")

    # --- eventi ----------------------------------------------------------------------

    def _trap_name(self, trap_oid):
        return self.app.mibs.name_of(trap_oid) if trap_oid else "—"

    def add_event(self, ev):
        name = self._trap_name(ev.trap_oid)
        self._append(ev, (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ev.time)), ev.source, ev.version,
                          ev.pdu, ev.security, name), "inform" if ev.pdu == "Inform" else "")
        if not self.winfo_viewable():
            self.app._status(f"{ev.pdu} {ev.version} da {ev.source}: {name}")

    def add_drop(self, source, reason):
        now = time.time()
        self._append((now, source, reason), (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now)), source,
                                             "", "Scartato", "", reason), "drop")
        if not self.winfo_viewable():
            self.app._status(f"Trap da {source} scartata: {reason}")

    def _append(self, item, values, tag):
        self.events.append(item)
        iid = self.list.insert("", "end", values=values, tags=(tag,) if tag else ())
        if len(self.events) > self.MAX_EVENTS:
            self.events.pop(0)
            self.list.delete(self.list.get_children()[0])
        if self.v_follow.get():
            self.list.selection_set(iid)
            self.list.see(iid)
        traps = sum(1 for e in self.events if not isinstance(e, tuple))
        self.v_count.set(f"{traps} trap, {len(self.events) - traps} scartate")

    def _on_select(self, _e=None):
        sel = self.list.selection()
        if not sel:
            return
        ev = self.events[self.list.index(sel[0])]
        self.vb.delete(*self.vb.get_children())
        if isinstance(ev, tuple):
            self.v_title.set(f"Messaggio scartato da {ev[1]}: {ev[2]}")
            return
        mibs = self.app.mibs
        title = f"{ev.pdu} {ev.version} da {ev.source} — {self._trap_name(ev.trap_oid)}"
        if ev.context:
            title += f"   (context '{ev.context}')"
        node, _ = mibs.best_node(ev.trap_oid) if ev.trap_oid else (None, ())
        if node is not None and node.kind == "notification":
            desc = dict(mibs.describe(node.oid)).get("Descrizione")
            if desc:
                title += "\n" + (desc if len(desc) < 400 else desc[:400] + "…")
        self.v_title.set(title)
        for oid, value in ev.var_binds:
            text, type_name = mibs.format_value(oid, value)
            self.vb.insert("", "end", values=(mibs.name_of(oid), one_line(text), type_name))

    def clear(self):
        self.events.clear()
        self.list.delete(*self.list.get_children())
        self.vb.delete(*self.vb.get_children())
        self.v_title.set("")
        self.v_count.set("0 trap")

    def export(self):
        if not self.events:
            return
        path = filedialog.asksaveasfilename(parent=self, defaultextension=".csv", filetypes=[("CSV", "*.csv")],
                                            initialfile="trap.csv")
        if not path:
            return
        mibs = self.app.mibs
        with open(path, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh, delimiter=";")
            w.writerow(["Ora", "Sorgente", "Versione", "Tipo", "Sicurezza", "Trap", "Variabili"])
            for ev in self.events:
                if isinstance(ev, tuple):
                    w.writerow([time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ev[0])), ev[1], "", "Scartato",
                                "", ev[2], ""])
                    continue
                vbs = " | ".join(f"{mibs.name_of(o)} = {mibs.format_value(o, v)[0]}" for o, v in ev.var_binds)
                w.writerow([time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ev.time)), ev.source, ev.version,
                            ev.pdu, ev.security, self._trap_name(ev.trap_oid), vbs])


class TrapUsersDialog(tk.Toplevel):
    def __init__(self, win: TrapWindow):
        super().__init__(win)
        self.win = win
        self.title("Utenti SNMPv3 per le trap")
        self.transient(win)
        self.geometry("760x420")
        frm = ttk.Frame(self, padding=8)
        frm.pack(fill="both", expand=True)

        cols = ("name", "level", "auth", "priv", "engine")
        self.tv = ttk.Treeview(frm, columns=cols, show="headings", height=8, selectmode="browse")
        for c, t, w in zip(cols, ("Utente", "Livello", "Auth", "Priv", "Engine ID mittente"),
                           (140, 110, 80, 110, 260)):
            self.tv.heading(c, text=t)
            self.tv.column(c, width=w)
        self.tv.pack(fill="both", expand=True)
        self.tv.bind("<<TreeviewSelect>>", self._on_select)

        f = ttk.LabelFrame(frm, text="Utente", padding=6)
        f.pack(fill="x", pady=(8, 0))
        self.v = {k: tk.StringVar() for k in ("name", "security_level", "auth_protocol", "auth_password",
                                              "priv_protocol", "priv_password", "engine_id")}
        self.v["security_level"].set("authPriv")
        self.v["auth_protocol"].set("SHA")
        self.v["priv_protocol"].set("AES-128")
        ttk.Label(f, text="Nome:").grid(row=0, column=0, sticky="e")
        ttk.Entry(f, textvariable=self.v["name"], width=18).grid(row=0, column=1, sticky="w", padx=(2, 10))
        ttk.Label(f, text="Livello:").grid(row=0, column=2, sticky="e")
        lvl = ttk.Combobox(f, textvariable=self.v["security_level"], values=SECURITY_LEVELS, state="readonly",
                           width=13)
        lvl.grid(row=0, column=3, sticky="w", padx=(2, 10))
        lvl.bind("<<ComboboxSelected>>", lambda e: self._update_state())
        ttk.Label(f, text="Engine ID mittente (hex):").grid(row=0, column=4, sticky="e")
        ttk.Entry(f, textvariable=self.v["engine_id"], width=26).grid(row=0, column=5, sticky="w", padx=2)
        ttk.Label(f, text="Autenticazione:").grid(row=1, column=0, sticky="e", pady=(4, 0))
        self.auth = ttk.Combobox(f, textvariable=self.v["auth_protocol"], values=list(AUTH_PROTOCOLS),
                                 state="readonly", width=10)
        self.auth.grid(row=1, column=1, sticky="w", padx=(2, 10), pady=(4, 0))
        ttk.Label(f, text="Password auth:").grid(row=1, column=2, sticky="e", pady=(4, 0))
        self.auth_pw = ttk.Entry(f, textvariable=self.v["auth_password"], width=16, show="•")
        self.auth_pw.grid(row=1, column=3, sticky="w", padx=(2, 10), pady=(4, 0))
        ttk.Label(f, text="Privacy:").grid(row=2, column=0, sticky="e", pady=(4, 0))
        self.priv = ttk.Combobox(f, textvariable=self.v["priv_protocol"], values=list(PRIV_PROTOCOLS),
                                 state="readonly", width=14)
        self.priv.grid(row=2, column=1, sticky="w", padx=(2, 10), pady=(4, 0))
        ttk.Label(f, text="Password priv:").grid(row=2, column=2, sticky="e", pady=(4, 0))
        self.priv_pw = ttk.Entry(f, textvariable=self.v["priv_password"], width=16, show="•")
        self.priv_pw.grid(row=2, column=3, sticky="w", padx=(2, 10), pady=(4, 0))
        ttk.Label(f, text="Engine ID vuoto = accetta trap da qualsiasi dispositivo\n"
                          "(l'engine ID viene appreso dai pacchetti ricevuti).",
                  foreground="#666").grid(row=1, column=4, rowspan=2, columnspan=2, sticky="w", padx=(10, 0))

        bf = ttk.Frame(frm)
        bf.pack(fill="x", pady=(8, 0))
        ttk.Button(bf, text="Aggiungi / Aggiorna", command=self.save_user).pack(side="left")
        ttk.Button(bf, text="Rimuovi", command=self.remove).pack(side="left", padx=4)
        ttk.Button(bf, text="Chiudi", command=self.destroy).pack(side="right")
        if not win.app.v_save_secrets.get():
            ttk.Label(bf, text="Password conservate solo per questa sessione (Opzioni → Ricorda le password).",
                      foreground="#777").pack(side="left", padx=10)
        self._refresh()
        self._update_state()

    def _refresh(self):
        self.tv.delete(*self.tv.get_children())
        for u in self.win.users:
            auth = u.auth_protocol if u.security_level != "noAuthNoPriv" else "—"
            priv = u.priv_protocol if u.security_level == "authPriv" else "—"
            self.tv.insert("", "end", values=(u.name, u.security_level, auth, priv, u.engine_id or "(qualsiasi)"))

    def _update_state(self):
        lvl = self.v["security_level"].get()
        a = lvl in ("authNoPriv", "authPriv")
        p = lvl == "authPriv"
        self.auth.configure(state="readonly" if a else "disabled")
        self.auth_pw.configure(state="normal" if a else "disabled")
        self.priv.configure(state="readonly" if p else "disabled")
        self.priv_pw.configure(state="normal" if p else "disabled")

    def _on_select(self, _e=None):
        sel = self.tv.selection()
        if not sel:
            return
        u = self.win.users[self.tv.index(sel[0])]
        for k in self.v:
            self.v[k].set(getattr(u, k))
        self._update_state()

    def save_user(self):
        d = {k: (var.get() if "password" in k else var.get().strip()) for k, var in self.v.items()}
        lvl = d["security_level"]
        err = None
        if not d["name"]:
            err = "Specificare il nome utente"
        elif lvl != "noAuthNoPriv" and len(d["auth_password"]) < 8:
            err = "La password di autenticazione deve avere almeno 8 caratteri"
        elif lvl == "authPriv" and len(d["priv_password"]) < 8:
            err = "La password di privacy deve avere almeno 8 caratteri"
        elif d["engine_id"]:
            h = d["engine_id"].replace(":", "").replace(" ", "")
            h = h[2:] if h.lower().startswith("0x") else h
            try:
                bytes.fromhex(h)
                d["engine_id"] = h.lower()
                if not 5 <= len(h) // 2 <= 32:
                    err = "L'engine ID deve essere lungo da 5 a 32 byte"
            except ValueError:
                err = "Engine ID non valido (esadecimale)"
        if err:
            messagebox.showerror("Utente v3", err, parent=self)
            return
        user = TrapUser.from_dict(d)
        users = self.win.users
        idx = next((i for i, u in enumerate(users) if u.name == user.name), None)
        if idx is None:
            users.append(user)
        else:
            users[idx] = user
        self._refresh()
        self.win.users_changed()

    def remove(self):
        sel = self.tv.selection()
        if sel:
            del self.win.users[self.tv.index(sel[0])]
            self._refresh()
            self.win.users_changed()


def main():
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
