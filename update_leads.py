import json

with open('memory/topics/bd-radar-leads.json') as f:
    data = json.load(f)

surfaced = data.get('surfaced', [])
leads = data.get('leads', [])

new_lead = {
    "key": "github:sparkleware/sparkleware",
    "class": "building",
    "who": "sparkleware (@sparklewarefun)",
    "handle": "sparkleware",
    "signal": "Y2K holographic registry for Aeon skill packs. 13 repos in Aeon ecosystem. Daily auto-refresh live. Bio: The discovery catalog for Aeon skill packs. No PR required. No approval queue. No friction. 3 stars.",
    "fit": 3,
    "score": 15,
    "first_seen": "2026-07-18",
    "repo_updated": "2026-07-18",
    "source": "gh_search_repos",
    "move": "DM @sparklewarefun - registry is live and daily-refreshing; talk about formalizing as official Atrium discovery layer and co-posting the one-click-install flow"
}

new_key = "github:sparkleware/sparkleware"
if new_key not in surfaced:
    surfaced.append(new_key)
if len(surfaced) > 300:
    surfaced = surfaced[-300:]

existing_keys = [l.get('key') for l in leads]
if new_lead['key'] not in existing_keys:
    leads.append(new_lead)
if len(leads) > 200:
    leads = leads[-200:]

data['surfaced'] = surfaced
data['leads'] = leads

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Total leads:", len(leads))
print("Surfaced LRU:", len(surfaced))
print("New key:", new_key)
