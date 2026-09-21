import json
lock = json.load(open('eyebrowlock.json'))
print('top type:', type(lock).__name__)
if isinstance(lock, dict):
    print('keys:', list(lock.keys()))

def iter_entries(l):
    if isinstance(l, list):
        return l
    for k in ('entries', 'skills', 'files', 'discovered'):
        if k in l and isinstance(l[k], list):
            print('using key', k)
            return l[k]
    # maybe dict of path->entry
    if isinstance(l, dict):
        vals = list(l.values())
        if vals and isinstance(vals[0], dict):
            return vals
    return []

entries = iter_entries(lock)
print('n entries:', len(entries))
targets = ['aeon-update', 'changelog', 'feature']
for e in entries:
    if not isinstance(e, dict):
        continue
    df = e.get('discoveredFrom', '') or e.get('path', '') or e.get('file', '')
    for t in targets:
        if df.endswith('skills/%s/SKILL.md' % t) or df == 'skills/%s/SKILL.md' % t:
            f = e.get('findings', [])
            print('MATCH', t, 'discoveredFrom=', df, 'findings=', len(f) if isinstance(f, list) else f)
# also dump one sample entry
if entries:
    import pprint
    print('--- sample entry keys ---', list(entries[0].keys()) if isinstance(entries[0], dict) else entries[0])
