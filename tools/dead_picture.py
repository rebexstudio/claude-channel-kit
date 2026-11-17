#!/usr/bin/env python3
"""dead_picture.py - "no dead picture" gate: how long does the picture go without a visible change?

Frames at 2 fps, 320x180 grey. A visible change between two samples 0.5 s apart = more than 2 % of the (unmasked) picture moving
more than 24 grey levels (label pops, highlights, camera moves, cuts). Mask the top and bottom rows (a pulsing stamp, a ticker)
so they cannot count as change.
Prints JSON: longest span without a change, where, and every span over --warn seconds.

Usage:  python3 tools/dead_picture.py video.mp4 [--ignore-top 18] [--ignore-bottom 30] [--warn 10] [--limit 7]
Needs ffmpeg and numpy. Exit 1 if the longest span exceeds --limit (default 7 s).
"""
import argparse, json, subprocess, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('video')
ap.add_argument('--ignore-top', type=int, default=18, help='rows (of 180) ignored at the top')
ap.add_argument('--ignore-bottom', type=int, default=30, help='rows (of 180) ignored at the bottom')
ap.add_argument('--warn', type=float, default=10.0)
ap.add_argument('--limit', type=float, default=7.0)
a = ap.parse_args()
W, H, FPS = 320, 180, 2
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', a.video, '-vf', f'fps={FPS},scale={W}:{H},format=gray', '-f', 'rawvideo', '-'],
                     capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.int16)[:, a.ignore_top:H - a.ignore_bottom, :]
if len(F) < 2:
    sys.exit('no frames decoded')
ch = [(np.abs(F[i] - F[i - 1]) > 24).sum() > .02 * F.shape[1] * F.shape[2] for i in range(1, len(F))]
T = [i / FPS for i, c in enumerate(ch, 1) if c]
D = len(F) / FPS
gaps = [(round(b - x, 2), round(x, 2)) for x, b in zip([0.0] + T, T + [D])]
worst = max(gaps)
print(json.dumps({'samples': len(F), 'changes': len(T), 'max_gap_s': worst[0], 'at_s': worst[1],
                  'spans_over_warn': [g for g in gaps if g[0] > a.warn]}))
sys.exit(1 if worst[0] > a.limit else 0)
