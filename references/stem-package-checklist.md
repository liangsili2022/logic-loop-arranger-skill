# Stem Package Checklist

Use this checklist before handing accompaniment stems to a songwriter, producer, or Logic Pro session.

The goal is a package that opens cleanly, stays aligned, and does not depend on fragile Logic Pro automation.

## Required Files

- Stereo reference mix or rough bounce.
- Full-length stems, exported from the same start point.
- Arrangement map with section names and timings.
- Logic delivery notes when a handoff note is needed.
- Source loop references when Apple Loops or third-party loops define the sound.
- Optional producer brief if the recipient needs creative context.

## Alignment

- Export every stem from 0:00 or bar 1, even when the part enters later.
- Keep all stems the same total length.
- Include silence at the start and end where needed so files remain aligned after import.
- Avoid trimming stems to only active regions unless the recipient explicitly requests clips.
- Confirm the stereo bounce and stems start at the same point.

## Session Format

- Use one sample rate across all audio files.
- Use one bit depth across all audio files.
- Document sample rate and bit depth in the handoff notes.
- Prefer WAV for interchange unless the recipient requests another format.
- Include tempo and key center in the notes, even when the harmony is intentionally ambiguous.

## Naming Conventions

Use predictable names that sort together:

```text
<Title> - Stereo Reference.wav
<Title> - Drums.wav
<Title> - Bass.wav
<Title> - Harmony.wav
<Title> - Texture.wav
<Title> - FX.wav
<Title> - Logic Delivery Notes.md
```

Guidelines:

- Keep the song or session title at the start of every filename.
- Use broad musical groups instead of unclear exports like `Audio 1.wav`.
- Avoid special characters that can break shell scripts or cloud sync tools.
- Use consistent capitalization and spacing.

## Source Loop References

When Apple Loops shape the arrangement, capture enough context for a future editor to understand the source:

- loop name
- role in the arrangement
- section where it appears
- any pitch, tempo, or edit treatment
- whether the loop is essential or replaceable

Example:

```text
Soft R&B Kit 02 - drums - verse and hook - tempo matched - essential groove
Warm Electric Keys 04 - harmony - full song - pitched down 2 semitones - replaceable
```

## Arrangement Map

Include a compact section map:

```text
Intro: 0:00-0:08 - keys and texture only
Verse: 0:08-0:33 - drums enter, bass restrained
Hook: 0:33-0:49 - wider drums, bass committed
Breakdown: 0:49-1:05 - drums thin out, texture remains
Final hook: 1:05-1:29 - restore energy with one new detail
Outro: 1:29-1:37 - reduce density and resolve
```

The map should help the recipient navigate the package without reopening the original arrangement environment.

## Sanity Checks

Before handoff:

- Import all stems into a clean Logic Pro project.
- Confirm every file starts together at 0:00 or bar 1.
- Confirm the summed stems roughly match the stereo reference.
- Check that the tempo and key notes match the session.
- Confirm no stem is accidentally muted, clipped, empty, or exported at the wrong length.
- Confirm all filenames match the package naming convention.
- Confirm source loop references are included when relevant.
- Confirm the package opens without private local paths.

## Logic Pro Handoff Boundaries

Keep the handoff practical and honest:

- Treat Logic Pro as the listening, editing, arranging, and finishing environment.
- Prefer clean audio files and clear notes over brittle UI automation.
- Do not promise that the package can populate chord tracks, plugin chains, or detailed region edits from outside Logic.
- Use generated notes to speed up import and review, not to replace musical judgment inside Logic.
