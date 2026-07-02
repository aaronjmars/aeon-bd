import json

with open('memory/topics/bd-radar-leads.json', 'r') as f:
    data = json.load(f)

new_leads = [
    {
        "key": "x:OrlixAI",
        "class": "building",
        "who": "OrlixAI (@OrlixAI / @tylerbroqs co-founder)",
        "handle": "@tylerbroqs",
        "signal": "orlixai.xyz live product on aeon — Agentic AI Playground on Base (search web, fetch URLs, analyze GitHub repos, query Base live), explicitly powered by the Aeon Framework. @tylerbroqs surfaced via xAI cache.",
        "fit": 3,
        "score": 15,
        "first_seen": "2026-07-02",
        "source": "xai_x+websearch",
        "move": "DM @tylerbroqs: orlixai.xyz is live on aeon — ECOSYSTEM.md entry + co-post opportunity while fresh"
    },
    {
        "key": "github:Owlch/MiroShark",
        "class": "forking",
        "who": "Owlch",
        "handle": "Owlch",
        "signal": "Owlch/MiroShark with own description: A Simple and Universal Swarm Intelligence Engine, Predicting Anything. Named identity on fork = intent signal.",
        "fit": 3,
        "score": 12,
        "first_seen": "2026-07-02",
        "source": "websearch",
        "move": "DM Owlch on GH: you gave the fork its own tagline — what are you building with MiroShark? TG invite"
    },
    {
        "key": "github:s97472091-pixel/aeon",
        "class": "forking",
        "who": "s97472091-pixel",
        "handle": "s97472091-pixel",
        "signal": "Aeon fork created 07-01T18:25, pushed 07-01T22:18 (4h own activity post-fork), +721 bytes above base. Vertical unknown.",
        "fit": 1,
        "score": 4,
        "first_seen": "2026-07-02",
        "repo_updated": "2026-07-01",
        "source": "gh_read_pat_forks",
        "move": "Watch — ping if description or issue appears"
    },
    {
        "key": "web:Zijian-Ni/awesome-ai-agents-2026",
        "class": "mentioning",
        "who": "Zijian-Ni (awesome-ai-agents-2026)",
        "handle": "Zijian-Ni",
        "signal": "A curated list of AI Agent frameworks for 2026 — the year agents went mainstream. Web search surfaced it. Distribution surface for aeon/miroshark listing.",
        "fit": 1,
        "score": 2,
        "first_seen": "2026-07-02",
        "source": "websearch",
        "move": "Verify aeon + MiroShark are listed; open PR if not"
    },
    {
        "key": "x:jay2jay01",
        "class": "mentioning",
        "who": "jay2jay01",
        "handle": "@jay2jay01",
        "signal": "X post 07-02: Top 10 Projects Launched Through @bankrbot — @aeonframework listed #2 with 40/40 Blockworks transparency score, 20% Bedrock Foundation stake. Promoter account.",
        "fit": 1,
        "score": 2,
        "first_seen": "2026-07-02",
        "link": "https://x.com/jay2jay01/status/2072545933179662406",
        "source": "xai_x",
        "move": "No action — confirms Bankr launch narrative circulating"
    },
    {
        "key": "x:baseboss_",
        "class": "mentioning",
        "who": "baseboss_",
        "handle": "@baseboss_",
        "signal": "X post 07-02: Top Bankr coins by Market Cap — aeon in list. Base-affiliated distribution surface.",
        "fit": 1,
        "score": 2,
        "first_seen": "2026-07-02",
        "link": "https://x.com/baseboss_/status/2072560908539253062",
        "source": "xai_x",
        "move": "No action — distribution surface"
    }
]

new_surfaced_keys = [
    "x:OrlixAI",
    "github:Owlch/MiroShark",
    "github:s97472091-pixel/aeon",
    "web:Zijian-Ni/awesome-ai-agents-2026",
    "x:jay2jay01",
    "x:baseboss_"
]

existing_keys = set(l["key"] for l in data["leads"])
added = 0
for lead in new_leads:
    if lead["key"] not in existing_keys:
        data["leads"].append(lead)
        added += 1

if len(data["leads"]) > 200:
    data["leads"] = data["leads"][-200:]

existing_surfaced = set(data["surfaced"])
for k in new_surfaced_keys:
    if k not in existing_surfaced:
        data["surfaced"].append(k)

if len(data["surfaced"]) > 300:
    data["surfaced"] = data["surfaced"][-300:]

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(data, f, indent=2)

print("OK added leads:", added, "surfaced total:", len(data["surfaced"]))
