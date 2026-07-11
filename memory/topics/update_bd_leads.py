import json

with open('memory/topics/bd-radar-leads.json') as f:
    state = json.load(f)

today = "2026-07-11"

new_leads = [
    {
        "key": "x:tryskopos",
        "class": "building",
        "who": "@tryskopos (Skopos, svector.xyz)",
        "handle": "@tryskopos",
        "signal": "Officially spotlit by @aeonframework 07-10 (28 likes/5RT). Agentic cross-chain DeFi platform built on aeon: tx-explain + token-safety + market reads (defi/narrative/fear-greed) + x402 pulse skill. 10+ chains, not just Base. Blockchain engineer, 180 GH repos.",
        "fit": 3,
        "score": 15,
        "first_seen": today,
        "source": "xai_x",
        "link": "https://x.com/aeonframework/status/2075556200184181152",
        "move": "DM @tryskopos - @aeonframework already spotlit them, make it official: ECOSYSTEM.md entry + TG invite + co-post the cross-chain angle"
    },
    {
        "key": "github:Svector-anu/skopos-aeon",
        "class": "building",
        "who": "Svector-anu (Skopos, svector.xyz)",
        "handle": "Svector-anu",
        "signal": "Aeon fork, created 07-06, pushed TODAY 07-11T06:00. +4850 bytes own content. Repo has full DeFi data (DEX/pools/fees/CoinGecko). Custom skills: defi-overview, fear-divergence, unlock-monitor, picks-tracker, verdikta-hunter, x402-monitor. Blockchain engineer, 180 public repos. Same actor as x:tryskopos.",
        "fit": 3,
        "score": 15,
        "first_seen": today,
        "repo_updated": today,
        "source": "gh_read_pat_forks",
        "move": "DM on GitHub (svector.xyz) - see x:tryskopos move"
    },
    {
        "key": "github:dan-and/issue-240",
        "class": "integrating",
        "who": "dan-and (heaviest non-core MiroShark operator)",
        "handle": "dan-and",
        "signal": "Filed MiroShark issue 240 (07-06): offline huggingface-models for air-gapped environments. Wants MiroShark running fully local with no cloud calls. Fourth signal this month (fork active 38d + issues 187, 193, now 240).",
        "fit": 3,
        "score": 9,
        "first_seen": today,
        "source": "gh_read_pat_issues",
        "move": "Reply on issue 240 directly - production air-gapped deployment signal. What is the use case? Offer MiroShark-local config path."
    },
    {
        "key": "github:RootLayer-Labs/MiroShark",
        "class": "forking",
        "who": "RootLayer Labs",
        "handle": "RootLayer-Labs",
        "signal": "Large org (282 public repos). MiroShark fork created 06-17, +528 bytes own content.",
        "fit": 2,
        "score": 4,
        "first_seen": today,
        "repo_updated": "2026-06-17",
        "source": "gh_read_pat_forks",
        "move": "Check what RootLayer Labs builds; if agent/infra play, DM on GH"
    },
    {
        "key": "github:Zarbel974/MiroShark",
        "class": "forking",
        "who": "Zarbel974",
        "handle": "Zarbel974",
        "signal": "MiroShark fork created 06-30, pushed 07-06 (6d activity), +247 bytes own content.",
        "fit": 1,
        "score": 2,
        "first_seen": today,
        "repo_updated": "2026-07-06",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    },
    {
        "key": "github:agproproducts-web/MiroShark",
        "class": "forking",
        "who": "agproproducts-web",
        "handle": "agproproducts-web",
        "signal": "MiroShark fork created TODAY 07-11. Unknown intent.",
        "fit": 1,
        "score": 2,
        "first_seen": today,
        "repo_updated": today,
        "source": "gh_read_pat_forks",
        "move": "Watch"
    },
    {
        "key": "github:R16008882/MiroShark",
        "class": "forking",
        "who": "R16008882",
        "handle": "R16008882",
        "signal": "MiroShark fork created 07-04, +305 bytes own content.",
        "fit": 1,
        "score": 2,
        "first_seen": today,
        "repo_updated": "2026-07-04",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    },
    {
        "key": "github:s97472091-pixel/aeon",
        "class": "forking",
        "who": "s97472091-pixel",
        "handle": "s97472091-pixel",
        "signal": "Aeon fork created 07-01, pushed 07-06 (5d activity), +1562 bytes own content.",
        "fit": 1,
        "score": 2,
        "first_seen": today,
        "repo_updated": "2026-07-06",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    },
    {
        "key": "github:mattsegura/aeon",
        "class": "forking",
        "who": "mattsegura",
        "handle": "mattsegura",
        "signal": "Aeon fork created 07-07, +2500 bytes own content.",
        "fit": 1,
        "score": 2,
        "first_seen": today,
        "repo_updated": "2026-07-07",
        "source": "gh_read_pat_forks",
        "move": "Watch"
    }
]

surfaced = state.get('surfaced', [])
existing_keys = set(surfaced)

added = 0
for lead in new_leads:
    if lead['key'] not in existing_keys:
        state['leads'].append(lead)
        surfaced.append(lead['key'])
        existing_keys.add(lead['key'])
        added += 1

if len(surfaced) > 300:
    surfaced = surfaced[-300:]

state['surfaced'] = surfaced

if len(state['leads']) > 200:
    state['leads'] = state['leads'][-200:]

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(state, f, indent=2)

print(f"Added {added} new leads. Total leads: {len(state['leads'])}. Surfaced LRU: {len(state['surfaced'])}")
