# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Короткие тесты l10n_check.py: python3 -m unittest discover -s review/tools/tests -v"""
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
sys.path.insert(0, TOOLS)
import l10n_check as lc  # noqa: E402

FX = os.path.join(HERE, "fixtures")
GLOSS = os.path.join(FX, "glossary.tsv")


def run(path, locale="ru", **kw):
    terms, desc = lc.load_glossary(kw.pop("glossary", GLOSS))
    opt = lc.Options(locale=locale, glossary=terms, glossary_desc=desc)
    cat = lc.load_catalog(path, locale, kw.pop("fmt", None))
    findings, summary = lc.check_catalog(cat, opt)
    return findings, summary, cat


def checks(findings, severity=None):
    return {(f.check, f.key.split(" | ")[-1]) for f in findings if severity is None or f.severity == severity}


class Placeholders(unittest.TestCase):
    def test_kinds(self):
        p = lc.placeholders("{name} {0} {} %s %1$d $pos {{user}} {:.2} 100% done")
        self.assertEqual(p["{name}"], 1)
        self.assertIn("%s", p)
        self.assertIn("%1$d", p)
        self.assertIn("$pos", p)
        self.assertIn("{{user}}", p)
        self.assertNotIn("% d", p)  # «100% done» не printf

    def test_rust_positional_reorder_and_spec(self):
        # LightCraft: {} → {1}/{0:.0} — законная перестановка и скрытие окончания
        self.assertEqual(lc.placeholders("Added {n} photo{} to “{}”"), lc.placeholders("В «{1}» добавлено фото: {n}{0:.0}"))
        self.assertNotEqual(lc.placeholders("{a} {b}"), lc.placeholders("{a}"))

    def test_fluent(self):
        self.assertEqual(set(lc.placeholders("Hi { $user }", "ftl")), {"{$user}"})

    def test_literal_braces_not_placeholder(self):
        self.assertEqual(lc.placeholders("params ({{id: value}})"), lc.placeholders("params ({{id: valor}})"))

    def test_tags_and_mnemonics(self):
        self.assertEqual(lc.tags("<b>x</b>"), lc.tags("<b>y</b>"))
        self.assertNotEqual(lc.tags("<b>x</b>"), lc.tags("<b>y"))
        self.assertEqual(lc.mnemonics("&File"), 1)
        self.assertEqual(lc.mnemonics("Merge & Center"), 0)
        self.assertEqual(lc.mnemonics("Expected &, \\\\"), 0)


class CraftTsv(unittest.TestCase):
    def test_common(self):
        f, s, _ = run(os.path.join(FX, "craft-i18n/locales/ru/common.tsv"))
        got = checks(f, "error")
        for want in [("duplicate", "Save"), ("context", "X"), ("escape", "Bad\\q"), ("ellipsis", "Open…"),
                     ("placeholders", "Layer {name}"), ("empty", "Hello"), ("plural-forms", "{n} layer|{n} layers"),
                     ("markup", "<b>Bold</b> text")]:
            self.assertIn(want, got)
        self.assertIn(("untranslated", "Export PDF"), checks(f, "warn"))
        self.assertIn(("mixed-script", "Move down"), checks(f, "warn"))
        self.assertIn(("clean-room", "Visit https://example.org"), checks(f, "warn"))
        self.assertIn(("glossary", "Shadow Color"), checks(f, "warn"))
        self.assertNotIn(("glossary", "Shadow"), checks(f))      # «Тень» ≈ «Тени»
        self.assertEqual(s["missing"], 2)                         # Close и Crop есть только в de
        self.assertGreater(s["error"], 0)

    def test_redundant_override(self):
        f, _, _ = run(os.path.join(FX, "craft-i18n/locales/ru/photocraft.tsv"))
        self.assertIn(("redundant-override", "Save"), checks(f, "error"))
        self.assertNotIn(("glossary", "Crop"), checks(f))          # «предложен» по умолчанию не проверяется

    def test_glossary_proposed_opt_in(self):
        terms, _ = lc.load_glossary(GLOSS, "accepted+proposed")
        self.assertIn("Crop", [t.en for t in terms])


class OtherFormats(unittest.TestCase):
    def test_tsv2(self):
        f, s, cat = run(os.path.join(FX, "tsv2/i18n/ru.tsv"))
        self.assertEqual(cat.fmt, "tsv2")
        self.assertIn(("duplicate", "Save"), checks(f, "error"))
        self.assertIn(("placeholders", "Email {n}"), checks(f, "error"))
        self.assertIn(("whitespace", " Spaced"), checks(f, "warn"))

    def test_json_with_en(self):
        f, s, _ = run(os.path.join(FX, "json/locales/ru.json"))
        self.assertIn(("duplicate", "ui.save"), checks(f, "error"))
        self.assertIn(("placeholders", "ui.count"), checks(f, "error"))
        self.assertIn(("extra", "ui.stale"), checks(f, "error"))
        self.assertEqual(s["missing"], 1)

    def test_json_key_is_english(self):
        f, s, _ = run(os.path.join(FX, "jsonkey/locales/ru.json"))
        self.assertEqual(s["error"], 0)
        self.assertEqual(s["missing"], 1)

    def test_toml_plurals(self):
        f, s, _ = run(os.path.join(FX, "toml/locales/ru.toml"))
        self.assertIn(("plural-forms", "Delete {n} items"), checks(f, "warn"))
        self.assertIn(("placeholders", "Delete {n} items"), checks(f, "error"))
        self.assertNotIn(("plural-forms", "Export {n} layers"), checks(f))
        self.assertIn(("extra", "Stale"), checks(f, "error"))
        self.assertNotIn(("extra", "align.left"), checks(f))      # [commands] нет в en — не сверяется

    def test_rust_match(self):
        f, s, cat = run(os.path.join(FX, "rust/i18n/ru.rs"))
        keys = {e.key for e in cat.entries}
        self.assertIn('Raw "quoted"', keys)
        self.assertIn("Long {name}", keys)
        self.assertIn("Open", keys)
        self.assertNotIn("fake", keys)                             # комментарий не каталог
        self.assertIn(("duplicate", "Save"), checks(f, "error"))
        self.assertEqual(s["missing"], 1)

    def test_rust_multi_table(self):
        f, s, cat = run(os.path.join(FX, "rustmulti/i18n.rs"))
        self.assertEqual(cat.meta["tables"], ["RUSSIAN"])
        self.assertEqual(len(cat.entries), 2)
        self.assertIn(("ellipsis-dots", "Open…"), checks(f, "warn"))
        f2, s2, cat2 = run(os.path.join(FX, "rustmulti/i18n.rs"), locale="de")
        self.assertEqual(cat2.meta["tables"], ["GERMAN"])

    def test_ftl(self):
        f, s, _ = run(os.path.join(FX, "ftl/ru/main.ftl"))
        self.assertIn(("placeholders", "hello"), checks(f, "error"))
        self.assertIn(("plural-forms", "items"), checks(f, "warn"))
        self.assertIn(("extra", "stale"), checks(f, "error"))
        self.assertEqual(s["missing"], 1)

    def test_no_glossary_file(self):
        terms, desc = lc.load_glossary(os.path.join(FX, "nope.tsv"))
        self.assertEqual(terms, [])
        self.assertIn("en<TAB>ru", desc)


class Cli(unittest.TestCase):
    def test_exit_codes_and_outputs(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            bad = subprocess.run([sys.executable, os.path.join(TOOLS, "l10n_check.py"), "check",
                                  os.path.join(FX, "json/locales/ru.json"), "--out-dir", tmp, "--name", "t", "--quiet"])
            self.assertEqual(bad.returncode, 1)
            names = sorted(os.listdir(tmp))
            self.assertTrue(names[0].endswith("-t.md") and names[1].endswith("-t.tsv"))
            ok = subprocess.run([sys.executable, os.path.join(TOOLS, "l10n_check.py"), "check",
                                 os.path.join(FX, "jsonkey/locales/ru.json"), "--quiet"])
            self.assertEqual(ok.returncode, 0)

    def test_discover(self):
        out = subprocess.run([sys.executable, os.path.join(TOOLS, "l10n_check.py"), "discover", os.path.join(FX, "..", "..", "tests")],
                             capture_output=True, text=True)
        self.assertEqual(out.stdout, "")  # папка fixtures пропускается при поиске


if __name__ == "__main__":
    unittest.main()
