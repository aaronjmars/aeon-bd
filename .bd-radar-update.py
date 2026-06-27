import json

with open('memory/topics/bd-radar-leads.json', 'r') as f:
    state = json.load(f)

new_leads = [
    {
        "key": "github:sparkleware/aeon-pulse",
        "class": "building",
        "who": "sparkleware (aeon-pulse)",
        "handle": "sparkleware",
        "signal": "9th standalone skill repo from sparkleware — daily activity summary for the Aeon framework. Builder already runs 8 aeon skill repos + registry + MiroShark fork.",
        "fit": 3,
        "score": 15,
        "first_seen": "2026-06-27",
        "known": True,
        "source": "gh_search_repos",
        "move": "Already in TG — acknowledge the expansion, ask if aeon-pulse goes in the skill registry"
    },
    {
        "key": "x:usephylax",
        "class": "integrating",
        "who": "Phylax (@usephylax)",
        "handle": "@usephylax",
        "signal": "Public X post 06-26: Phylax is now the security pre-screen for skill installs in @aeonframework. Integration announced live. Fork already in surfaced.",
        "fit": 3,
        "score": 9,
        "first_seen": "2026-06-27",
        "link": "https://x.com/usephylax/status/2070579374966165675",
        "source": "xai_x",
        "move": "Reply + quote their post: co-write a skill-triage + Phylax explainer thread"
    },
    {
        "key": "x:AIonBase_",
        "class": "mentioning",
        "who": "AIonBase_",
        "handle": "@AIonBase_",
        "signal": "Alpha of the week: @miroshark_ — solid breakdown of the pay-per-run sim. Project account (Base AI/agents updates). 4 likes. 06-26.",
        "fit": 3,
        "score": 6,
        "first_seen": "2026-06-27",
        "link": "https://x.com/AIonBase_/status/2070647545454535113",
        "source": "xai_x",
        "move": "Reply thanking them, drop the 50% affiliate angle for the Base AI audience"
    },
    {
        "key": "github:hellosimplerick/MiroShark",
        "class": "forking",
        "who": "hellosimplerick",
        "handle": "hellosimplerick",
        "signal": "MiroShark fork created 06-18, size 63530 bytes (+1148 above drive-by base ~62382). Largest own-content MiroShark fork not yet surfaced.",
        "fit": 1,
        "score": 4,
        "first_seen": "2026-06-27",
        "repo_updated": "2026-06-18",
        "source": "gh_read_pat_forks",
        "move": "Watch — ping if they push again or add a description"
    },
    {
        "key": "github:shiblyrelyn/MiroShark",
        "class": "forking",
        "who": "shiblyrelyn",
        "handle": "shiblyrelyn",
        "signal": "MiroShark fork created 06-22, size 63269 (+887 bytes own content).",
        "fit": 1,
        "score": 4,
        "first_seen": "2026-06-27",
        "repo_updated": "2026-06-22",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    },
    {
        "key": "github:rbenegas/MiroShark",
        "class": "forking",
        "who": "rbenegas",
        "handle": "rbenegas",
        "signal": "MiroShark fork created 06-21, size 63251 (+869 bytes own content).",
        "fit": 1,
        "score": 4,
        "first_seen": "2026-06-27",
        "repo_updated": "2026-06-21",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    },
    {
        "key": "github:madmystic/aeon",
        "class": "forking",
        "who": "madmystic",
        "handle": "madmystic",
        "signal": "Aeon fork created 06-26T17:33, size 33703 (+340 bytes own content). GH has nextcloud-mcp-server + NethunterApp repos — security/tools builder.",
        "fit": 1,
        "score": 4,
        "first_seen": "2026-06-27",
        "repo_updated": "2026-06-26",
        "source": "gh_read_pat_forks",
        "move": "Watch — if they publish a skill or add a description, reach out"
    },
    {
        "key": "github:saivarmadpr/aeon",
        "class": "forking",
        "who": "saivarmadpr",
        "handle": "saivarmadpr",
        "signal": "Aeon fork created 06-22, size 33600 (+237 bytes). Unknown vertical.",
        "fit": 1,
        "score": 4,
        "first_seen": "2026-06-27",
        "repo_updated": "2026-06-22",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    },
    {
        "key": "github:SamsShow/aeon",
        "class": "forking",
        "who": "SamsShow",
        "handle": "SamsShow",
        "signal": "Aeon fork created 06-26, size 33690 (+327 bytes). Unknown vertical.",
        "fit": 1,
        "score": 4,
        "first_seen": "2026-06-27",
        "repo_updated": "2026-06-26",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    }
]

new_surfaced = [
    "github:sparkleware/aeon-pulse",
    "x:usephylax",
    "x:AIonBase_",
    "github:hellosimplerick/MiroShark",
    "github:shiblyrelyn/MiroShark",
    "github:rbenegas/MiroShark",
    "github:madmystic/aeon",
    "github:saivarmadpr/aeon",
    "github:SamsShow/aeon",
    "github:KK-OS/aeon",
    "github:P9LLI/aeon",
    "github:maredek-bot/aeon",
    "github:vladimirvalcourt/aeon",
    "github:oscarlund121/MiroShark",
    "github:AiBot-Tools/MiroShark",
    "github:JusteOgodja/MiroShark",
    "github:karim-78/MiroShark-fork",
    "github:reset980reset980/MiroShark",
    "github:MiguelBits/MiroShark",
    "github:RaziqGit/MiroShark",
    "github:BuiltByEcho/MiroShark",
    "github:NurstarK/aeon-upstream",
    "github:NurstarK/MiroShark",
    "github:NASTYZUNI/aeon",
]

existing_keys = {l['key'] for l in state['leads']}
for lead in new_leads:
    if lead['key'] not in existing_keys:
        state['leads'].append(lead)

state['leads'] = state['leads'][-200:]

existing_surfaced = set(state['surfaced'])
for key in new_surfaced:
    if key not in existing_surfaced:
        state['surfaced'].append(key)
state['surfaced'] = state['surfaced'][-300:]

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(state, f, indent=2)

print(f"Leads total: {len(state['leads'])}")
print(f"Surfaced total: {len(state['surfaced'])}")
print("Done.")
