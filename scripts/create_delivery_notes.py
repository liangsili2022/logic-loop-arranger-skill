#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_AUTOMATION_BOUNDARIES = [
    "Use Logic Pro for listening, editing, arranging, and finishing.",
    "Prefer clean asset preparation and imports over brittle UI scripting.",
    "Do not promise deterministic chord-track, plugin, or deep region editing from outside Logic.",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create Logic Pro delivery notes for accompaniment handoff packages."
    )
    parser.add_argument("--title", required=True, help="Session or song title")
    parser.add_argument("--tempo", required=True, help="Tempo or tempo range")
    parser.add_argument("--key", required=True, help="Key center")
    parser.add_argument(
        "--section",
        action="append",
        default=[],
        help="Section map entry. Repeat for each section.",
    )
    parser.add_argument(
        "--stem",
        action="append",
        default=[],
        help="Expected stem filename or stem group. Repeat for each stem.",
    )
    parser.add_argument("--sample-rate", default="48 kHz", help="Expected sample rate")
    parser.add_argument("--bit-depth", default="24-bit", help="Expected bit depth")
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        help="Additional Logic import note. Repeat as needed.",
    )
    parser.add_argument("--out", default="logic-delivery-notes.md", help="Output file path")
    return parser


def bullet_list(items: list[str], fallback: str) -> list[str]:
    values = [item.strip() for item in items if item.strip()]
    if not values:
        return [f"- {fallback}"]
    return [f"- {item}" for item in values]


def build_notes(args: argparse.Namespace) -> str:
    lines = [
        f"# Logic Delivery Notes: {args.title}",
        "",
        "## Session",
        f"- Title: {args.title}",
        f"- Tempo: {args.tempo}",
        f"- Key: {args.key}",
        f"- Sample rate: {args.sample_rate}",
        f"- Bit depth: {args.bit_depth}",
        "",
        "## Section Map",
        *bullet_list(args.section, "TBD - add section names, timings, and energy notes."),
        "",
        "## Stem Naming",
        "- Export stems from 0:00 and keep them full song length.",
        "- Use consistent title prefixes so files sort together in Finder and Logic.",
        *bullet_list(args.stem, "TBD - list expected stem filenames before export."),
        "",
        "## Logic Import Notes",
        f"- Create or open a Logic Pro project at {args.sample_rate} / {args.bit_depth}.",
        f"- Set the project tempo to {args.tempo} and key center to {args.key}.",
        "- Import all stems at bar 1 / 0:00 so they stay aligned.",
        "- Keep the stereo bounce or rough mix as a muted reference track.",
        "- Color-code drums, bass, harmony, and texture groups before editing.",
        *bullet_list(args.note, "No extra import notes provided."),
        "",
        "## Automation Boundaries",
        *[f"- {item}" for item in DEFAULT_AUTOMATION_BOUNDARIES],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    out_path = Path(args.out)
    out_path.write_text(build_notes(args), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
