import json, subprocess

UP = "aeonfun/aeon"
BASE = "95142d19705ca379815e7fc9493a497ee0504e8d"
HEAD = "ba01e9f3e4495c8f761ab483000639cc8d5f5221"

r = subprocess.run(["gh", "api",
    f"repos/{UP}/compare/{BASE}...{HEAD}", "--paginate"],
    capture_output=True, text=True)
data = json.loads(r.stdout)
commits = data["commits"]

# For each file of interest, which commits touched it? Requires per-commit files.
interest = [
    ".github/README.md", ".github/workflows/ci-tests.yml", "CHANGELOG.md",
    "docs/skill-packs.md", "skills/idea-pipeline/SKILL.md", "skills/vuln-scanner/SKILL.md",
    "skills/miroshark-matchday/SKILL.md", "skills/create-prove/SKILL.md",
    "skills/sc-audit/SKILL.md", "aeon.yml",
]
touched = {p: [] for p in interest}
for c in commits:
    sha = c["sha"][:7]
    msg = c["commit"]["message"].split("\n")[0]
    rc = subprocess.run(["gh", "api", f"repos/{UP}/commits/{c['sha']}",
                         "--jq", ".files[].filename"], capture_output=True, text=True)
    files = set(rc.stdout.split("\n"))
    for p in interest:
        if p in files:
            touched[p].append(sha)

for p in interest:
    print(p, "->", ", ".join(touched[p]) if touched[p] else "(none)")
