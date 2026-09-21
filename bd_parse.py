import json, datetime

repos = ["aeonfun/aeon", "aaronjmars/aeon-agent", "aaronjmars/miroshark-aeon", "MiroShark/MiroShark"]

state = json.load(open("memory/topics/bd-radar-leads.json"))
surfaced = set(state.get("surfaced", []))

now = datetime.datetime(2026, 9, 21, tzinfo=datetime.timezone.utc)

print("=== FORKS with push gap (not in surfaced) ===")
for repo in repos:
    slug = repo.replace("/", "-")
    path = "/tmp/bd-forks-" + slug + ".json"
    try:
        data = json.load(open(path))
    except Exception:
        continue
    if not isinstance(data, list):
        continue
    for f in data:
        full = f.get("full_name")
        owner = f.get("owner", {}).get("login")
        created = f.get("created_at")
        pushed = f.get("pushed_at")
        key = "github:" + full
        if key in surfaced:
            continue
        try:
            c = datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))
            p = datetime.datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        except Exception:
            continue
        gap = (p - c).total_seconds()
        if gap > 3600:  # pushed meaningfully after created = own activity
            print(repo, "|", full, "| created", created, "| pushed", pushed, "| gap_hours", round(gap/3600,1), "| size", f.get("size"))

print()
print("=== OPEN ISSUES (not PRs, not in surfaced) ===")
for repo in repos:
    slug = repo.replace("/", "-")
    path = "/tmp/bd-issues-" + slug + ".json"
    try:
        data = json.load(open(path))
    except Exception:
        continue
    if not isinstance(data, list):
        continue
    for i in data:
        if "pull_request" in i:
            continue
        num = i.get("number")
        key = "github-issue:" + repo + "#" + str(num)
        if key in surfaced:
            continue
        title = i.get("title", "")
        user = i.get("user", {}).get("login")
        created = i.get("created_at")
        body = (i.get("body") or "")[:200].replace("\n", " ")
        print(repo, "#" + str(num), "|", title, "| by", user, "| created", created, "| body:", body)
