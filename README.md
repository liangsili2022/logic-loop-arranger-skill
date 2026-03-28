# Logic Loop Arranger

`Logic Loop Arranger` is an open-source Codex skill for creating accompaniment in Logic Pro with Apple Loops.

It is designed to act less like a generic assistant and more like a top-tier music producer:
- it starts by narrowing taste
- it translates vague creative language into production decisions
- it helps shape arrangement, structure, and delivery targets
- it prepares a Logic-friendly handoff instead of pretending Logic has a full external API

This repository is intentionally focused on accompaniment.

It does not target:
- lyric writing
- topline melody writing
- vocal synthesis
- deep plugin automation inside Logic Pro

## Why this exists

There are already useful adjacent projects for:
- Logic UI automation
- Logic Scripter examples
- MIDI scripting inside Logic

What is still missing is a practical middle layer:

an agent workflow that helps a creator move from:
- vague taste
- artist references
- mood words
- arrangement goals

to:
- a locked production brief
- a coherent Apple Loops accompaniment direction
- a clean handoff for Logic Pro

That is the gap this skill is meant to fill.

## What the skill does

- runs a producer-style creative intake
- locks a compact production brief before building
- guides Apple Loops selection and arrangement choices
- helps structure intros, verses, pre-choruses, hooks, bridges, and outros
- supports accompaniment packaging for WAV, stems, and Logic handoff
- keeps Logic automation honest and realistic

## Core idea

The skill should feel like a Grammy-level producer in the room:
- decisive
- taste-driven
- collaborative
- focused on narrowing direction before touching production

The interaction style matters as much as the technical steps.

## Who it is for

- songwriters building a backing track before toplining
- producers sketching Apple-Loops-based demos quickly
- artists who want a guided production brief before arranging
- Codex users who need a Logic-friendly accompaniment workflow

## Repository layout

```text
logic-loop-arranger-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   └── example-briefs.md
├── references/
│   ├── accompaniment-workflow.md
│   ├── intake-patterns.md
│   └── logic-automation-limits.md
├── scripts/
│   └── create_producer_brief.py
├── LICENSE
├── .gitignore
└── README.md
```

## Install locally

Copy this folder into your Codex skills directory:

```bash
cp -R logic-loop-arranger-skill "$CODEX_HOME/skills/"
```

Then trigger it with requests about:
- creating a Logic Pro accompaniment
- arranging with Apple Loops
- extending or refining a backing track
- preparing stems and Logic-ready delivery assets

## Quick start

Examples of the kinds of prompts this skill should handle well:

- “Help me build a slow R&B accompaniment in Logic with Apple Loops.”
- “I want a late-night pop/R&B backing track, more SZA than glossy radio.”
- “Turn this vague mood into a producer brief before we arrange anything.”
- “Expand this Apple Loops beat into a full song structure and prep stems for Logic.”

For sample creative briefs, see [examples/example-briefs.md](examples/example-briefs.md).

## Bundled assets

### References

- [references/intake-patterns.md](references/intake-patterns.md)
  Producer-style intake prompts and ambiguity-reduction patterns

- [references/accompaniment-workflow.md](references/accompaniment-workflow.md)
  Loop selection, arrangement, export, and packaging heuristics

- [references/logic-automation-limits.md](references/logic-automation-limits.md)
  Honest guidance on what Logic Pro can and cannot be automated reliably

### Script

- [scripts/create_producer_brief.py](scripts/create_producer_brief.py)
  A small helper for turning a locked direction into a reusable brief file

## Design principles

- Producer-first interaction
- Minimal but high-value questions
- Taste translation before execution
- Coherent loop-family selection over random stacking
- Deterministic packaging where possible
- Honest boundaries around Logic Pro automation

## Current scope

This repository is a strong open-source foundation for:
- interactive accompaniment direction
- producer-style workflow scaffolding
- repeatable handoff thinking for Logic Pro sessions

It is not yet a full automation toolkit for authoring Logic sessions.

## Roadmap ideas

- more example briefs across genres
- helper scripts for delivery note generation
- optional packaging templates for stems and Logic prep
- a stronger public prompt library for producer-style intake

## License

MIT
