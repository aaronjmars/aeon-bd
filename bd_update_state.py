import json

with open('memory/topics/bd-radar-leads.json') as f:
    data = json.load(f)

new_leads = [
    {
        "key": "github:agentjido/jido",
        "class": "adjacent",
        "who": "agentjido/jido",
        "signal": "1,774★ Elixir autonomous agent framework — distributed, autonomous behavior + dynamic workflows. Active 07-23.",
        "fit": 3,
        "score": 3,
        "surfaced": "2026-07-27",
        "source": "gh_search_repos",
        "move": "DM agentjido: Aeon handles scheduling/cron + memory at skills layer — Elixir agents could delegate long-horizon runs to Aeon. Cross-post opp."
    },
    {
        "key": "github:TheMindExpansionNetwork/mindbot-framework",
        "class": "adjacent",
        "who": "TheMindExpansionNetwork/mindbot-framework",
        "signal": "'The agent you can prove.' Hash-chained, Merkle-anchored, budget-capped autonomous agent framework. Pushed 07-26. Direct philosophy match with Aeon's public-traces ethos.",
        "fit": 3,
        "score": 3,
        "surfaced": "2026-07-27",
        "source": "gh_search_repos",
        "move": "DM MindExpansionNetwork on GH: our frameworks share the same core thesis — verifiable, budget-capped, public. Co-publish a piece on 'the agent you can prove.'"
    },
    {
        "key": "github:numbpill3d/sigil",
        "class": "adjacent",
        "who": "numbpill3d/sigil",
        "signal": "vault-native semi-autonomous agent framework — memory is a markdown/obsidian vault, not a vector db. Pushed 07-22.",
        "fit": 2,
        "score": 2,
        "surfaced": "2026-07-27",
        "source": "gh_search_repos",
        "move": "GH comment: sigil's markdown vault memory matches Aeon's memory/ pattern — have you seen skills-as-markdown?"
    },
    {
        "key": "github:joshuamschultz/Arc",
        "class": "adjacent",
        "who": "joshuamschultz/Arc",
        "signal": "Arc: Autonomous agent framework — 4★, 29KB, pushed 07-27. Early-stage, active today.",
        "fit": 2,
        "score": 2,
        "surfaced": "2026-07-27",
        "source": "gh_search_repos",
        "move": "Watch — if they ship a skill-pack pattern or mention scheduling, reach out."
    },
    {
        "key": "github:michaelmillshealy716-sudo/Kinetic-Alpha-Agentic-Technical-Analysis-Execution",
        "class": "adjacent",
        "who": "michaelmillshealy716-sudo (Kinetic-Alpha)",
        "signal": "Autonomous agentic framework for real-time TA + market execution. Topics: ai-agents, trading-automation, quantitative-finance. 3★, pushed 07-27.",
        "fit": 2,
        "score": 2,
        "surfaced": "2026-07-27",
        "source": "gh_search_repos",
        "move": "MiroShark angle: simulate the market before executing. DM if they ship real users."
    }
]

new_keys = [l["key"] for l in new_leads]

surfaced = data.get("surfaced", [])
for k in new_keys:
    if k not in surfaced:
        surfaced.append(k)
if len(surfaced) > 300:
    surfaced = surfaced[-300:]
data["surfaced"] = surfaced

leads = data.get("leads", [])
existing_keys = {l.get("key") for l in leads}
for nl in new_leads:
    if nl["key"] not in existing_keys:
        leads.append(nl)

if len(leads) > 200:
    leads.sort(key=lambda x: x.get("score", 0))
    leads = leads[len(leads)-200:]

data["leads"] = leads

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated: {len(leads)} leads, {len(surfaced)} surfaced")
