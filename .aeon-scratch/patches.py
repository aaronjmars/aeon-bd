#!/usr/bin/env python3
import json, subprocess
UPSTREAM="aeonfun/aeon"; BASELINE="b7a909aa412d8e654df15417fcff0682dac39682"; HEAD="8b8d719715ec9bb68fb858a1e334d23209047d82"
r=subprocess.run(["gh","api",f"repos/{UPSTREAM}/compare/{BASELINE}...{HEAD}"],capture_output=True,text=True)
d=json.loads(r.stdout)
want=[".github/README.md",".github/workflows/aeon.yml","CHANGELOG.md","docs/skill-packs.md","llms.txt"]
for f in d["files"]:
    if f["filename"] in want:
        p=f.get("patch","(no patch - binary or too large)")
        lines=p.splitlines()
        if len(lines)>40: lines=lines[:40]+["... (truncated, %d more lines)"%(len(p.splitlines())-40)]
        print("### "+f["filename"]+"  (+%d-%d)"%(f["additions"],f["deletions"]))
        print("```diff")
        print("\n".join(lines))
        print("```")
        print()
