#!/usr/bin/env python3
"""blocklist_scan.py - ship gate: nothing private may reach a shipped file.

Scans text sources (scripts, SRTs, packaging, card/overlay code, JSON), file NAMES, embedded media metadata, and (if tesseract and
ffmpeg are installed) OCR of one frame every 2 s of any video. Patterns = built-ins (e-mail addresses, home-folder paths, key-like
strings) + one case-insensitive regex per line of blocklist.txt (your own terms: employer, client, your name, handles to keep off screen).
Exit 0 = clean, 1 = HIT (the ship is blocked).

Usage:  python3 tools/blocklist_scan.py <file-or-folder> [...]   [--list path/to/blocklist.txt]
"""
import glob, os, re, shutil, subprocess, sys, tempfile

AT = chr(64)
BUILTIN = [
    (re.compile(r'[A-Za-z0-9._%+-]+' + AT + r'[A-Za-z0-9.-]+\.[A-Za-z]{2,}'), 'e-mail address'),
    (re.compile('/Us' + 'ers/[^/\\s]+/'), 'absolute home-folder path'),
    (re.compile(r'\b(?:s' + r'k|x' + r'i)-[A-Za-z0-9_-]{16,}'), 'key-like string'),
    (re.compile(r'(?i)\bapi' + r'[_-]?key\b\s*[:=]'), 'key assignment'),
]
TEXT = {'.md', '.txt', '.srt', '.vtt', '.js', '.html', '.json', '.py', '.sh', '.css', '.csv'}
IMG = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.tif', '.tiff'}
VID = {'.mp4', '.mov'}
SKIP_DIRS = {'out', 'node_modules', '.git', 'logs'}
TESS = shutil.which('tesseract')
SELF = os.path.abspath(__file__)


def load_list(path):
    pats = []
    if path and os.path.exists(path):
        for line in open(path, encoding='utf-8'):
            line = line.strip()
            if line and not line.startswith('#'):
                pats.append((re.compile(line, re.I), 'blocklist: ' + line))
    return pats


def main(argv):
    lst = os.path.join(os.path.dirname(SELF), 'blocklist.txt')
    if '--list' in argv:
        i = argv.index('--list'); lst = argv[i + 1]; argv = argv[:i] + argv[i + 2:]
    pats = BUILTIN + load_list(lst)
    hits, ocr = [], []

    def scan_text(path, text):
        for n, line in enumerate(text.splitlines(), 1):
            for rx, why in pats:
                if rx.search(line):
                    hits.append((path, n, why, line.strip()[:100]))

    def scan(path):
        if os.path.abspath(path) == SELF or os.path.basename(path) in ('blocklist.txt', 'blocklist.example.txt'):
            return
        ext = os.path.splitext(path)[1].lower()
        for rx, why in pats:
            if rx.search(os.path.basename(path)):
                hits.append((path, 0, why + ' (file name)', ''))
        if ext in TEXT:
            scan_text(path, open(path, encoding='utf-8', errors='replace').read())
        elif ext in IMG | VID | {'.m4a', '.mp3', '.wav'}:
            if shutil.which('ffprobe'):
                meta = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format_tags:stream_tags', '-of', 'flat', path],
                                      capture_output=True, text=True).stdout
                scan_text(path + ' [metadata]', meta)
            if ext in VID and TESS and shutil.which('ffmpeg'):
                with tempfile.TemporaryDirectory() as td:
                    subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf', 'fps=1/2,scale=1920:-2', os.path.join(td, 'o_%04d.png')], check=True)
                    frames = sorted(glob.glob(os.path.join(td, 'o_*.png')))
                    for i, f in enumerate(frames):
                        txt = subprocess.run([TESS, f, '-', '-l', 'eng', '--psm', '11'], capture_output=True, text=True).stdout
                        scan_text(f'{path} [OCR frame at {i * 2} s]', txt)
                    ocr.append(f'{os.path.basename(path)}: {len(frames)} frames')
            elif ext in IMG and ext != '.svg' and TESS:
                txt = subprocess.run([TESS, path, '-', '-l', 'eng', '--psm', '11'], capture_output=True, text=True).stdout
                scan_text(path + ' [OCR]', txt)
            if ext == '.svg':
                scan_text(path, open(path, encoding='utf-8', errors='replace').read())

    for root in argv[1:]:
        if os.path.isdir(root):
            for d, dirs, files in os.walk(root):
                dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
                for f in files:
                    scan(os.path.join(d, f))
        else:
            scan(root)
    for h in hits:
        print('HIT', *h, sep=' | ')
    print('BLOCKLIST SCAN', 'CLEAN' if not hits else f'BLOCKED ({len(hits)} hits)',
          '| OCR: ' + ('; '.join(ocr) if ocr else ('none run' if TESS else 'tesseract not installed: do the contact-sheet eye pass')))
    return 1 if hits else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
