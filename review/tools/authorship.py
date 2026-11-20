#!/usr/bin/env python3
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Шапка авторства и имена исполнителей (RULES-AUTHORSHIP.md). Подключается из l10n_check.py.

Достоверность поддержки комментариев — в COMMENT_POLICY (источник у каждой строки).
"""
from __future__ import annotations

import difflib
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


def mandatory_prefix(text: str, fmt: str) -> tuple[str, str, int]:
    """Обязательная первая строка инструментов: shebang или <?xml?>.

    `# Clean room:` сюда не входит (craft-i18n tree.rs ищет его в любой строке).
    Возвращает (префикс, остаток, номер первой строки после префикса).
    """
    bom = ""
    if text.startswith("\ufeff"):
        text = text[1:]
        bom = "\ufeff"
    if fmt == "xml":
        m = re.match(r"(\s*<\?xml[^?]*\?>[ \t]*\r?\n?)", text)
        if m:
            nxt = 1 + m.group(1).count("\n")
            if not m.group(1).endswith("\n") and not m.group(1).endswith("\r"):
                nxt = 1
            return bom + m.group(1), text[m.end():], max(nxt, 2 if m.group(1).rstrip("\r\n") else 1)
    m = re.match(r"(#![^\n]*\r?\n?)", text)
    if m:
        return bom + m.group(1), text[m.end():], 2 if m.group(1).endswith("\n") or m.group(1).endswith("\r") else 1
    return bom, text, 1


def _is_hash_comment(line: str) -> bool:
    return line.lstrip().startswith("#")


def _is_rust_comment_start(line: str) -> bool:
    s = line.lstrip()
    return s.startswith("//") or s.startswith("/*")


def leading_comments(text: str, fmt: str) -> tuple[str, int]:
    """Ведущий блок авторских комментариев после обязательного префикса: (текст, первая строка блока).

    Пустые строки в начале пропускаются; пустые внутри блока сохраняются; хвостовые пустые отбрасываются.
    """
    _prefix, rest, start_line = mandatory_prefix(text, fmt)
    if fmt in ("xml", "md"):
        pos = 0
        # пропустить пробелы в начале
        mws = re.match(r"\s*", rest)
        pos = mws.end() if mws else 0
        first_line = start_line + rest[:pos].count("\n")
        blocks = []
        while True:
            m = re.match(r"(\s*)(<!--.*?-->)", rest[pos:], re.S)
            if not m:
                break
            blocks.append(m.group(0))
            pos += m.end()
        raw = "".join(blocks).rstrip() + ("\n" if blocks else "")
        return raw, first_line if blocks else start_line
    lines = rest.splitlines(keepends=True)
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    first = start_line + i
    if fmt == "rust":
        j = i
        last = i - 1
        while j < len(lines):
            if not lines[j].strip():
                j += 1
                continue
            s = lines[j].lstrip()
            if s.startswith("//"):
                last = j
                j += 1
                continue
            if s.startswith("/*"):
                last = j
                if "*/" not in lines[j]:
                    j += 1
                    while j < len(lines):
                        last = j
                        if "*/" in lines[j]:
                            j += 1
                            break
                        j += 1
                else:
                    j += 1
                continue
            break
        block_lines = lines[i : last + 1] if last >= i else []
    else:
        is_c = _is_hash_comment
        j = i
        last = i - 1
        while j < len(lines):
            if not lines[j].strip():
                j += 1
                continue
            if is_c(lines[j]):
                last = j
                j += 1
                continue
            break
        block_lines = lines[i : last + 1] if last >= i else []
    raw = "".join(block_lines).rstrip() + ("\n" if block_lines else "")
    return raw, first


def find_header(text: str, fmt: str) -> list[tuple[int, str, str]]:
    """Все вхождения шапки в комментариях: (строка, сырой текст, внутренность)."""
    hits = []
    if fmt in ("xml", "md"):
        for m in re.finditer(r"<!--(.*?)-->", text, re.S):
            inner = re.sub(r"\s+", " ", m.group(1)).strip()
            if header_ok(inner):
                hits.append((text[: m.start()].count("\n") + 1, m.group(0), inner))
        return hits
    i = 0
    lines = text.splitlines()
    while i < len(lines):
        i += 1
        line = lines[i - 1]
        if fmt == "rust":
            inner = _inner_slash(line)
            if inner is not None:
                if header_ok(inner):
                    hits.append((i, line, inner))
                continue
            if line.lstrip().startswith("/*"):
                start = i
                chunk = line
                raw = [line]
                while "*/" not in chunk and i < len(lines):
                    i += 1
                    raw.append(lines[i - 1])
                    chunk += "\n" + lines[i - 1]
                inner = re.sub(r"^\s*/\*+!?\s*|\s*\*/\s*$", "", chunk, flags=re.S).strip()
                if header_ok(inner):
                    hits.append((start, "\n".join(raw), inner))
            continue
        inner = _inner_hash(line)
        if inner is not None and header_ok(inner):
            hits.append((i, line, inner))
    return hits


def comments_after_header(text: str, fmt: str, header_line: int) -> str:
    """Комментарии сразу после шапки (до первого не-комментария)."""
    # вырезаем строку(и) шапки и берём leading_comments от хвоста
    prefix, rest, start = mandatory_prefix(text, fmt)
    # построчно отбросим всё до конца шапки
    # проще: взять текст начиная со строки после header
    lines = text.splitlines(keepends=True)
    # если шапка многострочная (/* */ или <!-- -->), найти её конец
    hits = find_header(text, fmt)
    hit = next((h for h in hits if h[0] == header_line), None)
    if not hit:
        return ""
    raw = hit[1]
    # индекс конца шапки в тексте
    pos = 0
    # найти raw после начала соответствующей строки
    line_start = 0 if header_line == 1 else len("".join(text.splitlines(keepends=True)[: header_line - 1]))
    idx = text.find(raw, line_start)
    if idx < 0:
        idx = line_start
        after = text[idx + len(lines[header_line - 1] if header_line <= len(lines) else raw) :]
    else:
        after = text[idx + len(raw) :]
    # после --> или \n шапки может не быть перевода строки в raw
    if after.startswith("\n") or after.startswith("\r"):
        # не глотаем: leading_comments пропустит ведущие пустые; «сразу после» —
        # одну пустую строку считаем ещё допустимой паузой перед блоком? нет: пустые
        # в начале leading_comments пропускаются, сравнение блока от первого комментария.
        pass
    block, _ = leading_comments(after if fmt != "xml" else (
        # для XML обязательный префикс уже позади; не подсовывать остаток как новый xml-файл
        after
    ), "toml" if fmt == "xml" else fmt)
    # XML/MD: leading_comments на хвосте без <?xml?> — fmt xml всё ещё ищет <!-- -->
    if fmt in ("xml", "md"):
        block, _ = leading_comments(after, fmt)
    elif fmt == "rust":
        block, _ = leading_comments(after, "rust")
    else:
        block, _ = leading_comments(after, fmt)
    return block


def norm_comment_block(block: str) -> str:
    lines = [ln.rstrip() for ln in block.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def comments_equal(a: str, b: str) -> bool:
    return norm_comment_block(a) == norm_comment_block(b)


def upstream_rev(repo: str) -> str | None:
    if not has_origin(repo):
        return None
    for rev in ("origin/HEAD", "origin/main", "origin/master"):
        if git(repo, "rev-parse", "--verify", rev).strip():
            return rev
    mb = git(repo, "merge-base", "HEAD", "origin/HEAD").strip()
    return mb or None


def upstream_file(repo: str, relpath: str) -> str | None:
    """Содержимое пути в origin/HEAD (или merge-base), либо None если файла там нет."""
    rev = upstream_rev(repo)
    if not rev:
        return None
    # git show rev:path — только если файл есть
    try:
        r = subprocess.run(
            ["git", "--no-optional-locks", "-C", repo, "show", f"{rev}:{relpath}"],
            capture_output=True, timeout=60,
        )
    except Exception:  # noqa: BLE001
        return None
    if r.returncode != 0:
        mb = git(repo, "merge-base", "HEAD", rev).strip()
        if not mb or mb == rev:
            return None
        try:
            r = subprocess.run(
                ["git", "--no-optional-locks", "-C", repo, "show", f"{mb}:{relpath}"],
                capture_output=True, timeout=60,
            )
        except Exception:  # noqa: BLE001
            return None
        if r.returncode != 0:
            return None
    try:
        return r.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return r.stdout.decode("utf-8", errors="replace")


# docs/catalog-format.md: «# <Language> (<locale>) interface catalog for <every Crafting App | AppName>.»
CRAFT_CATALOG_TEMPLATE_RE = re.compile(
    r"^#\s+.+\([^)]*\)\s+interface catalog for .+\.\s*$"
)
RU_MARK_RE = re.compile(r"""xml:lang\s*=\s*["']ru["']|\[[Rr][Uu]\]""", re.I)
ATTRIBUTION_RU_PHRASE = (
    "SuperSfera LLC (AI-assisted, produced under the direction of SuperSfera LLC)"
)
BOT_IN_TREE = "в текущем дереве"
BOT_IN_HISTORY = "только в истории коммитов, в дереве уже убрано"


def is_craft_i18n_catalog(path: str | None) -> bool:
    """TSV в locales/<язык>/ репозитория craft-i18n (есть docs/catalog-format.md)."""
    if not path:
        return False
    p = os.path.abspath(path)
    parent = os.path.dirname(p)
    locales = os.path.dirname(parent)
    if os.path.basename(locales) != "locales":
        return False
    root = os.path.dirname(locales)
    return os.path.isfile(os.path.join(root, "docs", "catalog-format.md"))


def is_catalog_template_line(line: str) -> bool:
    return bool(CRAFT_CATALOG_TEMPLATE_RE.match(line.rstrip("\r\n")))


def is_our_header_line(line: str) -> bool:
    return HEADER_TEXT in line


def is_comment_line(line: str, fmt: str) -> bool:
    s = line.lstrip()
    if fmt == "rust":
        return s.startswith("//") or s.startswith("/*") or s.startswith("*")
    if fmt in ("xml", "md"):
        return "<!--" in line
    return s.startswith("#")


def is_ru_locale_file(path: str) -> bool:
    """Отдельный файл языка ru (locales/ru/…, ru.tsv, ru.json, *.ru.md), не смешанный xml/desktop."""
    norm = path.replace("\\", "/").lower()
    name = os.path.basename(norm)
    if name.endswith(".ru.md"):
        return True
    stem = os.path.splitext(name)[0]
    if stem in {"ru", "ru_ru", "ru-ru"} or stem.startswith("ru."):
        return True
    parts = norm.split("/")
    for i, part in enumerate(parts):
        if part == "locales" and i + 1 < len(parts):
            loc = parts[i + 1]
            if loc in {"ru", "ru_ru", "ru-ru"} or loc.startswith("ru.") or loc.startswith("ru-"):
                return True
    return False


def ru_content_lines(text: str, path: str, fmt: str) -> list[str]:
    """Строки перевода (не шапка и не комментарии) для решения, есть ли наш ru."""
    ru_file = is_ru_locale_file(path)
    rows: list[str] = []
    for line in text.splitlines():
        if is_our_header_line(line):
            continue
        if ru_file:
            if not line.strip() or is_comment_line(line, fmt):
                continue
            rows.append(line.rstrip())
        elif RU_MARK_RE.search(line):
            rows.append(line.rstrip())
    return rows


def has_our_ru_translation(path: str, fmt: str, repo: str | None, text: str | None = None) -> bool:
    """True, если файл новый или локально добавлены/изменены ru-строки.

    Чужой ru-файл, идентичный upstream (без наших ru-строк), даёт False.
    Если репозитория или origin нет — не отличить, считаем нашим.
    """
    if not repo or not has_origin(repo):
        return True
    rel = os.path.relpath(os.path.abspath(path), os.path.abspath(repo))
    if rel.startswith(".."):
        return True
    rel = rel.replace(os.sep, "/")
    if text is None:
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            return True
    up = upstream_file(repo, rel)
    if up is None:
        return True
    return ru_content_lines(text, path, fmt) != ru_content_lines(up, path, fmt)


def strip_our_headers(text: str, fmt: str) -> str:
    """Убрать нашу шапку, остальной текст не трогать."""
    if fmt in ("xml", "md"):
        def repl(m):
            inner = re.sub(r"\s+", " ", m.group(1)).strip()
            return "" if header_ok(inner) else m.group(0)
        return re.sub(r"<!--(.*?)-->", repl, text, flags=re.S)
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if fmt == "rust" and line.lstrip().startswith("/*"):
            raw = [line]
            chunk = line
            j = i
            if "*/" not in line:
                j += 1
                while j < len(lines):
                    raw.append(lines[j])
                    chunk += "\n" + lines[j]
                    if "*/" in lines[j]:
                        break
                    j += 1
            inner = re.sub(r"^\s*/\*+!?\s*|\s*\*/\s*$", "", chunk, flags=re.S).strip()
            if header_ok(inner):
                i = j + 1
                continue
            out.extend(raw)
            i = j + 1
            continue
        inner = _inner_slash(line) if fmt == "rust" else _inner_hash(line)
        if inner is not None and header_ok(inner):
            i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out)


def comment_block_diff(upstream: str, current: str) -> str:
    a = norm_comment_block(upstream).splitlines()
    b = norm_comment_block(current).splitlines()
    lines = list(difflib.unified_diff(a, b, fromfile="upstream", tofile="файл без нашей шапки", lineterm=""))
    if not lines:
        return ""
    if len(lines) > 40:
        lines = lines[:40] + ["…"]
    return "\n".join(lines)


def added_lines_in_current_tree(repo: str) -> dict[str, list[tuple[int, str]]]:
    """Добавленные строки текущего дерева относительно origin (включая незакоммиченное)."""
    out: dict[str, list[tuple[int, str]]] = {}
    rev = upstream_rev(repo)
    if rev:
        try:
            r = subprocess.run(
                ["git", "--no-optional-locks", "-C", repo, "diff",
                 "--no-color", "--no-ext-diff", rev],
                capture_output=True, text=True, timeout=180,
            )
            if r.returncode == 0:
                out = _parse_patches(r.stdout)
        except Exception:  # noqa: BLE001
            pass
    for path in git(repo, "ls-files", "-o", "--exclude-standard").splitlines():
        path = path.strip()
        if not path:
            continue
        abs_p = os.path.join(repo, path)
        if not os.path.isfile(abs_p):
            continue
        try:
            with open(abs_p, encoding="utf-8", errors="replace") as fh:
                lines = fh.read().splitlines()
        except OSError:
            continue
        out.setdefault(path, []).extend(list(enumerate(lines, 1)))
    return out


def bot_hit_in_current_tree(current_added: dict, path: str, names: list[str], patterns: list[dict]) -> bool:
    want = {n.lower() for n in names}
    for _ln, content in current_added.get(path, []):
        hits = {h.lower() for h in match_bot(content, patterns, "diff")}
        if hits & want:
            return True
    return False


def check_attribution(repo: str, relpath_fn) -> list[tuple]:
    """Строка ru в craft-i18n/ATTRIBUTION.md: нужная формулировка, если строку меняли локально."""
    findings: list[tuple] = []
    path = os.path.join(repo, "ATTRIBUTION.md")
    if not os.path.isfile(path):
        return findings
    if not os.path.isfile(os.path.join(repo, "docs", "catalog-format.md")):
        return findings
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            cur = fh.read()
    except OSError:
        return findings
    up = upstream_file(repo, "ATTRIBUTION.md") if has_origin(repo) else None
    up_rows = {}
    if up is not None:
        for ln, line in _iter_attribution_ru_rows(up):
            up_rows[ln] = line
            # сверка по тексту строки, не только по номеру
        up_texts = {line for _ln, line in _iter_attribution_ru_rows(up)}
    else:
        up_texts = set()
    file_disp = relpath_fn(path) if path else "ATTRIBUTION.md"
    for ln, line in _iter_attribution_ru_rows(cur):
        if up is not None and line in up_texts:
            continue  # чужая строка, не трогали
        if ATTRIBUTION_RU_PHRASE not in line:
            findings.append((
                "warn", "authorship-attribution",
                "в строке ru ATTRIBUTION.md, которая менялась локально, нет формулировки "
                f"«{ATTRIBUTION_RU_PHRASE}»; имён исполнителей в этой строке быть не должно",
                ln, "ru", "", line[:80], file_disp,
            ))
    return findings


def _iter_attribution_ru_rows(text: str):
    for i, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\|\s*`ru`\s*\|", line) or re.match(r"^\|\s*ru\s*\|", line, re.I):
            yield i, line



def check_header(cat, add, repo: str | None = None) -> None:
    """add(sev, check, e, msg, line=...). repo — корень git-клона (для сверки авторских комментариев)."""
    fmt = cat.fmt
    if is_shared_rust(cat):
        return
    policy = COMMENT_POLICY.get(fmt)
    if policy is None:
        return
    supports, syntax, src = policy
    try:
        with open(cat.path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as exc:
        add("warn", "authorship-header", None, f"не удалось прочитать файл для шапки: {exc}", line=1)
        return
    ours = has_our_ru_translation(cat.path, fmt, repo, text)
    if not supports:
        if looks_like_comment_header(text):
            add("error", "authorship-header-breaks", None,
                "шапка ломает формат (комментарии в этом формате нельзя: файл не разберётся). "
                f"Источник: {src}", line=1)
        elif not ours:
            return
        if ours or looks_like_comment_header(text):
            # «не поддерживает» не пишем для чужого идентичного JSON без шапки
            add("warn", "authorship-header-unsupported", None,
                "формат не поддерживает комментарии — шапку ставить нельзя, авторство только в описании PR и коммите "
                f"(RULES-AUTHORSHIP.md). Источник: {src}", line=1)
        return
    hits = find_header(text, fmt)
    if not ours:
        if hits:
            add("warn", "authorship-header-unneeded", None,
                "шапка в файле без нашего перевода: чужой ru-файл идентичен upstream "
                "(или локально не добавлялись и не менялись ru-строки) — шапка здесь не нужна",
                line=hits[0][0])
        return
    expect = syntax or f"# {HEADER_TEXT}"
    _pref, _rest, after_prefix = mandatory_prefix(text, fmt)
    craft = is_craft_i18n_catalog(cat.path) and fmt == "craft-tsv"
    first_rest = _rest.splitlines()[0] if _rest.splitlines() else ""
    if craft:
        expected_line = after_prefix + 1  # шаблонная строка первая, шапка вторая
        on_place = (
            is_catalog_template_line(first_rest)
            and hits
            and hits[0][0] == expected_line
        )
        where = (
            "второй строкой, сразу после шаблонной "
            "«# <Язык> (ru) interface catalog …» (docs/catalog-format.md)"
        )
    else:
        expected_line = after_prefix
        first_nonempty = expected_line
        for i, ln in enumerate(_rest.splitlines(), expected_line):
            if ln.strip():
                first_nonempty = i
                break
        on_place = bool(hits) and hits[0][0] == first_nonempty == expected_line
        where = "первой строкой файла"
        if _pref.replace("\ufeff", "").strip():
            where = "сразу после обязательной первой строки (<?xml?> или shebang)"
    if not hits:
        add("warn", "authorship-header", None,
            f"нет шапки авторства: должна быть {where}: `{expect}` "
            f"(RULES-AUTHORSHIP.md). Формат допускает комментарии — {src}. "
            "«# Clean room:» в craft-i18n не держит первое место (tree.rs ищет его в любой строке).",
            line=expected_line)
    elif not on_place:
        line_no = hits[0][0]
        add("warn", "authorship-header-placement", None,
            f"шапка не на месте: должна быть {where} (строка {expected_line}); сейчас строка {line_no}. "
            "Авторские комментарии — сразу после шапки, без изменений. "
            "«# Clean room:» первым оставлять не нужно (craft-i18n tree.rs:251 ищет его в любой строке).",
            line=line_no)

    if repo:
        relpath = os.path.relpath(os.path.abspath(cat.path), os.path.abspath(repo))
        if relpath.startswith(".."):
            return
        up = upstream_file(repo, relpath.replace(os.sep, "/"))
        if up is None:
            return
        up_block, _ = leading_comments(up, fmt)
        if not norm_comment_block(up_block):
            return
        cur_block, _ = leading_comments(strip_our_headers(text, fmt), fmt)
        if not comments_equal(cur_block, up_block):
            diff = comment_block_diff(up_block, cur_block)
            extra = f" Дифф (после удаления нашей шапки; часть строк шаблона в upstream могла легитимно отличаться):\n{diff}" if diff else ""
            add("warn", "authorship-header-comments", None,
                "изменён авторский комментарий: после удаления нашей шапки ведущий блок комментариев "
                "должен совпасть с upstream (origin/HEAD или merge-base)." + extra,
                line=hits[0][0] if hits else expected_line)


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
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
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
                # для адресов (*@box*, *assistant*@*) звёздочка не пересекает пробел:
                # иначе «SuperSfera LLC … @user» в тексте ловилось бы как *assistant*@*.
                glue = r"\S*" if "@" in line else ".*"
                rx = re.compile(glue.join(re.escape(p) for p in line.split("*")), re.I)
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
                f"{BOT_IN_TREE}: в комментарии/метаданных имя исполнителя: «{'», «'.join(hits)}» "
                "(RULES-AUTHORSHIP.md; список review/tools/bot_names.txt)",
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
    remotes = git(repo, "remote")
    return "origin" in remotes.split()


def local_commits(repo: str) -> list[dict]:
    """Коммиты на локальных ветках (и HEAD), не достижимые из origin/*."""
    if not has_origin(repo):
        return []
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


def _added_lines_from_diff(diff: str) -> list[tuple[int, str]]:
    """Номер строки в новом файле и текст добавленных строк (без +++)."""
    out = []
    new_line = 0
    for row in diff.splitlines():
        if row.startswith("@@"):
            m = re.search(r"\+(\d+)", row)
            new_line = int(m.group(1)) if m else 0
            continue
        if row.startswith("+++") or row.startswith("---"):
            continue
        if row.startswith("\\"):
            continue
        if row.startswith("+"):
            out.append((new_line, row[1:]))
            new_line += 1
        elif row.startswith("-"):
            continue
        else:
            new_line += 1
    return out


def _changed_paths(repo: str) -> set[str]:
    """Пути, которые меняют локальные коммиты или незакоммиченные правки (включая неотслеживаемые)."""
    paths: set[str] = set()
    # файлы из локальных коммитов
    names = git(repo, "log", "--branches", "HEAD", "--not", "--remotes=origin/*",
                "--name-only", "--pretty=format:", timeout=180)
    for line in names.splitlines():
        line = line.strip()
        if line:
            paths.add(line)
    rev = upstream_rev(repo)
    if rev:
        for line in git(repo, "diff", "--name-only", "--no-renames", rev, timeout=180).splitlines():
            line = line.strip()
            if line:
                paths.add(line)
    # незакоммиченные относительно HEAD (на случай, если origin не достаётся)
    for line in git(repo, "diff", "--name-only", "--no-renames", "HEAD", timeout=120).splitlines():
        line = line.strip()
        if line:
            paths.add(line)
    for line in git(repo, "ls-files", "-o", "--exclude-standard", timeout=60).splitlines():
        line = line.strip()
        if line:
            paths.add(line)
    return paths



def _parse_patches(diff: str) -> dict[str, list[tuple[int, str]]]:
    """path -> список (номер строки в новой версии, текст) из одного или нескольких hunks."""
    out: dict[str, list[tuple[int, str]]] = {}
    path = None
    buf: list[tuple[int, str]] = []
    new_line = 0
    def flush():
        nonlocal buf, path
        if path and buf:
            out.setdefault(path, []).extend(buf)
        buf = []
    for row in diff.splitlines():
        if row.startswith("diff --git "):
            flush()
            path = None
            continue
        if row.startswith("+++ "):
            name = row[4:].strip()
            if name.startswith("b/"):
                name = name[2:]
            path = None if name == "/dev/null" else name
            continue
        if row.startswith("Binary files") or row.startswith("GIT binary"):
            path = None
            buf = []
            continue
        if path is None:
            continue
        if row.startswith("@@"):
            m = re.search(r"\+(\d+)", row)
            new_line = int(m.group(1)) if m else 0
            continue
        if row.startswith("+++") or row.startswith("---"):
            continue
        if row.startswith("\\"):
            continue
        if row.startswith("+"):
            buf.append((new_line, row[1:]))
            new_line += 1
        elif row.startswith("-"):
            continue
        else:
            new_line += 1
    flush()
    return out


def scan_local_diffs(repo: str, patterns: list[dict], relpath_fn) -> list[tuple]:
    """Имена исполнителей в добавленных строках («+») каждого локального коммита и незакоммиченных правок.

    Не смотрим весь файл и не смотрим контекст/upstream: иначе строка вроде
    «Filip Strajnar with SuperSfera LLC» из origin дала бы ложное срабатывание.
    Позднейший коммит, убравший имя, не отменяет находку в коммите, который его добавил.
    """
    findings: list[tuple] = []
    if not patterns:
        return findings

    current_added = added_lines_in_current_tree(repo)

    def emit(path: str, line_no: int, content: str, source: str, commit: str):
        hits = match_bot(content, patterns, "diff")
        if not hits:
            return
        abs_p = os.path.join(repo, path)
        file_disp = relpath_fn(abs_p) if os.path.exists(abs_p) else path
        if source.startswith("незакоммичен") or bot_hit_in_current_tree(current_added, path, hits, patterns):
            kind = BOT_IN_TREE
        else:
            kind = BOT_IN_HISTORY
        findings.append((
            "warn", "assistant-name",
            f"{kind}: {source}: имя исполнителя «{'», «'.join(hits)}» в «{content.strip()[:120]}» "
            f"({commit}; RULES-AUTHORSHIP.md)",
            line_no, commit, path, content.strip()[:80], file_disp,
        ))

    # 1) каждый локальный коммит — его собственный патч
    for c in local_commits(repo):
        try:
            r = subprocess.run(
                ["git", "--no-optional-locks", "-C", repo, "show",
                 "--format=", "--no-color", "--no-ext-diff", c["hash"]],
                capture_output=True, text=True, timeout=180,
            )
            patch = r.stdout
        except Exception:  # noqa: BLE001
            continue
        if not patch.strip():
            continue
        for path, added in _parse_patches(patch).items():
            for line_no, content in added:
                emit(path, line_no, content, "добавленная строка локального коммита", c["hash"][:10])

    # 2) незакоммиченные правки (индекс + рабочее дерево относительно HEAD)
    try:
        r = subprocess.run(
            ["git", "--no-optional-locks", "-C", repo, "diff", "--no-color", "--no-ext-diff", "HEAD"],
            capture_output=True, text=True, timeout=180,
        )
        uncommitted = r.stdout
    except Exception:  # noqa: BLE001
        uncommitted = ""
    for path, added in _parse_patches(uncommitted).items():
        for line_no, content in added:
            emit(path, line_no, content, "незакоммиченная правка", "незакоммичено")

    # 3) новые неотслеживаемые файлы — все строки считаются добавленными
    for path in git(repo, "ls-files", "-o", "--exclude-standard").splitlines():
        path = path.strip()
        if not path:
            continue
        abs_p = os.path.join(repo, path)
        if not os.path.isfile(abs_p):
            continue
        try:
            with open(abs_p, encoding="utf-8", errors="replace") as fh:
                lines = fh.read().splitlines()
        except OSError:
            continue
        for line_no, content in enumerate(lines, 1):
            emit(path, line_no, content, "незакоммиченный новый файл", "незакоммичено")
    return findings


def scan_local_commits(repo: str, patterns: list[dict], relpath) -> list[tuple]:
    """Находки по авторам/сообщениям локальных коммитов и по добавленным строкам их диффов.

    Если origin нет — одно предупреждение, историю не сканируем (иначе вся история клона
    считалась бы «локальной»). Кортеж: (sev, check, msg, line, key, en, ru, file|None).
    """
    findings: list[tuple] = []
    repo_disp = relpath(repo)
    if not has_origin(repo):
        findings.append(("warn", "assistant-name",
                         f"в `{repo_disp}` нет remote origin — локальные коммиты не отличить от полной истории, пропуск "
                         "(git log --not --remotes=origin/*)", 0, repo_disp, "", "", repo_disp))
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
                             f"{BOT_IN_HISTORY}: локальный коммит {short} в `{repo_disp}`: " + "; ".join(hits) +
                             " (не достижим из origin/*; RULES-AUTHORSHIP.md)",
                             0, short, c["author"], c["subject"][:80], repo_disp))
    findings.extend(scan_local_diffs(repo, patterns, relpath))
    findings.extend(check_attribution(repo, relpath))
    return findings
