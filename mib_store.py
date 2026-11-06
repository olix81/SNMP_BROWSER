"""Gestione dei moduli MIB: compilazione (pysmi), caricamento, albero dei nodi e formattazione dei valori."""

import os
import re
import shutil
import threading
from dataclasses import dataclass
from pathlib import Path

from pysnmp.smi import builder, view, compiler
from pysnmp.proto import rfc1902
from pysnmp.proto.rfc1905 import NoSuchObject, NoSuchInstance, EndOfMibView
from pyasn1.type import univ
from pysmi.reader.httpclient import HttpReader
from pysmi.writer import pyfile as _pysmi_pyfile

from mib_fixer import fix_mib, annotate


class _OsReplaceShim:
    """pysmi usa os.rename, che su Windows fallisce se il file di destinazione esiste già."""

    def __getattr__(self, name):
        return os.replace if name == "rename" else getattr(os, name)


_pysmi_pyfile.os = _OsReplaceShim()


class CachingHttpReader(HttpReader):
    """HttpReader che salva una copia locale di ogni MIB sorgente scaricata."""

    def __init__(self, url, cache_dir):
        super().__init__(url)
        self._cache_dir = Path(cache_dir)

    def get_data(self, mibname, **options):
        info, data = super().get_data(mibname, **options)
        try:
            (self._cache_dir / f"{info.name}.mib").write_text(data, encoding="utf-8")
        except Exception:
            pass
        return info, data

REMOTE_MIB_SOURCE = "https://mibs.pysnmp.com/asn1/@mib@"

DEFAULT_MIBS = (
    "SNMPv2-MIB", "IF-MIB", "IP-MIB", "TCP-MIB", "UDP-MIB", "HOST-RESOURCES-MIB",
    "ENTITY-MIB", "SNMP-FRAMEWORK-MIB", "SNMP-USER-BASED-SM-MIB", "SNMP-VIEW-BASED-ACM-MIB",
    "SNMP-COMMUNITY-MIB",
)

NODE_KINDS = {
    "MibIdentifier": "folder", "ObjectIdentity": "folder", "ModuleIdentity": "module",
    "MibScalar": "scalar", "MibTable": "table", "MibTableRow": "row", "MibTableColumn": "column",
    "NotificationType": "notification", "ObjectGroup": "group", "NotificationGroup": "group",
    "ModuleCompliance": "group", "AgentCapabilities": "group",
}

KIND_NAMES = {
    "folder": "Nodo", "module": "Modulo", "scalar": "Scalare", "table": "Tabella",
    "row": "Riga (entry)", "column": "Colonna", "notification": "Notifica (trap)",
    "group": "Gruppo/Conformità", "virtual": "Nodo",
}

# RFC-1212 / RFC-1215 definiscono solo le macro OBJECT-TYPE e TRAP-TYPE (in commento): pysmi non
# riesce a leggerli e quindi nessuna MIB SMIv1 che li importa compila. Bastano moduli segnaposto.
SMI_V1_STUBS = {
    name: f"{name} DEFINITIONS ::= BEGIN\nIMPORTS ObjectName FROM RFC1155-SMI;\nEND\n"
    for name in ("RFC-1212", "RFC-1215")
}

WELL_KNOWN = {(1,): "iso", (1, 3): "org", (1, 3, 6): "dod", (1, 3, 6, 1): "internet"}

MODULE_RE = re.compile(r"^\s*([A-Za-z][\w-]*)\s+DEFINITIONS\s*(?:IMPLICIT\s+TAGS\s*)?::=\s*BEGIN", re.M)


@dataclass
class MibNode:
    oid: tuple
    label: str
    module: str
    kind: str
    obj: object = None


def oid_str(oid):
    return ".".join(str(x) for x in oid)


def parse_numeric_oid(text):
    text = text.strip().lstrip(".")
    if re.fullmatch(r"\d+(\.\d+)*", text):
        return tuple(int(x) for x in text.split("."))
    return None


def format_timeticks(ticks):
    ticks = int(ticks)
    cs = ticks % 100
    s = ticks // 100
    d, s = divmod(s, 86400)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{d}d {h:02d}:{m:02d}:{s:02d}.{cs:02d}"


class MibStore:
    def __init__(self, base_dir: Path, use_remote=True):
        self.src_dir = Path(base_dir) / "mibs"
        self.orig_dir = Path(base_dir) / "mibs_original"
        self.cache_dir = Path(base_dir) / "mibs_cache"
        self.compiled_dir = Path(base_dir) / "compiled"
        for d in (self.src_dir, self.cache_dir, self.compiled_dir):
            d.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()
        self.builder = builder.MibBuilder()
        self.builder.loadTexts = True
        stub_dir = Path(base_dir) / "mibs_stubs"
        stub_dir.mkdir(parents=True, exist_ok=True)
        for name, text in SMI_V1_STUBS.items():
            p = stub_dir / f"{name}.mib"
            if not p.exists():
                p.write_text(text, encoding="ascii")
        # 'C:\...' verrebbe letto come schema URL: si usano URI file:///
        sources = [stub_dir.resolve().as_uri(), self.src_dir.resolve().as_uri(), self.cache_dir.resolve().as_uri()]
        # Registrata prima del compilatore, così pysmi riconosce i moduli già compilati
        self.builder.add_mib_sources(builder.DirMibSource(str(self.compiled_dir)))
        compiler.add_mib_compiler(self.builder, sources=sources, destination=str(self.compiled_dir))
        if use_remote:
            # i sorgenti scaricati vengono salvati: servono anche per compilare MIB future offline
            self.builder.get_mib_compiler().add_sources(CachingHttpReader(REMOTE_MIB_SOURCE, self.cache_dir))
        self.view = view.MibViewController(self.builder)
        self.loaded = []          # moduli richiesti esplicitamente dall'utente
        self._nodes = None        # cache oid -> MibNode
        self._by_label = None     # cache label -> [MibNode]

    # --- caricamento ---------------------------------------------------

    def load(self, names):
        """Carica (compilando se necessario) i moduli indicati. Restituisce (ok, errori{nome: msg})."""
        ok, errors = [], {}
        with self.lock:
            for name in names:
                try:
                    self.builder.load_modules(name)
                except Exception as exc:
                    # il modulo può esistere con il nome scritto in un'altra capitalizzazione
                    alt = self._module_name_ci(name)
                    try:
                        if alt is None:
                            raise exc
                        self.builder.load_modules(alt)
                        name = alt
                    except Exception as exc2:
                        errors[name] = self._describe_error(name, str(exc2) or exc2.__class__.__name__)
                        continue
                if name not in self.builder.mibSymbols:  # caricato tramite file con altra capitalizzazione
                    name = self._module_name_ci(name) or name
                ok.append(name)
                if name not in self.loaded:
                    self.loaded.append(name)
            self._nodes = self._by_label = None
        return ok, errors

    def _is_available(self, module):
        """True se il modulo è già disponibile compilato in una delle sorgenti di pysnmp."""
        for src in self.builder.get_mib_sources():
            try:
                src.read(module)
                return True
            except Exception:
                continue
        return False

    def _describe_error(self, module, msg):
        """Traduce l'errore grezzo di pysmi/pysnmp in un messaggio comprensibile."""
        # la coda "caused by <MibNotFoundError>: ... search path (...)" è solo una conseguenza
        core = msg.split(" caused by ", 1)[0]
        core = core.split(" compilation error(s): ", 1)[-1]

        missing = []
        for dep in re.findall(r"([A-Za-z][\w-]*): missing", core) + re.findall(r'no module "([\w-]+)"', core):
            if dep not in missing:
                missing.append(dep)
        if module in missing or (self._module_name_ci(module) or module) in missing:
            return (f"File sorgente di {module} non trovato.\n"
                    f"Copia il file MIB in:\n{self.src_dir}")
        missing = [m for m in missing if not self._is_available(m)]
        if missing:
            return ("Mancano le MIB da cui questo modulo importa:\n"
                    + "\n".join(f"  • {m}" for m in missing)
                    + f"\n\nProcurale (di solito dal fornitore dell'apparato) e copiale in:\n{self.src_dir}")

        m = re.search(r"Bad grammar near (?:token .*? |offset \d+ )?at MIB ([\w-]+), line (\d+)", core)
        if m:
            return (f"Errore di sintassi nel file {m.group(1)}.mib alla riga {m.group(2)}.\n"
                    f"File: {self.src_dir / (m.group(1) + '.mib')}")
        return core

    def import_file(self, path):
        """Importa un file MIB nella cartella sorgenti, correggendone maiuscole/minuscole e caratteri
        non ammessi. Il file originale non viene modificato (una copia va in mibs_original).
        Restituisce (nome modulo, lista correzioni [(riga, vecchio, nuovo)])."""
        path = Path(path)
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("latin-1")
        fixed, changes = fix_mib(text, self._module_symbols, self._resolve_import_module)
        m = MODULE_RE.search(fixed)
        if not m:
            raise ValueError(f"{path.name}: intestazione 'DEFINITIONS ::= BEGIN' non trovata")
        module = m.group(1)
        self.orig_dir.mkdir(parents=True, exist_ok=True)
        orig = self.orig_dir / f"{module}{path.suffix or '.mib'}"
        if path.resolve() != orig.resolve() and path.parent.resolve() != self.src_dir.resolve():
            shutil.copyfile(path, orig)
        (self.src_dir / f"{module}.mib").write_text(annotate(fixed, changes, path.name), encoding="utf-8")
        # forza la ricompilazione se il modulo era già stato compilato o caricato
        for old in self.compiled_dir.glob(f"{module}.py*"):
            old.unlink(missing_ok=True)
        with self.lock:
            try:
                self.builder.unload_modules(module)
            except Exception:
                pass
            self._nodes = self._by_label = None
        return module, changes

    def _module_symbols(self, module):
        """Simboli definiti in un modulo (compilandolo se serve); None se non disponibile."""
        with self.lock:
            try:
                self.builder.load_modules(module)
            except Exception:
                return None
            if module not in self.builder.mibSymbols:
                module = self._module_name_ci(module)
            return set(self.builder.mibSymbols[module]) if module in self.builder.mibSymbols else None

    def _module_name_ci(self, module):
        """Nome effettivo di un modulo noto con capitalizzazione diversa da 'module', se esiste."""
        low = module.lower()
        found = set()
        for d, pattern in ((self.compiled_dir, "*.py"), (self.src_dir, "*.mib"), (self.cache_dir, "*.mib")):
            for p in d.glob(pattern):
                if p.stem.lower() == low and p.stem != module:
                    found.add(p.stem)
        found |= {m for m in self.builder.mibSymbols if m.lower() == low and m != module}
        return found.pop() if len(found) == 1 else None

    def _resolve_import_module(self, module):
        """Per il normalizzatore: nome corretto di un modulo importato, o None se va bene così."""
        # su Windows il file system ignora le maiuscole: il caricamento può riuscire anche con il
        # nome sbagliato, ma il modulo viene registrato con il nome vero
        self._module_symbols(module)
        if module in self.builder.mibSymbols:
            return None
        return self._module_name_ci(module)

    def unload(self, name):
        with self.lock:
            if name in self.loaded:
                self.loaded.remove(name)
            try:
                self.builder.unload_modules(name)
            except Exception:
                pass
            self._nodes = self._by_label = None

    def modules(self):
        with self.lock:
            return sorted(m for m in self.builder.mibSymbols if not m.startswith(("__", "ASN1")))

    # --- albero ----------------------------------------------------------

    def nodes(self):
        with self.lock:
            if self._nodes is not None:
                return self._nodes
            nodes = {}
            for mod, syms in list(self.builder.mibSymbols.items()):
                if mod.startswith(("__", "ASN1")):
                    continue
                for label, obj in syms.items():
                    kind = NODE_KINDS.get(type(obj).__name__)
                    if kind is None:
                        continue
                    try:
                        oid = tuple(obj.getName())
                    except Exception:
                        continue
                    if not oid:
                        continue
                    if oid not in nodes or (nodes[oid].kind == "folder" and kind != "folder"):
                        nodes[oid] = MibNode(oid, label, mod, kind, obj)
            # aggiunge i nodi intermedi mancanti
            for oid in list(nodes):
                for i in range(1, len(oid)):
                    p = oid[:i]
                    if p not in nodes:
                        nodes[p] = MibNode(p, WELL_KNOWN.get(p, str(p[-1])), "", "virtual")
            self._nodes = nodes
            by_label = {}
            for n in nodes.values():
                by_label.setdefault(n.label, []).append(n)
            self._by_label = by_label
            return nodes

    def node(self, oid):
        return self.nodes().get(tuple(oid))

    def best_node(self, oid):
        """Nodo MIB più specifico che contiene l'OID, e suffisso (indice) residuo."""
        nodes = self.nodes()
        oid = tuple(oid)
        for i in range(len(oid), 0, -1):
            n = nodes.get(oid[:i])
            if n is not None and n.kind != "virtual":
                return n, oid[i:]
        return None, oid

    def children(self, oid):
        oid = tuple(oid)
        return sorted((n for o, n in self.nodes().items() if len(o) == len(oid) + 1 and o[:-1] == oid),
                      key=lambda n: n.oid)

    # --- risoluzione nomi ------------------------------------------------

    def resolve(self, text):
        """'1.3.6.1...', 'sysDescr.0', 'IF-MIB::ifDescr.3' -> tuple OID."""
        text = text.strip()
        num = parse_numeric_oid(text)
        if num is not None:
            return num
        module = None
        if "::" in text:
            module, text = text.split("::", 1)
        sym, _, suffix = text.partition(".")
        idx = parse_numeric_oid(suffix) if suffix else ()
        if idx is None:
            raise ValueError(f"Indice non valido: '{suffix}'")
        self.nodes()
        with self.lock:
            if module:
                obj = self.builder.mibSymbols.get(module, {}).get(sym)
                if obj is None or not hasattr(obj, "getName"):
                    raise ValueError(f"Oggetto '{module}::{sym}' non trovato (modulo caricato?)")
                return tuple(obj.getName()) + idx
            cands = self._by_label.get(sym)
            if not cands:
                raise ValueError(f"Oggetto '{sym}' non trovato nelle MIB caricate")
            return cands[0].oid + idx

    def name_of(self, oid):
        node, suffix = self.best_node(oid)
        if node is None:
            return oid_str(oid)
        name = f"{node.module}::{node.label}"
        return name + ("." + oid_str(suffix) if suffix else "")

    # --- valori ----------------------------------------------------------

    def _syntax(self, node):
        if node is None or node.obj is None or not hasattr(node.obj, "getSyntax"):
            return None
        try:
            return node.obj.getSyntax()
        except Exception:
            return None

    def format_value(self, oid, value):
        """Restituisce (testo valore, nome tipo)."""
        if isinstance(value, (NoSuchObject, NoSuchInstance, EndOfMibView)):
            return value.__class__.__name__, "—"
        type_name = value.__class__.__name__
        with self.lock:
            node, _ = self.best_node(oid)
            syntax = self._syntax(node) if node is not None and node.kind in ("scalar", "column") else None
            if syntax is not None:
                try:
                    typed = syntax.clone(value)
                    tc = typed.__class__.__name__
                    if tc != type_name:
                        type_name = f"{type_name} ({tc})"
                    named = getattr(typed, "namedValues", None)
                    if isinstance(typed, univ.Integer) and named and int(typed) in named:
                        return f"{named.getName(int(typed))}({int(typed)})", type_name
                    value = typed
                except Exception:
                    pass
        if isinstance(value, rfc1902.TimeTicks):
            return f"{int(value)} ({format_timeticks(value)})", type_name
        if isinstance(value, univ.ObjectIdentifier):
            o = tuple(value)
            name = self.name_of(o)
            return (f"{name} ({oid_str(o)})" if name != oid_str(o) else oid_str(o)), type_name
        try:
            return value.prettyPrint(), type_name
        except Exception:
            return str(value), type_name

    SET_TYPES = ("Auto (da MIB)", "INTEGER", "OCTET STRING", "Hex-STRING", "OBJECT IDENTIFIER",
                 "IpAddress", "Counter32", "Gauge32", "Unsigned32", "TimeTicks", "Counter64")

    def make_value(self, oid, type_name, text):
        if type_name.startswith("Auto"):
            node, _ = self.best_node(oid)
            syntax = self._syntax(node) if node is not None and node.kind in ("scalar", "column") else None
            if syntax is None:
                raise ValueError("Tipo non determinabile dalla MIB: sceglierlo manualmente")
            if isinstance(syntax, univ.Integer):
                t = text.strip()
                m = re.fullmatch(r"\w[\w-]*\((-?\d+)\)", t)  # accetta anche 'up(1)'
                if m:
                    t = m.group(1)
                return syntax.clone(int(t) if re.fullmatch(r"-?\d+", t) else t)
            if isinstance(syntax, univ.ObjectIdentifier):
                return syntax.clone(self.resolve(text))
            if isinstance(syntax, univ.OctetString) and text.strip().lower().startswith("0x"):
                return syntax.clone(hexValue=text.strip()[2:].replace(" ", "").replace(":", ""))
            return syntax.clone(text)
        if type_name == "INTEGER":
            return rfc1902.Integer32(int(text))
        if type_name == "OCTET STRING":
            return rfc1902.OctetString(text)
        if type_name == "Hex-STRING":
            h = text.strip()
            h = h[2:] if h.lower().startswith("0x") else h
            return rfc1902.OctetString(hexValue=re.sub(r"[\s:.-]", "", h))
        if type_name == "OBJECT IDENTIFIER":
            return rfc1902.ObjectName(self.resolve(text))
        cls = {"IpAddress": rfc1902.IpAddress, "Counter32": rfc1902.Counter32, "Gauge32": rfc1902.Gauge32,
               "Unsigned32": rfc1902.Unsigned32, "TimeTicks": rfc1902.TimeTicks,
               "Counter64": rfc1902.Counter64}[type_name]
        return cls(text.strip()) if type_name == "IpAddress" else cls(int(text))

    # --- dettagli nodo -----------------------------------------------------

    def describe(self, oid):
        """Lista di (campo, valore) per il pannello dettagli."""
        with self.lock:
            node = self.node(oid)
            if node is None:
                return [("OID", oid_str(oid))]
            info = [("Nome", node.label), ("Modulo", node.module or "—"), ("OID", oid_str(node.oid)),
                    ("Tipo nodo", KIND_NAMES.get(node.kind, node.kind))]
            obj = node.obj
            if obj is None:
                return info
            syntax = self._syntax(node)
            if syntax is not None:
                tc = syntax.__class__.__name__
                base = next((c.__name__ for c in syntax.__class__.__mro__
                             if c.__module__.startswith(("pysnmp.proto", "pyasn1.type"))), tc)
                info.append(("Sintassi", tc if tc == base else f"{tc} ({base})"))
                named = getattr(syntax, "namedValues", None)
                if named:
                    info.append(("Valori", ", ".join(f"{n}({v})" for n, v in named.items())))
                spec = getattr(syntax, "subtypeSpec", None)
                if spec is not None and len(spec):
                    s = re.sub(r"<\w+ object, consts ", "(", str(spec)).replace(">", ")")
                    info.append(("Vincoli", s))
                hint = getattr(syntax, "displayHint", None)
                if hint:
                    info.append(("Display hint", hint))
            for label, getter in (("Accesso", "getMaxAccess"), ("Stato", "getStatus"), ("Unità", "getUnits")):
                if hasattr(obj, getter):
                    try:
                        v = getattr(obj, getter)()
                        if v:
                            info.append((label, str(v)))
                    except Exception:
                        pass
            if node.kind == "row" and hasattr(obj, "getIndexNames"):
                idx = [f"{'IMPLIED ' if implied else ''}{sym}" for implied, mod, sym in obj.getIndexNames()]
                if idx:
                    info.append(("Indici", ", ".join(idx)))
            if node.kind == "notification" and hasattr(obj, "getObjects"):
                objs = [f"{m}::{s}" for m, s in obj.getObjects()]
                if objs:
                    info.append(("Oggetti", ", ".join(objs)))
            for label, getter in (("Descrizione", "getDescription"), ("Riferimento", "getReference")):
                if hasattr(obj, getter):
                    try:
                        v = getattr(obj, getter)()
                        if v:
                            info.append((label, re.sub(r"[ \t]+", " ", str(v)).strip()))
                    except Exception:
                        pass
            return info

    def table_columns(self, table_oid):
        """Per un nodo tabella o riga restituisce (oid riga, [colonne])."""
        node = self.node(table_oid)
        if node is None:
            return None, []
        row = node
        if node.kind == "table":
            rows = [c for c in self.children(node.oid) if c.kind == "row"]
            if not rows:
                return None, []
            row = rows[0]
        elif node.kind == "column":
            row = self.node(node.oid[:-1])
        if row is None or row.kind != "row":
            return None, []
        def readable(c):  # le colonne indice 'not-accessible' non vengono mai restituite dall'agent
            try:
                return str(c.obj.getMaxAccess()) != "not-accessible"
            except Exception:
                return True

        return row.oid, [c for c in self.children(row.oid) if c.kind == "column" and readable(c)]
