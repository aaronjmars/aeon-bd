import json

path = "memory/topics/bd-radar-leads.json"
state = json.load(open(path))

new_leads = [
    {
        "key": "github:Syanhlu/MiroShark",
        "class": "building",
        "who": "Syanhlu/MiroShark",
        "signal": "VNG-hackathon-track team shipped a full Vietnamese-market Miroshark adaptation (personas, vi locale, Facebook/Threads/TikTok platforms, OpenAI provider, LLM stance judge, AMM signal export, A/B harness) over 10 commits, 2026-07-09/11; zero activity since (72d quiet, hackathon submission via sibling repo 'Agamotto — Team Team's submission for vng track')",
        "fit": 3,
        "score": 15,
        "date_found": "2026-09-21",
        "url": "https://github.com/Syanhlu/MiroShark"
    },
    {
        "key": "x:coolcoder56",
        "class": "mentioning",
        "who": "coolcoder56 (Asmit, SDE, 15,720 followers)",
        "signal": "Organic discovery thread (09-18): 'went down a bit of a rabbit hole' on Aeon, described GitHub-Actions-native agents + vuln-scanner securing 'Google, NVIDIA and SpaceX' repos (SpaceX detail unverified, same unverified-amplification pattern flagged 08-23); 12 likes/2rt/5 replies/1,537 views",
        "fit": 3,
        "score": 6,
        "date_found": "2026-09-21",
        "url": "https://x.com/coolcoder56/status/2101002038691930318"
    },
]

existing_keys = {l["key"] for l in state["leads"]}
for nl in new_leads:
    if nl["key"] not in existing_keys:
        state["leads"].append(nl)

state["leads"] = state["leads"][-200:]

surfaced = state.get("surfaced", [])
for nl in new_leads:
    if nl["key"] not in surfaced:
        surfaced.append(nl["key"])
state["surfaced"] = surfaced[-300:]

with open(path, "w") as f:
    json.dump(state, f, indent=None)

print("leads:", len(state["leads"]), "surfaced:", len(state["surfaced"]))
