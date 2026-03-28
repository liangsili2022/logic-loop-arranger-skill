#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a compact producer brief for accompaniment-focused sessions."
    )
    parser.add_argument("--title", default="Untitled Session")
    parser.add_argument("--style", required=True, help="Genre or substyle")
    parser.add_argument("--mood", required=True, help="Emotional direction")
    parser.add_argument("--references", default="", help="Comma-separated artist or song references")
    parser.add_argument("--tempo", required=True, help="Tempo or tempo range")
    parser.add_argument("--key", default="TBD", help="Key center")
    parser.add_argument("--harmony", default="TBD", help="Harmonic direction")
    parser.add_argument("--palette", required=True, help="Primary production palette")
    parser.add_argument("--finish", default="songwriting demo", help="Expected polish level")
    parser.add_argument("--deliverable", required=True, help="Requested output package")
    parser.add_argument("--out", default="producer-brief.txt", help="Output file path")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    references = [item.strip() for item in args.references.split(",") if item.strip()]
    lines = [
        f"Title: {args.title}",
        "Brief:",
        f"- Style: {args.style}",
        f"- Mood: {args.mood}",
        f"- Tempo: {args.tempo}",
        f"- Key: {args.key}",
        f"- Harmony: {args.harmony}",
        f"- Palette: {args.palette}",
        f"- Finish level: {args.finish}",
        f"- Deliverable: {args.deliverable}",
    ]

    if references:
        lines.append(f"- References: {', '.join(references)}")

    out_path = Path(args.out)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
