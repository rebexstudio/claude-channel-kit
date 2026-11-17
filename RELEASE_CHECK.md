# Release check

Blocklist scan over the whole folder before publishing. Required result: zero hits.

Patterns searched (case-insensitive, whole folder, excluding this file): the employer/company words and the standalone two-letter company abbreviation, e-mail addresses, the two key-prefix strings, the key-assignment word, absolute home-folder paths, the three channel handles, the owner's name and its parts, plus project names (channel names, video slugs, decision numbers of the source workspace).

Command (run from the repo root; the exact term list lives in the manager workspace's release notes and is not repeated here so this file stays clean):

    python3 tools/blocklist_scan.py .      # built-ins: e-mail, home path, key-like strings, key assignments
    grep -rniE '<terms above>' . --exclude=RELEASE_CHECK.md

Result (2026-11-17): **0 hits**. Two false positives in earlier runs (a flag name containing the key-prefix letters, renamed; an over-broad probe term matching ordinary words, narrowed) were resolved. `tools/blocklist_scan.py .` reports CLEAN.

Not covered: nothing under `research/`, `send/` or `references/` exists in this repo by design; no research data, channel database, competitor lists, scripts, channel numbers, keys or `.env` are included.

## Decisions applied (2026-11-17)
Repo name: `claude-channel-kit` (account github.com/rebexstudio; README remote line and LICENSE holder name the account only, no person). The kit starts with the `setup` interview skill. Show-specific content removed: second grep for fox, Rook, workshop, Cavendish, Robert, kraft/accent/palette words, mascot, presenter-as-default, the old show/channel names and "Thursday" as a default slot gives hits only in the allowed places: the README "as is" line, the account name `rebexstudio` (README, LICENSE), and the neutral analysis term "presenter share" in `rea-video`. Final result: **0 unexpected hits**; `tools/blocklist_scan.py .` CLEAN.
