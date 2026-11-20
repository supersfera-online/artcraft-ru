#!/usr/bin/env python3
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Снимок состояния папок отдела локализации и «что изменилось с прошлого раза».

  state.py snapshot            записать снимок в review/state/last.txt (старый → prev.txt)
  state.py changed [--update]  сравнить текущее состояние с last.txt; --update затем перезаписать снимок
  state.py changed --paths     печатать только изменённые пути (для run_all.sh --only-changed)

Снимок: для каждого git-клона — HEAD, ветка, `git status --porcelain`; для файлов перевода и
упаковки (*.tsv, locales/*, i18n/*.rs, *.ftl, *.desktop, metainfo, mime, docs/locali*.md,
glossary) — sha256 и размер. Только чтение папок; пишет лишь в review/state/.
Код возврата `changed`: 0 — без изменений, 3 — есть изменения или нет прошлого снимка.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import os
import re
import subprocess
import sys

L10N = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STATE_DIR = os.path.join(L10N, "review", "state")
ROOTS = ["craft-i18n", "apps", "solidcraft", "packaging", "cli", "docs", "glossary"]
SKIP = {".git", "target", "node_modules", ".cargo"}
RELEVANT = re.compile(
    r"(\.tsv$|\.ftl$|\.desktop$|\.metainfo\.xml(\.in)?$|\.mime\.xml$|/locales?/[^/]+\.(json|toml|rs)$|/locales/[^/]+/mod\.rs$|"
    r"/i18n/[^/]+\.(rs|txt)$|/i18n\.rs$|/docs/(locali[sz]ation[^/]*|translating|internationalization)\.md$|"
    r"(^|/)ATTRIBUTION\.md$|(^|/)GLOSSARY\.md$|craft-i18n\.rev$|^glossary/)"
)


def git(repo: str, *args: str) -> str:
    try:
        return subprocess.run(["git", "--no-optional-locks", "-C", repo, *args], capture_output=True, text=True, timeout=600).stdout
    except Exception:  # noqa: BLE001
        return ""


def find_repos(root: str, depth: int = 3) -> list[str]:
    out = []
    for d, dirs, files in os.walk(root):
        rel_depth = os.path.relpath(d, root).count(os.sep)
        if ".git" in dirs or ".git" in files:
            out.append(d)
        dirs[:] = [x for x in dirs if x not in SKIP] if rel_depth < depth else []
    return sorted(out)


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def take() -> list[str]:
    lines = []
    for r in ROOTS:
        root = os.path.join(L10N, r)
        if not os.path.isdir(root):
            lines.append(f"missing\t{r}")
            continue
        for repo in find_repos(root):
            relp = os.path.relpath(repo, L10N)
            head = git(repo, "rev-parse", "HEAD").strip() or "(нет HEAD: клон не закончен?)"
            branch = git(repo, "rev-parse", "--abbrev-ref", "HEAD").strip()
            lines.append(f"repo\t{relp}\t{head}\t{branch}")
            for st in git(repo, "status", "--porcelain", "--untracked-files=normal").splitlines():
                lines.append(f"status\t{relp}\t{st}")
        for d, dirs, files in os.walk(root):
            dirs[:] = sorted(x for x in dirs if x not in SKIP)
            for f in sorted(files):
                p = os.path.join(d, f)
                relp = os.path.relpath(p, L10N)
                if RELEVANT.search(relp) and os.path.isfile(p):
                    try:
                        lines.append(f"file\t{relp}\t{sha256(p)}\t{os.path.getsize(p)}")
                    except OSError:
                        pass
    return lines


def parse(lines: list[str]) -> dict:
    s = {"repo": {}, "status": {}, "file": {}}
    for line in lines:
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if parts[0] == "repo":
            s["repo"][parts[1]] = (parts[2], parts[3] if len(parts) > 3 else "")
        elif parts[0] == "status":
            s["status"].setdefault(parts[1], set()).add(parts[2])
        elif parts[0] == "file":
            s["file"][parts[1]] = parts[2]
    return s


def write(lines: list[str]) -> str:
    os.makedirs(STATE_DIR, exist_ok=True)
    last = os.path.join(STATE_DIR, "last.txt")
    if os.path.exists(last):
        os.replace(last, os.path.join(STATE_DIR, "prev.txt"))
    now = _dt.datetime.now().astimezone()
    with open(last, "w", encoding="utf-8") as fh:
        fh.write(f"# l10n state snapshot {now:%Y-%m-%d %H:%M:%S %Z} (America/Los_Angeles)\n")
        fh.write("\n".join(lines) + "\n")
    return last


def owner(path: str, repos: list[str]) -> str:
    best = ""
    for r in repos:
        if (path == r or path.startswith(r + "/")) and len(r) > len(best):
            best = r
    return best or path.split("/")[0]


def diff(old: dict, new: dict) -> tuple[list[str], set]:
    msgs, changed = [], set()
    repos = sorted(set(old["repo"]) | set(new["repo"]))
    for r in repos:
        o, n = old["repo"].get(r), new["repo"].get(r)
        if o is None:
            msgs.append(f"+ новый клон: {r} @ {n[0][:10]} ({n[1]})")
            changed.add(r)
        elif n is None:
            msgs.append(f"- клон исчез: {r}")
            changed.add(r)
        elif o != n:
            log = git(os.path.join(L10N, r), "log", "--format=%h %ci %an: %s", f"{o[0]}..{n[0]}", "--max-count=20").strip()
            msgs.append(f"* {r}: HEAD {o[0][:10]} ({o[1]}) → {n[0][:10]} ({n[1]})" + ("\n    " + log.replace("\n", "\n    ") if log else ""))
            changed.add(r)
        so, sn = old["status"].get(r, set()), new["status"].get(r, set())
        if so != sn:
            for st in sorted(sn - so)[:40]:
                msgs.append(f"  {r}: git status + {st}")
            for st in sorted(so - sn)[:40]:
                msgs.append(f"  {r}: git status − {st}")
            if len(sn ^ so) > 80:
                msgs.append(f"  {r}: … всего изменений в git status: {len(sn ^ so)}")
            changed.add(r)
    all_repos = sorted(set(new["repo"]) | set(old["repo"]))
    files = sorted(set(old["file"]) | set(new["file"]))
    shown = 0
    for f in files:
        o, n = old["file"].get(f), new["file"].get(f)
        if o == n:
            continue
        mark = "+" if o is None else "-" if n is None else "~"
        if shown < 200:
            msgs.append(f"  файл {mark} {f}")
        shown += 1
        changed.add(owner(f, all_repos))
    if shown > 200:
        msgs.append(f"  … всего изменённых файлов перевода/упаковки: {shown}")
    return msgs, changed


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("snapshot")
    c = sub.add_parser("changed")
    c.add_argument("--update", action="store_true", help="после сравнения перезаписать снимок")
    c.add_argument("--paths", action="store_true", help="печатать только изменённые клоны/папки (по одной на строку)")
    a = p.parse_args(argv)
    lines = take()
    if a.cmd == "snapshot":
        path = write(lines)
        s = parse(lines)
        print(f"снимок: {path} — клонов {len(s['repo'])}, строк git status {sum(len(v) for v in s['status'].values())}, файлов с хэшем {len(s['file'])}")
        return 0
    last = os.path.join(STATE_DIR, "last.txt")
    if not os.path.exists(last):
        if a.paths:
            for r in ROOTS:
                print(r)
        else:
            print("прошлого снимка нет (review/state/last.txt) — считаю, что изменилось всё")
        if a.update:
            write(lines)
        return 3
    with open(last, encoding="utf-8") as fh:
        old_lines = fh.read().splitlines()
    when = old_lines[0][len("# l10n state snapshot "):] if old_lines and old_lines[0].startswith("#") else "?"
    msgs, changed = diff(parse(old_lines), parse(lines))
    if a.paths:
        for r in sorted(changed):
            print(r)
    elif msgs:
        print(f"Изменения с прошлого снимка ({when}):")
        print("\n".join(msgs))
        print("Затронуто: " + ", ".join(sorted(changed)))
    else:
        print(f"Изменений нет с прошлого снимка ({when}).")
    if a.update:
        write(lines)
    return 3 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
