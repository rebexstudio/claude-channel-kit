#!/usr/bin/env python3
"""text_check.py - text containment and size gate, measured from the layout, not by eye.

Input: a JSON list of every text element on screen, written by your renderer (one entry per element per sampled time):
  [{"t": 12.4, "shot": "s07", "text": "ONE NIGHT?", "x": 120, "y": 640, "w": 800, "h": 90, "font_px": 80}, ...]
  x, y, w, h = bounding box in pixels of a 1920x1080 frame; font_px = font size; the cap height is estimated as font_px * 0.7.
Checks: (1) CONTAINED: the box lies inside the safe area (default 5 % margin on every side) and inside the frame;
        (2) SIZE: cap height >= --floor px (default 52 at 1080p) so it stays readable at phone size.
Usage:  python3 tools/text_check.py probe.json [--margin 0.05] [--floor 52] [--cap-ratio 0.7]
Exit 1 if any element fails.
"""
import argparse, json, sys

ap = argparse.ArgumentParser()
ap.add_argument('probe')
ap.add_argument('--margin', type=float, default=0.05)
ap.add_argument('--floor', type=float, default=52)
ap.add_argument('--cap-ratio', type=float, default=0.7)
ap.add_argument('--frame', default='1920x1080')
a = ap.parse_args()
FW, FH = map(int, a.frame.split('x'))
mx, my = FW * a.margin, FH * a.margin
bad = {}
for e in json.load(open(a.probe)):
    why = []
    if e['x'] < 0 or e['y'] < 0 or e['x'] + e['w'] > FW or e['y'] + e['h'] > FH:
        why.append('outside frame')
    elif e['x'] < mx or e['y'] < my or e['x'] + e['w'] > FW - mx or e['y'] + e['h'] > FH - my:
        why.append('outside safe area')
    cap = e['font_px'] * a.cap_ratio
    if cap < a.floor - 0.5:
        why.append(f'cap {cap:.0f} px < {a.floor:g}')
    for w in why:
        bad.setdefault((e.get('shot', '?'), e['text'], w), e['t'])
for (shot, text, w), t in sorted(bad.items(), key=lambda kv: kv[1]):
    print(f'{shot} @ {t:.1f}s  {w}: {text[:50]!r}')
print(f'{len(bad)} text problems')
sys.exit(1 if bad else 0)
