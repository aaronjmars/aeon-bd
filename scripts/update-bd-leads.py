import json

d = json.load(open('memory/topics/bd-radar-leads.json'))

new_leads = [
    dict(key="x:svector_eth", cls="building", score=15, who="@svector_eth / Svector-anu/svectors-lab", signal="Wired Aeon fork onto Grok harness, ~1s TG via Cloudflare Worker. @grok replied positively. 14+ days continuous commits.", source="x", date="2026-07-20"),
    dict(key="github:Svector-anu/svectors-lab", cls="building", score=15, who="Svector-anu (svector_eth, svector.xyz, @tryskopos)", signal="Aeon fork renamed svectors-lab, size 38903, confirmed on Grok harness.", source="github", date="2026-07-20"),
    dict(key="github:swarm-ai-research/aeon", cls="building", score=15, who="swarm-ai-research (swarm-ai.org, 10 repos)", signal="Research org running Aeon+MiroShark operationally. Sanitized aeon snapshot pushed today. Has aeon-atlas, swarm 211KB, agency-os.", source="github", date="2026-07-20"),
    dict(key="github:kain205/mirofish-vn-lab", cls="forking", score=6, who="kain205 Nguyen Binh Thanh Vietnam 43 repos", signal="MiroShark fork renamed mirofish-vn-lab, active lab context, pushed 07-19.", source="github", date="2026-07-20"),
    dict(key="github:Sauken-69/aeon", cls="forking", score=2, who="Sauken-69 sparse profile", signal="New aeon fork 07-19, size 36157 +3KB own content.", source="github", date="2026-07-20"),
    dict(key="x:Frankc426", cls="mentioning", score=1, who="@Frankc426 Metacade Club member", signal="Good to see @aeonframework on the list - 1 like, token holder.", source="x", date="2026-07-20"),
]

new_keys = [l["key"] for l in new_leads]

surfaced = d["surfaced"]
surfaced.extend(new_keys)
if len(surfaced) > 300:
    surfaced = surfaced[-300:]
d["surfaced"] = surfaced

leads = d["leads"]
leads.extend(new_leads)
if len(leads) > 200:
    leads = leads[-200:]
d["leads"] = leads

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(d, f, indent=2)

print("leads=" + str(len(d["leads"])) + " surfaced=" + str(len(d["surfaced"])))
