from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKLIST = ROOT / "references" / "stem-package-checklist.md"
README = ROOT / "README.md"


class StemPackageChecklistTest(unittest.TestCase):
    def test_checklist_exists_and_covers_required_topics(self) -> None:
        self.assertTrue(CHECKLIST.is_file())
        content = CHECKLIST.read_text(encoding="utf-8")

        expected_sections = [
            "# Stem Package Checklist",
            "## Required Files",
            "## Alignment",
            "## Session Format",
            "## Naming Conventions",
            "## Source Loop References",
            "## Arrangement Map",
            "## Sanity Checks",
            "## Logic Pro Handoff Boundaries",
        ]

        for section in expected_sections:
            with self.subTest(section=section):
                self.assertIn(section, content)

    def test_readme_links_to_checklist(self) -> None:
        content = README.read_text(encoding="utf-8")

        self.assertIn(
            "[references/stem-package-checklist.md](references/stem-package-checklist.md)",
            content,
        )


if __name__ == "__main__":
    unittest.main()
