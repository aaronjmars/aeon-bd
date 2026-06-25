import json, os

with open('memory/topics/ecosystem-entrants-state.json') as f:
    state = json.load(f)

state['last_run'] = '2026-06-25'
state['last_status'] = 'ECOSYSTEM_ENTRANTS_QUIET'

for url, entry in state['entries'].items():
    entry['last_seen'] = '2026-06-25'

tmp = 'memory/topics/ecosystem-entrants-state.json.tmp'
with open(tmp, 'w') as f:
    json.dump(state, f, indent=2)
os.rename(tmp, 'memory/topics/ecosystem-entrants-state.json')

print('State updated. Entries:', len(state['entries']))
