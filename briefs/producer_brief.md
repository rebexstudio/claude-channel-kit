# Producer brief (copy, fill, send as the first message of a producer session)

Start the session with the strongest model; one session per video, kept for the whole video.

**Channel:** `<name>` · **Video slug:** `<slug>` · **Folder:** `<path>`
**Read first:** `state/STATE.md`, `state/<channel>.md`, `state/gates.md`, `logs/error_ledger.md`.
**Skills:** use `packaging` for Gate 0, `rea-video` on our own cut before a fix round.

**Task:** `<one sentence: the video, its claim, its length band>`
**Inputs:** `<script/plan/assets already in the folder>`
**Done when:** every HARD gate for the current stage passes (scripts in `tools/`), the deliverable is in `send/`, and `producer_log.md` has the gate output.

**Yes-rules for this job** (nothing else is allowed without a new yes in your chat):
- Spend: `<none | up to N credits of X, human said yes on date>`
- Downloads / installs: `<none | named>`
- Public actions: none. The manager schedules and uploads.

**Report** only when the deliverable is in `send/` or a human decision is needed: one line + path, under 150 words. Progress goes in `producer_log.md`.
**Hard rules:** blocklist scan before `send/`; no secrets read or printed; no personal text on screen; every number sourced.
