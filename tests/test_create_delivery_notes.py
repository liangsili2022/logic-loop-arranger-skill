from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "create_delivery_notes.py"
README = ROOT / "README.md"


class CreateDeliveryNotesTest(unittest.TestCase):
    def test_writes_logic_delivery_notes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "delivery-notes.md"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--title",
                    "Night Drive Demo",
                    "--tempo",
                    "92-98 BPM",
                    "--key",
                    "D minor",
                    "--section",
                    "Intro: 0:00-0:08, keys and texture only",
                    "--section",
                    "Hook: 0:33-0:49, wider drums and bass commitment",
                    "--stem",
                    "Night Drive Demo - Drums.wav",
                    "--stem",
                    "Night Drive Demo - Bass.wav",
                    "--stem",
                    "Night Drive Demo - Music.wav",
                    "--out",
                    str(out_path),
                ],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), str(out_path))

            content = out_path.read_text(encoding="utf-8")
            self.assertIn("# Logic Delivery Notes: Night Drive Demo", content)
            self.assertIn("- Tempo: 92-98 BPM", content)
            self.assertIn("- Key: D minor", content)
            self.assertIn("## Section Map", content)
            self.assertIn("- Intro: 0:00-0:08, keys and texture only", content)
            self.assertIn("## Stem Naming", content)
            self.assertIn("- Night Drive Demo - Drums.wav", content)
            self.assertIn("## Logic Import Notes", content)
            self.assertIn("## Automation Boundaries", content)

    def test_readme_documents_basic_command(self) -> None:
        content = README.read_text(encoding="utf-8")

        self.assertIn("scripts/create_delivery_notes.py", content)
        self.assertIn("--section", content)
        self.assertIn("--stem", content)


if __name__ == "__main__":
    unittest.main()
