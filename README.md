# Channel-manager starter kit

An open workspace template for running a small YouTube operation with Claude Code sessions: one manager session that decides and keeps the files, producer sessions that build one video each, research sessions that read and measure. It is text files, three skills and four gate scripts. No framework, no service, nothing to install beyond Python.

**as is, no support, updated on Thursdays**

## What is in it
- `CLAUDE.md`: the manager's standing instructions (fill the `<…>` fields once).
- `state/`: `STATE.md` (shared rules), `channel_template.md` (one page per channel), `gates.md` (the stops in production).
- `DECISIONS.md`: format for new decisions; `logs/error_ledger.md` and `logs/spend_ledger.md`: headers plus one invented example row each.
- `.claude/skills/`: `setup` (first-run interview), `rea-video` (break one video into a sheet), `packaging` (title and thumbnail before the script), `channel-note` (profile one channel).
- `briefs/`: a starter brief for a producer session and one for a research session.
- `tools/`: `blocklist_scan.py`, `dead_picture.py`, `text_check.py`, `sentence_match.py`; see `tools/README.md`.

## How to start
1. Copy the folder and open it in Claude Code as the manager session. It starts with an interview (the `setup` skill: niche, channel name, language, audience, length and cadence, voice tool, monthly budget) and fills `CLAUDE.md` and the state templates from your answers.
2. Copy `tools/blocklist.example.txt` to `tools/blocklist.txt` and add the terms that must never reach a video (employer, clients, your name).
3. Copy `state/channel_template.md` once per channel; copy `briefs/producer_brief.md` and send it as the first message of a producer session.
4. Keep both ledgers current: the error ledger after every fault, the spend ledger on every spend.

## The method in ten lines
1. The manager decides and keeps state; producers produce; research reads; the human owns logins, uploads and payments.
2. Rules live in files (`state/`), not in chat; a decision that changes a rule edits the state file in the same step.
3. Nothing goes public before the human has watched the file; AI review is a floor, never a pass.
4. No spend, download or install without the human's yes in the chat that runs it, estimate shown first.
5. A gate is measured or counted by script, never scored by opinion; instruments run before eyes.
6. Every fault becomes one line in the error ledger with the check that now catches it; every job reads the ledger first.
7. Titles are claims, paradoxes or questions, never surveys; packaging is made before the script.
8. Open on a concrete thing and a number; plant one question early and pay it late.
9. Adapt a model channel's structure, never its script; every number has a source.
10. Producers report only on finished work; one session per video; messages between sessions point at files.

## Where it lives
Published by the account rebexstudio. Remote: `https://github.com/rebexstudio/claude-channel-kit`.

Build your own character and look; this kit gives the method, not the show.

## License
MIT, see `LICENSE`.
