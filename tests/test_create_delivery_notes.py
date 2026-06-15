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
    def read_output(self, *args: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "delivery-notes.md"
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

    def test_writes_logic_delivery_notes_with_repeated_sections_stems_and_notes(self) -> None:
        lines = self.read_output(
            "--title",
            "Night Drive Demo",
            "--tempo",
            "92-98 BPM",
            "--key",
            "D minor",
            "--section",
            "Intro: 0:00-0:08, keys texture only",
            "--section",
            "Hook: 0:33-0:49, wider drums bass commitment",
            "--stem",
            "Night Drive Demo - Drums.wav",
            "--stem",
            "Night Drive Demo - Bass.wav",
            "--stem",
            "Night Drive Demo - Music.wav",
            "--note",
            "Keep rough mix muted comparison.",
        )

        self.assertEqual(
            lines,
            [
                "# Logic Delivery Notes: Night Drive Demo",
                "",
                "## Session",
                "- Title: Night Drive Demo",
                "- Tempo: 92-98 BPM",
                "- Key: D minor",
                "- Sample rate: 48 kHz",
                "- Bit depth: 24-bit",
                "",
                "## Section Map",
                "- Intro: 0:00-0:08, keys texture only",
                "- Hook: 0:33-0:49, wider drums bass commitment",
                "",
                "## Stem Naming",
                "- Export stems from 0:00 and keep them full song length.",
                "- Use consistent title prefixes so files sort together in Finder and Logic.",
                "- Night Drive Demo - Drums.wav",
                "- Night Drive Demo - Bass.wav",
                "- Night Drive Demo - Music.wav",
                "",
                "## Logic Import Notes",
                "- Create or open a Logic Pro project at 48 kHz / 24-bit.",
                "- Set the project tempo to 92-98 BPM and key center to D minor.",
                "- Import all stems at bar 1 / 0:00 so they stay aligned.",
                "- Keep the stereo bounce or rough mix as a muted reference track.",
                "- Color-code drums, bass, harmony, and texture groups before editing.",
                "- Keep rough mix muted comparison.",
                "",
                "## Automation Boundaries",
                "- Use Logic Pro for listening, editing, arranging, and finishing.",
                "- Prefer clean asset preparation and imports over brittle UI scripting.",
                "- Do not promise deterministic chord-track, plugin, or deep region editing from outside Logic.",
            ],
        )

    def test_uses_fallback_sections_stems_and_notes(self) -> None:
        lines = self.read_output(
            "--title",
            "Untitled",
            "--tempo",
            "120 BPM",
            "--key",
            "C major",
        )

        self.assertEqual(
            lines,
            [
                "# Logic Delivery Notes: Untitled",
                "",
                "## Session",
                "- Title: Untitled",
                "- Tempo: 120 BPM",
                "- Key: C major",
                "- Sample rate: 48 kHz",
                "- Bit depth: 24-bit",
                "",
                "## Section Map",
                "- TBD - add section names, timings, and energy notes.",
                "",
                "## Stem Naming",
                "- Export stems from 0:00 and keep them full song length.",
                "- Use consistent title prefixes so files sort together in Finder and Logic.",
                "- TBD - list expected stem filenames before export.",
                "",
                "## Logic Import Notes",
                "- Create or open a Logic Pro project at 48 kHz / 24-bit.",
                "- Set the project tempo to 120 BPM and key center to C major.",
                "- Import all stems at bar 1 / 0:00 so they stay aligned.",
                "- Keep the stereo bounce or rough mix as a muted reference track.",
                "- Color-code drums, bass, harmony, and texture groups before editing.",
                "- No extra import notes provided.",
                "",
                "## Automation Boundaries",
                "- Use Logic Pro for listening, editing, arranging, and finishing.",
                "- Prefer clean asset preparation and imports over brittle UI scripting.",
                "- Do not promise deterministic chord-track, plugin, or deep region editing from outside Logic.",
            ],
        )

    def test_readme_documents_basic_command_and_output_contract(self) -> None:
        content = README.read_text(encoding="utf-8")
        self.assertIn("scripts/create_delivery_notes.py", content)
        self.assertIn("--section", content)
        self.assertIn("--stem", content)
        self.assertIn("The generated note keeps a fixed section order", content)
        self.assertIn("The generated brief always writes `Title:` then `Brief:`", content)


if __name__ == "__main__":
    unittest.main()
