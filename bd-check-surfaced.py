#!/usr/bin/env python3
import json

with open('memory/topics/bd-radar-leads.json') as f:
    d = json.load(f)

surfaced = d['surfaced']
checks = ['Hollup', 'clawhunter', 'Danypsy', 'nigelon11', 'Marr554', 'freezerboi', 'amir-rezaei', 'maredek-bot', 'binyangzhu000', 'Svector-anu', 'swarm-ai-research']
for c in checks:
    found = [s for s in surfaced if c.lower() in s.lower()]
    print(f'{c}: {found if found else "NOT SURFACED"}')

print(f"\nTotal surfaced: {len(surfaced)}")
print("First 10:", surfaced[:10])
