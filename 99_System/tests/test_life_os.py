import argparse
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "99_System" / "scripts"))

import life_os


class LifeOSTests(unittest.TestCase):
    def test_cli_help_works(self):
        parser = life_os.build_parser()
        help_text = parser.format_help()
        self.assertIn("Life OS engine", help_text)
        self.assertIn("refresh-dashboards", help_text)

    def test_required_folders_list_is_available(self):
        self.assertIn("00_Inbox", life_os.REQUIRED_FOLDERS)
        self.assertIn("08_Relationships", life_os.REQUIRED_FOLDERS)
        self.assertIn("99_System/reports", life_os.REQUIRED_FOLDERS)

    def test_required_dashboards_exist(self):
        for dashboard in life_os.REQUIRED_DASHBOARDS:
            self.assertTrue((ROOT / dashboard).exists(), dashboard)

    def test_templates_and_schemas_exist(self):
        for template in life_os.TEMPLATE_FILES:
            self.assertTrue((ROOT / "90_Templates" / template).exists(), template)
        for schema in life_os.SCHEMA_FILES:
            self.assertTrue((ROOT / "99_System" / "schemas" / schema).exists(), schema)

    def test_obsidian_link_parser_detects_links(self):
        text = "See [[10_Maps_Of_Content/Life_OS_Home|home]] and ![[image.png]]."
        self.assertEqual(
            life_os.extract_obsidian_links(text),
            ["10_Maps_Of_Content/Life_OS_Home", "image.png"],
        )

    def test_root_triage_classifier(self):
        destination, reason, confidence = life_os.classify_root_file(Path("Clinical Case.md"))
        self.assertEqual(destination, "02_Medicine/")
        self.assertIn("medical", reason)
        self.assertEqual(confidence, "high")

    def test_report_generation(self):
        path = life_os.inbox_report(argparse.Namespace())
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("type: report", text)
        self.assertIn("## Summary", text)


if __name__ == "__main__":
    unittest.main()

