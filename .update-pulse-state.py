import json
p = "memory/topics/product-pulse-state.json"
d = json.load(open(p))

snap = {
    "date": "2026-06-17",
    "github": {
        "aaronjmars/aeon": {"stars": 517, "issues": 2, "open_prs": 2, "pushed": "2026-06-16T23:54:33Z", "last_commit_age_days": 0, "release": None},
        "aaronjmars/MiroShark": {"stars": 1297, "issues": 1, "open_prs": 0, "pushed": "2026-06-16T17:39:26Z", "last_commit_age_days": 0, "release": None},
        "aaronjmars/aeon-agent": {"stars": 9, "issues": 2, "open_prs": 2, "pushed": "2026-06-17T07:37:44Z", "last_commit_age_days": 0, "release": None, "ci_24h": {"success": 34, "failed": 2, "cancelled": 0}},
        "aaronjmars/miroshark-aeon": {"stars": 14, "issues": 1, "open_prs": 1, "pushed": "2026-06-17T07:45:58Z", "last_commit_age_days": 0, "release": None, "ci_24h": {"success": 32, "failed": 0, "cancelled": 0}},
        "aaronjmars/minitor": {"stars": 11, "issues": 1, "open_prs": 1, "pushed": "2026-06-16T16:08:47Z", "last_commit_age_days": 0, "release": None},
        "aaronjmars/soul-aaronjmars": {"stars": 10, "issues": 0, "open_prs": 0, "pushed": "2026-06-11T12:53:25Z", "last_commit_age_days": 6, "release": None},
    },
    "github_private": {
        "aaronjmars/aeon-website": {"private": True, "issues": 0, "open_prs": 0, "pushed": "2026-06-16T14:58:50Z", "last_commit_age_days": 0, "release": None},
        "aaronjmars/aeon-wc": {"private": True, "issues": 0, "open_prs": 0, "pushed": "2026-06-08T19:24:30Z", "last_commit_age_days": 9, "release": None},
        "aaronjmars/miroshark-website": {"private": True, "issues": 0, "open_prs": 0, "pushed": "2026-06-15T18:08:19Z", "last_commit_age_days": 1, "release": None},
        "aaronjmars/MiroShark-x402": {"private": True, "issues": 0, "open_prs": 0, "pushed": "2026-06-15T18:04:08Z", "last_commit_age_days": 1, "release": None},
    },
    "github_misses": [],
    "x": {"@aeonframework": {"followers": 151750, "posts": None}, "@miroshark_": {"followers": 2085, "posts": None}},
    "x_note": "followers via xAI prefetch cache; lifetime post counts returned 'unknown' -> null",
}

hist_entry = {
    "date": "2026-06-17",
    "stars": {"aeon": 517, "MiroShark": 1297, "aeon-agent": 9, "miroshark-aeon": 14, "minitor": 11, "soul-aaronjmars": 10},
    "ci_24h": {"aeon-agent": {"success": 34, "failed": 2, "cancelled": 0}, "miroshark-aeon": {"success": 32, "failed": 0, "cancelled": 0}},
    "x": {"aeon": 151750, "miroshark": 2085},
    "private_visible": True,
}

d["history"] = [h for h in d["history"] if h.get("date") != "2026-06-17"]
d["history"].append(hist_entry)
d["history"] = d["history"][-30:]
d["snapshot"] = snap
d["last_run"] = "2026-06-17T09:30:00Z"
json.dump(d, open(p, "w"), indent=2)
print("history dates:", [h["date"] for h in d["history"]])
