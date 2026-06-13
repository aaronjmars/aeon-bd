import json
p = "memory/topics/bd-radar-leads.json"
d = json.load(open(p))
today = "2026-06-13"
new = [
 ("github:powerloom/aeon-skills", "building", "Powerloom datamarket skill pack runs on Aeon (established Base data protocol)", 15),
 ("github:mnemedb/aeon-skill-pack-mneme", "building", "Mneme persistent memory layer for Aeon - vector+graph, 8 skills", 15),
 ("github:tenequm", "integrating", "aeon issue #464: add glim.sh live-data MCP (x402+MPP) to catalog - explicit ask", 9),
 ("github:madebyshun/blue-agent", "integrating", "x402 endpoint wrapping MiroShark 4-persona consensus (blue-agent)", 9),
 ("github:saluca-labs/pantheon", "integrating", "MiroShark to Tiresias app-proxy bridge (pantheon)", 9),
 ("github:LiamVisionary/hivemindos", "integrating", "MiroShark Companion integration; LiamVisionary forked both 06-02", 9),
 ("github:Jeremyliu-621/soon", "integrating", "pipeline targeting miroshark api/graph+api/simulation; miroshark-vs-mirofish pick", 9),
 ("github:sinfronterasai/aeon", "forking", "forked 06-12, own commits 06-13 (org-named)", 4),
 ("github:ashneil12/aeon-upstream", "forking", "forked 06-12, own activity 06-13, tracks -upstream", 4),
 ("github:liquidpadbot/aeon-skill-pack-liquidpad", "building", "LiquidPad skill pack - burn/launch/fee monitoring on Aeon", 5),
 ("github:ryjin111/aeon-skill-pack-mythosforge", "building", "MythosForge ops-monitoring skills for Aeon", 5),
 ("github:gitlawbounty/gitbounty-skill-pack", "building", "gitbounty bounty-hunting skills on gitlawb network", 5),
 ("github:AdversaLLC", "adjacent", "forked BOTH aeon+MiroShark 06-12, no commits yet (security org) - watch", 3),
]
surf = d.get("surfaced", [])
leads = d.get("leads", [])
for key, cls, sig, score in new:
    if key not in surf:
        surf.append(key)
    leads.append({"key": key, "class": cls, "signal": sig, "score": score, "surfaced": today})
d["surfaced"] = surf[-300:]
d["leads"] = leads[-200:]
json.dump(d, open(p, "w"), indent=2)
print("surfaced", len(d["surfaced"]), "leads", len(d["leads"]))
