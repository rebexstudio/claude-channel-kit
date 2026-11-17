# Error ledger · one line per mistake found in a delivery · read before every producer/research job

The manager adds a line whenever a gate item is added because of a fault. Every line names a check that now catches the mistake; a line with no check is not finished.

| Date found | Video | What went wrong | Measurable check that now catches it |
|---|---|---|---|
| 2026-01-15 | example video 1 | picture and sentence drifted out of step for several seconds in beat 4 | Gate 3 sentence-level picture match: ≥20 sampled points, 0 mismatches (`tools/sentence_match.py`) |
