---
name: channel-note
description: Write research/<channel>/CHANNEL_NOTE.md on one rival or model YouTube channel — facts table, how it is made, compared with us, a "for the manager" list, sources and limits — and add its row to references/channel_database.md. Use whenever asked for a channel note, a profile of a channel, "what is X channel doing", whether a channel is worth learning from, or to add a channel to the channel database. Do NOT use for a single video breakdown (rea-video), for a new video's title/thumbnail (packaging), or for earnings estimates without a channel note.
---

# channel-note: one channel, one CHANNEL_NOTE.md

Keep finished notes under `research/<channel>/CHANNEL_NOTE.md`; read two before you start. They are metadata-first, honest about what was not watched, and end in advice the manager can use.

## Standing rules
- **Paid tools (stats, videos, outliers, earnings, comments) only after the human's yes** in this session's chat, with the credit estimate. Downloads only after a yes with a size estimate; videos in a browser are muted.
- Free data first: yt-dlp metadata (`/videos`, `/shorts`, per-video), the channel About page, descriptions, chapters, tags, thumbnails.
- Never read or print API keys or `.env` files.
- Numbers are copied as sources give them. Never invent; write `n/a`. Mark every judgement as judgement. Estimates (earnings, effort) are labelled estimates.

## Where numbers come from
Page data / yt-dlp for: subs, video count, first upload, per-video views/likes/comments/length, titles, tags, chapters. A paid tool (after yes) for: earnings estimate, outlier scores, views/subs of rivals, comment themes. Put the pull date next to each block; a note with numbers and no date is unusable.

## Sections, in this order
Header: `# <Channel> (@handle): channel note`, then one paragraph: what was used (metadata, pages, thumbnails; video played/downloaded yes/no; credits spent).
1. **Facts** (table or bullets): channel id, subs, videos, total views, first upload and age, cadence, length band, median and best views, views÷subs for the top video. Add title and thumbnail patterns with medians per pattern where there are ≥8 videos; over/under-performers vs the median.
2. **How it is made**: pipeline, tools, voice, music, picture type, cost per video. State the source of each claim (creator's own words / thumbnails / video watched) and keep inference marked as judgement. If one video was analysed, add a short "Confirmed from the video" block pointing to its `rea-video` sheet.
3. **Compared with us**: against the relevant channel of ours (look, pipeline, format, length, cadence); say what is out of our reach.
4. **For the manager**: numbered, actionable: adapt / avoid, topic collisions with our videos, what is worth a real test. Say what the note does *not* prove.
5. **Sources and limits**: every file and tool, what was not checked and what a next step would cost (download size, credits).

## Row in `references/channel_database.md`
1. Search the channel by name and id in `channel_database.md` and `channel_database.csv`. If a row exists, **extend its cells** and add the new source and date; never add a second row. Where sources disagree show both: "16.6K (archive); 14.4K (other)".
2. Otherwise add one row to the right section table and the same row to the csv (section letter as the first column).
3. Exact 14 columns, in this order:
`Channel | Handle or id | Lane/topic | Age or first upload | Subs | Videos | Median views | Best views | Typical length | Cadence | Format | Key finding for us | Source file(s) | Data date`
4. Rules: no row without a source file path; `Data date` = the date the numbers were pulled, not the date written; `n/a` when unmeasured; if only an average exists write "n/a (average X)"; earnings are estimates, not revenue.

A channel-note run writes the note and the database row (md + csv), nothing else. Do not edit `DECISIONS.md` or state files; tell the manager what to log.
