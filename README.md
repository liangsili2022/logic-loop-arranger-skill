# Logic Loop Arranger

An open-source Codex skill for interactive accompaniment creation in Logic Pro using Apple Loops.

This skill is designed to behave like a high-level record producer:
- it starts by clarifying taste and direction
- it narrows mood, references, tempo, key, and deliverables
- it then guides or executes accompaniment creation
- it packages results for Logic-friendly handoff

This project is intentionally focused on accompaniment only.

It does not target:
- lyric writing
- topline melody writing
- vocal synthesis
- deep plugin-level Logic Pro automation

## What the skill does

- Creative intake with producer-style questioning
- Production brief creation
- Apple Loops arrangement guidance
- Section planning for pop / R&B / hip-hop accompaniment
- Export and handoff guidance
- Logic Pro workflow support with realistic automation limits

## Repository layout

```text
logic-loop-arranger-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── accompaniment-workflow.md
│   ├── intake-patterns.md
│   └── logic-automation-limits.md
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
- expanding or refining a backing track
- preparing Logic-friendly export packages

## Design principles

- Producer-first interaction
- Minimal but high-value questions
- Strong taste translation
- Deterministic packaging where possible
- Honest boundaries around Logic Pro automation

## Status

Current version is a strong skill skeleton for accompaniment ideation and workflow guidance.

Next likely upgrades:
- bundled helper scripts for repeatable arrangement packaging
- example project briefs
- optional templates for stems and delivery notes

