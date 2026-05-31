# Contributing

Thanks for helping improve Logic Loop Arranger.

This project is intentionally narrow: it helps Codex guide accompaniment creation in Logic Pro with Apple Loops. Contributions should preserve that focus.

## Good contributions

- clearer producer-intake prompts
- stronger accompaniment workflow references
- genre-specific brief examples
- small helper scripts for brief, note, or handoff generation
- tests for scripts and examples
- documentation that makes Logic Pro automation boundaries more honest

## Out of scope

- lyric generation
- lead-vocal melody writing
- vocal synthesis
- claims of full Logic Pro project automation
- brittle UI scripting for deep plugin or region editing
- unrelated DAW integrations without a clear maintenance path

## Local checks

Run these before opening a pull request:

```bash
python3 -m compileall scripts tests
python3 -m unittest discover -s tests
```

## Pull request guidelines

- Keep changes small and focused.
- Explain the user workflow the change improves.
- Include examples when changing prompts or references.
- Add or update tests when changing scripts.
- Do not add large binary assets unless they are essential and documented.

## Maintainer review checklist

- The change keeps the skill accompaniment-focused.
- The change does not overpromise Logic Pro automation.
- The README, examples, and skill instructions remain consistent.
- Scripts remain dependency-light unless there is a strong reason.
- The contribution is usable by a new Codex user without private context.
