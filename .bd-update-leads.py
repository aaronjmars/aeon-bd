import json

path = "memory/topics/bd-radar-leads.json"
d = json.load(open(path))

new_leads = [
    {"key":"x:thecultos+github:cultosdev/aeon","class":"building","who":"CultOS (@thecultos / cultosdev / thesmithdao)","signal":"Project account tweeted \"we choose Aeon\" (Aug 26); same-day live forked instance running custom cron'd skill cultos-acp-review + dedicated cultos-aeon-skills pack repo for CultOS ACP jobs","fit":3,"score":15,"date_found":"2026-08-27","url":"https://x.com/thecultos/status/2092651447200440566"},
    {"key":"github:JessieJanie/aeon-skill-pack-skim","class":"building","who":"JessieJanie/aeon-skill-pack-skim","signal":"Pay-per-call clean web reads via Skim, x402 $0.002 USDC on Base, built for Aeon","fit":3,"score":15,"date_found":"2026-08-27","url":"https://github.com/JessieJanie/aeon-skill-pack-skim"},
    {"key":"github:financedistrict-platform/fd-aeon-skills","class":"building","who":"financedistrict-platform/fd-aeon-skills","signal":"Finance District Agent Wallet companion skill for Aeon - second repo from this ecosystem (pairs with raul1stdigital/aeon-finance-district)","fit":3,"score":15,"date_found":"2026-08-27","url":"https://github.com/financedistrict-platform/fd-aeon-skills"},
    {"key":"github:verdikta/aeon-skill-pack-verdikta","class":"building","who":"verdikta/aeon-skill-pack-verdikta","signal":"Aeon skill pack for Verdikta - hunt AI-judged bounties on Base with hard client-side spend caps","fit":3,"score":15,"date_found":"2026-08-27","url":"https://github.com/verdikta/aeon-skill-pack-verdikta"},
    {"key":"github:LSO-AI/aeon-skills","class":"building","who":"LSO-AI/aeon-skills","signal":"LoneStarOracle AEON skills - weather, crypto, macro, gov contracts, oil leases, audits","fit":3,"score":15,"date_found":"2026-08-27","url":"https://github.com/LSO-AI/aeon-skills"},
    {"key":"github:richard7463/ai2human-aeon-skill-pack","class":"building","who":"richard7463/ai2human-aeon-skill-pack","signal":"AI2Human Create Task Aeon skill pack: dispatch blocked human steps, proof -> verify -> settle","fit":3,"score":15,"date_found":"2026-08-27","url":"https://github.com/richard7463/ai2human-aeon-skill-pack"},
    {"key":"github:techdigger/aeon-skill-pack-agentlink","class":"building","who":"techdigger/aeon-skill-pack-agentlink","signal":"AgentLink Aeon skill pack - verified human-backed on-chain identity on Base","fit":3,"score":15,"date_found":"2026-08-27","url":"https://github.com/techdigger/aeon-skill-pack-agentlink"},
    {"key":"github:sparkleware-expansion-2026-08-27","class":"building","who":"Sparkleware (known partner, expanding)","signal":"7 more Aeon skill repos found beyond sparkleware/sparkleware: aeon-pulse, eth-gas-watch, registry-watch, morning-briefing, hn-top, arxiv-digest, proof-of-loadout (last one also preflights a MiroShark sim)","fit":3,"score":15,"date_found":"2026-08-27","url":"https://github.com/sparkleware/aeon-pulse"},
    {"key":"github:Muriel-Salvan/x_aeon_agents","class":"building","who":"Muriel-Salvan/x_aeon_agents","signal":"AI agents skills to be used for X-Aeon projects","fit":1,"score":5,"date_found":"2026-08-27","url":"https://github.com/Muriel-Salvan/x_aeon_agents"},
    {"key":"github:hansj73/aeon","class":"building","who":"hansj73/aeon","signal":"Fresh fork (created Aug 26) already running its own cron - Telegram auto-commit, fetch-tweets success","fit":1,"score":5,"date_found":"2026-08-27","url":"https://github.com/hansj73/aeon"},
    {"key":"github:agenticluke/claude-skill-aeon-plus","class":"building","who":"agenticluke/claude-skill-aeon-plus","signal":"Improved fork of K-Dense-AI/scientific-agent-skills adapted as an aeon skill","fit":1,"score":5,"date_found":"2026-08-27","url":"https://github.com/agenticluke/claude-skill-aeon-plus"},
    {"key":"github:AntFleet/bench-miroshark","class":"adjacent","who":"AntFleet/bench-miroshark","signal":"AntFleet benchmark mirror of aaronjmars/MiroShark - two-model security review methodology","fit":1,"score":1,"date_found":"2026-08-27","url":"https://github.com/AntFleet/bench-miroshark"},
]

existing_keys = set(l["key"] for l in d["leads"])
added = 0
for l in new_leads:
    if l["key"] not in existing_keys:
        d["leads"].append(l)
        added += 1

d["leads"] = d["leads"][-200:]

surfaced = d.get("surfaced", [])
for l in new_leads:
    if l["key"] not in surfaced:
        surfaced.append(l["key"])
d["surfaced"] = surfaced[-300:]

json.dump(d, open(path, "w"), indent=2)
print("added", added, "total leads", len(d["leads"]), "surfaced", len(d["surfaced"]))
