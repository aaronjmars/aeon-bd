import json
lock = json.load(open('eyebrowlock.json'))
arts = lock['artifacts']
targets = ['aeon-update', 'changelog', 'feature', 'vuln-scanner', 'idea-pipeline', 'create-prove', 'sc-audit']
for v in arts:
    df = v.get('discoveredFrom', '')
    for t in targets:
        if df.endswith('skills/%s/SKILL.md' % t):
            print('=====', t, '=====')
            print(json.dumps(v, indent=1))
