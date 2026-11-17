---
name: rea-video
description: Reverse-engineer one YouTube video (a rival's, a model channel's, or our own cut) into a SHEET.md — duration, wpm, shots and cuts/min, acts, picture mix, caption grammar, music level, hook beats, withheld object, orientation device, packaging, plus a stills sheet; when the video is our own, also the "≤7 ranked fixes" review. Use whenever asked to "rea" a video, analyse/break down a video, make a SHEET.md, check cuts per minute, pace or hook, or review our own cut against a model. Do NOT use for channel-level notes (use channel-note), titles/thumbnails for a new video (use packaging), or for writing scripts.
---

# rea-video: one video in, one SHEET.md out

Why this exists: every producer used to get the same brief re-typed. Keep your finished sheets under `research/<slug>/SHEET.md`; open one before you start and match its tone: plain, numbers first, by-eye corrections where the tool is wrong.

## Inputs
- A video URL or a local file (copy it read-only; never edit anything in `send/`).
- Channel context: whose video it is (rival / model / ours), and which of our channels it feeds. If the human gave a question list (e.g. "joke rate", "presenter share"), answer those as extra sections.
- Output folder: `research/<slug>/` (sheet, `stills`, `transcript_timed.txt`).

## Standing rules (they bind this skill without exception)
1. **No download without the human's yes in this session's chat**, asked with a size estimate ("720p, about 0.1 GB, 10 min"). A yes in another chat is not a yes here. Prefer 720p.
2. **Muted playback.** Videos watched in a browser are muted; stills and transcripts are the working material.
3. **Delete the source file after the sheet is written** (keep stills, transcript, report). Note "source deleted" in the sheet header.
4. **No paid-tool credits without a yes** (transcripts, stats, comments all cost). Free route first: yt-dlp metadata and auto-captions, page data.
5. Never read or print API keys or `.env` files; nothing personal goes into stills.
6. Do not copy scripts or wording from the video. The sheet records structure, never lines to reuse.

## Method
1. Decompose the file at 720p with ffmpeg (scene-change detection for shots and cuts, `loudnorm`/`ebur128` for loudness; stem separation only if installed). Log to `decompose.log`.
2. Pull ~13–30 evenly spaced stills into one sheet (`<slug>_stills.png`, tile = one frame, time in the caption). Look at them; add a timed transcript (`transcript_timed.txt`) from auto-captions. If captions roll, the raw word count is 3× too high: dedupe before computing wpm.
3. **Correct the tool by eye.** Automatic picture-type labels are guesses from pixel statistics and are often wrong on flat graphics or stick figures; trust the shot list, cut rate and loudness, and say which labels you overrode and why. For a one-scene video the shot count is meaningless: count visible changes from 2 fps frames instead.
4. Write `SHEET.md`.

## SHEET.md: fixed sections, in this order
Title line: `# <Channel> — "<video title>"`, then URL · analysed date · tools used · resolution · "source deleted".
1. **Fact table** (Field | Value): duration · views / age · channel size (subs, videos, views÷subs) · narration (words, **wpm**, hook and recap wpm) · shots (count, median, p10/p90, longest) · **cuts/min** overall and per minute · camera split · voice share of runtime.
2. **Acts** (% of runtime): span · % · shots · median shot · cuts/min · main picture. Say if the shape is fast hook / slow middle / fast recap.
3. **Picture mix** by eye (share of runtime, shots, median hold). Mark the shot-mix categories used (code graphics, archive, stock, 3D, map, cards, presenter). Note what is absent.
4. **Caption and label grammar**: slates, source tags, callouts, stamps, burned-in subtitles yes/no.
5. **Audio**: music tempo/key if measured; **music under voice in dB**; voice share; deliberate drops (≥12 dB); swells; "no bed" is a result, not a gap. Write "not measured" when stems were skipped.
6. **Hook, first 40 s**: table Time | Picture | Line/job. Count **hook beats** ("8 beats in 47 s").
7. **Withheld object and payoffs**: main question, where planted, where paid (% of runtime); refrains.
8. **Orientation device**: home-base picture, return count, **median gap between returns (s)**.
9. **Retention devices** (list) and, where relevant: **presenter share** and **joke rate** (joke beats per minute, aside pattern). Skip these two for formats without a presenter or jokes, and say so.
10. **The tool's verdict, and whether to trust it.**
11. **What our look could borrow** (3–5 numbered items, structure only) and what it cannot.
12. **Packaging**: title pattern, thumbnail (content, words, face yes/no), timeliness, views/subs. A table; the full craft is the `packaging` skill.
Units: seconds as `s`, times `m:ss`, loudness dB (whole-mix) with the stem gap noted, wpm over spoken span, percentages of runtime.

## Reviewing OUR OWN cut: add "≤7 ranked fixes"
Add a comparison table against the model (or against the targets in `state/gates.md`; say which targets do not apply to the format), then:

| # | Fix | Where | Evidence | Effort |
Rules: **at most 7**, ranked by effect on retention; each fix cites a time range and a measured number ("left panel empty 54 s = 28% of runtime"); effort is Small / Medium / Large; say which fixes need a re-voice (prefer none). Close with a one-line summary of which fixes move retention most. End the sheet with **Caveats** (what was estimated, what was not measured).

## Finish
Report to the requester: sheet path, 3 headline numbers, any rule you could not follow. Do not edit state files or `DECISIONS.md`; the manager does that.
