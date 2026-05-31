from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "create_producer_brief.py"


class CreateProducerBriefTest(unittest.TestCase):
    def test_writes_expected_brief_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "brief.txt"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
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
                    "stereo WAV and Logic import notes",
                    "--out",
                    str(out_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.stdout.strip(), str(out_path))
            content = out_path.read_text(encoding="utf-8")
            self.assertIn("Title: Night Drive Demo", content)
            self.assertIn("- Style: contemporary alt-R&B accompaniment", content)
            self.assertIn("- Mood: late-night, intimate, unresolved", content)
            self.assertIn("- References: SZA, Brent Faiyaz", content)
            self.assertTrue(content.endswith("\n"))


if __name__ == "__main__":
    unittest.main()
