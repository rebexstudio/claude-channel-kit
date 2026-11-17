# tools/

Self-contained gate scripts. Python 3; `numpy` and `ffmpeg` for `dead_picture.py`; `tesseract` optional for OCR in `blocklist_scan.py`. None of them touches the network. Each exits 1 when its gate fails, so a build script can stop on it.

| Script | Gate | Usage |
|---|---|---|
| `blocklist_scan.py` | privacy, before `send/` | `python3 tools/blocklist_scan.py send/ production/video1/script.md` (copy `blocklist.example.txt` to `blocklist.txt` and add your own terms first) |
| `dead_picture.py` | no dead picture, silent build | `python3 tools/dead_picture.py out/video.mp4 --limit 7` |
| `text_check.py` | text contained in the safe area and large enough | `python3 tools/text_check.py out/probe.json --floor 52` |
| `sentence_match.py` | the picture shows what the voice names | `python3 tools/sentence_match.py plan.json screen.json [aliases.json]` |

`text_check.py` and `sentence_match.py` read plain JSON your renderer writes (formats are in each file's header), so they work with any renderer.
