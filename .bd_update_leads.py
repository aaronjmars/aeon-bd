import json

with open('memory/topics/bd-radar-leads.json') as f:
    data = json.load(f)

new_leads = [
    {
        "key": "x:AIonBase_",
        "class": "mentioning",
        "who": "AIonBase_ (Base AI ecosystem trending-account)",
        "signal": "Ranked $aeon #3 in \"Top AI/robotics plays on Base this week\" (42 likes/9rt/12replies, 09-14) and again in \"Trending AI on Base\" (8 likes, 09-15) - two separate ecosystem-ranking posts in 24h",
        "fit": 3,
        "score": 6,
        "date_found": "2026-09-15",
        "first_seen": "2026-09-15",
        "url": "https://x.com/AIonBase_/status/2099592773137580118"
    },
    {
        "key": "x:freya_xbt",
        "class": "mentioning",
        "who": "freya_xbt (Base AI ecosystem cataloger)",
        "signal": "Four-tier Base AI ecosystem map places @aeonframework in \"OG\" tier and @miroshark_ in \"Based\" tier, the first single post naming both products together in a competitive ranking (33 likes/4rt/6replies); post ends \"who belongs on the list next?\"",
        "fit": 3,
        "score": 6,
        "date_found": "2026-09-15",
        "first_seen": "2026-09-15",
        "url": "https://x.com/freya_xbt/status/2099509561673556263"
    },
    {
        "key": "x:0xProject",
        "class": "adjacent",
        "who": "0xProject (0x Protocol, 273k followers)",
        "signal": "Published viral hook-safety research - analyzed 84,000 Uniswap v4 hooks, found only 19% safe (608 likes/82rt/71replies) - data that directly validates Aeon's pre-audited-hooks marketplace thesis; @aeonframework already replied same-thread pitching the marketplace",
        "fit": 3,
        "score": 3,
        "date_found": "2026-09-15",
        "first_seen": "2026-09-15",
        "url": "https://x.com/0xProject/status/2099578032960995502"
    },
    {
        "key": "x:haydenzadams",
        "class": "adjacent",
        "who": "Hayden Adams (Founder, Uniswap - 2.28M followers)",
        "signal": "Viral \"skill issue\" tweet dismissing malicious-hook complaints (288 likes/65replies/33k views) opened a live hook-security debate; @aeonframework already replied in-thread pitching the audited-hooks marketplace, and contributor @0xNurstar is separately amplifying it to Uniswap hook communities",
        "fit": 3,
        "score": 3,
        "date_found": "2026-09-15",
        "first_seen": "2026-09-15",
        "url": "https://x.com/haydenzadams/status/2099711270115013085"
    }
]

data["leads"].extend(new_leads)

surfaced = data["surfaced"]
for lead in new_leads:
    if lead["key"] not in surfaced:
        surfaced.append(lead["key"])
surfaced.sort()
data["surfaced"] = surfaced

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(data, f, separators=(',', ':'))

print("leads total:", len(data["leads"]))
print("surfaced total:", len(data["surfaced"]))
