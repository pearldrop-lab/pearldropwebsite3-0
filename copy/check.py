#!/usr/bin/env python3
"""Mechanical checks for the service-page copy. Run from the repo root:
       python3 copy/check.py
Exits non-zero if anything fails. Craft is a human/QC job; this only catches
the things a script can prove."""
import re, sys, glob, collections

FILES = sorted(glob.glob('copy/services/**/*.md', recursive=True))
FACTS = open('copy/SOURCE-FACTS.md').read()
APPROVED_URL = set(re.findall(r'`(https://(?:www\.youtube\.com|player\.vimeo\.com)[^`]+)`', FACTS))
TITLE_BY_URL = {m.group(2): m.group(1) for m in re.finditer(r'- \*\*(.+?)\*\* — `([^`]+)`', FACTS)}
BANNED = ['resonate', 'seamless', 'elevate', 'unlock', 'bespoke', 'cutting-edge',
          'fast-paced', 'we pride ourselves', 'take it to the next level', 'solutions']
US = [r'\borganiz', r'\brealiz', r'\bcolor\b', r'\bprogram\b', r'\bcenter\b', r'\boptimiz']

fails = collections.defaultdict(list)


def field(text, label):
    m = re.search(r'\*\*%s:\*\*\s*`?([^`\n]+)`?' % re.escape(label), text)
    if not m:
        return None
    v = m.group(1).strip().strip('`')
    return re.sub(r'\s*\*\(\d+\)\*\s*$', '', v).strip()


h1s = []
for f in FILES:
    t = open(f).read()
    low = t.lower()
    short = f.replace('copy/services/', '')

    for b in BANNED:
        if b in low:
            fails['banned word'].append(f'{short}: "{b}"')
    for p in US:
        if re.search(p, low):
            fails['US spelling'].append(f'{short}: {re.search(p, low).group(0)}')

    h1 = field(t, 'H1')
    if not h1:
        fails['missing H1'].append(short)
    else:
        h1s.append((short, h1))
        if not 45 <= len(h1) <= 65:
            fails['H1 length'].append(f'{short}: {len(h1)} chars')

    ti = field(t, 'Title tag')
    if ti and len(ti) > 60:
        fails['title >60'].append(f'{short}: {len(ti)}')
    if ti and h1 and ti.split('|')[0].strip().lower() == h1.lower():
        fails['title == H1'].append(short)

    me = field(t, 'Meta description')
    if me and not 140 <= len(me) <= 158:
        fails['meta length'].append(f'{short}: {len(me)}')

    urls = re.findall(r'`(https://(?:www\.youtube\.com|player\.vimeo\.com)[^`]+)`', t)
    for u in urls:
        if u not in APPROVED_URL:
            fails['unapproved embed URL'].append(f'{short}: {u}')
    for m in re.finditer(r'\*\*(.+?)\*\*[^|\n]*\|[^|\n]*\|\s*`([^`]+)`', t):
        real = TITLE_BY_URL.get(m.group(2).strip())
        if real and real.lower()[:18] != m.group(1).strip().lower()[:18]:
            fails['film title/URL mismatch'].append(f'{short}: "{m.group(1)}" vs "{real}"')

# cross-page: H1 construction monotony
n_that = sum(1 for _, h in h1s if ' that ' in h)
if n_that > 8:
    fails['H1 monotony'].append(f'{n_that}/{len(h1s)} H1s use "X that Y" — target 8 or fewer')

# cross-page: repeated sentences
sent = collections.Counter()
where = collections.defaultdict(set)
for f in FILES:
    body = open(f).read()
    for s in re.split(r'(?<=[.!?])\s+', re.sub(r'[|`*#>\[\]()]', ' ', body)):
        s = ' '.join(s.split())
        if len(s.split()) >= 7:
            sent[s.lower()] += 1
            where[s.lower()].add(f.replace('copy/services/', ''))
for s, c in sent.items():
    if c > 1 and len(where[s]) > 1:
        fails['sentence reused across pages'].append(f'{sorted(where[s])}: "{s[:70]}..."')

print(f'{len(FILES)} files checked\n')
if not fails:
    print('PASS — all mechanical checks clean')
    sys.exit(0)
for k in sorted(fails):
    print(f'{k}: {len(fails[k])}')
    for r in fails[k][:10]:
        print('   ', r)
    print()
sys.exit(1)
