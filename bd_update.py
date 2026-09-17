import json

with open('memory/topics/bd-radar-leads.json') as f:
    data = json.load(f)

new_lead = {
    "key": "x:xvader",
    "class": "mentioning",
    "who": "xvader",
    "signal": "18-part Indonesian-language deep-technical thread comparing MiroFish vs MiroShark, explains real origin (Aaron forked/translated/moved to local Neo4j), full setup guides for both, warns to check commit count/date to avoid the wrong repo, honest pros/cons (no public benchmarks yet, cost warnings) - counters the MiroFish-fork mischaracterization memory has tracked since 09-06",
    "fit": 3,
    "score": 6,
    "date_found": "2026-09-17",
    "first_seen": "2026-09-17",
    "url": "https://x.com/xvader/status/2100409573253472578",
}
data["leads"].append(new_lead)
if "x:xvader" not in data["surfaced"]:
    data["surfaced"].append("x:xvader")

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(data, f)
print("done", len(data["leads"]), len(data["surfaced"]))
