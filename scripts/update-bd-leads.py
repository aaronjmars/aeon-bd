import json

with open('memory/topics/bd-radar-leads.json', 'r') as f:
    state = json.load(f)

today = '2026-07-05'

new_lead_keys = [
    'github:luis212/NovaShoal-Swarm-Sim',
    'github:AI-Risk-Management/aeon-skill-schema',
    'github:swarm-ai-research/swarm',
    'github:microchipgnu/frames-monorepo',
    'github:Zarbel974/MiroShark',
    'github:asimog/cancerhawk',
    'github:nigelon11/aeon',
    'github:freezerboi/aeon',
    'github:Marr554/aeon',
    'x:0xLiamVisionary',
]

new_leads = [
    {'key': 'github:luis212/NovaShoal-Swarm-Sim', 'class': 'building', 'who': 'luis212/NovaShoal-Swarm-Sim', 'signal': '151 stars MiroShark app, pushed today', 'date': today, 'score': 15},
    {'key': 'github:AI-Risk-Management/aeon-skill-schema', 'class': 'building', 'who': 'AI-Risk-Management/aeon-skill-schema', 'signal': 'AeonBrain wire format on Aeon skill schema', 'date': today, 'score': 15},
    {'key': 'github:swarm-ai-research/swarm', 'class': 'building', 'who': 'swarm-ai-research/swarm', 'signal': 'Multi-agent risk research org, MiroShark fork active', 'date': today, 'score': 15},
    {'key': 'github:microchipgnu/frames-monorepo', 'class': 'integrating', 'who': 'microchipgnu (@microchipgnu)', 'signal': 'x402.miroshark.xyz in x402 merchant catalog', 'date': today, 'score': 12},
    {'key': 'github:Zarbel974/MiroShark', 'class': 'forking', 'who': 'Zarbel974 (Abel/Wope)', 'signal': 'Active MiroShark fork with own commits', 'date': today, 'score': 12},
    {'key': 'github:asimog/cancerhawk', 'class': 'building', 'who': 'asimog/cancerhawk', 'signal': 'Cancer research sim pipeline using MiroShark', 'date': today, 'score': 10},
    {'key': 'github:nigelon11/aeon', 'class': 'forking', 'who': 'nigelon11', 'signal': 'Active aeon fork (July 2-4)', 'date': today, 'score': 8},
    {'key': 'github:freezerboi/aeon', 'class': 'forking', 'who': 'freezerboi (@freezer_boi)', 'signal': 'Designer forking aeon, active today', 'date': today, 'score': 8},
    {'key': 'github:Marr554/aeon', 'class': 'forking', 'who': 'Marr554', 'signal': '11-day active aeon fork, pushed today', 'date': today, 'score': 8},
    {'key': 'x:0xLiamVisionary', 'class': 'mentioning', 'who': '@0xLiamVisionary (HivemindOS)', 'signal': 'Public post endorsing both aeon+miroshark integrations, 50L+12RT', 'date': today, 'score': 6},
]

existing_surfaced = state.get('surfaced', [])
for key in new_lead_keys:
    if key not in existing_surfaced:
        existing_surfaced.append(key)
state['surfaced'] = existing_surfaced[-300:]

existing_leads = state.get('leads', [])
existing_leads.extend(new_leads)
state['leads'] = existing_leads[-200:]

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(state, f, indent=2)

print("Updated: " + str(len(state['surfaced'])) + " surfaced, " + str(len(state['leads'])) + " leads")
