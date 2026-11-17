---
name: setup
description: First-run interview that fills this kit for a new channel. Use when CLAUDE.md or state/STATE.md still contain empty `<…>` fields, or when the human asks to set up, start over or add a channel. Asks the niche, channel name, language, audience, video length and cadence, voice tool and monthly budget, then fills CLAUDE.md and the state templates from the answers and writes the first DECISIONS.md entry. Do NOT use once the fields are filled, except to add a channel.
---

# setup: interview first, files second

Ask in two or three short rounds, never all at once. One question at a time is fine; offer a default only when one is obvious. Write nothing until the answers are in.

## Questions
1. **Niche / topic lane** and who the **audience** is (one sentence).
2. **Channel name** (or "undecided": leave `<channel name>` and note it as open).
3. **Language** of the videos and of the subtitles.
4. **Video length** band and **cadence** (videos per week or month, and the preferred slot, if any).
5. **Voice tool** (a text-to-speech service, own voice, none yet) and the **monthly budget** for tools in total.
6. **Goal** for the first six months (views, subscribers, revenue step) and the **freeze length** (how many videos before changing concept; suggest 4).
7. Anything that must **never** appear in a video (employer, clients, names): these go to `tools/blocklist.txt`.

## Then, in this order
1. Fill every `<…>` field in `CLAUDE.md` and `state/STATE.md` (goal, slot, loudness target if the voice tool needs one, allowed links, freeze length).
2. Copy `state/channel_template.md` to `state/<channel-slug>.md` and fill promise, format, packaging rules from the answers; leave "Open questions" for what the human did not know.
3. Edit `state/gates.md` thresholds that depend on the answers (pace in words per minute for the language, length-dependent items).
4. Create `tools/blocklist.txt` from `tools/blocklist.example.txt` with the answers to question 7.
5. Replace the example row in `DECISIONS.md` with **D-001 · Setup interview**: the answers, the date, "decided by: the human".
6. Add the first line of `logs/spend_ledger.md` only when a spend actually happens; record the monthly budget in `state/STATE.md`.
7. Read the filled files back to the human in ten lines, ask for corrections, and stop. Do not start production.

Never invent an answer. If the human says "you decide", propose one, mark it as a proposal in `DECISIONS.md`, and let them confirm.
