#!/usr/bin/env python3
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""l10n_check.py: проверка русских (или любых) каталогов перевода против английского источника.

Только stdlib Python 3.11+, без сети, только чтение проверяемых файлов.

Форматы (проверено по клонам 20.11.2026, см. review/README.md):
  craft-tsv  контекст<TAB>англ.<TAB>перевод  (storytold/craft-i18n locales/*/*.tsv; cadcraft,
             filmcraft, vectorcraft, craft-launcher crates/ui-egui/src/i18n/*.tsv)
  tsv2       англ.<TAB>перевод  (craft-anything crates/ui-egui/src/i18n/*.tsv)
  json       плоский/вложенный JSON: ключ = англ. текст (lightcraft locales/*.json) или ключ = id
             при наличии en.json рядом (solidcraft assets/locales/*.json)
  toml       FigCraft locales/*.toml: [ui] ключ = англ., значения строки или {one,few,many,other}
  rust       таблицы Rust: ("en","ru") / ("ctx","en","ru") в const/static, match-ветки
             "en" => "ru" (designcraft, gridcraft, effectcraft, materialcraft, texturecraft,
             soundcraft locales/<язык>/mod.rs)
  ftl        Fluent .ftl (в клонах не найдено; поддержка по спецификации Fluent, тест на фикстуре)

Подкоманды:
  check PATH...     проверить файлы каталогов (формат определяется сам или --format)
  discover ROOT...  найти каталоги языка --locale в папках и вывести TSV: программа, формат, путь
  glossary-info     показать, как прочитан glossary.tsv

Код возврата: 0 — нет ошибок (severity=error), 1 — есть ошибки (или предупреждения при
--fail-on warn), 2 — сбой запуска/чтения.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as _dt
import io
import json
import os
import re
import sys
import tomllib
from dataclasses import dataclass, field

import authorship as auth  # noqa: E402

VERSION = "1.3 (2026-11-20)"
L10N_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_GLOSSARY = os.path.join(L10N_ROOT, "glossary", "glossary.tsv")

SEVERITIES = ("error", "warn", "info")


@dataclass
class Entry:
    key: str                      # уникальный ключ в каталоге
    source: str | None            # английский текст (None, если неизвестен: id без en-файла)
    value: str | None             # перевод (для множественного числа — None)
    forms: dict | None = None     # формы мн. числа
    src_forms: dict | None = None # английские формы мн. числа
    context: str = ""
    line: int = 0
    kind: str = "plain"           # plain | plural | id | msg
    table: str = ""               # для Rust: имя таблицы
    default_variant: list = field(default_factory=list)


@dataclass
class Catalog:
    path: str
    fmt: str
    locale: str
    entries: list = field(default_factory=list)
    problems: list = field(default_factory=list)   # (severity, check, line, key, message)
    meta: dict = field(default_factory=dict)


@dataclass
class Finding:
    severity: str
    check: str
    program: str
    file: str
    line: int
    key: str
    en: str
    ru: str
    message: str


LOCALE_RE = re.compile(r"^[a-z]{2,3}([_-][A-Za-z0-9]{2,8})*$")
NON_LOCALE_STEMS = {
    "mod", "lib", "tests", "test", "table", "scan", "plural", "pseudo", "catalog", "system", "gaps",
    "audit", "detect", "lang", "translate", "effects", "ui", "live_tests", "build", "main", "en",
    "pt_functions", "es_functions", "i18n", "awaiting", "common",
}
LANG_WORDS = {
    "RUSSIAN": "ru", "GERMAN": "de", "FRENCH": "fr", "SPANISH": "es", "PORTUGUESE": "pt-br",
    "BRAZILIAN_PORTUGUESE": "pt-br", "JAPANESE": "ja", "SIMPLIFIED_CHINESE": "zh-hans",
    "TRADITIONAL_CHINESE": "zh-hant", "CHINESE": "zh", "UKRAINIAN": "uk", "CZECH": "cs",
    "POLISH": "pl", "GEORGIAN": "ka", "SWEDISH": "sv", "ITALIAN": "it", "KOREAN": "ko",
    "ARABIC": "ar", "HEBREW": "he", "TURKISH": "tr", "DUTCH": "nl", "GREEK": "el",
    "HUNGARIAN": "hu", "VIETNAMESE": "vi", "BOSNIAN": "bs", "SERBIAN": "sr", "ROMANIAN": "ro",
    "FINNISH": "fi", "DANISH": "da", "NORWEGIAN": "nb", "CATALAN": "ca", "BULGARIAN": "bg",
    "KAZAKH": "kk", "ESTONIAN": "et", "LATVIAN": "lv", "LITHUANIAN": "lt", "SLOVAK": "sk",
    "SLOVENIAN": "sl", "CROATIAN": "hr", "THAI": "th", "HINDI": "hi", "INDONESIAN": "id",
    "MALAY": "ms", "PERSIAN": "fa", "TAMIL": "ta", "BENGALI": "bn", "TELUGU": "te",
    "ENGLISH": "en", "HANS": "zh-hans", "HANT": "zh-hant",
}
CODE_TO_WORDS = collections.defaultdict(list)
for _w, _c in LANG_WORDS.items():
    CODE_TO_WORDS[_c].append(_w)


def norm_locale(code: str) -> str:
    return code.replace("_", "-").lower()


def rel(path: str) -> str:
    p = os.path.abspath(path)
    if p.startswith(L10N_ROOT + os.sep):
        return os.path.relpath(p, L10N_ROOT)
    return path


def short(s: str | None, n: int = 160) -> str:
    if s is None:
        return ""
    s = s.replace("\t", "\\t").replace("\n", "\\n").replace("\r", "\\r")
    return s if len(s) <= n else s[: n - 1] + "…"


def read_text(path: str) -> str:
    with open(path, "rb") as fh:
        data = fh.read()
    text = data.decode("utf-8")
    return text[1:] if text.startswith("\ufeff") else text


# --------------------------------------------------------------------------------------------
# Плейсхолдеры и разметка

RE_DOUBLE = re.compile(r"\{\{\s*([A-Za-z_$][\w.$-]*)\s*\}\}")
RE_FLUENT = re.compile(r"\{\s*([$-][A-Za-z][\w-]*)")
RE_BRACE = re.compile(r"\{[^{}\s]*\}")
RE_PRINTF = re.compile(r"%(?:\d+\$)?[-+0#]*(?:\d+|\*)?(?:\.\d+)?(?:hh|h|ll|l|L|z|j|t)?[diouxXeEfFgGaAcsp@]")
RE_DOLLAR = re.compile(r"(?<![\w\\$])\$[A-Za-z_][A-Za-z0-9_]*")
KNOWN_TAGS = "b|i|u|s|a|br|p|em|strong|code|span|sup|sub|small|big|font|img|li|ul|ol|kbd|tt|h[1-6]|hr|mark|del|ins|q|link"
RE_TAG = re.compile(r"</?(?:" + KNOWN_TAGS + r"|\d+)(?:\s[^<>]*)?/?>", re.I)
RE_MNEMONIC = re.compile(r"(?<![\w&])&(?=[A-Za-zА-Яа-яЁё0-9])(?![A-Za-z]+;|#\d+;)")
RE_URL = re.compile(r"(?:https?://|www\.)[^\s\"'<>)»]+", re.I)
RE_WORD = re.compile(r"[A-Za-zÀ-ÿА-Яа-яЁё]+")
RE_CYR = re.compile(r"[А-Яа-яЁё]")
RE_LAT = re.compile(r"[A-Za-z]")
FOREIGN_PRODUCTS = re.compile(
    r"\b(Adobe|Photoshop|Illustrator|InDesign|Premiere|After Effects|Lightroom|Acrobat|Autodesk|AutoCAD|"
    r"Fusion 360|SolidWorks|Figma|Microsoft|Excel|PowerPoint|CorelDRAW|Corel|"
    r"Affinity|Final Cut|DaVinci|Pro Tools|Cubase|Ableton|FL Studio|Cinema 4D|Keynote|LibreOffice)\b"
)
RE_COPYRIGHT = re.compile(r"©|\(c\)\s*\d{4}|copyright|все права защищены|all rights reserved", re.I)


def placeholders(text: str | None, fmt: str = "") -> collections.Counter:
    """Мультимножество плейсхолдеров: {{x}}, Fluent {$x}, {name}/{0}/{}/{:.2}, %s/%d/%1$s, $var."""
    c: collections.Counter = collections.Counter()
    if not text:
        return c
    rest = text
    for m in RE_DOUBLE.finditer(rest):
        c["{{" + m.group(1).strip() + "}}"] += 1
    rest = RE_DOUBLE.sub(" ", rest)
    if fmt == "ftl" or "{ $" in rest or "{$" in rest:
        for m in RE_FLUENT.finditer(rest):
            c["{" + m.group(1) + "}"] += 1
        rest = re.sub(r"\{\s*[$-][A-Za-z][\w-]*[^{}]*\}", " ", rest)
        rest = re.sub(r"\{\s*[$-][A-Za-z][\w-]*\s*->", " ", rest)
    implicit = 0
    positional = set()
    for m in RE_BRACE.finditer(rest):
        tok = m.group(0)
        if ":" in tok:
            # спецификация формата Rust ({:.0}, {n:2}, {date:%Y}) не часть имени: LightCraft
            # нарочно прячет англ. окончание мн. числа через {:.0} (docs/localization-*.md)
            tok = tok.split(":", 1)[0] + "}"
        inner = tok[1:-1]
        if inner == "":
            positional.add(implicit)   # {} в Rust берёт следующий неявный аргумент
            implicit += 1
        elif inner.isdigit():
            positional.add(int(inner))  # {0}, {1}: явный номер, перестановка законна
        else:
            c[tok] += 1
    for i in positional:
        c["{#%d}" % i] = 1
    rest = RE_BRACE.sub(" ", rest)
    rest = rest.replace("%%", " ")
    for m in RE_PRINTF.finditer(rest):
        c[m.group(0)] += 1
    rest = RE_PRINTF.sub(" ", rest)
    for m in RE_DOLLAR.finditer(rest):
        c[m.group(0)] += 1
    return c


def tags(text: str | None) -> collections.Counter:
    out = collections.Counter()
    for t in RE_TAG.findall(text or ""):
        name = re.match(r"</?\s*([A-Za-z0-9]+)", t).group(1).lower()
        out[("/" if t.startswith("</") else "") + name] += 1
    return out


def mnemonics(text: str | None) -> int:
    return len(RE_MNEMONIC.findall(text or ""))


def has_letters(text: str) -> bool:
    return any(ch.isalpha() for ch in text)


# --------------------------------------------------------------------------------------------
# TSV


def unescape_craft(s: str) -> tuple[str, str | None]:
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch != "\\":
            out.append(ch)
            i += 1
            continue
        if i + 1 >= len(s):
            return "".join(out), "обратный слэш в конце колонки (нужно \\\\)"
        nxt = s[i + 1]
        if nxt == "n":
            out.append("\n")
        elif nxt == "t":
            out.append("\t")
        elif nxt == "\\":
            out.append("\\")
        else:
            return "".join(out) + s[i:], f"неизвестный escape \\{nxt} (разрешены \\n, \\t, \\\\)"
        i += 2
    return "".join(out), None


def detect_tsv_columns(text: str) -> int:
    counts = collections.Counter()
    for line in text.split("\n")[:400]:
        line = line.rstrip("\r")
        if not line or line.lstrip().startswith("#"):
            continue
        counts[line.count("\t") + 1] += 1
    return counts.most_common(1)[0][0] if counts else 3


def load_tsv(path: str, locale: str, fmt: str | None = None) -> Catalog:
    text = read_text(path)
    ncols = 2 if fmt == "tsv2" else 3 if fmt == "craft-tsv" else detect_tsv_columns(text)
    fmt = "tsv2" if ncols == 2 else "craft-tsv"
    cat = Catalog(path, fmt, locale)
    cat.meta["header"] = [l for l in text.split("\n")[:40] if l.startswith("#")]
    seen: dict[str, int] = {}
    for i, raw in enumerate(text.split("\n"), 1):
        line = raw[:-1] if raw.endswith("\r") else raw
        if fmt == "tsv2":
            if not line.strip() or line.lstrip().startswith("#"):
                continue
        elif not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if fmt == "tsv2":
            if len(cols) != 2:
                cat.problems.append(("error", "parse", i, "", f"{len(cols)} колонок, ожидалось 2 (англ.<TAB>перевод)"))
                continue
            src = cols[0].replace("\\n", "\n")
            val = cols[1].rstrip().replace("\\n", "\n")
            key = src
            e = Entry(key=key, source=src, value=val, line=i)
        else:
            if len(cols) != 3:
                cat.problems.append(("error", "parse", i, "", f"{len(cols)} колонок, ожидалось 3 (контекст<TAB>англ.<TAB>перевод)"))
                continue
            bad = next((ch for ch in line if ch != "\t" and (ord(ch) < 32 or ord(ch) == 0x7F or ch == "\ufeff")), None)
            if bad is not None:
                cat.problems.append(("error", "parse", i, "", f"невидимый символ {bad!r} в строке"))
            ctx, e1 = unescape_craft(cols[0])
            src, e2 = unescape_craft(cols[1])
            val, e3 = unescape_craft(cols[2])
            for err in (e1, e2, e3):
                if err:
                    # правило craft-i18n (docs/catalog-format.md); в репозиториях программ парсеры свои
                    sev = "error" if is_craft_i18n_file(path) else "warn"
                    cat.problems.append((sev, "escape", i, src, err + ("" if sev == "error" else " — правило craft-i18n; проверить парсер программы")))
            if not src:
                cat.problems.append(("error", "parse", i, "", "пустой английский текст"))
                continue
            key = ctx + "\x1f" + src
            kind = {"@plural": "plural", "@id": "id", "@msg": "msg", "@msgplural": "msgplural"}.get(ctx, "plain")
            if kind == "msgplural" and is_craft_i18n_file(path):
                kind = "plain"
            if ctx.startswith("@") and kind == "plain":
                cat.problems.append(("error", "context", i, src, f"неизвестный служебный контекст {ctx!r} (в craft-i18n есть @plural, @id, @msg; @msgplural — только у VectorCraft)"))
            e = Entry(key=key, source=src, value=val, context=ctx, line=i, kind=kind)
            if kind in ("plural", "msgplural"):
                e.src_forms = {str(k): v for k, v in enumerate(src.split("|"))}
                e.forms = {str(k): v for k, v in enumerate(val.split("|"))} if val else {}
                e.value = None
            if kind == "id":
                e.source = None
        if key in seen:
            cat.problems.append(("error", "duplicate", i, short(e.source or key.replace("\x1f", " | ")), f"ключ повторяется (первый раз в строке {seen[key]})"))
            continue
        seen[key] = i
        cat.entries.append(e)
    return cat


# --------------------------------------------------------------------------------------------
# JSON / TOML


def _json_pairs_hook(dups: list):
    def hook(pairs):
        d = {}
        for k, v in pairs:
            if k in d:
                dups.append(k)
            d[k] = v
        return d
    return hook


def _flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            out.update(_flatten(v, prefix + k + "."))
        else:
            out[prefix + k] = v
    return out


def _json_lines(text: str) -> dict:
    lines = {}
    for i, line in enumerate(text.split("\n"), 1):
        m = re.match(r'\s*"((?:[^"\\]|\\.)*)"\s*:', line)
        if m:
            try:
                k = json.loads('"' + m.group(1) + '"')
            except Exception:  # noqa: BLE001
                continue
            lines.setdefault(k, i)
    return lines


def json_split_name(path: str) -> tuple[str, str]:
    """ru-formats.json -> ("ru", "-formats"); pt-BR.json -> ("pt-BR", "")."""
    base = os.path.basename(path)
    base = base[:-5] if base.endswith(".json") else base
    m = re.match(r"^([a-z]{2,3}(?:[_-](?:[A-Za-z]{2}|[A-Za-z]{4}|\d{3}))?)(-formats|-[a-z]+s)?$", base)
    if not m:
        return base, ""
    return m.group(1), m.group(2) or ""


def load_json_raw(path: str):
    text = read_text(path)
    dups: list = []
    data = json.loads(text, object_pairs_hook=_json_pairs_hook(dups))
    return data, dups, _json_lines(text)


def load_json(path: str, locale: str, en_path: str | None) -> Catalog:
    cat = Catalog(path, "json", locale)
    try:
        data, dups, lines = load_json_raw(path)
    except Exception as exc:  # noqa: BLE001
        cat.problems.append(("error", "parse", 0, "", f"JSON не читается: {exc}"))
        return cat
    for k in dups:
        cat.problems.append(("error", "duplicate", lines.get(k, 0), k, "ключ повторяется в JSON (побеждает последний)"))
    flat = _flatten(data) if isinstance(data, dict) else {}
    en = None
    if en_path:
        en_data, _, _ = load_json_raw(en_path)
        en = _flatten(en_data)
        cat.meta["en_path"] = en_path
    for k, v in flat.items():
        line = lines.get(k, lines.get(k.split(".")[-1], 0))
        if not isinstance(v, str):
            cat.problems.append(("warn", "parse", line, k, f"значение не строка: {type(v).__name__}"))
            continue
        src = en.get(k) if en is not None else k
        cat.entries.append(Entry(key=k, source=src if isinstance(src, str) else None, value=v, line=line))
    cat.meta["key_is_english"] = en is None
    return cat


def _toml_lines(text: str) -> dict:
    lines = {}
    section = ""
    for i, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        m = re.match(r"^\[([^\]]+)\]\s*$", s)
        if m:
            section = m.group(1).strip()
            continue
        m = re.match(r'^"((?:[^"\\]|\\.)*)"\s*=', s) or re.match(r"^([A-Za-z0-9_.-]+)\s*=", s)
        if m:
            k = m.group(1)
            if s.startswith('"'):
                try:
                    k = json.loads('"' + k + '"')
                except Exception:  # noqa: BLE001
                    pass
            lines.setdefault(section + "\x1f" + k, i)
    return lines


def load_toml(path: str, locale: str, en_path: str | None) -> Catalog:
    cat = Catalog(path, "toml", locale)
    text = read_text(path)
    try:
        data = tomllib.loads(text)
    except Exception as exc:  # noqa: BLE001
        cat.problems.append(("error", "parse", 0, "", f"TOML не читается (в т.ч. повтор ключа): {exc}"))
        return cat
    lines = _toml_lines(text)
    en = None
    if en_path:
        en = tomllib.loads(read_text(en_path))
        cat.meta["en_path"] = en_path
    cat.meta["sections"] = {}
    for section, table in data.items():
        if section == "meta" or not isinstance(table, dict):
            continue
        en_sec = en.get(section) if isinstance(en, dict) else None
        cat.meta["sections"][section] = en_sec is not None
        for k, v in table.items():
            key = section + "\x1f" + k
            line = lines.get(key, 0)
            src, src_forms = None, None
            if en_sec is not None:
                ev = en_sec.get(k)
                if isinstance(ev, dict):
                    src_forms = {kk: vv for kk, vv in ev.items() if isinstance(vv, str)}
                    src = src_forms.get("other")
                elif isinstance(ev, str):
                    src = ev
            elif en is None and section == "ui":
                src = k
            if isinstance(v, dict):
                forms = {kk: vv for kk, vv in v.items() if isinstance(vv, str)}
                cat.entries.append(Entry(key=key, source=src, value=None, forms=forms, src_forms=src_forms,
                                         line=line, kind="plural", context=section))
            elif isinstance(v, str):
                kind = "plain" if (en_sec is not None or section == "ui") else "id"
                cat.entries.append(Entry(key=key, source=src, value=v, line=line, kind=kind, context=section))
            else:
                cat.problems.append(("warn", "parse", line, k, f"значение не строка и не таблица форм: {type(v).__name__}"))
    return cat


# --------------------------------------------------------------------------------------------
# Fluent


def load_ftl(path: str, locale: str) -> Catalog:
    cat = Catalog(path, "ftl", locale)
    text = read_text(path)
    cur = None
    cur_attr = None
    buf: dict[str, list] = {}
    order: list[tuple[str, int]] = []
    for i, line in enumerate(text.split("\n"), 1):
        line = line.rstrip("\r")
        if line.startswith("#") or (not line.strip() and cur is None):
            continue
        m = re.match(r"^(-?[A-Za-z][\w-]*)\s*=\s?(.*)$", line)
        if m and not line[0].isspace():
            cur = m.group(1)
            cur_attr = cur
            if cur in buf:
                cat.problems.append(("error", "duplicate", i, cur, "сообщение Fluent повторяется"))
            buf[cur] = [m.group(2)]
            order.append((cur, i))
            continue
        if cur is None:
            cat.problems.append(("error", "parse", i, "", "строка вне сообщения Fluent"))
            continue
        ma = re.match(r"^\s+\.([A-Za-z][\w-]*)\s*=\s?(.*)$", line)
        if ma:
            cur_attr = cur + "." + ma.group(1)
            buf[cur_attr] = [ma.group(2)]
            order.append((cur_attr, i))
            continue
        if not line.strip():
            buf[cur_attr].append("")
        elif line[0].isspace():
            buf[cur_attr].append(line.strip())
        else:
            cat.problems.append(("error", "parse", i, "", "непонятная строка Fluent"))
    for key, line in order:
        val = "\n".join(buf[key]).strip()
        e = Entry(key=key, source=None, value=val, line=line)
        if "->" in val:
            variants = re.findall(r"^\s*(\*?)\[([^\]]+)\]", val, re.M)
            if variants:
                e.kind = "plural"
                e.forms = {v.strip(): "" for _, v in variants}
                e.default_variant = [v for star, v in variants if star]
        cat.entries.append(e)
    return cat


# --------------------------------------------------------------------------------------------
# Rust

RE_RAW_START = re.compile(r'b?r(#*)"')
RE_IDENT = re.compile(r"[A-Za-z_]\w*")
RE_NUM = re.compile(r"[0-9][0-9A-Za-z_.]*")
RE_CHAR = re.compile(r"'(\\(?:u\{[0-9A-Fa-f]+\}|x[0-9A-Fa-f]{2}|.)|[^\\'])'")
RE_LIFETIME = re.compile(r"'[A-Za-z_]\w*")
RE_UESC = re.compile(r"u\{([0-9A-Fa-f_]+)\}")


def _rust_string(text: str, j: int, line: int):
    """Обычная строка Rust с позиции после кавычки. Возвращает (значение, позиция после, строки)."""
    n = len(text)
    buf = []
    while j < n and text[j] != '"':
        c = text[j]
        if c == "\\":
            nx = text[j + 1] if j + 1 < n else ""
            if nx == "n":
                buf.append("\n"); j += 2
            elif nx == "t":
                buf.append("\t"); j += 2
            elif nx == "r":
                buf.append("\r"); j += 2
            elif nx == "0":
                buf.append("\0"); j += 2
            elif nx in "\\\"'":
                buf.append(nx); j += 2
            elif nx == "u":
                mm = RE_UESC.match(text, j + 1)
                if mm:
                    buf.append(chr(int(mm.group(1).replace("_", ""), 16)))
                    j = mm.end()
                else:
                    buf.append("\\u"); j += 2
            elif nx == "x":
                buf.append(chr(int(text[j + 2:j + 4], 16))); j += 4
            elif nx in "\r\n":
                j += 1
                while j < n and text[j] in " \t\r\n":
                    if text[j] == "\n":
                        line += 1
                    j += 1
            else:
                buf.append("\\" + nx); j += 2
        else:
            if c == "\n":
                line += 1
            buf.append(c)
            j += 1
    return "".join(buf), j + 1, line


def rust_tokens(text: str):
    """Токены Rust: ('str', значение, строка), ('id', имя, строка), ('p', знак, строка)."""
    i, n, line = 0, len(text), 1
    while i < n:
        ch = text[i]
        if ch == "\n":
            line += 1
            i += 1
            continue
        if ch.isspace():
            i += 1
            continue
        if text.startswith("//", i):
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        if text.startswith("/*", i):
            depth, i = 1, i + 2
            while i < n and depth:
                if text.startswith("/*", i):
                    depth += 1
                    i += 2
                elif text.startswith("*/", i):
                    depth -= 1
                    i += 2
                else:
                    if text[i] == "\n":
                        line += 1
                    i += 1
            continue
        if ch in "rb":
            m = RE_RAW_START.match(text, i)
            if m:
                hashes = m.group(1)
                start = m.end()
                end = text.find('"' + hashes, start)
                if end < 0:
                    return
                s = text[start:end]
                yield ("str", s, line)
                line += s.count("\n")
                i = end + 1 + len(hashes)
                continue
            if ch == "b" and i + 1 < n and text[i + 1] == '"':
                s, i, nl = _rust_string(text, i + 2, line)
                yield ("str", s, line)
                line = nl
                continue
        if ch == '"':
            s, i, nl = _rust_string(text, i + 1, line)
            yield ("str", s, line)
            line = nl
            continue
        if ch == "'":
            mm = RE_CHAR.match(text, i)
            if mm:
                i = mm.end()
                yield ("p", "char", line)
                continue
            mm = RE_LIFETIME.match(text, i)
            i = mm.end() if mm else i + 1
            continue
        if ch.isalpha() or ch == "_":
            mm = RE_IDENT.match(text, i)
            yield ("id", mm.group(0), line)
            i = mm.end()
            continue
        if ch.isdigit():
            mm = RE_NUM.match(text, i)
            yield ("p", "num", line)
            i = mm.end()
            continue
        if text.startswith("=>", i):
            yield ("p", "=>", line)
            i += 2
            continue
        if text.startswith("::", i):
            yield ("p", "::", line)
            i += 2
            continue
        yield ("p", ch, line)
        i += 1


SKIP_MACROS = {"format", "vec", "println", "eprintln", "print", "write", "writeln", "assert", "assert_eq",
               "assert_ne", "matches", "include_str", "concat", "panic", "debug_assert", "format_args"}


def rust_tables(text: str):
    """Записи каталога: список (таблица, вид, [строки], строка). вид: 'tuple' или 'arm'."""
    toks = list(rust_tokens(text))
    out = []
    names = [""] * len(toks)
    cur, depth, stmt_depth, pending = "", 0, None, None
    fn_name, fn_depth = "", None
    for idx, (k, v, ln) in enumerate(toks):
        nxt = toks[idx + 1] if idx + 1 < len(toks) else ("p", "", 0)
        if k == "id" and v in ("const", "static") and nxt[0] == "id":
            pending = toks[idx + 2][1] if nxt[1] == "mut" and idx + 2 < len(toks) else nxt[1]
        elif k == "id" and v == "fn" and nxt[0] == "id":
            fn_name, fn_depth = "fn:" + nxt[1], depth
        elif k == "id" and nxt == ("p", "!", nxt[2]) and idx + 2 < len(toks) and toks[idx + 2][1] in ("{", "(", "["):
            if v not in SKIP_MACROS and not cur and v != "macro_rules":
                cur, stmt_depth = "macro:" + v, depth
        if k == "p" and v == "=" and pending and not cur:
            cur, stmt_depth, pending = pending, depth, None
        names[idx] = cur or fn_name
        if k == "p" and v in "([{":
            depth += 1
        elif k == "p" and v in ")]}":
            depth -= 1
            if cur.startswith("macro:") and depth == stmt_depth:
                cur, stmt_depth = "", None
            if fn_depth is not None and depth == fn_depth and v == "}":
                fn_name, fn_depth = "", None
        elif k == "p" and v == ";" and cur and depth == stmt_depth:
            cur, stmt_depth, pending = "", None, None
    # кортежи только из строковых литералов: ("en", "ru") и ("ctx", "en", "ru")
    stack = []
    for idx, (k, v, ln) in enumerate(toks):
        if k == "p" and v in "([{":
            stack.append([idx, v, [], []])
            continue
        if k == "p" and v in ")]}":
            if not stack:
                continue
            open_idx, opener, items, curtok = stack.pop()
            if curtok:
                items.append(curtok)
            if opener == "(" and len(items) in (2, 3) and all(len(it) == 1 and it[0][0] == "str" for it in items):
                prev = toks[open_idx - 1] if open_idx > 0 else ("p", "", 0)
                if prev[0] != "id":  # не вызов функции f("a", "b")
                    out.append((names[open_idx], "tuple", [it[0][1] for it in items], toks[open_idx][2]))
            if stack:
                stack[-1][3].append(("grp", None, ln))
            continue
        if stack:
            if k == "p" and v == ",":
                if stack[-1][3]:
                    stack[-1][2].append(stack[-1][3])
                stack[-1][3] = []
            else:
                stack[-1][3].append((k, v, ln))
    # ветки match и макросов: "a" | "b" => "x",  => { "x" },  => Some("x")
    for idx, (k, v, ln) in enumerate(toks):
        if not (k == "p" and v == "=>"):
            continue
        lhs = []
        j = idx - 1
        while j >= 0 and toks[j][0] == "str":
            lhs.append(toks[j])
            if j - 1 >= 0 and toks[j - 1][0] == "p" and toks[j - 1][1] == "|":
                j -= 2
                continue
            break
        if not lhs:
            continue
        r = toks[idx + 1:idx + 5]
        val = None
        if r and r[0][0] == "str" and (len(r) < 2 or r[1][1] in (",", "}", ")")):
            val = r[0][1]
        elif len(r) >= 3 and r[0][1] == "{" and r[1][0] == "str" and r[2][1] == "}":
            val = r[1][1]
        elif len(r) >= 4 and r[0][1] == "Some" and r[1][1] == "(" and r[2][0] == "str" and r[3][1] == ")":
            val = r[2][1]
        if val is None:
            continue
        for t in reversed(lhs):
            out.append((names[idx], "arm", [t[1], val], t[2]))
    out.sort(key=lambda x: x[3])
    return out


def _lang_word(name: str) -> str | None:
    base = name.split(":")[-1].upper()
    for word in sorted(LANG_WORDS, key=len, reverse=True):
        if base == word or base.startswith(word + "_") or base.endswith("_" + word):
            return word
    return None


def rust_table_lang(name: str) -> str | None:
    w = _lang_word(name)
    return LANG_WORDS[w] if w else None


def rust_table_group(name: str, arity: int) -> str:
    base = name.split(":")[-1].upper()
    w = _lang_word(name)
    rest = base.replace(w, "", 1) if w else base
    rest = re.sub(r"(^|_)(EFFECTS|PANELS|ROWS|TABLE|CATALOG)(?=$|_)", "_", rest.strip("_")).strip("_")
    return f"{arity}:{rest}"


def rust_file_locale(path: str) -> str | None:
    stem = os.path.basename(path)[:-3]
    if stem == "mod":
        stem = os.path.basename(os.path.dirname(path))
    if stem in NON_LOCALE_STEMS or not LOCALE_RE.match(stem):
        return None
    return norm_locale(stem)


def load_rust(path: str, locale: str, table_filter: str | None = None) -> Catalog:
    cat = Catalog(path, "rust", locale)
    rows = rust_tables(read_text(path))
    file_loc = rust_file_locale(path)
    want = norm_locale(locale)
    selected = []
    for table, kind, strs, line in rows:
        tname = table.split(":")[-1]
        if table_filter:
            if not re.fullmatch(table_filter, tname):
                continue
        elif file_loc is not None:
            if file_loc != want:
                continue
            if table.startswith("fn:") and kind == "tuple":
                continue  # кортежи внутри функций — код, не каталог
        elif rust_table_lang(table) != want:
            continue
        selected.append((table, kind, strs, line))
    seen: dict[tuple, int] = {}
    groups = set()
    for table, kind, strs, line in selected:
        if len(strs) == 3:
            ctx, src, val = strs
            key = ctx + "\x1f" + src
        else:
            ctx, (src, val) = "", strs
            key = src
        groups.add(rust_table_group(table, len(strs)))
        tkey = (table, key)
        if tkey in seen:
            cat.problems.append(("error", "duplicate", line, short(src), f"ключ повторяется в {table or 'файле'} (первый раз в строке {seen[tkey]})"))
            continue
        seen[tkey] = line
        cat.entries.append(Entry(key=key, source=src, value=val, context=ctx, line=line, table=table))
    cat.meta["tables"] = sorted({t for t, *_ in selected})
    cat.meta["groups"] = groups
    cat.meta["file_locale"] = file_loc
    return cat


# --------------------------------------------------------------------------------------------
# Определение формата и эталона


def guess_format(path: str) -> str:
    low = path.lower()
    if low.endswith(".desktop"):
        return "desktop"
    if low.endswith(".md"):
        return "md"
    if low.endswith(".xml") or low.endswith(".xml.in") or low.endswith(".mime.xml"):
        return "xml"
    for ext, fmt in ((".tsv", "tsv"), (".json", "json"), (".toml", "toml"), (".rs", "rust"), (".ftl", "ftl")):
        if low.endswith(ext):
            return fmt
    raise ValueError(f"не знаю формат файла: {path}")


def is_craft_i18n_file(path: str) -> str | None:
    """Корень craft-i18n, если файл лежит в его locales/<язык>/."""
    p = os.path.abspath(path)
    root = os.path.dirname(os.path.dirname(os.path.dirname(p)))
    if os.path.basename(os.path.dirname(os.path.dirname(p))) == "locales" and os.path.isfile(os.path.join(root, "docs", "catalog-format.md")):
        return root
    return None


def craft_plural_forms(root: str | None, locale: str) -> int:
    if root:
        f = os.path.join(root, "tools", "plural_forms.tsv")
        if os.path.isfile(f):
            for line in read_text(f).split("\n"):
                cols = line.split("\t")
                if len(cols) >= 2 and cols[0] == locale and cols[1].isdigit():
                    return int(cols[1])
    return {"ru": 3, "uk": 3, "pl": 3, "cs": 3, "ja": 1, "zh-hans": 1, "zh-hant": 1, "ko": 1, "ar": 6}.get(locale, 2)


def sibling_locale_files(path: str, fmt: str) -> list[str]:
    """Тот же каталог на других языках (суррогат английского эталона)."""
    p = os.path.abspath(path)
    d = os.path.dirname(p)
    base = os.path.basename(p)
    out = []
    craft_root = is_craft_i18n_file(p)
    if craft_root:
        locs = os.path.join(craft_root, "locales")
        for loc in sorted(os.listdir(locs)):
            f = os.path.join(locs, loc, base)
            if loc != os.path.basename(d) and os.path.isfile(f):
                out.append(f)
        return out
    if fmt in ("tsv", "craft-tsv", "tsv2"):
        for f in sorted(os.listdir(d)):
            if f.endswith(".tsv") and f != base and LOCALE_RE.match(f[:-4]):
                out.append(os.path.join(d, f))
    elif fmt == "json":
        _, suffix = json_split_name(p)
        for f in sorted(os.listdir(d)):
            if not f.endswith(".json") or f == base:
                continue
            l2, s2 = json_split_name(f)
            if s2 == suffix and LOCALE_RE.match(l2) and norm_locale(l2) != "en":
                out.append(os.path.join(d, f))
    elif fmt == "rust":
        if base == "mod.rs":
            parent = os.path.dirname(d)
            for sub in sorted(os.listdir(parent)):
                f = os.path.join(parent, sub, "mod.rs")
                if sub != os.path.basename(d) and os.path.isfile(f) and LOCALE_RE.match(sub):
                    out.append(f)
        else:
            for f in sorted(os.listdir(d)):
                if f.endswith(".rs") and f != base and rust_file_locale(os.path.join(d, f)):
                    out.append(os.path.join(d, f))
    return out


def find_en_file(path: str, fmt: str) -> str | None:
    p = os.path.abspath(path)
    d = os.path.dirname(p)
    if fmt == "json":
        _, suffix = json_split_name(p)
        f = os.path.join(d, "en" + suffix + ".json")
        return f if os.path.isfile(f) and f != p else None
    if fmt == "toml":
        f = os.path.join(d, "en.toml")
        return f if os.path.isfile(f) and f != p else None
    if fmt == "ftl":
        loc_dir = os.path.dirname(d)
        for en in ("en-US", "en", "en-us", "en_US"):
            f = os.path.join(loc_dir, en, os.path.basename(p))
            if os.path.isfile(f) and f != p:
                return f
    return None


def load_catalog(path: str, locale: str, fmt: str | None = None, rust_table: str | None = None,
                 en_override: str | None = None) -> Catalog:
    fmt = fmt or guess_format(path)
    if fmt in ("tsv", "craft-tsv", "tsv2"):
        return load_tsv(path, locale, None if fmt == "tsv" else fmt)
    if fmt == "json":
        return load_json(path, locale, en_override if en_override is not None else find_en_file(path, "json"))
    if fmt == "toml":
        return load_toml(path, locale, en_override if en_override is not None else find_en_file(path, "toml"))
    if fmt == "rust":
        return load_rust(path, locale, rust_table)
    if fmt in ("desktop", "xml", "md"):
        return Catalog(path, fmt, locale)
    if fmt == "ftl":
        cat = load_ftl(path, locale)
        en = en_override or find_en_file(path, "ftl")
        if en:
            en_cat = load_ftl(en, "en")
            emap = {e.key: e for e in en_cat.entries}
            for e in cat.entries:
                if e.key in emap:
                    e.source = emap[e.key].value
                    e.src_forms = emap[e.key].forms
            cat.meta["en_path"] = en
            cat.meta["en_keys"] = set(emap)
        return cat
    raise ValueError(fmt)


def _pick_ref(per_lang: dict, ref: str, what: str):
    per_lang = {k: v for k, v in per_lang.items() if v}
    if not per_lang:
        return None, f"эталон не найден ({what}: пусто)", {}
    sizes = {k: len(v) for k, v in per_lang.items()}
    biggest = max(sizes, key=sizes.get)
    if ref in ("auto", "union"):
        u = set().union(*per_lang.values())
        return u, f"объединение {len(per_lang)} яз. ({what}); самый большой {biggest} = {sizes[biggest]}", sizes
    if ref == "largest":
        return per_lang[biggest], f"самый большой язык {biggest} ({what})", sizes
    loc = norm_locale(ref)
    if loc in per_lang:
        return per_lang[loc], f"язык {loc} ({what})", sizes
    return None, f"язык {ref} не найден среди: {', '.join(sorted(per_lang))}", sizes


def reference_keys(cat: Catalog, ref: str):
    """Ключи эталона: en-файл, если есть; иначе объединение (или выбранный) другой язык."""
    if cat.fmt in ("desktop", "xml", "md"):
        return None, "не каталог ключей (упаковка / документ)", {}
    if cat.fmt == "json" and cat.meta.get("en_path"):
        data, _, _ = load_json_raw(cat.meta["en_path"])
        return set(_flatten(data)), "en: " + rel(cat.meta["en_path"]), {}
    if cat.fmt == "toml" and cat.meta.get("en_path"):
        en = tomllib.loads(read_text(cat.meta["en_path"]))
        keys = set()
        for sec, table in en.items():
            if sec != "meta" and isinstance(table, dict):
                keys |= {sec + "\x1f" + k for k in table}
        return keys, "en: " + rel(cat.meta["en_path"]) + " (секции без en не сверяются)", {}
    if cat.fmt == "ftl" and cat.meta.get("en_keys") is not None:
        return cat.meta["en_keys"], "en: " + rel(cat.meta["en_path"]), {}
    if ref == "none":
        return None, "нет (сверка ключей отключена)", {}
    if cat.fmt == "rust" and cat.meta.get("file_locale") is None:
        per_lang: dict = collections.defaultdict(set)
        groups = cat.meta.get("groups", set())
        for table, kind, strs, line in rust_tables(read_text(cat.path)):
            tl = rust_table_lang(table)
            if not tl or tl == cat.locale or rust_table_group(table, len(strs)) not in groups:
                continue
            per_lang[tl].add(strs[0] + "\x1f" + strs[1] if len(strs) == 3 else strs[0])
        return _pick_ref(per_lang, ref, "таблицы других языков в том же файле")
    files = sibling_locale_files(cat.path, cat.fmt)
    if not files:
        return None, "эталон не найден (нет en-файла и других языков рядом)", {}
    per_lang = {}
    for f in files:
        if cat.fmt == "rust":
            loc = rust_file_locale(f) or f
        elif is_craft_i18n_file(f):
            loc = os.path.basename(os.path.dirname(f))
        elif cat.fmt == "json":
            loc = json_split_name(f)[0]
        else:
            loc = os.path.basename(f).rsplit(".", 1)[0]
        try:
            other = load_catalog(f, norm_locale(loc), "rust" if cat.fmt == "rust" else (cat.fmt if cat.fmt != "json" else "json"),
                                 en_override="" if cat.fmt == "json" else None)
        except Exception:  # noqa: BLE001
            continue
        per_lang[norm_locale(loc)] = {e.key for e in other.entries}
    return _pick_ref(per_lang, ref, "другие языки того же каталога")


# --------------------------------------------------------------------------------------------
# Глоссарий


@dataclass
class GlossTerm:
    en: str
    pattern: re.Pattern
    ru_alts: list
    status: str
    scope: str | None
    line: int
    where: set = field(default_factory=set)


def _ru_norm(s: str) -> str:
    return s.lower().replace("ё", "е")


def _ru_stem(word: str) -> str:
    w = _ru_norm(word)
    if not RE_CYR.search(w):
        return w
    if len(w) > 6:
        return w[:-2]
    if len(w) >= 4:
        return w[:-1]
    return w


GLOSSARY_FORMAT = "en<TAB>ru<TAB>где_встречается<TAB>источник<TAB>пометка (первая строка — заголовок; минимум en<TAB>ru)"


def load_glossary(path: str | None, statuses: str = "accepted") -> tuple[list, str]:
    if not path or path == "none":
        return [], "Глоссарий: отключён (--glossary none)"
    if not os.path.isfile(path):
        return [], f"Глоссарий: файла {rel(path)} нет — проверка пропущена. Ожидаемый формат: {GLOSSARY_FORMAT}"
    rows = list(csv.reader(io.StringIO(read_text(path)), delimiter="\t", quoting=csv.QUOTE_NONE))
    rows = [r for r in rows if r and r[0].strip() and not r[0].lstrip().startswith("#")]
    header = [h.strip().lower() for h in rows[0]] if rows else []
    has_header = bool(header) and header[0] == "en"
    idx_status = idx_where = None
    if has_header:
        idx_where = next((i for i, h in enumerate(header) if h in ("где_встречается", "где", "programs", "scope")), None)
        idx_status = next((i for i, h in enumerate(header) if h in ("пометка", "статус", "status", "примечание", "note")), None)
    terms, skipped = [], 0
    for n, row in enumerate(rows[1:] if has_header else rows, 2 if has_header else 1):
        if not row or not row[0].strip() or row[0].startswith("#") or len(row) < 2:
            continue
        en, ru = row[0].strip(), row[1].strip()
        note = row[idx_status].strip() if idx_status is not None and idx_status < len(row) else (row[2].strip() if len(row) > 2 else "")
        st = note.lower()
        status = ("accepted" if st.startswith("принят") else "proposed" if st.startswith("предлож")
                  else "disputed" if st.startswith("спорн") else "unknown" if st else "accepted")
        scope = None
        msc = re.match(r"принят\s+(?:только\s+)?для\s+([\w-]+)", st)
        if msc:
            scope = msc.group(1).lower()
        if statuses == "accepted" and status != "accepted":
            skipped += 1
            continue
        if statuses == "accepted+proposed" and status not in ("accepted", "proposed"):
            skipped += 1
            continue
        base = re.sub(r"\s*\((?!s\))[^)]*\)\s*$", "", en).strip()
        if not ru or not base or "/" in base:
            skipped += 1
            continue
        pat = re.escape(base).replace(r"\(s\)", "s?").replace(r"\ ", r"\s+")
        alts = [a.strip() for a in re.split(r"\s+/\s+|\s+или\s+|;", ru) if a.strip()]
        where = set()
        if idx_where is not None and idx_where < len(row):
            for w in row[idx_where].split(","):
                w = w.strip().lower()
                if w:
                    where.add("common" if w.startswith("common") else w.split()[0])
        terms.append(GlossTerm(en, re.compile(r"(?<![\w-])" + pat + r"(?![\w-])", re.I), alts, status, scope, n, where))
    return terms, f"Глоссарий: `{rel(path)}` — терминов в проверке {len(terms)} (статусы: {statuses}), пропущено строк {skipped}"


def glossary_ok(value: str, alts: list) -> bool:
    v = _ru_norm(value)
    for alt in alts:
        words = [w for w in re.split(r"[\s\-–—]+", alt) if w and has_letters(w)]
        if words and all(_ru_stem(w) in v for w in words):
            return True
    return False


# --------------------------------------------------------------------------------------------
# Проверки


@dataclass
class Options:
    locale: str = "ru"
    ref: str = "auto"
    max_ratio: float = 1.5
    ratio_min_en: int = 4
    short_en: int = 25
    max_len: int = 40
    glossary: list = field(default_factory=list)
    glossary_desc: str = ""
    program: str = ""
    examples: int = 15
    bot_patterns: list = field(default_factory=list)
    _commit_repos: set = field(default_factory=set)  # уже просканированные git-корни


RU_PLURAL = ("one", "few", "many", "other")


def craft_template_problem(source: str) -> str | None:
    literal, after_ph, rest = 0, False, source
    while "{" in rest:
        before, after_open = rest.split("{", 1)
        if "}" not in after_open:
            return "@msg-шаблон: «{» без «}» — никогда не совпадёт"
        if not before and after_ph:
            return "@msg-шаблон: два плейсхолдера подряд — никогда не совпадёт"
        literal += len(before)
        after_ph = True
        rest = after_open.split("}", 1)[1]
    if after_ph and literal + len(rest) == 0:
        return "@msg-шаблон без текста — совпадёт с любым сообщением"
    return None


def guess_program(path: str) -> str:
    if is_craft_i18n_file(path):
        return "craft-i18n:" + os.path.basename(path).rsplit(".", 1)[0]
    parts = rel(path).split(os.sep)
    if parts[0] in ("apps", "cli", "docs") and len(parts) > 1:
        return parts[2] if parts[1] == "src" and len(parts) > 2 else parts[1]
    if parts[0] == "packaging" and len(parts) > 2 and parts[1] == "src":
        return parts[2]
    if parts[0] == "craft-i18n":
        return "craft-i18n:" + os.path.basename(path).rsplit(".", 1)[0]
    if parts[0] == "solidcraft":
        return "solidcraft"
    return parts[0] if parts[0] not in ("", "..") else os.path.basename(path)


def _diff_counter(a: collections.Counter, b: collections.Counter) -> str:
    parts = []
    if a - b:
        parts.append("пропал: " + ", ".join(sorted((a - b).elements())))
    if b - a:
        parts.append("лишний: " + ", ".join(sorted((b - a).elements())))
    return "; ".join(parts)


def check_catalog(cat: Catalog, opt: Options) -> tuple[list, dict]:
    prog = opt.program or guess_program(cat.path)
    F: list[Finding] = []
    fname = rel(cat.path)

    def add(sev, check, e, msg, line=None, key=None, en=None, ru=None, file=None):
        if e is not None:
            ru_text = e.value if e.value is not None else " | ".join((e.forms or {}).values())
        F.append(Finding(sev, check, prog, file if file is not None else fname,
                         line if line is not None else (e.line if e else 0),
                         short(key if key is not None else (e.key.replace("\x1f", " | ") if e else ""), 120),
                         short(en if en is not None else (e.source if e else "")),
                         short(ru if ru is not None else (ru_text if e else "")),
                         msg))

    for sev, check, line, key, msg in cat.problems:
        add(sev, check, None, msg, line=line, key=key, en="", ru="")

    root = auth.git_root(cat.path)
    under_review = os.path.abspath(cat.path).startswith(os.path.join(L10N_ROOT, "review") + os.sep)
    auth.check_header(cat, add, repo=None if under_review else root)
    auth.check_bot_names_in_file(cat, opt.bot_patterns, add)
    if opt.bot_patterns and root and root not in opt._commit_repos:
        if not under_review:
            opt._commit_repos.add(root)
            for row in auth.scan_local_commits(root, opt.bot_patterns, rel):
                sev, check, msg, line, key, en, ru = row[:7]
                file = row[7] if len(row) > 7 and row[7] else rel(root)
                add(sev, check, None, msg, line=line, key=key, en=en, ru=ru, file=file)

    craft_root = is_craft_i18n_file(cat.path)
    strict_keys = cat.fmt in ("json", "toml", "ftl") and bool(cat.meta.get("en_path"))
    nforms = craft_plural_forms(craft_root, opt.locale) if cat.fmt == "craft-tsv" else None

    if craft_root and not any(h.startswith("# Clean room:") for h in cat.meta.get("header", [])):
        add("error", "clean-room-header", None, "нет строки «# Clean room:» в заголовке (CI craft-i18n её требует: docs/catalog-format.md)", line=1, key="", en="", ru="")

    ru_words: collections.Counter = collections.Counter()
    for e in cat.entries:
        src = e.source
        # ---------- множественное число
        if e.forms is not None:
            forms = e.forms
            if cat.fmt == "craft-tsv":
                vals = list(forms.values())
                if not vals or any(not v for v in vals):
                    add("error", "empty", e, "пустой перевод или пустая форма @plural")
                elif nforms and len(vals) != nforms:
                    add("error" if craft_root else "warn", "plural-forms", e, f"{len(vals)} форм(ы), для «{opt.locale}» нужно {nforms} (one|few|many через «|»)")
                sf = list((e.src_forms or {}).values())
                if craft_root and len(sf) != 2:
                    add("error", "plural-forms", e, "английский источник @plural должен быть one|other")
                ref_ph = placeholders(sf[-1]) if sf else collections.Counter()
                for v in vals:
                    if v and set(placeholders(v)) != set(ref_ph):
                        add("error", "placeholders", e, f"форма «{short(v, 60)}»: плейсхолдеры {sorted(placeholders(v))} ≠ англ. {sorted(ref_ph)}")
                        break
            elif cat.fmt == "toml":
                cats = set(forms)
                unknown = cats - {"zero", "one", "two", "few", "many", "other"}
                if unknown:
                    add("error", "plural-forms", e, f"неизвестные категории: {sorted(unknown)}")
                if "other" not in cats:
                    add("error", "plural-forms", e, "нет обязательной формы other")
                if opt.locale == "ru":
                    miss = [c for c in RU_PLURAL if c not in cats]
                    if miss:
                        add("warn", "plural-forms", e, f"для русского не хватает форм: {', '.join(miss)} (нужны one/few/many/other)")
                ref = placeholders((e.src_forms or {}).get("other") or src)
                for c, v in forms.items():
                    if not v.strip():
                        add("error", "empty", e, f"пустая форма {c}")
                    elif set(placeholders(v)) != set(ref):
                        add("error", "placeholders", e, f"форма {c}: плейсхолдеры {sorted(placeholders(v))} ≠ англ. {sorted(ref)}")
            elif cat.fmt == "ftl":
                cats = set(forms)
                if opt.locale == "ru" and cats & set(RU_PLURAL) and not set(RU_PLURAL) <= cats:
                    add("warn", "plural-forms", e, f"выбор по числу: есть {sorted(cats)}, для ru нужны one/few/many/other")
                if not e.default_variant:
                    add("error", "plural-forms", e, "в селекторе нет варианта по умолчанию *[...]")
            for v in forms.values():
                ru_words.update(w.lower() for w in RE_WORD.findall(v) if RE_CYR.search(w))
            if cat.fmt != "ftl":
                continue
        val = e.value
        if val is None:
            continue
        ru_words.update(w.lower() for w in RE_WORD.findall(val) if RE_CYR.search(w))
        # ---------- пустые
        if not val.strip():
            add("error" if cat.fmt in ("craft-tsv", "tsv2", "rust") else "warn", "empty", e,
                "пустой перевод (в craft-i18n — ошибка CI; в остальных строка покажется по-английски)")
            continue
        if src is None:
            continue
        # ---------- непереведённые
        if val == src and RE_LAT.search(src) and e.forms is None:
            single = len(src.split()) == 1 or src.isupper() or bool(re.search(r"\d", src))
            add("info" if single else "warn", "untranslated", e,
                "совпадает с английским" + (" (имя/бренд/единица? может быть намеренно)" if single else ""))
        # ---------- плейсхолдеры
        if e.kind != "id":
            ps, pv = placeholders(src, cat.fmt), placeholders(val, cat.fmt)
            if cat.fmt == "ftl":
                if set(ps) != set(pv):
                    add("error", "placeholders", e, "переменные Fluent не совпадают; " + _diff_counter(collections.Counter(set(ps)), collections.Counter(set(pv))))
            elif ps != pv:
                add("error", "placeholders", e, "плейсхолдеры не совпадают; " + _diff_counter(ps, pv))
            if e.kind == "msg":
                pr = craft_template_problem(src)
                if pr:
                    add("error" if craft_root else "warn", "msg-template", e,
                        pr + ("" if craft_root else " (правило craft-i18n; разбор шаблонов в программе может отличаться)"))
        # ---------- разметка
        ts, tv = tags(src), tags(val)
        if ts != tv:
            add("error", "markup", e, f"теги не совпадают; {_diff_counter(ts, tv)}")
        if src.count("\n") != val.count("\n"):
            add("warn", "newlines", e, f"переносов строки (\\n): англ. {src.count(chr(10))}, перевод {val.count(chr(10))}")
        if src.count("\t") != val.count("\t"):
            add("warn", "tabs", e, f"табуляций: англ. {src.count(chr(9))}, перевод {val.count(chr(9))}")
        if mnemonics(src) != mnemonics(val):
            add("warn", "mnemonic", e, f"&-мнемоник: англ. {mnemonics(src)}, перевод {mnemonics(val)}")
        if src[:1].isspace() != val[:1].isspace() or src[-1:].isspace() != val[-1:].isspace():
            add("warn", "whitespace", e, "пробел в начале/конце есть только в одном из текстов")
        s_end, v_end = src.rstrip(), val.rstrip()
        if s_end.endswith("…") != v_end.endswith("…"):
            dots = s_end.endswith("...") or v_end.endswith("...")
            add("error" if (cat.fmt == "craft-tsv" and not dots) else "warn", "ellipsis", e,
                "конечное «…» есть только в одном из текстов" + (" (в другом — «...»)" if dots else ""))
        if "..." in val and "..." not in src:
            add("warn", "ellipsis-dots", e, "в переводе «...» (три точки), в английском их нет — нужен символ «…»")
        if s_end.endswith(":") != v_end.endswith(":"):
            add("info", "colon", e, "двоеточие в конце есть только в одном из текстов")
        for w in RE_WORD.findall(val):
            if RE_CYR.search(w) and RE_LAT.search(w):
                add("warn", "mixed-script", e, f"слово «{w}» смешивает кириллицу и латиницу (подмена букв?)")
                break
        # ---------- длина
        ls, lv = len(src), len(val)
        if ls >= opt.ratio_min_en and lv / ls > opt.max_ratio:
            add("info", "length-ratio", e, f"длина ru/en = {lv}/{ls} = {lv / ls:.2f} > {opt.max_ratio}")
        if ls <= opt.short_en and lv > opt.max_len:
            add("warn", "length-abs", e, f"короткая англ. строка ({ls} симв.) → перевод {lv} > {opt.max_len}: проверить обрезку на снимке")
        # ---------- чистая комната: видимые маркеры
        src_urls = {u.rstrip(".,;:!?") for u in RE_URL.findall(src)}
        for u in RE_URL.findall(val):
            u = u.rstrip(".,;:!?")
            if u not in src_urls:
                add("warn", "clean-room", e, f"в переводе URL, которого нет в английском: {u}")
        if RE_COPYRIGHT.search(val) and not RE_COPYRIGHT.search(src):
            add("warn", "clean-room", e, "в переводе копирайт, которого нет в английском")
        for m in FOREIGN_PRODUCTS.finditer(val):
            if m.group(0).lower() not in src.lower():
                add("warn", "clean-room", e, f"в переводе имя чужого продукта «{m.group(0)}», которого нет в английском")
        # ---------- глоссарий
        if opt.glossary and e.kind != "id":
            pbase = prog.lower().split(":")[-1]
            hits = [t for t in opt.glossary if (not t.scope or t.scope in pbase)
                    and (not t.where or pbase in t.where) and t.pattern.search(src)]
            by_pat: dict = collections.defaultdict(list)
            for t in hits:
                by_pat[t.pattern.pattern].append(t)
            for same in by_pat.values():
                alts = [a for t in same for a in t.ru_alts]
                if not glossary_ok(val, alts):
                    add("warn", "glossary", e, f"«{same[0].en.split(' (')[0]}» → по глоссарию «{' / '.join(alts)}» "
                        f"(glossary.tsv:{','.join(str(t.line) for t in same)}; термин помечен для: {', '.join(sorted(same[0].where)) or 'всех'})")

    # ---------- ё/е
    yo = {w for w in ru_words if "ё" in w}
    for w, cnt in sorted(ru_words.items()):
        if "е" in w and "ё" not in w:
            for i, ch in enumerate(w):
                alt = w[:i] + "ё" + w[i + 1:]
                if ch == "е" and alt in yo:
                    add("info", "yo", None, f"«{w}» ({cnt}×) и «{alt}» ({ru_words[alt]}×) в одном каталоге", line=0, key=w, en="", ru=alt)
                    break

    # ---------- сверка ключей
    kset = {e.key for e in cat.entries}
    ref_keys, ref_desc, sizes = reference_keys(cat, opt.ref)
    missing, extra = [], []
    if ref_keys is not None:
        missing = sorted(ref_keys - kset)
        if cat.fmt == "toml":
            with_en = {s for s, has in cat.meta.get("sections", {}).items() if has}
            extra = sorted(k for k in kset - ref_keys if k.split("\x1f")[0] in with_en)
        else:
            extra = sorted(kset - ref_keys)
        key_is_en = cat.fmt in ("craft-tsv", "tsv2", "rust") or cat.meta.get("key_is_english")
        for k in missing:
            add("info", "missing", None, "нет в переводе (покажется по-английски)", line=0,
                key=k.replace("\x1f", " | "), en=k.split("\x1f")[-1] if key_is_en else "", ru="")
        lines = {e.key: e.line for e in cat.entries}
        for k in extra:
            add("error" if strict_keys else "warn", "extra", None,
                "ключа нет в " + ("en-файле — программа его не покажет" if strict_keys else "других языках: новый, устаревший или опечатка в ключе?"),
                line=lines.get(k, 0), key=k.replace("\x1f", " | "), en="", ru="")
    # ---------- craft-i18n: правила репозитория
    if craft_root and os.path.basename(cat.path) != "common.tsv":
        common = os.path.join(os.path.dirname(cat.path), "common.tsv")
        if os.path.isfile(common):
            cm = {e.key: (e.value, tuple((e.forms or {}).values())) for e in load_tsv(common, opt.locale, "craft-tsv").entries}
            for e in cat.entries:
                if e.key in cm and cm[e.key] == (e.value, tuple((e.forms or {}).values())):
                    add("error", "redundant-override", e, "совпадает с common.tsv (контекст, англ. и перевод): CI craft-i18n отвергает такое переопределение")
    if craft_root and os.path.basename(cat.path) == "common.tsv" and "@id\x1flanguage.name" not in kset:
        add("error", "language-name", None, "нет строки @id<TAB>language.name<TAB><имя языка>", line=0, key="", en="", ru="")

    summary = {
        "file": fname, "program": prog, "format": cat.fmt, "locale": cat.locale,
        "entries": len(cat.entries), "ref": ref_desc,
        "ref_keys": len(ref_keys) if ref_keys is not None else None,
        "missing": len(missing), "extra": len(extra),
        "tables": ", ".join(cat.meta.get("tables", [])) if cat.fmt == "rust" else "",
        "ref_sizes": sizes,
    }
    for s in SEVERITIES:
        summary[s] = sum(1 for f in F if f.severity == s)
    return F, summary


# --------------------------------------------------------------------------------------------
# Поиск каталогов

SKIP_DIRS = {".git", "target", "node_modules", "vendor", "third_party", "fixtures", "testdata", "dist", ".cargo", "pending"}


def discover(roots: list, locale: str) -> list:
    """(программа, формат, путь, примечание) для каталогов языка locale."""
    loc = norm_locale(locale)
    words = CODE_TO_WORDS.get(loc, [])
    table_re = re.compile(r"\b(?:const|static)\s+(?:" + "|".join(words) + r")\w*\s*:\s*&(?:'static\s+)?\[") if words else None
    out, seen = [], set()

    def push(row):
        if row[2] not in seen:
            seen.add(row[2])
            out.append(row)

    for root in roots:
        root = os.path.abspath(root)
        if not os.path.isdir(root):
            continue
        for d, dirs, files in os.walk(root):
            dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS and not x.startswith("."))
            base_d = os.path.basename(d)
            parent = os.path.basename(os.path.dirname(d))
            for f in sorted(files):
                p = os.path.join(d, f)
                stem, ext = os.path.splitext(f)
                ext = ext.lower()
                if ext == ".tsv":
                    if parent == "locales" and norm_locale(base_d) == loc and is_craft_i18n_file(p):
                        push((guess_program(p), "craft-tsv", p, "craft-i18n"))
                    elif norm_locale(stem) == loc and base_d == "i18n":
                        with open(p, encoding="utf-8", errors="replace") as fh:
                            fmt = "tsv2" if detect_tsv_columns(fh.read(40000)) == 2 else "craft-tsv"
                        push((guess_program(p), fmt, p, "каталог в репозитории программы"))
                elif ext == ".json" and base_d == "locales":
                    l2, _ = json_split_name(p)
                    if norm_locale(l2) == loc:
                        push((guess_program(p), "json", p, "en-файл рядом" if find_en_file(p, "json") else "ключ = англ. текст"))
                elif ext == ".toml" and base_d == "locales" and norm_locale(stem) == loc:
                    push((guess_program(p), "toml", p, "en.toml рядом" if find_en_file(p, "toml") else "ключ = англ. текст"))
                elif ext == ".ftl" and (norm_locale(base_d) == loc or norm_locale(base_d).startswith(loc + "-")):
                    push((guess_program(p), "ftl", p, "Fluent"))
                elif ext == ".desktop":
                    try:
                        with open(p, encoding="utf-8", errors="replace") as fh:
                            txt = fh.read()
                    except OSError:
                        continue
                    if re.search(r"^(Name|GenericName|Comment|Keywords)\[ru\]\s*=", txt, re.M):
                        push((guess_program(p), "desktop", p, "ярлык с русскими полями"))
                elif (low := f.lower()).endswith(".xml") or low.endswith(".xml.in"):
                    if not any(x in low for x in ("metainfo", "mime", "appdata")):
                        continue
                    try:
                        with open(p, encoding="utf-8", errors="replace") as fh:
                            txt = fh.read()
                    except OSError:
                        continue
                    if 'xml:lang="ru"' in txt or "xml:lang='ru'" in txt:
                        push((guess_program(p), "xml", p, "metainfo/mime с xml:lang=ru"))
                elif low.endswith(".ru.md"):
                    push((guess_program(p), "md", p, "русский документ"))
                elif ext == ".rs" and ("i18n" in d or "locales" in d or "i18n" in stem or "locali" in stem):
                    if (base_d in ("i18n",) and norm_locale(stem) == loc) or (stem == "mod" and parent == "locales" and norm_locale(base_d) == loc):
                        push((guess_program(p), "rust", p, "файл языка"))
                    elif table_re and stem not in ("tests",):
                        try:
                            with open(p, encoding="utf-8", errors="replace") as fh:
                                txt = fh.read()
                        except OSError:
                            continue
                        if table_re.search(txt):
                            push((guess_program(p), "rust", p, "таблица " + "/".join(words) + "* в общем файле"))
    return out


# --------------------------------------------------------------------------------------------
# Отчёты

CHECK_TITLES = {
    "parse": "Разбор файла", "escape": "Экранирование", "context": "Служебный контекст",
    "duplicate": "Дубликаты ключей", "empty": "Пустые переводы", "untranslated": "Совпадает с английским",
    "placeholders": "Плейсхолдеры", "msg-template": "@msg-шаблоны", "markup": "Теги разметки",
    "newlines": "Переносы \\n", "tabs": "Табуляции", "mnemonic": "&-мнемоники", "whitespace": "Пробелы по краям",
    "ellipsis": "Конечное «…»", "ellipsis-dots": "«...» вместо «…»", "colon": "Двоеточие в конце",
    "mixed-script": "Кириллица+латиница в слове", "length-ratio": "Длина ru/en",
    "length-abs": "Длинный перевод короткой строки", "clean-room": "Маркеры чистой комнаты",
    "clean-room-header": "Заголовок Clean room", "glossary": "Глоссарий", "yo": "ё/е в одном каталоге",
    "missing": "Нет в переводе", "extra": "Лишние ключи", "redundant-override": "Лишнее переопределение common",
    "language-name": "Имя языка", "plural-forms": "Формы множественного числа",
    "authorship-header": "Шапка авторства", "authorship-header-unsupported": "Формат без комментариев (шапка)",
    "authorship-header-breaks": "Шапка ломает формат", "authorship-header-placement": "Шапка не на месте",
    "authorship-header-comments": "Изменён авторский комментарий",
    "authorship-header-unneeded": "Шапка в файле без нашего перевода",
    "authorship-attribution": "Формулировка ATTRIBUTION.md (ru)", "assistant-name": "Имя исполнителя",
}


def write_tsv(path: str, findings: list):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    def clean(x) -> str:
        return short(str(x), 100000)  # \t и \n уже экранированы в short()

    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write("severity\tcheck\tprogram\tfile\tline\tkey\ten\tru\tmessage\n")
        for f in findings:
            fh.write("\t".join(clean(x) for x in (f.severity, f.check, f.program, f.file, f.line, f.key, f.en, f.ru, f.message)) + "\n")


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("`", "'")


def render_md(title: str, summaries: list, findings: list, opt: Options, tsv_path: str | None, argv: list) -> str:
    now = _dt.datetime.now().astimezone()
    errs = sum(s["error"] for s in summaries)
    warns = sum(s["warn"] for s in summaries)
    infos = sum(s["info"] for s in summaries)
    out = [f"# Ревизия локализации: {title}", ""]
    out.append(f"- Когда: {now:%Y-%m-%d %H:%M} {now.tzname()} (America/Los_Angeles)")
    out.append(f"- Инструмент: `review/tools/l10n_check.py` {VERSION}; запуск: `{md_escape(' '.join(argv))}`")
    out.append(f"- Язык `{opt.locale}`; эталон ключей `{opt.ref}`; длина: ru/en > {opt.max_ratio} при en ≥ {opt.ratio_min_en} — info; en ≤ {opt.short_en} и ru > {opt.max_len} — warn")
    out.append(f"- {opt.glossary_desc}")
    if tsv_path:
        out.append(f"- Все находки построчно: `{rel(tsv_path)}`")
    out.append(f"- **Итог: ошибок {errs}**, предупреждений {warns}, справочных {infos} — " + ("**НЕ ПРОЙДЕНО** (есть ошибки)" if errs else "ошибок нет"))
    out.append("")
    out.append("Достоверность: все цифры — **[проверено: подсчёт этим скриптом по файлам на box в момент запуска]**. "
               "Что значит находка, решает человек: «совпадает с английским», «длина» и «глоссарий» часто законны.")
    out.append("")
    out.append("## Каталоги")
    out.append("")
    out.append("| Программа | Файл | Формат | Записей | Эталон | Ключей в эталоне | Нет в переводе | Лишних | Ошибки | Предупр. | Справ. |")
    out.append("|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|")
    for s in summaries:
        fmt = s["format"] + (f" ({md_escape(s['tables'])})" if s.get("tables") else "")
        out.append(f"| {md_escape(s['program'])} | `{md_escape(s['file'])}` | {fmt} | {s['entries']} | {md_escape(s['ref'])} | "
                   f"{'—' if s['ref_keys'] is None else s['ref_keys']} | {s['missing']} | {s['extra']} | {s['error']} | {s['warn']} | {s['info']} |")
    out.append("")
    order = {s: i for i, s in enumerate(SEVERITIES)}
    by = collections.Counter((f.severity, f.check) for f in findings)
    if by:
        out.append("## Находки по видам")
        out.append("")
        out.append("| Важность | Проверка | Сколько |")
        out.append("|---|---|---:|")
        for (sev, chk), n in sorted(by.items(), key=lambda x: (order[x[0][0]], -x[1])):
            out.append(f"| {sev} | {CHECK_TITLES.get(chk, chk)} (`{chk}`) | {n} |")
        out.append("")
        out.append(f"## Примеры (до {opt.examples} на вид; полный список — в TSV)")
        out.append("")
        groups = collections.defaultdict(list)
        for f in findings:
            groups[(f.severity, f.check)].append(f)
        for (sev, chk), items in sorted(groups.items(), key=lambda x: (order[x[0][0]], x[0][1])):
            out.append(f"### {sev}: {CHECK_TITLES.get(chk, chk)} — {len(items)}")
            out.append("")
            out.append("| Файл:строка | Ключ / англ. | Перевод | Что не так |")
            out.append("|---|---|---|---|")
            for f in items[: opt.examples]:
                keyen = f.key if (not f.en or f.en in f.key) else f"{f.key} → {f.en}" if f.key != f.en else f.en
                out.append(f"| `{md_escape(os.path.basename(f.file))}:{f.line}` | {md_escape(short(keyen, 100))} | {md_escape(short(f.ru, 100))} | {md_escape(f.message)} |")
            out.append("")
    out.append("## Что скрипт не проверяет")
    out.append("")
    out.append("- **Чистая комната по существу** — совпадение с чужими публичными русскими переводами (Adobe, Autodesk, Microsoft, Figma…) без этих источников не определить: **не автоматизируемо**, проверяется процессом (кто и как переводил, запись в ATTRIBUTION, описание PR). Скрипт ловит только видимые маркеры: чужие URL, копирайты, имена чужих продуктов, которых нет в английском.")
    out.append("- **Живой интерфейс** (обрезка, «ё» в шрифте, переключение языка) — только по снимкам правообладателя: `review/screenshot-checklists/`.")
    out.append("- **Смысл, стиль, род/падеж**, согласование с числом в строках без форм мн. числа — только человек.")
    out.append("- **Полнота относительно кода**: эталон — en-файл, если он есть, иначе объединение других языков; строк, которых нет ни в одном каталоге, скрипт не видит. Для этого — штатные проверки репозиториев (`run_all.sh --native`).")
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------------------------
# CLI


def cmd_check(a, argv) -> int:
    terms, desc = load_glossary(a.glossary, a.glossary_status)
    bot_path = None if a.bot_names in ("none", "") else (a.bot_names or auth.DEFAULT_BOT_NAMES)
    opt = Options(locale=norm_locale(a.locale), ref=a.ref, max_ratio=a.max_ratio, ratio_min_en=a.ratio_min_en,
                  short_en=a.short_en, max_len=a.max_len, glossary=terms, glossary_desc=desc,
                  program=a.program or "", examples=a.examples,
                  bot_patterns=auth.compile_bot_patterns(bot_path))
    all_f, sums = [], []
    for path in a.paths:
        try:
            cat = load_catalog(path, opt.locale, None if a.format == "auto" else a.format, a.rust_table, a.en)
            f, s = check_catalog(cat, opt)
        except Exception as exc:  # noqa: BLE001
            print(f"ОШИБКА: не удалось проверить {path}: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 2
        all_f += f
        sums.append(s)
    keep = SEVERITIES[: SEVERITIES.index(a.min_severity) + 1]
    shown = [f for f in all_f if f.severity in keep]
    title = a.title or (sums[0]["program"] if len(sums) == 1 else f"{len(sums)} каталогов")
    md_path, tsv_path = a.md, a.tsv
    if a.out_dir:
        stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        name = re.sub(r"[^\w.-]+", "_", a.name or title)
        md_path = md_path or os.path.join(a.out_dir, f"{stamp}-{name}.md")
        tsv_path = tsv_path or os.path.join(a.out_dir, f"{stamp}-{name}.tsv")
    if tsv_path:
        write_tsv(tsv_path, shown)
    md = render_md(title, sums, shown, opt, tsv_path, ["l10n_check.py"] + argv)
    if md_path:
        os.makedirs(os.path.dirname(os.path.abspath(md_path)), exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write(md)
    if a.json_summary:
        print(json.dumps({"summaries": sums, "md": md_path, "tsv": tsv_path}, ensure_ascii=False, default=str))
    elif not a.quiet:
        print(md if not md_path else f"отчёт: {md_path}\nнаходки: {tsv_path}")
    errs = sum(s["error"] for s in sums)
    warns = sum(s["warn"] for s in sums)
    return 1 if errs or (a.fail_on == "warn" and warns) else 0


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    p = argparse.ArgumentParser(prog="l10n_check.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version=VERSION)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--locale", default="ru", help="проверяемый язык (ru); для пробы на других языках — de, fr…")
        sp.add_argument("--glossary", default=DEFAULT_GLOSSARY, help="путь к glossary.tsv или none")
        sp.add_argument("--glossary-status", default="accepted", choices=["accepted", "accepted+proposed", "all"],
                        help="какие термины проверять (по умолчанию только «принят»)")

    c = sub.add_parser("check", help="проверить каталоги")
    common(c)
    c.add_argument("paths", nargs="+")
    c.add_argument("--format", default="auto", choices=["auto", "craft-tsv", "tsv2", "tsv", "json", "toml", "rust", "ftl"])
    c.add_argument("--ref", default="auto", help="эталон ключей: auto (en-файл, иначе объединение языков) | union | largest | <код языка> | none")
    c.add_argument("--en", default=None, help="явный путь к английскому файлу (json/toml/ftl)")
    c.add_argument("--rust-table", default=None, help="regex имени таблицы Rust (напр. RUSSIAN|GERMAN)")
    c.add_argument("--max-ratio", type=float, default=1.5)
    c.add_argument("--ratio-min-en", type=int, default=4)
    c.add_argument("--short-en", type=int, default=25)
    c.add_argument("--max-len", type=int, default=40)
    c.add_argument("--program", default=None)
    c.add_argument("--title", default=None)
    c.add_argument("--md", default=None, help="путь markdown-отчёта")
    c.add_argument("--tsv", default=None, help="путь TSV с находками")
    c.add_argument("--out-dir", default=None, help="папка: <ГГГГММДД-ЧЧММСС>-<имя>.md/.tsv")
    c.add_argument("--name", default=None)
    c.add_argument("--examples", type=int, default=15)
    c.add_argument("--min-severity", default="info", choices=list(SEVERITIES), help="до какой важности писать находки")
    c.add_argument("--fail-on", default="error", choices=["error", "warn"])
    c.add_argument("--json-summary", action="store_true")
    c.add_argument("--quiet", action="store_true")
    c.add_argument("--assistant-names", default=auth.DEFAULT_BOT_NAMES,
                   help="список имён исполнителей (по умолчанию review/tools/bot_names.txt); none — не проверять")

    d = sub.add_parser("discover", help="найти каталоги языка")
    d.add_argument("roots", nargs="+")
    d.add_argument("--locale", default="ru")

    g = sub.add_parser("glossary-info", help="как прочитан глоссарий")
    common(g)
    g.add_argument("--limit", type=int, default=50)

    a = p.parse_args(argv)
    try:
        if a.cmd == "check":
            return cmd_check(a, argv)
        if a.cmd == "discover":
            w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
            for row in discover(a.roots, a.locale):
                w.writerow(row)
            return 0
        if a.cmd == "glossary-info":
            terms, desc = load_glossary(a.glossary, a.glossary_status)
            print(desc)
            for t in terms[: a.limit]:
                print(f"{t.line}\t{t.en}\t{' / '.join(t.ru_alts)}\t{t.status}\t{t.scope or ''}")
            return 0
    except BrokenPipeError:
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
