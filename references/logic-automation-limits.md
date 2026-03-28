# Logic Automation Limits

## Core truth

Logic Pro does not expose a strong external composition API for agentic control.

What usually works:
- opening projects or files
- activating the app
- basic save / close operations
- limited GUI scripting
- handling simple prompts

What is fragile:
- deep region editing
- reliable chord-track editing
- plugin manipulation through UI scripting
- repeatable project-structure automation

## Recommended strategy

For accompaniment work:
- generate assets outside Logic when possible
- import audio and stems into Logic
- keep Logic as the editing and finishing environment

## Use GUI scripting only when

- opening a file
- confirming a sample-rate dialog
- revealing an asset for drag-and-drop
- starting playback if the window state is already stable

## Avoid promising

- robust chord-track population
- full project authoring through AppleScript
- deterministic plugin routing purely via UI automation

