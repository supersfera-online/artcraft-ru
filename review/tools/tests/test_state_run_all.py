# Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
"""Короткие тесты state.py (сравнение снимков) и run_all.py (разбор путей)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import run_all  # noqa: E402
import state  # noqa: E402


class StateDiff(unittest.TestCase):
    def test_no_change(self):
        lines = ["repo\tcraft-i18n\taaa\tmain", "status\tcraft-i18n\t?? x", "file\tcraft-i18n/locales/ru/a.tsv\th1\t10"]
        msgs, changed = state.diff(state.parse(lines), state.parse(lines))
        self.assertEqual(msgs, [])
        self.assertEqual(changed, set())

    def test_head_status_and_file_change(self):
        old = ["repo\tapps/figcraft\taaa\tmain", "file\tapps/figcraft/crates/ui-egui/locales/ru.toml\th1\t1"]
        new = ["repo\tapps/figcraft\tbbb\tmain", "status\tapps/figcraft\t M crates/ui-egui/locales/ru.toml",
               "file\tapps/figcraft/crates/ui-egui/locales/ru.toml\th2\t2", "repo\tapps/new\tccc\tmain"]
        msgs, changed = state.diff(state.parse(old), state.parse(new))
        self.assertEqual(changed, {"apps/figcraft", "apps/new"})
        text = "\n".join(msgs)
        self.assertIn("HEAD aaa", text)
        self.assertIn("git status +  M crates/ui-egui/locales/ru.toml", text)
        self.assertIn("файл ~ apps/figcraft/crates/ui-egui/locales/ru.toml", text)
        self.assertIn("новый клон: apps/new", text)

    def test_relevant_files(self):
        for p in ("craft-i18n/locales/ru/common.tsv", "apps/x/crates/ui-egui/locales/ru.json",
                  "packaging/src/x/packaging/linux/ai.storyteller.x.desktop", "glossary/glossary.tsv"):
            self.assertTrue(state.RELEVANT.search(p), p)
        self.assertFalse(state.RELEVANT.search("apps/x/src/main.rs"))


class Targets(unittest.TestCase):
    def test_target_of(self):
        L = run_all.L10N
        self.assertEqual(run_all.target_of(f"{L}/craft-i18n/locales/ru/photocraft.tsv"), ("craft-i18n", "craft-i18n"))
        self.assertEqual(run_all.target_of(f"{L}/apps/figcraft/crates/ui-egui/locales/ru.toml"), ("apps-figcraft", "apps/figcraft"))
        self.assertEqual(run_all.target_of(f"{L}/packaging/src/lightcraft/x/ru.json"), ("packaging-lightcraft", "packaging/src/lightcraft"))
        self.assertEqual(run_all.target_of(f"{L}/solidcraft/solidcraft/assets/locales/ru.json"), ("solidcraft", "solidcraft/solidcraft"))

    def test_native_list_parses(self):
        rows = run_all.load_native()
        self.assertTrue(any(r["repo"] == "craft-i18n" and r["auto"] for r in rows))
        self.assertFalse(any("--add-missing" in r["cmd"] for r in rows))


if __name__ == "__main__":
    unittest.main()
