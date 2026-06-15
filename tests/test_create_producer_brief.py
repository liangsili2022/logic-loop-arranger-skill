from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "create_producer_brief.py"


class CreateProducerBriefTest(unittest.TestCase):
    def read_output(self, *args: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "brief.txt"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), *args, "--out", str(out_path)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.stdout.strip(), str(out_path))
            content = out_path.read_text(encoding="utf-8")

        self.assertTrue(content.endswith("\n"))
        return content.splitlines()

    def test_writes_expected_brief_fields_in_fixed_order(self) -> None:
        lines = self.read_output(
            "--title",
            "Night Drive Demo",
            "--style",
            "contemporary alt-R&B accompaniment",
            "--mood",
            "late-night, intimate, unresolved",
            "--references",
            "SZA, Brent Faiyaz",
            "--tempo",
            "92-98 BPM",
            "--key",
            "D minor",
            "--harmony",
            "moody minor loop",
            "--palette",
            "soft drums, warm keys, sub bass",
            "--finish",
            "songwriting demo",
            "--deliverable",
            "stereo WAV, Logic import notes",
        )

        self.assertEqual(
            lines,
            [
                "Title: Night Drive Demo",
                "Brief:",
                "- Style: contemporary alt-R&B accompaniment",
                "- Mood: late-night, intimate, unresolved",
                "- Tempo: 92-98 BPM",
                "- Key: D minor",
                "- Harmony: moody minor loop",
                "- Palette: soft drums, warm keys, sub bass",
                "- Finish level: songwriting demo",
                "- Deliverable: stereo WAV, Logic import notes",
                "- References: SZA, Brent Faiyaz",
            ],
        )

    def test_omits_references_when_not_provided_and_keeps_defaults(self) -> None:
        lines = self.read_output(
            "--style",
            "alt-pop accompaniment",
            "--mood",
            "tense, sparse",
            "--tempo",
            "104 BPM",
            "--palette",
            "tight drums, dry bass, muted keys",
            "--deliverable",
            "stereo WAV",
        )

        self.assertEqual(
            lines,
            [
                "Title: Untitled Session",
                "Brief:",
                "- Style: alt-pop accompaniment",
                "- Mood: tense, sparse",
                "- Tempo: 104 BPM",
                "- Key: TBD",
                "- Harmony: TBD",
                "- Palette: tight drums, dry bass, muted keys",
                "- Finish level: songwriting demo",
                "- Deliverable: stereo WAV",
            ],
        )
        self.assertFalse(any(line.startswith("- References:") for line in lines))


if __name__ == "__main__":
    unittest.main()
