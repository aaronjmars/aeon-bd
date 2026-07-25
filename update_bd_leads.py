import json

with open('memory/topics/bd-radar-leads.json') as f:
    data = json.load(f)

leads = data['leads']
surfaced = data['surfaced']

new_leads = [
    {
        "key": "github:HKUDS/Vibe-Trading",
        "class": "integrating",
        "who": "HKUDS (Vibe-Trading, 27401 stars)",
        "handle": "HKUDS",
        "signal": "@aeonframework security bot already had PR #390 MERGED (Pillow+langchain CVE fix, merged 07-05) on 27k-star Python trading AI platform. Active contributor relationship established.",
        "fit": 2,
        "score": 10,
        "first_seen": "2026-07-25",
        "repo_updated": "2026-07-24",
        "link": "https://github.com/HKUDS/Vibe-Trading/pull/390",
        "source": "gh_search_code",
        "move": "DM HKUDS maintainer on GH: aeon scanner already merged security fix on Vibe-Trading - make the partnership official. Co-announce + ECOSYSTEM.md entry."
    },
    {
        "key": "github:koala73/worldmonitor",
        "class": "integrating",
        "who": "koala73 (worldmonitor, 73614 stars)",
        "handle": "koala73",
        "signal": "73k-star geopolitical AI dashboard (Palantir-inspired, MCP, OSINT). Aeon bot opened PR #5518 (tauri CVE-2026-42184, CVSS 8.8 fix) on 07-23. PR open with trust:caution label.",
        "fit": 1,
        "score": 5,
        "first_seen": "2026-07-25",
        "link": "https://github.com/koala73/worldmonitor/pull/5518",
        "source": "gh_search_code",
        "move": "Watch PR #5518 - if merged, immediate DM koala73: 73k-star security partnership, co-announce + ECOSYSTEM.md."
    },
    {
        "key": "github:AdversaLLC/MiroShark",
        "class": "forking",
        "who": "AdversaLLC (security org)",
        "handle": "AdversaLLC",
        "signal": "Known security org (forked aeonfun/aeon 06-12, no commits). Now ALSO forked MiroShark/MiroShark. Cross-product escalation from adjacent.",
        "fit": 3,
        "score": 6,
        "first_seen": "2026-07-25",
        "known": True,
        "escalating": True,
        "source": "gh_read_pat_forks",
        "move": "Watch - security org forked both products. If commits appear on either, DM: what are you building?"
    },
    {
        "key": "github:mirkosalvato1-ctrl/aeon",
        "class": "forking",
        "who": "mirkosalvato1-ctrl",
        "handle": "mirkosalvato1-ctrl",
        "signal": "Fork of aeonfun/aeon (+2777 bytes own content, created+pushed 07-23). ctrl suffix may connect to already-surfaced CTRL_automation (score 15).",
        "fit": 1,
        "score": 2,
        "first_seen": "2026-07-25",
        "source": "gh_read_pat_forks",
        "move": "Watch - verify if CTRL_automation team; if so, escalate."
    },
]

existing_keys = set(lead.get('key', '') for lead in leads)
surfaced_set = set(surfaced)
truly_new = []
for lead in new_leads:
    key = lead['key']
    if key not in existing_keys and key not in surfaced_set:
        truly_new.append(lead)
        print("NEW:", key)
    else:
        print("SKIP:", key)

leads.extend(truly_new)
if len(leads) > 200:
    leads = leads[len(leads)-200:]

new_keys = [lead['key'] for lead in truly_new]
surfaced.extend(new_keys)
if len(surfaced) > 300:
    surfaced = surfaced[len(surfaced)-300:]

data['leads'] = leads
data['surfaced'] = surfaced

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Done. Leads: {len(leads)}, Surfaced LRU: {len(surfaced)}")
print("New keys:", new_keys)
