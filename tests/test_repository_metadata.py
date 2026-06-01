from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class RepositoryMetadataTest(unittest.TestCase):
    def test_expected_oss_docs_exist(self) -> None:
        expected_docs = [
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "CONTRIBUTING.md",
            "LICENSE",
            "PROMOTION.md",
            "ROADMAP.md",
            "SECURITY.md",
        ]

        for relative_path in expected_docs:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

    def test_readme_links_to_maintainer_docs(self) -> None:
        content = README.read_text(encoding="utf-8")

        expected_links = [
            "[CONTRIBUTING.md](CONTRIBUTING.md)",
            "[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)",
            "[SECURITY.md](SECURITY.md)",
            "[CHANGELOG.md](CHANGELOG.md)",
            "[ROADMAP.md](ROADMAP.md)",
            "[PROMOTION.md](PROMOTION.md)",
        ]

        for link in expected_links:
            with self.subTest(link=link):
                self.assertIn(link, content)

    def test_readme_repository_layout_mentions_test_suite(self) -> None:
        content = README.read_text(encoding="utf-8")

        expected_test_entries = [
            "test_create_producer_brief.py",
            "test_example_briefs.py",
            "test_repository_metadata.py",
        ]

        for entry in expected_test_entries:
            with self.subTest(entry=entry):
                self.assertIn(entry, content)


if __name__ == "__main__":
    unittest.main()
