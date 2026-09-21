import json
lock = json.load(open('eyebrowlock.json'))
arts = lock['artifacts']
print('artifacts type:', type(arts).__name__, 'len', len(arts) if hasattr(arts,'__len__') else '?')
if isinstance(arts, dict):
    ks = list(arts.keys())
    print('sample keys:', ks[:5])
    sample = arts[ks[0]]
    print('sample entry:', json.dumps(sample, indent=1)[:600])
    targets = ['aeon-update', 'changelog', 'feature', 'vuln-scanner', 'idea-pipeline']
    for k, v in arts.items():
        for t in targets:
            if ('skills/%s/SKILL.md' % t) in k:
                fnd = v.get('findings') if isinstance(v, dict) else None
                print('MATCH', t, 'key=', k, 'findings=', (len(fnd) if isinstance(fnd,list) else fnd))
elif isinstance(arts, list):
    print('list sample:', json.dumps(arts[0], indent=1)[:600])
    targets = ['aeon-update', 'changelog', 'feature', 'vuln-scanner', 'idea-pipeline']
    for v in arts:
        df = v.get('discoveredFrom','') if isinstance(v,dict) else ''
        for t in targets:
            if df.endswith('skills/%s/SKILL.md' % t):
                fnd = v.get('findings')
                print('MATCH', t, 'findings=', (len(fnd) if isinstance(fnd,list) else fnd))
