# Decision log · all channels

Format: one entry per decision, newest on top. Reversals are new entries, not edits.

**Do not read this file to learn the rules.** Current rules live in `state/`. When a decision changes a rule, update the state file in the same step. Deliveries ("X delivered, checks passed") go in the channel's own log, not here. Move entries older than a month to `archive/DECISIONS_through_<date>.md`.

Entry format:

```
- **D-<n> · <short title> (<who decided>, <date>).** Decision: <one or two sentences>. Why: <the evidence or the fault>. Changes: <state file / gate / skill edited>.
```

## <date>
- **D-001 · Example: one video a week in a fixed slot (human, 2026-01-01).** Decision: weekly, same weekday and hour. Why: a fixed slot is easier to keep than a "best time"; cadence is the lever we control. Changes: `state/STATE.md` working rules.
