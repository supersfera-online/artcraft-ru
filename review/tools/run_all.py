#!/usr/bin/env python3
# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Прогон всех проверок перевода по папкам отдела (вызывается из run_all.sh).

Находит каталоги языка (по умолчанию ru) в craft-i18n/, apps/, solidcraft/, packaging/ (а также
cli/ и docs/, если там появились клоны), проверяет каждый клон отдельным отчётом
review/reports/<ГГГГММДД-ЧЧММСС>-<цель>.md (+ .tsv) и пишет сводку <…>-run_all.md.
Штатные проверки репозиториев (native_checks.tsv) печатаются; с --native запускаются.
Ничего не публикует и не меняет в клонах; сборка cargo — в ~/.cache/l10n-review/target.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import shutil
import subprocess
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
import l10n_check as lc  # noqa: E402

L10N = lc.L10N_ROOT
REPORTS = os.path.join(L10N, "review", "reports")
DEFAULT_ROOTS = ["craft-i18n", "apps", "solidcraft", "packaging", "cli", "docs"]
CACHE = os.path.expanduser("~/.cache/l10n-review")


def target_of(path: str) -> tuple[str, str]:
    """(имя цели, корень клона относительно L10N) для пути каталога."""
    parts = os.path.relpath(path, L10N).split(os.sep)
    if parts[0] == "craft-i18n":
        return "craft-i18n", "craft-i18n"
    if parts[0] == "solidcraft":
        return "solidcraft", "/".join(parts[:2])
    if parts[0] == "packaging" and len(parts) > 2:
        return f"packaging-{parts[2]}", "/".join(parts[:3])
    if parts[0] in ("apps", "cli", "docs"):
        if len(parts) > 2 and parts[1] == "src":
            return f"{parts[0]}-{parts[2]}", "/".join(parts[:3])
        return f"{parts[0]}-{parts[1]}", "/".join(parts[:2])
    return parts[0], parts[0]


def git_status(repo: str) -> str:
    try:
        return subprocess.run(["git", "--no-optional-locks", "-C", repo, "status", "--porcelain"], capture_output=True, text=True, timeout=600).stdout
    except Exception:  # noqa: BLE001
        return ""


def load_native() -> list[dict]:
    rows = []
    with open(os.path.join(TOOLS, "native_checks.tsv"), encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            repo, auto, cmd, note = (line.rstrip("\n").split("\t") + ["", "", "", ""])[:4]
            rows.append({"repo": repo, "auto": auto == "yes", "cmd": cmd, "note": note})
    return rows


def native_repo_path(name: str) -> str | None:
    if name == "craft-i18n":
        return os.path.join(L10N, "craft-i18n")
    if name == "solidcraft":
        return os.path.join(L10N, "solidcraft", "solidcraft")
    for cand in (os.path.join(L10N, "apps", name), os.path.join(L10N, "packaging", "src", name),
                 os.path.join(L10N, "packaging", "src", name + "-r2"), os.path.join(L10N, "cli", "src", name)):
        if os.path.isfile(os.path.join(cand, "Cargo.toml")):
            return cand
    return None


def run_native(rows: list[dict], wanted: set | None, timeout: int, stamp: str) -> list[dict]:
    results = []
    cargo = shutil.which("cargo")
    for r in rows:
        if r["cmd"] == "-":
            continue
        run_it = (wanted is None and r["auto"]) or (wanted is not None and r["repo"] in wanted)
        if not run_it:
            continue
        repo = native_repo_path(r["repo"])
        res = {**r, "path": repo, "status": "", "log": ""}
        if not cargo:
            res["status"] = "не запускалось: cargo не найден (rustup можно поставить в ~ без sudo)"
        elif not repo:
            res["status"] = "не запускалось: клона нет или он неполный"
        else:
            cmd = r["cmd"].replace("{CRAFT_I18N_DIR}", os.path.join(L10N, "craft-i18n"))
            log = os.path.join(REPORTS, f"{stamp}-native-{r['repo']}-{len(results)}.log")
            env = dict(os.environ, CARGO_TARGET_DIR=os.path.join(CACHE, "target", r["repo"]))
            before = git_status(repo)
            t0 = _dt.datetime.now()
            with open(log, "w", encoding="utf-8") as fh:
                fh.write(f"$ cd {repo}\n$ CARGO_TARGET_DIR={env['CARGO_TARGET_DIR']} {cmd}\n\n")
                fh.flush()
                try:
                    p = subprocess.run(["bash", "-c", cmd], cwd=repo, env=env, stdout=fh, stderr=subprocess.STDOUT, timeout=timeout)
                    code = p.returncode
                except subprocess.TimeoutExpired:
                    code = "timeout"
            secs = int((_dt.datetime.now() - t0).total_seconds())
            after = git_status(repo)
            res["status"] = f"код {code}, {secs} с" + ("" if before == after else " — ВНИМАНИЕ: git status клона изменился во время прогона (см. лог)")
            if before != after:
                with open(log, "a", encoding="utf-8") as fh:
                    fh.write("\n\n# git status до:\n" + before + "\n# git status после:\n" + after)
            res["log"] = log
            res["code"] = code
        results.append(res)
    return results


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--locale", default="ru")
    p.add_argument("--only-changed", action="store_true", help="проверять только клоны, изменившиеся с прошлого снимка (state.py)")
    p.add_argument("--native", nargs="?", const="auto", default=None,
                   help="запустить штатные проверки: без значения — помеченные auto=yes; или список через запятую (craft-i18n,solidcraft,photocraft)")
    p.add_argument("--native-timeout", type=int, default=1800)
    p.add_argument("--no-snapshot", action="store_true", help="не обновлять review/state/last.txt после прогона")
    p.add_argument("--roots", default=" ".join(DEFAULT_ROOTS))
    p.add_argument("--glossary", default=lc.DEFAULT_GLOSSARY)
    p.add_argument("--extra-args", default="", help="доп. аргументы для l10n_check.py check (строкой)")
    a = p.parse_args(argv)

    os.makedirs(REPORTS, exist_ok=True)
    now = _dt.datetime.now().astimezone()
    stamp = now.strftime("%Y%m%d-%H%M%S")
    roots = [os.path.join(L10N, r) for r in a.roots.split()]

    changes_text, changed = "", None
    st = subprocess.run([sys.executable, os.path.join(TOOLS, "state.py"), "changed"], capture_output=True, text=True)
    changes_text = st.stdout.strip()
    if a.only_changed:
        pc = subprocess.run([sys.executable, os.path.join(TOOLS, "state.py"), "changed", "--paths"], capture_output=True, text=True)
        changed = set(pc.stdout.split())
        if pc.returncode == 0:
            print("изменений с прошлого снимка нет — проверять нечего")
            return 0

    found = lc.discover(roots, a.locale)
    targets: dict[str, dict] = {}
    for prog, fmt, path, note in found:
        name, root = target_of(path)
        t = targets.setdefault(name, {"root": root, "files": [], "programs": set()})
        t["files"].append(path)
        t["programs"].add(prog)
    if changed is not None and not ({"glossary"} & changed or any(c in ("craft-i18n", "apps", "packaging", "solidcraft") for c in changed)):
        targets = {k: v for k, v in targets.items() if any(v["root"] == c or v["root"].startswith(c + "/") for c in changed)}

    # одинаковые клоны (apps/, cli/src/, packaging/src/ одной программы) с теми же файлами проверяем один раз
    import hashlib
    seen: dict[tuple, str] = {}
    aliases: dict[str, list[str]] = {}
    order = sorted(targets, key=lambda n: (0 if n in ("craft-i18n", "solidcraft") else 1 if n.startswith("apps-") else 2 if n.startswith("packaging-") else 3, n))
    for name in order:
        t = targets[name]
        key = []
        for f in sorted(t["files"]):
            with open(f, "rb") as fh:
                key.append((os.path.relpath(f, os.path.join(L10N, t["root"])), hashlib.sha256(fh.read()).hexdigest()))
        key = tuple(key)
        if key in seen:
            aliases.setdefault(seen[key], []).append(name)
            t["dup_of"] = seen[key]
        else:
            seen[key] = name

    results = []
    extra = a.extra_args.split()
    for name in order:
        t = targets[name]
        if t.get("dup_of"):
            continue
        md = os.path.join(REPORTS, f"{stamp}-{name}.md")
        tsv = os.path.join(REPORTS, f"{stamp}-{name}.tsv")
        cmd = [sys.executable, os.path.join(TOOLS, "l10n_check.py"), "check", *t["files"], "--locale", a.locale,
               "--glossary", a.glossary, "--title", name, "--md", md, "--tsv", tsv, "--json-summary", *extra]
        p2 = subprocess.run(cmd, capture_output=True, text=True, cwd=L10N)
        try:
            sums = json.loads(p2.stdout)["summaries"]
        except Exception:  # noqa: BLE001
            sums = []
        results.append({"name": name, "aliases": aliases.get(name, []), "root": t["root"], "code": p2.returncode, "md": md, "tsv": tsv, "sums": sums,
                        "stderr": p2.stderr.strip()[-500:]})
        print(f"{name}: код {p2.returncode}, файлов {len(t['files'])}" + (f" (= {', '.join(aliases[name])})" if name in aliases else ""), flush=True)

    # программы без ru-каталога в репозитории
    with_ru = {prog for prog, *_ in found}
    no_ru = []
    for base in ("packaging/src", "apps"):
        d = os.path.join(L10N, base)
        if os.path.isdir(d):
            for x in sorted(os.listdir(d)):
                if os.path.isdir(os.path.join(d, x)) and x not in with_ru and x.replace("-r2", "") not in with_ru:
                    no_ru.append(f"{base}/{x}")
    craft_ru = sorted(os.path.basename(f)[:-4] for f in os.listdir(os.path.join(L10N, "craft-i18n", "locales", a.locale))) \
        if os.path.isdir(os.path.join(L10N, "craft-i18n", "locales", a.locale)) else []

    native_rows = load_native()
    native_results = []
    if a.native:
        wanted = None if a.native == "auto" else set(x.strip() for x in a.native.split(",") if x.strip())
        native_results = run_native(native_rows, wanted, a.native_timeout, stamp)

    # сводка
    total_err = sum(s["error"] for r in results for s in r["sums"])
    out = [f"# Сводный прогон проверок перевода ({a.locale})", ""]
    out.append(f"- Когда: {now:%Y-%m-%d %H:%M} {now.tzname()} (America/Los_Angeles); запуск: `run_all.sh {' '.join(argv if argv is not None else sys.argv[1:])}`")
    out.append(f"- Папки: {', '.join(os.path.relpath(r, L10N) for r in roots)}; режим: {'только изменённые' if a.only_changed else 'все'}")
    out.append(f"- Целей проверено: {len(results)} (ещё {sum(len(r['aliases']) for r in results)} — копии тех же файлов в других клонах); **ошибок всего: {total_err}** — " + ("НЕ ПРОЙДЕНО" if total_err else "ошибок нет"))
    out.append("- Достоверность: **[проверено: подсчёт скриптами review/tools по файлам на box в момент запуска]**")
    out.append("")
    out.append("## Изменения с прошлого снимка")
    out.append("")
    out.append("```")
    out.append(changes_text[:6000] if changes_text else "(нет данных)")
    out.append("```")
    out.append("")
    out.append("## Цели")
    out.append("")
    out.append("| Цель | Каталоги | Записей | Нет в переводе | Лишних | Ошибки | Предупр. | Справ. | Отчёт |")
    out.append("|---|---|---:|---:|---:|---:|---:|---:|---|")
    for r in results:
        s = r["sums"]
        files = "<br>".join(f"`{os.path.relpath(os.path.join(L10N, x['file']), os.path.join(L10N, r['root']))}` ({x['format']})" for x in s) or f"сбой: {lc.md_escape(r['stderr'])}"
        label = r["name"] + ("<br>(те же файлы: " + ", ".join(r["aliases"]) + ")" if r["aliases"] else "")
        out.append(f"| {label} | {files} | {sum(x['entries'] for x in s)} | {sum(x['missing'] for x in s)} | {sum(x['extra'] for x in s)} | "
                   f"{sum(x['error'] for x in s)} | {sum(x['warn'] for x in s)} | {sum(x['info'] for x in s)} | `{os.path.relpath(r['md'], L10N)}` |")
    out.append("")
    out.append("## Без каталога этого языка в репозитории программы")
    out.append("")
    out.append("Программы, где поиск не нашёл файла языка `" + a.locale + "` (ни TSV/JSON/TOML/FTL, ни Rust-таблицы). "
               "Часть из них переводится в craft-i18n — там сейчас есть: " + (", ".join(craft_ru) or "—") + ".")
    out.append("")
    for x in no_ru:
        prog = x.split("/")[-1].replace("-r2", "")
        note = f" — ru есть в craft-i18n: `locales/{a.locale}/{prog}.tsv`" if prog in craft_ru else ""
        out.append(f"- `{x}`{note}")
    out.append("")
    # шапка и имена исполнителей — сводка по TSV
    import collections as _c
    auth_counts = _c.Counter()
    bot_rows = []
    for r in results:
        tsv = r.get("tsv")
        if not tsv or not os.path.isfile(tsv):
            continue
        with open(tsv, encoding="utf-8") as fh:
            next(fh, None)
            for line in fh:
                cols = line.rstrip("\n").split("\t")
                if len(cols) < 9:
                    continue
                sev, chk, prog, file, ln, key, en, ru, msg = (cols + [""] * 9)[:9]
                if chk.startswith("authorship-header") or chk == "assistant-name":
                    auth_counts[chk] += 1
                    if chk == "assistant-name":
                        bot_rows.append((file, ln, key, msg))
    out.append("## Шапка авторства и имена исполнителей")
    out.append("")
    out.append("Правило: `RULES-AUTHORSHIP.md`. Проверки — предупреждения (на код возврата не влияют), кроме «шапка ломает формат» (ошибка).")
    out.append("")
    out.append("| Проверка | Сколько |")
    out.append("|---|---:|")
    titles = {"authorship-header": "нет шапки", "authorship-header-placement": "шапка не на месте",
              "authorship-header-comments": "изменён авторский комментарий",
              "authorship-header-unneeded": "шапка в файле без нашего перевода",
              "authorship-header-unsupported": "формат не поддерживает комментарии (JSON)",
              "authorship-header-breaks": "шапка ломает формат",
              "authorship-attribution": "нет формулировки SuperSfera в строке ru ATTRIBUTION.md",
              "assistant-name": "имя исполнителя"}
    for k, title in titles.items():
        out.append(f"| {title} (`{k}`) | {auth_counts[k]} |")
    out.append("")
    if bot_rows:
        hist_mark = "только в истории коммитов"
        tree_rows = [r for r in bot_rows if hist_mark not in r[3]]
        hist_rows = [r for r in bot_rows if hist_mark in r[3]]

        def emit_bots(title, rows):
            out.append(title)
            out.append("")
            for file, ln, key, msg in rows[:80]:
                out.append(f"- `{lc.md_escape(file)}`" + (f":{ln}" if ln not in ("0", "") else "")
                           + (f" `{lc.md_escape(key)}`" if key else "") + f" — {lc.md_escape(msg)}")
            if len(rows) > 80:
                out.append(f"- … ещё {len(rows) - 80}, полный список в TSV целей")
            out.append("")

        if tree_rows:
            emit_bots(f"Находки имён исполнителей — в текущем дереве ({len(tree_rows)}):", tree_rows)
        if hist_rows:
            emit_bots(f"Находки имён исполнителей — только в истории коммитов, в дереве уже убрано ({len(hist_rows)}). "
                      "Координатор переписывает историю при сборке:", hist_rows)

    out.append("## Штатные проверки репозиториев")
    out.append("")
    if native_results:
        out.append("| Репозиторий | Команда | Результат | Лог |")
        out.append("|---|---|---|---|")
        for r in native_results:
            out.append(f"| {r['repo']} | `{lc.md_escape(r['cmd'])}` | {lc.md_escape(r['status'])} | {('`' + os.path.relpath(r['log'], L10N) + '`') if r['log'] else ''} |")
        out.append("")
    out.append("Список (`review/tools/native_checks.tsv`; auto=yes запускается `run_all.sh --native`, остальные — `--native=<имя>`):")
    out.append("")
    out.append("| Репозиторий | auto | Команда | Источник / статус |")
    out.append("|---|---|---|---|")
    for r in native_rows:
        out.append(f"| {r['repo']} | {'да' if r['auto'] else 'нет'} | `{lc.md_escape(r['cmd'])}` | {lc.md_escape(r['note'])} |")
    out.append("")
    summary_path = os.path.join(REPORTS, f"{stamp}-run_all.md")
    with open(summary_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"сводка: {summary_path}")

    if not a.no_snapshot:
        subprocess.run([sys.executable, os.path.join(TOOLS, "state.py"), "snapshot"], capture_output=True)
    if any(r["code"] == 2 for r in results):
        return 2
    native_fail = any(isinstance(r.get("code"), str) or (isinstance(r.get("code"), int) and r["code"] != 0) for r in native_results)
    return 1 if total_err or native_fail else 0


if __name__ == "__main__":
    sys.exit(main())
