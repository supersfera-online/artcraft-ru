#!/usr/bin/env python3
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Шапка авторства и имена исполнителей (RULES-AUTHORSHIP.md). Подключается из l10n_check.py.

Достоверность поддержки комментариев — в COMMENT_POLICY (источник у каждой строки).
"""
from __future__ import annotations

import os
import re
import subprocess

HEADER_TEXT = "Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0"
DEFAULT_BOT_NAMES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bot_names.txt")

# fmt -> (supports_comments, comment_syntax_example, source)
# supports: True / False / None (не отдельный ru-файл — шапку не требуем)
COMMENT_POLICY = {
    "craft-tsv": (True, f"# {HEADER_TEXT}",
                  "проверено: craft-i18n docs/catalog-format.md («Lines starting with # and blank lines are ignored»); "
                  "crates/craft-i18n-tests/src/catalog.rs: line.starts_with('#'); "
                  "то же в парсерах cadcraft/filmcraft/vectorcraft/craft-launcher/photocraft (starts_with('#')); "
                  "эмпирически 20.11.2026: временная копия ru/common.tsv с шапкой первой строкой, "
                  "cargo test --workspace --locked — код 0"),
    "tsv2": (True, f"# {HEADER_TEXT}",
             "проверено: craft-anything crates/ui-egui/src/i18n.rs: «# comments», "
             "filter trim_start().starts_with('#'); тест catalog_parse_and_fallback"),
    "toml": (True, f"# {HEADER_TEXT}",
             "проверено: FigCraft crates/ui-egui/build.rs парсит toml::Table (комментарии «#» — часть TOML); "
             "в ru.toml уже есть комментарии в начале файла"),
    "rust": (True, f"// {HEADER_TEXT}",
             "проверено: синтаксис Rust; // перед //! допустим (модульная документация остаётся)"),
    "ftl": (True, f"# {HEADER_TEXT}",
            "проверено: Fluent (комментарии # / ## / ###); в клонах отдела .ftl нет, проверка — по спецификации и загрузчику l10n_check"),
    "desktop": (True, f"# {HEADER_TEXT}",
                "проверено: спецификация Desktop Entry (строки «#» — комментарии); парсер update-desktop-database их игнорирует"),
    "xml": (True, f"<!-- {HEADER_TEXT} -->",
            "проверено: XML-комментарии <!-- -->; в шаблонах metainfo/mime авторов уже есть комментарий сразу после <?xml?>"),
    "md": (True, f"<!-- {HEADER_TEXT} -->",
           "проверено: в Markdown комментарий — HTML <!-- -->; заголовок «# …» комментарием не является"),
    "json": (False, None,
             "проверено: LightCraft и SolidCraft читают serde_json::from_str (комментариев нет); "
             "RULES-AUTHORSHIP.md: «В JSON комментариев нет — отметка только в описании PR и коммите»"),
}


def comment_syntax(fmt: str) -> str:
    ok, syntax, _ = COMMENT_POLICY.get(fmt, (False, None, ""))
    return syntax or HEADER_TEXT


def _inner_hash(line: str) -> str | None:
    s = line.lstrip()
    if s.startswith("#"):
        return s[1:].strip()
    return None


def _inner_slash(line: str) -> str | None:
    s = line.lstrip()
    m = re.match(r"^//(/|!)?\s?(.*)$", s)
    return m.group(2).strip() if m else None


def first_comment(text: str, fmt: str) -> tuple[int, str, str] | None:
    """Первая строка-комментарий: (номер, сырая строка, текст внутри). Пропуск BOM, пустых и <?xml?>."""
    if text.startswith("\ufeff"):
        text = text[1:]
    if fmt in ("craft-tsv", "tsv2", "toml", "ftl", "desktop"):
        for i, line in enumerate(text.splitlines(), 1):
            if not line.strip():
                continue
            inner = _inner_hash(line)
            if inner is not None:
                return i, line, inner
            return None
        return None
    if fmt == "rust":
        i = 0
        for line in text.splitlines():
            i += 1
            if not line.strip():
                continue
            inner = _inner_slash(line)
            if inner is not None:
                return i, line, inner
            if line.lstrip().startswith("/*"):
                # однострочный или начало блока
                raw_lines = [line]
                start = i
                chunk = line
                if "*/" not in line:
                    rest = text.splitlines()[i:]
                    for j, nxt in enumerate(rest, i + 1):
                        raw_lines.append(nxt)
                        chunk += "\n" + nxt
                        if "*/" in nxt:
                            i = j
                            break
                inner = re.sub(r"^\s*/\*+!?\s*|\s*\*/\s*$", "", chunk, flags=re.S).strip()
                return start, "\n".join(raw_lines), inner
            return None  # первый непустой токен — не комментарий (код или #![attr])
        return None
    if fmt in ("xml", "md"):
        # пропустить объявление XML и пустые строки; найти первый <!-- -->
        pos = 0
        if fmt == "xml":
            m = re.match(r"\s*<\?xml[^?]*\?>\s*", text)
            if m:
                pos = m.end()
        # номер строки
        prefix = text[:pos]
        m = re.search(r"<!--(.*?)-->", text[pos:], re.S)
        if not m:
            return None
        start = pos + m.start()
        line_no = text[:start].count("\n") + 1
        inner = re.sub(r"\s+", " ", m.group(1)).strip()
        return line_no, text[start: pos + m.end()], inner
    return None


def looks_like_comment_header(text: str) -> bool:
    """Шапка (или строка-комментарий) стоит в начале файла, который комментариев не допускает."""
    if text.startswith("\ufeff"):
        text = text[1:]
    for line in text.splitlines():
        if not line.strip():
            continue
        s = line.lstrip()
        if s.startswith(("#", "//", "/*")) or HEADER_TEXT in line:
            return True
        return False
    return False


def header_ok(inner: str) -> bool:
    return inner.strip() == HEADER_TEXT


def is_shared_rust(cat) -> bool:
    return getattr(cat, "fmt", None) == "rust" and cat.meta.get("file_locale") is None


def check_header(cat, add) -> None:
    """add(sev, check, e, msg, line=...)."""
    fmt = cat.fmt
    if is_shared_rust(cat):
        return  # общий файл нескольких языков (например EffectCraft i18n.rs) — не ru-файл
    policy = COMMENT_POLICY.get(fmt)
    if policy is None:
        return
    supports, syntax, src = policy
    try:
        text = open(cat.path, encoding="utf-8", errors="replace").read()
    except OSError as exc:
        add("warn", "authorship-header", None, f"не удалось прочитать файл для шапки: {exc}", line=1)
        return
    if not supports:
        add("warn", "authorship-header-unsupported", None,
            "формат не поддерживает комментарии — шапку ставить нельзя, авторство только в описании PR и коммите "
            f"(RULES-AUTHORSHIP.md). Источник: {src}", line=1)
        if looks_like_comment_header(text):
            add("error", "authorship-header-breaks", None,
                "шапка ломает формат (комментарии в этом формате нельзя: файл не разберётся). "
                f"Источник: {src}", line=1)
        return
    first = first_comment(text, fmt)
    expect = syntax or f"# {HEADER_TEXT}"
    if first is None:
        add("warn", "authorship-header", None,
            f"нет шапки авторства: первой строкой-комментарием должно быть `{expect}` "
            f"(RULES-AUTHORSHIP.md). Формат допускает комментарии — {src}", line=1)
        return
    line_no, raw, inner = first
    if not header_ok(inner):
        add("warn", "authorship-header", None,
            f"первая строка-комментарий не шапка авторства (сейчас: {raw.strip()[:120]}). "
            f"Ожидалось: `{expect}` (RULES-AUTHORSHIP.md)", line=line_no)


# -------------------- комментарии файла (для имён исполнителей) --------------------

def iter_hash_comments(text: str):
    for i, line in enumerate(text.splitlines(), 1):
        inner = _inner_hash(line)
        if inner is not None:
            yield i, inner


def iter_rust_line_comments(text: str):
    """Комментарии, начинающиеся в строке (// и /* */). Строковые литералы не разбираем глубоко:
    берём только строки, у которых после обрезки слева стоит // или /* — шапка и метаданные файла."""
    i = 0
    lines = text.splitlines()
    while i < len(lines):
        i += 1
        line = lines[i - 1]
        s = line.lstrip()
        inner = _inner_slash(line)
        if inner is not None:
            yield i, inner
            continue
        if s.startswith("/*"):
            start = i
            chunk = s
            while "*/" not in chunk and i < len(lines):
                i += 1
                if i <= len(lines):
                    chunk += "\n" + lines[i - 1]
            inner = re.sub(r"^\s*/\*+!?\s*|\s*\*/\s*$", "", chunk, flags=re.S).strip()
            yield start, inner


def iter_xml_comments(text: str):
    for m in re.finditer(r"<!--(.*?)-->", text, re.S):
        line_no = text[: m.start()].count("\n") + 1
        yield line_no, re.sub(r"\s+", " ", m.group(1)).strip()


def file_comment_texts(path: str, fmt: str) -> list[tuple[int, str]]:
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    if fmt in ("craft-tsv", "tsv2", "toml", "ftl", "desktop"):
        return list(iter_hash_comments(text))
    if fmt == "rust":
        return list(iter_rust_line_comments(text))
    if fmt in ("xml", "md"):
        return list(iter_xml_comments(text))
    return []


def compile_bot_patterns(path: str | None = None) -> list[dict]:
    path = path or DEFAULT_BOT_NAMES
    out = []
    if not path or path == "none" or not os.path.isfile(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for i, raw in enumerate(fh, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            fields = "all"
            if line.lower().startswith("author:"):
                fields = "author"
                line = line.split(":", 1)[1].strip()
            if not line:
                continue
            if "*" in line:
                rx = re.compile(".*".join(re.escape(p) for p in line.split("*")), re.I)
            else:
                rx = re.compile(r"(?<![\w])" + re.escape(line) + r"(?![\w])", re.I)
            out.append({"raw": line, "rx": rx, "fields": fields, "line": i})
    return out


def match_bot(text: str, patterns: list[dict], where: str) -> list[str]:
    if not text:
        return []
    hits = []
    for p in patterns:
        if p["fields"] == "author" and where not in ("author", "committer", "author-email", "committer-email"):
            continue
        if p["rx"].search(text):
            hits.append(p["raw"])
    return hits


def check_bot_names_in_file(cat, patterns, add) -> None:
    if not patterns:
        return
    for line_no, inner in file_comment_texts(cat.path, cat.fmt):
        hits = match_bot(inner, patterns, "comment")
        if hits:
            add("warn", "assistant-name", None,
                f"в комментарии/метаданных имя исполнителя: «{'», «'.join(hits)}» (RULES-AUTHORSHIP.md; список review/tools/bot_names.txt)",
                line=line_no, key="", en="", ru=inner[:80])


def git_root(path: str) -> str | None:
    d = os.path.abspath(path if os.path.isdir(path) else os.path.dirname(path))
    while True:
        if os.path.isdir(os.path.join(d, ".git")) or os.path.isfile(os.path.join(d, ".git")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def git(repo: str, *args: str, timeout: int = 120) -> str:
    try:
        r = subprocess.run(["git", "--no-optional-locks", "-C", repo, *args],
                           capture_output=True, text=True, timeout=timeout)
        return r.stdout if r.returncode == 0 else ""
    except Exception:  # noqa: BLE001
        return ""


def has_origin(repo: str) -> bool:
    refs = git(repo, "rev-parse", "--verify", "refs/remotes/origin")
    # rev-parse on a directory may fail; check remotes
    remotes = git(repo, "remote")
    return "origin" in remotes.split()


def local_commits(repo: str) -> list[dict]:
    """Коммиты на локальных ветках (и HEAD), не достижимые из origin/*."""
    if not has_origin(repo):
        return []
    # --branches + HEAD: все локальные ветки; --not --remotes=origin/* : не из upstream origin
    text = git(repo, "log", "--branches", "HEAD", "--not", "--remotes=origin/*",
               "--format=%H%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%s%x1f%b%x1e",
               timeout=180)
    out = []
    for rec in text.split("\x1e"):
        rec = rec.strip("\n")
        if not rec.strip():
            continue
        parts = rec.split("\x1f")
        if len(parts) < 6:
            continue
        h, an, ae, cn, ce, subj = parts[:6]
        body = parts[6] if len(parts) > 6 else ""
        out.append({"hash": h, "author": an, "author_email": ae, "committer": cn,
                    "committer_email": ce, "subject": subj, "body": body[:4000]})
    return out


def scan_local_commits(repo: str, patterns: list[dict], relpath) -> list[tuple]:
    """Список кортежей для add(): (sev, check, msg, line, key, en, ru) относительно репозитория.

    Если origin нет — одно предупреждение, историю не сканируем (иначе вся история клона
    без remote считалась бы «локальной»).
    """
    findings = []
    repo_disp = relpath(repo)
    if not has_origin(repo):
        findings.append(("warn", "assistant-name",
                         f"в `{repo_disp}` нет remote origin — локальные коммиты не отличить от полной истории, пропуск "
                         "(git log --not --remotes=origin/*)", 0, repo_disp, "", ""))
        return findings
    for c in local_commits(repo):
        fields = [
            ("author", "автор", c["author"]),
            ("author-email", "email автора", c["author_email"]),
            ("committer", "коммиттер", c["committer"]),
            ("committer-email", "email коммиттера", c["committer_email"]),
            ("message", "тема", c["subject"]),
            ("message", "тело", c["body"]),
        ]
        hits = []
        for where, label, text in fields:
            for name in match_bot(text, patterns, where):
                hits.append(f"{label}: «{name}» в «{text.strip().splitlines()[0][:80]}»" if text.strip() else f"{label}: «{name}»")
        if hits:
            short = c["hash"][:10]
            findings.append(("warn", "assistant-name",
                             f"локальный коммит {short} в `{repo_disp}`: " + "; ".join(hits) +
                             " (не достижим из origin/*; RULES-AUTHORSHIP.md)",
                             0, short, c["author"], c["subject"][:80]))
    return findings
