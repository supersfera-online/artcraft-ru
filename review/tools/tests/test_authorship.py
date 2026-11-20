# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Шапка авторства и имена исполнителей."""
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
sys.path.insert(0, TOOLS)
import authorship as auth  # noqa: E402
import l10n_check as lc  # noqa: E402

assistants = os.path.join(TOOLS, "bot_names.txt")


def check(path, fmt=None, assistants=assistants, locale="ru"):
    opt = lc.Options(locale=locale, bot_patterns=auth.compile_bot_patterns(assistants) if assistants and assistants != "none" else [])
    cat = lc.load_catalog(path, locale, fmt)
    findings, summary = lc.check_catalog(cat, opt)
    return findings, summary, cat


def of(findings, name):
    return [f for f in findings if f.check == name]


class Header(unittest.TestCase):
    def test_tsv_with_and_without(self):
        with tempfile.TemporaryDirectory() as tmp:
            good = os.path.join(tmp, "ru.tsv")
            with open(good, "w", encoding="utf-8") as fh:
                fh.write(f"# {auth.HEADER_TEXT}\n# other\n\tSave\tСохранить\n")
            f, _, cat = check(good, "craft-tsv", assistants="none")
            self.assertEqual(cat.entries[0].value, "Сохранить")
            self.assertFalse(of(f, "authorship-header"))

            bad = os.path.join(tmp, "ru-bad.tsv")
            with open(bad, "w", encoding="utf-8") as fh:
                fh.write("# Clean room: written from the plain meaning.\n\tSave\tСохранить\n")
            f, _, _ = check(bad, "craft-tsv", assistants="none")
            w = of(f, "authorship-header")
            self.assertEqual(len(w), 1)
            self.assertEqual(w[0].severity, "warn")
            self.assertIn("нет шапки", w[0].message)

    def test_json_unsupported_and_breaks(self):
        with tempfile.TemporaryDirectory() as tmp:
            ok = os.path.join(tmp, "ru.json")
            with open(ok, "w", encoding="utf-8") as fh:
                fh.write('{"Save": "Сохранить"}\n')
            f, s, _ = check(ok, "json", assistants="none")
            self.assertTrue(of(f, "authorship-header-unsupported"))
            self.assertFalse(of(f, "authorship-header-breaks"))
            self.assertEqual(s["error"], 0)

            brk = os.path.join(tmp, "ru-broken.json")
            with open(brk, "w", encoding="utf-8") as fh:
                fh.write(f"// {auth.HEADER_TEXT}\n{{\"Save\": \"Сохранить\"}}\n")
            f, s, _ = check(brk, "json", assistants="none")
            self.assertTrue(of(f, "authorship-header-unsupported"))
            err = of(f, "authorship-header-breaks")
            self.assertEqual(len(err), 1)
            self.assertEqual(err[0].severity, "error")
            self.assertIn("шапка ломает формат", err[0].message)
            self.assertGreaterEqual(s["error"], 1)

    def test_toml_rust_desktop_xml_md_ftl(self):
        with tempfile.TemporaryDirectory() as tmp:
            def write(name, body):
                path = os.path.join(tmp, name)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(body)
                return path

            toml = write("ru.toml", f"# {auth.HEADER_TEXT}\n[ui]\n\"Save\" = \"Сохранить\"\n")
            rust = write("ru.rs", f"// {auth.HEADER_TEXT}\npub fn t() {{ match x {{ \"Save\" => \"Сохранить\", _ => \"\" }} }}\n")
            desk = write("app.desktop", f"# {auth.HEADER_TEXT}\n[Desktop Entry]\nName=X\nName[ru]=X\n")
            xml = write("app.metainfo.xml",
                        f'<?xml version="1.0"?>\n<!-- {auth.HEADER_TEXT} -->\n<root><c xml:lang="ru">Привет</c></root>\n')
            md = write("README.ru.md", f"<!-- {auth.HEADER_TEXT} -->\n# Заголовок\n")
            ftl = write("main.ftl", f"# {auth.HEADER_TEXT}\nhello = Привет\n")
            for path, fmt in ((toml, "toml"), (rust, "rust"), (desk, "desktop"), (xml, "xml"), (md, "md"), (ftl, "ftl")):
                f, _, _ = check(path, fmt, assistants="none")
                self.assertFalse(of(f, "authorship-header"), msg=f"{fmt}: { [x.message for x in of(f,'authorship-header')] }")

    def test_shared_rust_skipped(self):
        # как EffectCraft: таблица RUSSIAN в общем i18n.rs — не отдельный ru-файл
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "i18n.rs")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write('const RUSSIAN: &[(&str, &str)] = &[("Save", "Сохранить")];\n')
            f, _, cat = check(path, "rust", assistants="none")
            self.assertIsNone(cat.meta.get("file_locale"))
            self.assertFalse(of(f, "authorship-header"))

    def test_exit_code_ignores_header_warn(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "ru.tsv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\tSave\tСохранить\n")
            r = subprocess.run([sys.executable, os.path.join(TOOLS, "l10n_check.py"), "check", path,
                                "--format", "craft-tsv", "--assistant-names", "none", "--ref", "none", "--quiet",
                                "--glossary", "none"])
            self.assertEqual(r.returncode, 0)


class BotNames(unittest.TestCase):
    def test_comment_hit_and_cursor_in_translation_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "ru.tsv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(f"# {auth.HEADER_TEXT}\n# written by SuperSfera LLC yesterday\n")
                fh.write("\tMove the cursor left\tСдвинуть курсор влево\n")
            f, _, _ = check(path, "craft-tsv")
            assistants = of(f, "assistant-name")
            self.assertEqual(len(assistants), 1)
            self.assertIn("SuperSfera LLC", assistants[0].message)
            # в тексте перевода «cursor» не ищем
            self.assertFalse(any("cursor" in (b.message + b.ru + b.en).lower() and "ассистент" not in b.message for b in assistants))

    def test_bare_cursor_only_in_author(self):
        pats = auth.compile_bot_patterns(assistants)
        self.assertTrue(auth.match_bot("Cursor", pats, "author"))
        self.assertFalse(auth.match_bot("Move the cursor left", pats, "comment"))
        self.assertFalse(auth.match_bot("Move the cursor left", pats, "message"))
        self.assertTrue(auth.match_bot("cursor agent did this", pats, "comment"))

    def test_star_at_is_email_like(self):
        pats = auth.compile_bot_patterns(assistants)
        self.assertTrue(auth.match_bot("SuperSfera LLC@local", pats, "author-email"))
        # «assistant» и позже «@user» в одной строке — не адрес
        self.assertFalse(auth.match_bot("| `bg` | later additions AI-assisted @someone", pats, "diff"))
        self.assertTrue(auth.match_bot("added with SuperSfera LLC, AI-assisted", pats, "diff"))

    def test_local_commits(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = os.path.join(tmp, "repo")
            os.makedirs(os.path.join(repo, "locales"))
            def g(*a):
                r = subprocess.run(["git", "-C", repo, *a], cwd=repo, capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                return r
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "-C", repo, "config", "user.name", "Alice"], check=True)
            subprocess.run(["git", "-C", repo, "config", "user.email", "alice@example.com"], check=True)
            with open(os.path.join(repo, "README"), "w") as fh:
                fh.write("a\n")
            g("add", "README")
            g("commit", "-m", "upstream start")
            g("remote", "add", "origin", "https://example.com/upstream.git")
            g("update-ref", "refs/remotes/origin/main", "HEAD")
            with open(os.path.join(repo, "locales", "ru.tsv"), "w", encoding="utf-8") as fh:
                fh.write(f"# {auth.HEADER_TEXT}\n\tSave\tСохранить\n")
            g("add", "locales/ru.tsv")
            env = dict(os.environ, GIT_AUTHOR_NAME="SuperSfera LLC", GIT_AUTHOR_EMAIL="SuperSfera LLC@box.local",
                       GIT_COMMITTER_NAME="SuperSfera LLC", GIT_COMMITTER_EMAIL="SuperSfera LLC@box.local")
            r = subprocess.run(["git", "-C", repo, "commit", "-m", "ru catalog"], env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            pats = auth.compile_bot_patterns(assistants)
            found = auth.scan_local_commits(repo, pats, lambda p: os.path.basename(p))
            self.assertTrue(found, "должен найти локальный коммит SuperSfera LLC")
            msg = found[0][2]
            self.assertIn("SuperSfera LLC", msg)
            self.assertIn("SuperSfera LLC@box.local", msg)  # *@box* или *assistant*@*
            # коммит, уже на origin, не должен попасть — проверим что Alice не в списке как единственная находка
            self.assertNotIn("Alice", msg)


class Discover(unittest.TestCase):
    def test_packaging_and_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            desk = os.path.join(tmp, "packaging", "linux")
            os.makedirs(desk)
            with open(os.path.join(desk, "app.desktop"), "w") as fh:
                fh.write("[Desktop Entry]\nName=X\nName[ru]=Икс\n")
            with open(os.path.join(tmp, "ai.storyteller.x.metainfo.xml.in"), "w") as fh:
                fh.write('<?xml version="1.0"?>\n<summary xml:lang="ru">Привет</summary>\n')
            with open(os.path.join(tmp, "README.ru.md"), "w") as fh:
                fh.write("<!-- x -->\n# Привет\n")
            rows = lc.discover([tmp], "ru")
            fmts = {r[1] for r in rows}
            self.assertEqual(fmts, {"desktop", "xml", "md"})
class HeaderPlacement(unittest.TestCase):
    def test_header_wrong_place_and_clean_room_not_anchor(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "ru.tsv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("# Clean room: written from the plain meaning.\n")
                fh.write(f"# {auth.HEADER_TEXT}\n\tSave\tСохранить\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            pl = of(f, "authorship-header-placement")
            self.assertEqual(len(pl), 1, [x.message for x in f if x.check.startswith("authorship")])
            self.assertIn("шапка не на месте", pl[0].message)
            self.assertFalse(of(f, "authorship-header"))  # шапка есть, но не на месте

    def test_xml_after_decl_and_shebang(self):
        with tempfile.TemporaryDirectory() as tmp:
            xml = os.path.join(tmp, "app.metainfo.xml")
            with open(xml, "w", encoding="utf-8") as fh:
                fh.write('<?xml version="1.0"?>\n')
                fh.write(f"<!-- {auth.HEADER_TEXT} -->\n<!-- AppStream metadata -->\n<root/>\n")
            f, _, _ = check(xml, "xml", assistants="none")
            self.assertFalse(of(f, "authorship-header"))
            self.assertFalse(of(f, "authorship-header-placement"))

            sh = os.path.join(tmp, "script.desktop")
            with open(sh, "w", encoding="utf-8") as fh:
                fh.write("#!/usr/bin/env true\n")
                fh.write(f"# {auth.HEADER_TEXT}\n[Desktop Entry]\nName=X\n")
            f, _, _ = check(sh, "desktop", assistants="none")
            self.assertFalse(of(f, "authorship-header-placement"), [x.message for x in of(f, "authorship-header-placement")])
            self.assertFalse(of(f, "authorship-header"))


def _git(cwd, *args, env=None, check=True):
    r = subprocess.run(["git", "-C", cwd, *args], cwd=cwd, capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        raise AssertionError(r.stderr)
    return r


class UpstreamCommentsAndDiff(unittest.TestCase):
    def _repo(self, tmp):
        repo = os.path.join(tmp, "repo")
        os.makedirs(repo)
        _git(repo, "init") if False else subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
        subprocess.run(["git", "-C", repo, "config", "user.name", "Alice"], check=True)
        subprocess.run(["git", "-C", repo, "config", "user.email", "alice@example.com"], check=True)
        os.makedirs(os.path.join(repo, "locales"), exist_ok=True)
        with open(os.path.join(repo, "locales", "ru.tsv"), "w", encoding="utf-8") as fh:
            fh.write("# Clean room: written from the plain meaning.\n\n\tSave\tСохранить\n")
        with open(os.path.join(repo, "ATTRIBUTION.md"), "w", encoding="utf-8") as fh:
            fh.write("# credits\n| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
        _git(repo, "add", "locales/ru.tsv", "ATTRIBUTION.md")
        _git(repo, "commit", "-m", "upstream start")
        _git(repo, "remote", "add", "origin", "https://example.com/upstream.git")
        _git(repo, "update-ref", "refs/remotes/origin/main", "HEAD")
        _git(repo, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
        return repo

    def test_header_then_unchanged_comments(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo(tmp)
            path = os.path.join(repo, "locales", "ru.tsv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(f"# {auth.HEADER_TEXT}\n# Clean room: written from the plain meaning.\n\n\tSave\tСохранить\n")
            _git(repo, "add", "locales/ru.tsv")
            _git(repo, "commit", "-m", "add header")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            self.assertFalse(of(f, "authorship-header"), [x.message for x in of(f, "authorship-header")])
            self.assertFalse(of(f, "authorship-header-placement"))
            self.assertFalse(of(f, "authorship-header-comments"), [x.message for x in of(f, "authorship-header-comments")])

    def test_edited_author_comment(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo(tmp)
            path = os.path.join(repo, "locales", "ru.tsv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(f"# {auth.HEADER_TEXT}\n# Clean room: CHANGED by us.\n\n\tSave\tСохранить\n\tOpen\tОткрыть\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            c = of(f, "authorship-header-comments")
            self.assertEqual(len(c), 1, [x.message for x in f if "authorship" in x.check])
            self.assertIn("изменён авторский комментарий", c[0].message)

    def test_diff_added_lines_not_upstream_text(self):
        """SuperSfera LLC в добавленной строке ATTRIBUTION ловится; тот же текст из origin — нет."""
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo(tmp)
            att = os.path.join(repo, "ATTRIBUTION.md")
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n")
                fh.write("| `ru` | missing rows added with SuperSfera LLC, AI-assisted |\n")
                fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            env = dict(os.environ, GIT_AUTHOR_NAME="Alice", GIT_AUTHOR_EMAIL="alice@example.com",
                       GIT_COMMITTER_NAME="Alice", GIT_COMMITTER_EMAIL="alice@example.com")
            _git(repo, "add", "ATTRIBUTION.md")
            subprocess.run(["git", "-C", repo, "commit", "-m", "record AI assistance"], env=env,
                           capture_output=True, text=True, check=True)
            pats = auth.compile_bot_patterns(assistants)
            found = auth.scan_local_commits(repo, pats, lambda p: os.path.relpath(p, repo) if os.path.isabs(p) else p)
            msgs = "\n".join(x[2] for x in found)
            files_lines = [(x[7] if len(x) > 7 else "", x[3], x[2]) for x in found]
            # добавленная строка ru ... SuperSfera LLC
            hits = [x for x in found if "SuperSfera LLC" in x[2] and "добавленная строка" in x[2]]
            self.assertTrue(hits, f"должна быть находка по диффу, got: {files_lines}")
            self.assertTrue(any("ATTRIBUTION.md" in (x[7] if len(x)>7 else "") or "ATTRIBUTION.md" in x[5] or "ATTRIBUTION.md" in x[2] for x in hits))
            # номер строки = 2 (ru row)
            self.assertTrue(any(x[3] == 2 for x in hits), hits)
            # upstream sl row must not appear as a diff hit
            self.assertFalse(any("Filip Strajnar" in x[2] and "добавленная" in x[2] for x in found), msgs)

    def test_diff_keeps_historical_addition(self):
        """Имя, добавленное в одном локальном коммите и убранное в следующем, всё равно ловится."""
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo(tmp)
            att = os.path.join(repo, "ATTRIBUTION.md")
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n")
                fh.write("| `ru` | missing rows added with SuperSfera LLC, AI-assisted |\n")
                fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            env = dict(os.environ, GIT_AUTHOR_NAME="Alice", GIT_AUTHOR_EMAIL="alice@example.com",
                       GIT_COMMITTER_NAME="Alice", GIT_COMMITTER_EMAIL="alice@example.com")
            _git(repo, "add", "ATTRIBUTION.md")
            subprocess.run(["git", "-C", repo, "commit", "-m", "record AI assistance"], env=env,
                           capture_output=True, text=True, check=True)
            first = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n")
                fh.write("| `ru` | missing rows added, AI-assisted |\n")
                fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            _git(repo, "add", "ATTRIBUTION.md")
            subprocess.run(["git", "-C", repo, "commit", "-m", "update credit"], env=env,
                           capture_output=True, text=True, check=True)
            pats = auth.compile_bot_patterns(assistants)
            found = auth.scan_local_diffs(repo, pats, lambda p: os.path.relpath(p, repo) if os.path.isabs(p) else p)
            hits = [x for x in found if "SuperSfera LLC" in x[2] and "добавленная строка локального коммита" in x[2]]
            self.assertTrue(hits, found)
            self.assertTrue(any(x[3] == 2 and x[4].startswith(first[:10]) for x in hits), hits)
            # текущий файл и upstream не дают повтор по строке sl
            self.assertFalse(any("Filip Strajnar" in x[2] for x in hits), hits)

    def test_uncommitted_added_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo(tmp)
            path = os.path.join(repo, "locales", "ru.tsv")
            with open(path, "a", encoding="utf-8") as fh:
                fh.write("\tOpen\tнаписано SuperSfera LLC\n")
            pats = auth.compile_bot_patterns(assistants)
            found = auth.scan_local_diffs(repo, pats, lambda p: os.path.relpath(p, repo) if os.path.isabs(p) else p)
            self.assertTrue(any("SuperSfera LLC" in x[2] and "незакоммичен" in x[2] for x in found), found)


def _init_git(repo, name="Alice", email="alice@example.com"):
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "-C", repo, "config", "user.name", name], check=True)
    subprocess.run(["git", "-C", repo, "config", "user.email", email], check=True)


def _origin(repo):
    _git(repo, "remote", "add", "origin", "https://example.com/upstream.git")
    _git(repo, "update-ref", "refs/remotes/origin/main", "HEAD")
    _git(repo, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")


TEMPLATE = "# Русский (ru) interface catalog for PhotoCraft.\n"
COLUMNS = (
    "# Columns, separated by a TAB:  context <TAB> English source text <TAB> translation\n"
    "# Clean room: written from the plain meaning.\n"
)
HEADER = f"# {auth.HEADER_TEXT}\n"
PHRASE = auth.ATTRIBUTION_RU_PHRASE


class CraftI18nHeader(unittest.TestCase):
    def _tree(self, tmp, body, name="photocraft.tsv"):
        repo = os.path.join(tmp, "craft-i18n")
        os.makedirs(os.path.join(repo, "docs"))
        os.makedirs(os.path.join(repo, "locales", "ru"))
        with open(os.path.join(repo, "docs", "catalog-format.md"), "w", encoding="utf-8") as fh:
            fh.write("# Catalog format\n\n# <Language> (<locale>) interface catalog for AppName.\n")
        path = os.path.join(repo, "locales", "ru", name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
        return repo, path

    def test_header_second_after_template_ok(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, path = self._tree(tmp, TEMPLATE + COLUMNS + "\tSave\tСохранить\n")
            _init_git(repo)
            _git(repo, "add", "docs/catalog-format.md", "locales/ru/photocraft.tsv")
            _git(repo, "commit", "-m", "upstream")
            _origin(repo)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(TEMPLATE + HEADER + COLUMNS + "\tSave\tСохранить\n\tOpen\tОткрыть\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            self.assertFalse(of(f, "authorship-header-placement"), [x.message for x in of(f, "authorship-header-placement")])
            self.assertFalse(of(f, "authorship-header"))
            self.assertFalse(of(f, "authorship-header-unneeded"))

    def test_header_first_in_craft_i18n_is_wrong_place(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, path = self._tree(tmp, HEADER + TEMPLATE + COLUMNS + "\tSave\tСохранить\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            pl = of(f, "authorship-header-placement")
            self.assertEqual(len(pl), 1, [x.message for x in f if x.check.startswith("authorship")])
            self.assertIn("шапка не на месте", pl[0].message)
            self.assertIn("второй строкой", pl[0].message)

    def test_comments_match_after_stripping_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, path = self._tree(tmp, TEMPLATE + COLUMNS + "\tSave\tСохранить\n")
            _init_git(repo)
            _git(repo, "add", "docs/catalog-format.md", "locales/ru/photocraft.tsv")
            _git(repo, "commit", "-m", "upstream")
            _origin(repo)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(TEMPLATE + HEADER + COLUMNS + "\tSave\tСохранить\n\tOpen\tОткрыть\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            self.assertFalse(of(f, "authorship-header-placement"))
            self.assertFalse(of(f, "authorship-header-comments"), [x.message for x in of(f, "authorship-header-comments")])

    def test_changed_comment_includes_diff(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, path = self._tree(tmp, TEMPLATE + COLUMNS + "\tSave\tСохранить\n")
            _init_git(repo)
            _git(repo, "add", "docs/catalog-format.md", "locales/ru/photocraft.tsv")
            _git(repo, "commit", "-m", "upstream")
            _origin(repo)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(TEMPLATE + HEADER + "# Clean room: CHANGED by us.\n\tSave\tСохранить\n\tOpen\tОткрыть\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            c = of(f, "authorship-header-comments")
            self.assertEqual(len(c), 1)
            self.assertIn("изменён авторский комментарий", c[0].message)
            self.assertIn("Clean room", c[0].message)


class OurTranslation(unittest.TestCase):
    def test_identical_upstream_no_header_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = os.path.join(tmp, "repo")
            os.makedirs(os.path.join(repo, "locales", "ru"))
            path = os.path.join(repo, "locales", "ru", "cadcraft.tsv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("# Русский (ru) interface catalog for CADCraft.\n\tSave\tСохранить\n")
            _init_git(repo)
            _git(repo, "add", "locales/ru/cadcraft.tsv")
            _git(repo, "commit", "-m", "upstream ru")
            _origin(repo)
            f, _, _ = check(path, "craft-tsv", assistants="none")
            self.assertFalse(of(f, "authorship-header"), [x.message for x in of(f, "authorship-header")])
            self.assertFalse(of(f, "authorship-header-unneeded"))

    def test_header_on_foreign_file_warned(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = os.path.join(tmp, "repo")
            os.makedirs(os.path.join(repo, "locales", "ru"))
            path = os.path.join(repo, "locales", "ru", "cadcraft.tsv")
            body = "# Русский (ru) interface catalog for CADCraft.\n\tSave\tСохранить\n"
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(body)
            _init_git(repo)
            _git(repo, "add", "locales/ru/cadcraft.tsv")
            _git(repo, "commit", "-m", "upstream ru")
            _origin(repo)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("# Русский (ru) interface catalog for CADCraft.\n" + HEADER + "\tSave\tСохранить\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            u = of(f, "authorship-header-unneeded")
            self.assertEqual(len(u), 1, [x.message for x in f if x.check.startswith("authorship")])
            self.assertIn("шапка в файле без нашего перевода", u[0].message)
            self.assertFalse(of(f, "authorship-header"))

    def test_mime_without_our_ru_no_header_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = os.path.join(tmp, "repo")
            os.makedirs(os.path.join(repo, "packaging"))
            path = os.path.join(repo, "packaging", "app.mime.xml")
            body = '<?xml version="1.0"?>\n<mime-info>\n  <comment xml:lang="de">x</comment>\n  <comment xml:lang="ru">Чужой</comment>\n</mime-info>\n'
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(body)
            _init_git(repo)
            _git(repo, "add", "packaging/app.mime.xml")
            _git(repo, "commit", "-m", "upstream")
            _origin(repo)
            f, _, _ = check(path, "xml", assistants="none")
            self.assertFalse(of(f, "authorship-header"))
            self.assertFalse(of(f, "authorship-header-unneeded"))

    def test_new_file_requires_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = os.path.join(tmp, "repo")
            os.makedirs(os.path.join(repo, "locales", "ru"))
            other = os.path.join(repo, "README")
            with open(other, "w") as fh:
                fh.write("x\n")
            _init_git(repo)
            _git(repo, "add", "README")
            _git(repo, "commit", "-m", "upstream")
            _origin(repo)
            path = os.path.join(repo, "locales", "ru", "new.tsv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\tSave\tСохранить\n")
            f, _, _ = check(path, "craft-tsv", assistants="none")
            self.assertTrue(of(f, "authorship-header"))


class AttributionAndBots(unittest.TestCase):
    def _repo(self, tmp, ru_line):
        repo = os.path.join(tmp, "craft-i18n")
        os.makedirs(os.path.join(repo, "docs"))
        os.makedirs(os.path.join(repo, "locales", "ru"))
        with open(os.path.join(repo, "docs", "catalog-format.md"), "w") as fh:
            fh.write("# Catalog format\n")
        with open(os.path.join(repo, "ATTRIBUTION.md"), "w", encoding="utf-8") as fh:
            fh.write("# credits\n")
            fh.write(ru_line)
            fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
        _init_git(repo)
        _git(repo, "add", "docs/catalog-format.md", "ATTRIBUTION.md")
        _git(repo, "commit", "-m", "upstream")
        _origin(repo)
        return repo

    def test_missing_phrase_on_local_ru_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo(tmp, "| `ru` | WordCraft: someone, AI-assisted |\n")
            att = os.path.join(repo, "ATTRIBUTION.md")
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n")
                fh.write("| `ru` | later additions, AI-assisted, no SuperSfera phrase |\n")
                fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            rows = auth.check_attribution(repo, lambda p: os.path.relpath(p, repo))
            self.assertTrue(rows, rows)
            self.assertEqual(rows[0][1], "authorship-attribution")
            self.assertIn("нет формулировки", rows[0][2])
            self.assertEqual(rows[0][3], 2)

    def test_phrase_present_ok_and_upstream_row_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo(tmp, "| `ru` | old credit |\n")
            att = os.path.join(repo, "ATTRIBUTION.md")
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n")
                fh.write(f"| `ru` | 2026-11-20: {PHRASE} |\n")
                fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            rows = auth.check_attribution(repo, lambda p: os.path.relpath(p, repo))
            self.assertFalse(rows, rows)

    def test_local_at_localhost_and_l10n_packaging(self):
        pats = auth.compile_bot_patterns(assistants)
        self.assertTrue(auth.match_bot("users.noreply.github.com", pats, "author-email"), "users.noreply.github.com должен ловиться")
        self.assertTrue(auth.match_bot("отдел локализации", pats, "author"))
        # не путать с обычной прозой
        self.assertFalse(auth.match_bot("hosted locally at localhost city", pats, "diff"))

    def test_history_vs_current_tree_split(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = os.path.join(tmp, "repo")
            os.makedirs(repo)
            att = os.path.join(repo, "ATTRIBUTION.md")
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            _init_git(repo)
            _git(repo, "add", "ATTRIBUTION.md")
            _git(repo, "commit", "-m", "upstream")
            _origin(repo)
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n")
                fh.write("| `ru` | missing rows added with SuperSfera LLC, AI-assisted |\n")
                fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            env = dict(os.environ, GIT_AUTHOR_NAME="Alice", GIT_AUTHOR_EMAIL="alice@example.com",
                       GIT_COMMITTER_NAME="Alice", GIT_COMMITTER_EMAIL="alice@example.com")
            _git(repo, "add", "ATTRIBUTION.md")
            subprocess.run(["git", "-C", repo, "commit", "-m", "add grok"], env=env, capture_output=True, check=True)
            first = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
            pats = auth.compile_bot_patterns(assistants)
            found = auth.scan_local_diffs(repo, pats, lambda p: os.path.relpath(p, repo) if os.path.isabs(p) else p)
            in_tree = [x for x in found if "SuperSfera LLC" in x[2] and auth.BOT_IN_TREE in x[2]]
            self.assertTrue(in_tree, found)
            # убрали имя
            with open(att, "w", encoding="utf-8") as fh:
                fh.write("# credits\n")
                fh.write(f"| `ru` | later additions, {PHRASE} |\n")
                fh.write("| `sl` | WordCraft: Filip Strajnar with SuperSfera LLC; already upstream |\n")
            _git(repo, "add", "ATTRIBUTION.md")
            subprocess.run(["git", "-C", repo, "commit", "-m", "drop grok"], env=env, capture_output=True, check=True)
            found = auth.scan_local_diffs(repo, pats, lambda p: os.path.relpath(p, repo) if os.path.isabs(p) else p)
            hist = [x for x in found if "SuperSfera LLC" in x[2] and auth.BOT_IN_HISTORY in x[2]]
            tree = [x for x in found if "SuperSfera LLC" in x[2] and auth.BOT_IN_TREE in x[2]]
            self.assertTrue(hist, found)
            self.assertTrue(any(x[4].startswith(first[:10]) for x in hist), hist)
            self.assertFalse(tree, tree)

