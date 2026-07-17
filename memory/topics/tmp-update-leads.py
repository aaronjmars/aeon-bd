import json

with open('memory/topics/bd-radar-leads.json') as f:
    d = json.load(f)

surfaced = d.get('surfaced', [])
leads = d.get('leads', [])

new_keys = [
    'github:jmthomasofficial/noesis-aeon',
    'x:SpaceTimeViking',
    'github:MiroShark/MiroShark',
]

added = []
for k in new_keys:
    if k not in surfaced:
        surfaced.append(k)
        added.append(k)

if len(surfaced) > 300:
    surfaced = surfaced[-300:]

new_lead = {
    'key': 'github:jmthomasofficial/noesis-aeon',
    'class': 'adjacent',
    'who': 'jmthomasofficial (JM Thomas)',
    'handle': 'jmthomasofficial',
    'signal': 'Autonomous-agent tooling builder: noesis-aeon (Aeon reference), hyped-fib (openclaw alternative), wardproof (AI agent security), remem (Claude Code memory), mcp-servers-hub. 152 repos, Jul 11 burst. Building in aeon-adjacent space.',
    'fit': 3,
    'score': 3,
    'first_seen': '2026-07-17',
    'source': 'gh_search_repos',
    'move': 'Check jmthomasofficial.com — if serious builder, DM on GH about Aeon as prod-ready version of what they are building toward'
}

leads = [l for l in leads if l.get('key') != new_lead['key']]
leads.append(new_lead)

if len(leads) > 200:
    leads = leads[-200:]

d['surfaced'] = surfaced
d['leads'] = leads

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(d, f, indent=2)

print('Added keys:', added)
print('Total surfaced:', len(surfaced))
print('Total leads:', len(leads))
