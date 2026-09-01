import json, subprocess
old = json.loads(subprocess.run(["git", "show", "HEAD:catalog/skills.json"],
                                capture_output=True, cwd=".").stdout)
new = json.load(open("catalog/skills.json"))
o = {s["slug"]: s for s in old["skills"]}
n = {s["slug"]: s for s in new["skills"]}
print("added:", sorted(set(n) - set(o)))
print("removed:", sorted(set(o) - set(n)))
changed = [k for k in sorted(set(o) & set(n)) if o[k] != n[k]]
print("changed:", changed)
for k in changed:
    diffs = {f: (o[k][f], n[k][f]) for f in o[k] if o[k][f] != n[k].get(f)}
    print(" ", k, diffs)
print("order same:", [s["slug"] for s in old["skills"]] == [s["slug"] for s in new["skills"]][:len(old["skills"])] or
      [s["slug"] for s in new["skills"]][:0])
newslugs = [s["slug"] for s in new["skills"]]
print("cortx at:", newslugs.index("cortx-reliability"), "between",
      newslugs[newslugs.index("cortx-reliability")-1], "and",
      newslugs[newslugs.index("cortx-reliability")+1])
