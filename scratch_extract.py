import re, glob

files = sorted(glob.glob('memory/logs/2026-09-1[6-9].md') + glob.glob('memory/logs/2026-09-2[0-2].md'))
for fn in files:
    text = open(fn).read()
    m = re.search(r'### fetch-tweets(.*?)(\n### |\Z)', text, re.S)
    print('=== ' + fn + ' ===')
    print(m.group(1) if m else 'NO BLOCK')
    print()
