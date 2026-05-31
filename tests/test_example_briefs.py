from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "example-briefs.md"


class ExampleBriefsTest(unittest.TestCase):
    def test_contains_target_genre_examples(self) -> None:
        content = EXAMPLES.read_text(encoding="utf-8")

        expected_headings = [
            "## Example 4: Sparse singer-songwriter sketch",
            "## Example 5: Sync bed instrumental cue",
            "## Example 6: Trap-influenced pop demo",
            "## Example 7: Upbeat pop/R&B chorus-lift demo",
        ]

        for heading in expected_headings:
            with self.subTest(heading=heading):
                self.assertIn(heading, content)

    def test_each_example_keeps_required_sections(self) -> None:
        content = EXAMPLES.read_text(encoding="utf-8")

        for example_number in range(1, 8):
            with self.subTest(example_number=example_number):
                marker = f"## Example {example_number}:"
                self.assertIn(marker, content)
                start = content.index(marker)
                next_marker = f"## Example {example_number + 1}:"
                end = content.find(next_marker, start + len(marker))
                section = content[start:] if end == -1 else content[start:end]

                self.assertIn("Input direction:", section)
                self.assertIn("Locked brief:", section)
                self.assertIn("- Style:", section)
                self.assertIn("- Deliverable:", section)


if __name__ == "__main__":
    unittest.main()
