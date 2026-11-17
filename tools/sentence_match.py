#!/usr/bin/env python3
"""sentence_match.py - sentence-level picture match: does the picture show what the voice names?

For every sentence of the narration, take the numbers and proper names it says; look at what is on screen from the sentence start to
0.5 s after its end; classify:  match = every named thing is on screen · loose = some · mismatch = none.
Also reports the lag (first appearance of a named thing minus the sentence start); a lag over --max-lag seconds is flagged.

Inputs (JSON):
  plan.json    [{"id": "b1s1", "t0": 3.2, "t1": 7.9, "text": "Forty ships crossed the hill in one night."}, ...]
  screen.json  [{"t": 3.2, "text": "40 SHIPS ONE NIGHT"}, {"t": 3.4, "text": "..."}, ...]   (all on-screen text per sample time;
               write it from your renderer's own layout, or OCR frames every 0.2-0.5 s; leave out always-on strips and stamps)
  aliases.json (optional) {"spoken respelling": "On-screen spelling"} for names spelled phonetically for the voice.
Usage:  python3 tools/sentence_match.py plan.json screen.json [aliases.json] [--max-lag 2]
Exit 1 if any sentence with named things mismatches or lags beyond --max-lag.
"""
import json, re, sys

ONES = {w: i for i, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
TENS = {w: 10 * (i + 2) for i, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety'.split())}
STOP = set('I THE OUR SO AND BUT NOW THEN HERE WHAT WHICH IS IT HE HIS ONE TWO FIRST DID WAS COULD HOW WHO WE IN UP ON AS A B IF NOT NO'.split())


def numbers(text):
    out = []
    for part in re.split(r'[,;:.?!"()]+', text.lower()):
        cur, any_ = 0, False
        for x in part.replace('-', ' ').split() + ['']:
            if x.isdigit():
                out.append(int(x)); continue
            if x in ONES or x in TENS:
                cur += ONES.get(x, 0) + TENS.get(x, 0); any_ = True
            elif x == 'hundred' and any_:
                cur *= 100
            elif x == 'thousand' and any_:
                cur *= 1000
            elif x == 'and' and any_:
                pass
            else:
                if any_ and cur > 2: out.append(cur)
                cur, any_ = 0, False
    return out


def names(text, alias):
    out = set()
    ws = re.sub(r'[“”"(),.;:?!…]', ' ', text).split()
    for i, w in enumerate(ws):
        w0 = re.sub(r"'s$", '', w)
        if w0.upper() in alias: out.add(alias[w0.upper()].upper()); continue
        if i > 0 and w0[:1].isupper() and len(w0) > 2 and w0.upper() not in STOP: out.add(w0.upper())
    return sorted(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    max_lag = float(sys.argv[sys.argv.index('--max-lag') + 1]) if '--max-lag' in sys.argv else 2.0
    if '--max-lag' in sys.argv: args = [a for a in args if a != str(max_lag) and a != sys.argv[sys.argv.index('--max-lag') + 1]]
    plan = json.load(open(args[0])); screen = sorted(json.load(open(args[1])), key=lambda s: s['t'])
    alias = {k.upper(): v for k, v in json.load(open(args[2])).items()} if len(args) > 2 else {}
    res = []
    for s in plan:
        keys = sorted({str(n) for n in numbers(s['text'])} | set(names(s['text'], alias)))
        if not keys:
            res.append((s['id'], 'none', None, [])); continue
        first = {}
        for fr in screen:
            if not (s['t0'] <= fr['t'] <= s['t1'] + 0.5): continue
            txt = fr['text'].upper().replace(',', '')
            for k in keys:
                if k not in first and re.search(r'(?<![0-9A-Z])' + re.escape(k) + r'(?![0-9A-Z])', txt):
                    first[k] = round(fr['t'] - s['t0'], 2)
        miss = [k for k in keys if k not in first]
        status = 'match' if not miss else 'loose' if first else 'mismatch'
        res.append((s['id'], status, min(first.values()) if first else None, miss))
    n = lambda st: sum(1 for r in res if r[1] == st)
    lags = [r[2] for r in res if r[2] is not None]
    bad = [r for r in res if r[1] == 'mismatch' or (r[2] or 0) > max_lag]
    for r in bad: print('FLAG', *r, sep=' | ')
    print(json.dumps({'sentences': len(res), 'with_named_things': len(res) - n('none'), 'match': n('match'), 'loose': n('loose'),
                      'mismatch': n('mismatch'), 'max_lag_s': max(lags) if lags else 0, 'lags_over_limit': sum(1 for l in lags if l > max_lag)}))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
