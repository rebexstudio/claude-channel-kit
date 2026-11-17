# STATE · shared rules (all channels)

Read this file plus your own channel's file in this folder. Nothing else is needed to start a job.
Only rules in force are listed; history is in `archive/`. Each rule may point at its decision, e.g. `[D-012]`.
Last rebuilt from the decision log: `<date>` (through D-`<n>`).

## Roles
- Manager decides. Producers (one session per channel) produce. Research sessions research. The human owns logins, uploads, payments.
- Anything public (publish, schedule, post) needs the human's single yes at that moment.
- Nothing goes public before the human has watched the file.
- Any spend, download or install needs the human's yes in that session's chat, estimate shown first.
- Goal: `<views / subscribers / revenue ladder>`.

## Working rules
- Error ledger: `logs/error_ledger.md`, one line per mistake found in a delivery with the check that now catches it; every producer and research job reads it before starting; the manager adds a line whenever a gate item is added because of a fault.
- Spend ledger: `logs/spend_ledger.md`, one line per spend; monthly summary to the human.
- Producers report only when a deliverable is in `send/` or a decision is needed.
- Mechanical checks run at low effort, judgment reviews at medium.
- Instruments before eyes: scripted checks run before any review.

## Privacy (hard rules, a hit blocks the ship)
- Nothing about the human's employer, clients or personal life in any video, script, SRT, thumbnail, title or description. Blocklist scan (text + OCR of frames every ~2 s) before anything goes to `send/`; the manager repeats it before upload.
- No screen recordings or screenshots of the human's computer or accounts. All on-screen software, chats and documents are invented textures.

## Content rules
- Descriptions carry a sources list; links only as allowed here: `<allowed links>`.
- No value judgement about any named channel on screen or in packaging.
- Model-channel method: structure, beats, hook pattern, length, cadence and packaging may be adapted; scripts are never copied.
- Every number has a source; our own calculations are labelled as ours.
- Audio: narration is the master, `<-14 LUFS>`; music and SFX ducked at least 10 dB under the voice.
- Every video ships with its own SRT made from the line timings.

## Disk
- After a stage passes its gate, producers delete that stage's intermediates (frame sequences, overlays, superseded parts) and keep code, assets, the composed file and the checks JSON. Never `send/`, never masters.

## Session hygiene
- A producer session lasts a whole video. Hand-off via `HANDOFF.md` only when the context cap is reached or the session stalls.
- Visual checks (contact sheet, OCR, phone-size frames) run in a cheaper subagent that returns only the verdict. Bash output goes to files; read tails only. No status polling.

## Freeze rule
- From a channel's first upload in its current form, no change to concept, look, voice or format until `<n>` videos are public. After that, changes come only from the channel's own data. Titles, thumbnails, topics, opens and length stay open to data from day one.

## Where things live
- `state/` current rules · `DECISIONS.md` new decisions only · `archive/` full history
- `send/` deliverables · `references/` notes on links and channels · `research/` reverse-engineering work
