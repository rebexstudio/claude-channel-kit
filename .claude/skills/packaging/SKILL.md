---
name: packaging
description: Gate 0 title and thumbnail package for one video, made before the script — five scored title variants (claim / paradox / question, under 70 characters), three one-scene thumbnails with 2–3 words, a phone-size side-by-side sheet and a rivals grid, and a packaging.md with the tables. Use whenever asked for Gate 0, packaging, "title and thumbnail", title variants, thumbnail concepts or a cover for a video, or when a title/thumbnail was rejected and needs redoing. Do NOT use for channel notes, video analysis (rea-video), scripts, channel art/avatar/banner, or for swapping a thumbnail after publishing.
---

# packaging: Gate 0, before the script

Rules come from `state/gates.md` (Gate 0 table). Order matters: a topic with no strong title is not made.

## Standing rules
- **Paid scoring credits and image generation only after the human's yes in this session's chat.** State the estimate first, then wait. A yes elsewhere does not carry over. Log credits spent in `packaging.md` and in `logs/spend_ledger.md`.
- Never read or print API keys or `.env` files; nothing personal on any image.
- No faces of real people, no invented quotes, never assert a legend as fact.

## 1. Angle
Pick the angle from the topic's testable claim (a number the video checks on screen) and the evidence line (lane outlier ≥3×, comment cluster or search phrase). Sell the doubt and the test, not "how they did it" if a rival already sold the trick. Check the rivals' titles and thumbnails for the same topic first (free: page data, yt-dlp).

## 2. Titles: five variants
- Form: **claim, paradox or question. Never a survey** ("Entire History of X"). Number first or a named place plus a number; "How" with a mechanism beats "Why …?"; a question may promise the test.
- **Under 70 characters** (count them, put the count in the table).
- Five distinct forms, not five rewordings. Mark the recommended one.
- Score all five with your scoring tool (advisory second opinion, no threshold) only after the yes; log scores.

## 3. Thumbnails: three variants
- **One scene with one predicament** (an object or crowd in trouble, a cutaway) + **2–3 words, ≥48 px at phone size**; the words are the question or the number.
- **Same layout across the whole catalogue**; the first thumbnail sets it. Variants differ in crop or moment, not in layout.
- **No chart elements, no faces of real people, no stamp** on the thumbnail.
- Route: code-drawn is the fallback; generated scene images are allowed under the same yes rule (estimate shown, invented imagery only).

## 4. HARD checks before anything leaves the folder
1. **Phone-size side-by-side sheet** (three thumbnails at ~168 px wide, one row): text readable, one idea each → `<ch>_<slug>_thumbs_phone.png`.
2. **Rivals grid**: the three placed among rivals' thumbnails for the same topic, at phone size → `<ch>_<slug>_thumbs_rivals.png`. Ours must read first in the grid or the concept goes back.
3. **Blocklist scan** (`tools/blocklist_scan.py`, including OCR on the images) clean, before anything goes to `send/`.
4. Big-screen glance at 1280×720 for artefacts.

## 5. Output files
- `send/<ch>_<slug>_thumb_A.jpg`, `_B.jpg`, `_C.jpg` (1280×720 JPG, <2 MB), plus the phone sheet and rivals grid. `<ch>` = channel short name, `<slug>` = video slug.
- `packaging.md` next to the production folder, with: angle paragraph (the doubt, the test, the rival taken); title table `# | Title | Form | Chars | Score`; credits line (yes quoted, credits spent); thumbnail table `| | File | Predicament | Words | Checked |`; recommendation for the human's pick, and what was not used and why.
- The human picks; no pick in 24 h = the manager takes the best-scored title and its thumbnail.

## Limits
The skill packages one video. After publishing, the 48 h click-through check and one thumbnail swap belong to the manager.
