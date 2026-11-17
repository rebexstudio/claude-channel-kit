# GATES · <channel>

A gate is a fixed stop in production. The work does not move to the next stage, and no credits are spent, until every **HARD** item passes. Items are measured by script or counted, not scored by opinion. **ADVISORY** items are measured and logged; a miss needs one line of reason, not a rebuild.
Add an item only when a real fault or a measured reference justifies it, and add the matching line to `logs/error_ledger.md`.

## Gate 0 · Packaging, before the script
| | Item | Pass when | Why |
|---|---|---|---|
| HARD | Title + thumbnail concept exist | one title, one thumbnail sketch, both readable at 168 px wide | packaging decides the click; a topic with no strong title is not made |
| HARD | Title states a claim, paradox, list or news | not a survey | surveys underperform claims in the lane data |
| HARD | Topic carries a testable claim | one claim with a number the video checks on screen | |
| HARD | Topic has evidence | a lane outlier ≥3×, a comment cluster, or a search phrase | |
| ADVISORY | Title / thumbnail score logged | number written down, no threshold | second opinion only |

## Gate 1 · Script, before any visual work
| | Item | Pass when | Why |
|---|---|---|---|
| HARD | Opening is concrete | first sentence names a person, place, date, number or something we did; no channel intro | |
| HARD | Hook density | ≥5 beats in the first 40 s | |
| HARD | One question planted and paid | planted in the first 60 s, paid at 85 % of runtime or later | |
| HARD | Every number has a source | source line per number, read verbatim | |

## Gate 2 · Silent build, before any narration is requested
| | Item | Pass when | Tool |
|---|---|---|---|
| HARD | No dead picture | longest span without visible change ≤ `<7>` s | `tools/dead_picture.py` |
| HARD | Text readable | cap height ≥ `<52>` px at 1080p; text inside the safe area | `tools/text_check.py` |
| HARD | Privacy clean | blocklist scan clean (text + OCR) | `tools/blocklist_scan.py` |

## Gate 3 · Voiced build, before the file goes to `send/`
| | Item | Pass when | Tool |
|---|---|---|---|
| HARD | Sentence-level picture match | every named thing the voice says appears on screen within ≤2 s | `tools/sentence_match.py` |
| HARD | Pace | narration `<130–160>` wpm set at generation, never time-stretched below 0.92× | log |
| HARD | Same composition never twice in a row | counted from the plan | plan |
| HARD | Loudness / ducking | master `<-14 LUFS>`, music ≥10 dB under voice | ffmpeg loudnorm |
| HARD | SRT shipped | made from the line timings | script |

## Gate 4 · Before upload (manager)
Blocklist scan repeated on the final file; title, description, SRT, thumbnail checked; human has watched; human's yes recorded.
