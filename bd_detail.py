import subprocess, json

targets = [
    ("aeonfun/aeon", "yghffhgx/aeon", "yghffhgx"),
    ("MiroShark/MiroShark", "Syanhlu/MiroShark", "Syanhlu"),
    ("MiroShark/MiroShark", "eyeinthesky6/MiroShark", "eyeinthesky6"),
]

for base, forkrepo, owner in targets:
    cmp_spec = base.split("/")[0] + ":main..." + owner + ":main"
    r = subprocess.run(["gh", "api", "repos/" + base + "/compare/" + cmp_spec], capture_output=True, text=True, timeout=30)
    d = json.loads(r.stdout)
    commits = d.get("commits", [])
    print("=====", forkrepo, "ahead", d.get("ahead_by"), "behind", d.get("behind_by"), "=====")
    for c in commits:
        msg = c["commit"]["message"].split("\n")[0]
        date = c["commit"]["author"]["date"]
        print(" ", date, "|", msg)
    print()

print("=== repo metadata ===")
for base, forkrepo, owner in targets:
    r = subprocess.run(["gh", "api", "repos/" + forkrepo], capture_output=True, text=True, timeout=30)
    d = json.loads(r.stdout)
    print(forkrepo, "| stars:", d.get("stargazers_count"), "| desc:", d.get("description"), "| pushed:", d.get("pushed_at"))
