"""Normalizzazione di file MIB non conformi a SMI per maiuscole/minuscole e caratteri dei nomi.

Il compilatore (pysmi) richiede che i nomi di oggetti/nodi inizino con la minuscola, quelli di
tipi e TEXTUAL-CONVENTION con la maiuscola, le parole chiave nella forma canonica e nessun '_'.
Molte MIB in uso non rispettano queste regole: qui se ne produce una copia corretta.
Gli OID non cambiano, quindi la MIB corretta resta valida per l'agent che usa l'originale.
"""

import re

VALUE_MACROS = {
    "OBJECT-TYPE", "MODULE-IDENTITY", "OBJECT-IDENTITY", "NOTIFICATION-TYPE", "TRAP-TYPE",
    "OBJECT-GROUP", "NOTIFICATION-GROUP", "MODULE-COMPLIANCE", "AGENT-CAPABILITIES",
}

KEYWORDS = [
    "DEFINITIONS", "BEGIN", "END", "IMPORTS", "FROM", "EXPORTS", "OBJECT", "IDENTIFIER", "MACRO",
    "TEXTUAL-CONVENTION", "SYNTAX", "MAX-ACCESS", "MIN-ACCESS", "ACCESS", "STATUS", "DESCRIPTION",
    "REFERENCE", "INDEX", "IMPLIED", "AUGMENTS", "DEFVAL", "UNITS", "DISPLAY-HINT", "LAST-UPDATED",
    "ORGANIZATION", "CONTACT-INFO", "REVISION", "OBJECTS", "NOTIFICATIONS", "ENTERPRISE", "VARIABLES",
    "MODULE", "MANDATORY-GROUPS", "GROUP", "WRITE-SYNTAX", "PRODUCT-RELEASE", "SUPPORTS", "INCLUDES",
    "VARIATION", "CREATION-REQUIRES", "SEQUENCE", "OF", "CHOICE", "SIZE", "INTEGER", "OCTET", "STRING",
    "BITS", "NULL", "MIN", "MAX", "IMPLICIT", "APPLICATION", "UNIVERSAL", "TAGS",
    "Integer32", "Unsigned32", "Counter32", "Counter64", "Gauge32", "TimeTicks", "IpAddress", "Opaque",
    "Counter", "Gauge", "NetworkAddress",
    "read-only", "read-write", "write-only", "read-create", "not-accessible", "accessible-for-notify",
    "not-implemented", "current", "deprecated", "obsolete", "mandatory", "optional",
] + sorted(VALUE_MACROS)
KEYWORD_MAP = {k.lower(): k for k in KEYWORDS}
# nomi di tipo che, scritti con la minuscola fuori da SYNTAX, sono quasi sempre etichette enum
# (es. DEFVAL { timeTicks }): in quella posizione non vanno toccati
TYPE_KEYWORDS = {"Integer32", "Unsigned32", "Counter32", "Counter64", "Gauge32", "TimeTicks", "IpAddress",
                 "Opaque", "Counter", "Gauge", "NetworkAddress", "INTEGER", "BITS"}

# tipi di base definiti in SNMPv2-SMI: molte MIB li usano senza importarli
SMI_BASE_TYPES = ("Integer32", "Unsigned32", "Counter32", "Counter64", "Gauge32", "TimeTicks",
                  "IpAddress", "Opaque")

TOKEN_RE = re.compile(
    r'(?P<comment>--.*?(?:--|$))'
    r'|(?P<string>"[^"]*")'
    r'|(?P<assign>::=)'
    r'|(?P<ident>[A-Za-z_](?:[A-Za-z0-9_]|-(?!-))*)'
    r'|(?P<ws>\s+)'
    r'|(?P<other>.)',
    re.M | re.S,
)


def _tokenize(text):
    return [[m.lastgroup, m.group()] for m in TOKEN_RE.finditer(text)]


def _fix_chars(name):
    if "_" not in name:
        return name
    name = re.sub(r"_+", "-", name)
    return re.sub(r"-{2,}", "-", name).strip("-") or "x"


def _lower_first(name):
    """FooValue -> fooValue, UPSStatus -> upsStatus, UPS-Name -> ups-Name."""
    run = re.match(r"[A-Z]*", name).group()
    if len(run) > 1 and name[len(run):len(run) + 1].islower():
        run = run[:-1]  # l'ultima maiuscola apre la parola successiva
    return run.lower() + name[len(run):] if run else name


def _upper_first(name):
    return name[:1].upper() + name[1:]


def fix_mib(text, symbols_of=None, module_name_of=None):
    """Restituisce (testo corretto, lista modifiche [(riga, vecchio, nuovo)]).

    symbols_of(modulo) -> insieme dei simboli definiti in un modulo importato (o None se ignoto);
    serve a correggere la capitalizzazione dei simboli importati.
    module_name_of(modulo) -> nome corretto di un modulo importato scritto con un'altra
    capitalizzazione (o None se va bene così / sconosciuto).
    """
    toks = _tokenize(text)
    sig = [i for i, (k, _) in enumerate(toks) if k not in ("ws", "comment")]

    def s(j):  # testo del j-esimo token significativo
        return toks[sig[j]][1] if 0 <= j < len(sig) else ""

    def canon(t):
        return KEYWORD_MAP.get(t.lower(), t)

    # --- 1. definizioni, import, posizione dei token -----------------------------------
    value_defs, type_defs = [], []
    imports = {}            # simbolo -> modulo
    ctx = [None] * len(sig)  # 'type' | 'value' | 'enum' per ogni token significativo
    depth = 0
    seq_depth = None         # profondità del blocco SEQUENCE { ... } corrente
    in_imports = False
    imports_j = smi_from_j = None  # posizione di IMPORTS e del FROM SNMPv2-SMI
    in_macro = False
    defval_depth = None
    enum_labels = []
    pending = []
    for j in range(len(sig)):
        t = s(j)
        kind = toks[sig[j]][0]
        # le definizioni di MACRO (moduli SMI di base) hanno una grammatica propria: non si toccano
        if in_macro or (kind == "ident" and canon(s(j + 1)) == "MACRO"):
            in_macro = canon(t) != "END" or not in_macro
            ctx[j] = "macro"
            continue
        if t == "{":
            if canon(s(j - 1)) in ("SEQUENCE", "CHOICE") and seq_depth is None:
                seq_depth = depth + 1
            if canon(s(j - 1)) == "DEFVAL":
                defval_depth = depth + 1
            depth += 1
            continue
        if t == "}":
            if seq_depth == depth:
                seq_depth = None
            if defval_depth == depth:
                defval_depth = None
            depth -= 1
            continue
        if kind != "ident" or ctx[j] == "module":
            continue
        up = canon(t)
        if up == "IMPORTS":
            in_imports = True
            imports_j = j
            continue
        if in_imports:
            if up == "FROM":
                module = s(j + 1)
                if module == "SNMPv2-SMI" and pending:
                    smi_from_j = j
                for sym in pending:
                    imports[sym] = module
                pending = []
                ctx[j + 1] = "module"
            elif ctx[j] != "module":
                pending.append(t)
            if s(j + 1) == ";" or (up == "FROM" and s(j + 2) == ";"):
                in_imports = False
            continue
        prev, nxt = s(j - 1), s(j + 1)
        is_kw = t.lower() in KEYWORD_MAP
        if depth == 0 and not is_kw and (
                canon(nxt) in VALUE_MACROS or
                (canon(nxt) == "OBJECT" and canon(s(j + 2)) == "IDENTIFIER" and s(j + 3) == "::=")):
            value_defs.append(t)
            ctx[j] = "value"
        elif depth == 0 and not is_kw and nxt == "::=":
            type_defs.append(t)
            ctx[j] = "type"
        elif nxt == "(" and prev in ("{", ","):
            ctx[j] = "enum"
            enum_labels.append(t)
        elif defval_depth is not None:
            ctx[j] = "defval"
        elif canon(prev) in ("SYNTAX", "OF", "WRITE-SYNTAX"):
            ctx[j] = "type"
        elif seq_depth is not None and depth == seq_depth:
            # membri di SEQUENCE/CHOICE: "nome Tipo, nome Tipo, ..."
            ctx[j] = "member" if prev in ("{", ",") else "type"
        else:
            ctx[j] = "value"

    # --- 2. mappe di rinomina ------------------------------------------------------------
    taken = set(value_defs) | set(type_defs) | set(imports)
    renames = {"value": {}, "type": {}}
    # etichette enum: devono iniziare con la minuscola per poter essere usate in DEFVAL
    enum_fix = {}
    for label in dict.fromkeys(enum_labels):
        new = _lower_first(_fix_chars(label))
        if new != label:
            enum_fix[label] = new

    def plan(name, kind):
        new = _fix_chars(name)
        new = _lower_first(new) if kind == "value" else _upper_first(new)
        if new == name:
            return
        base, n = new, 2
        while new in taken and new != name:
            new, n = f"{base}{n}", n + 1
        taken.add(new)
        renames[kind][name] = new

    for name in dict.fromkeys(value_defs):
        plan(name, "value")
    for name in dict.fromkeys(type_defs):
        plan(name, "type")

    module_fix = {}
    if module_name_of is not None:
        for mod in set(imports.values()):
            try:
                new = module_name_of(mod)
            except Exception:
                new = None
            if new and new != mod:
                module_fix[mod] = new
        imports = {sym: module_fix.get(mod, mod) for sym, mod in imports.items()}

    import_fix = {}
    if symbols_of is not None:
        by_module = {}
        for sym, mod in imports.items():
            by_module.setdefault(mod, []).append(sym)
        for mod, syms in by_module.items():
            try:
                known = symbols_of(mod)
            except Exception:
                known = None
            if not known:
                continue
            lower = {}
            for k in known:
                lower.setdefault(k.lower(), []).append(k)
            for sym in syms:
                cands = lower.get(sym.lower(), [])
                if sym not in known and len(cands) == 1:
                    import_fix[sym] = cands[0]

    exact_values = set(value_defs) | {import_fix.get(i, i) for i in imports if i[:1].islower()}
    exact_types = set(type_defs) | {import_fix.get(i, i) for i in imports if i[:1].isupper()}
    ci_index = {}
    for name in exact_values | exact_types:
        ci_index.setdefault(name.lower(), set()).add(name)

    def resolve(t, c):
        """Nome corretto per il token t nel contesto c, oppure None se da non toccare."""
        if c == "enum" or (c == "defval" and t in enum_fix):
            return enum_fix.get(t)
        if c == "defval":
            c = "value"  # DEFVAL { altroOggetto }
        if t in import_fix:
            return import_fix[t]
        is_val, is_type = t in exact_values, t in exact_types
        if is_val or is_type:
            if c == "type" and is_type:
                return renames["type"].get(t, t)
            if c != "type" and is_val:
                return renames["value"].get(t, t)
            return renames["value" if is_val else "type"].get(t, t)
        if c in ("enum", "macro", "member"):
            return None
        if t.lower() in KEYWORD_MAP:
            kw = KEYWORD_MAP[t.lower()]
            if c == "value" and t[:1].islower() and kw in TYPE_KEYWORDS:
                return None
            return kw
        cands = ci_index.get(t.lower())
        if cands:
            want_type = c == "type"
            pick = sorted(cands, key=lambda n: (n[:1].isupper() != want_type, n))[0]
            return resolve(pick, "type" if pick[:1].isupper() else "value")
        return None

    # --- 3. riscrittura ----------------------------------------------------------------
    changes, seen = [], set()
    line_of = _line_index(toks)
    for j, idx in enumerate(sig):
        kind, t = toks[idx]
        if kind != "ident":
            continue
        new = resolve(t, ctx[j]) if ctx[j] != "module" else module_fix.get(t)
        if new is None:
            new = t
        new = _fix_chars(new)  # nomi di moduli, etichette enum, ecc.
        if new != t:
            toks[idx][1] = new
            if (t, new) not in seen:
                seen.add((t, new))
                changes.append((line_of[idx], t, new))
        # "SYNTAX BITS" senza l'elenco { nome(n), ... } non è SMI valido: sul filo BITS viaggia
        # come OCTET STRING, quindi la sostituzione non cambia i valori scambiati con l'agent
        if toks[idx][1] == "BITS" and s(j - 1) == "SYNTAX" and s(j + 1) != "{":
            toks[idx][1] = "OCTET STRING"
            changes.append((line_of[idx], "SYNTAX BITS (senza elenco bit)", "SYNTAX OCTET STRING"))

    # --- 4. tipi di base SMI usati ma non importati ----------------------------------------
    missing = {}  # tipo -> riga del primo utilizzo
    for j, idx in enumerate(sig):
        t = toks[idx][1]
        if (ctx[j] == "type" and t in SMI_BASE_TYPES and t not in imports
                and t not in type_defs and t not in missing):
            missing[t] = line_of[idx]
    if missing and imports_j is not None:
        names = [t for t in SMI_BASE_TYPES if t in missing]
        if smi_from_j is not None:
            toks[sig[smi_from_j - 1]][1] += ", " + ", ".join(names)
        else:
            toks[sig[imports_j]][1] += "\n    " + ", ".join(names) + " FROM SNMPv2-SMI"
        for name in names:
            changes.append((missing[name], f"{name} (non importato)", f"{name} FROM SNMPv2-SMI"))
    return "".join(t for _, t in toks), changes


def _line_index(toks):
    lines, line = [], 1
    for _, t in toks:
        lines.append(line)
        line += t.count("\n")
    return lines


def annotate(text, changes, source_name):
    """Aggiunge in testa un commento che elenca le correzioni applicate."""
    if not changes:
        return text
    head = [f"-- File corretto automaticamente da SNMP MIB Browser (originale: {source_name})."]
    head += [f"--   riga {ln}: {old} -> {new}" for ln, old, new in changes]
    return "\n".join(head) + "\n\n" + text
