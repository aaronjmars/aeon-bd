import subprocess, json

candidates = [
    ("aeonfun/aeon", "Corykidios/aeon", "Corykidios"),
    ("aeonfun/aeon", "traveler3022/aeon", "traveler3022"),
    ("aeonfun/aeon", "thesmithdao/aeon", "thesmithdao"),
    ("aeonfun/aeon", "thanhdat3007-create/aeon", "thanhdat3007-create"),
    ("aeonfun/aeon", "yghffhgx/aeon", "yghffhgx"),
    ("aeonfun/aeon", "kdegeek/aeon", "kdegeek"),
    ("MiroShark/MiroShark", "AmirF194/MiroShark", "AmirF194"),
    ("MiroShark/MiroShark", "Marc-oss-hub/MiroShark", "Marc-oss-hub"),
    ("MiroShark/MiroShark", "q-qp-p/MiroShark", "q-qp-p"),
    ("MiroShark/MiroShark", "binyangzhu000-sudo/MiroShark", "binyangzhu000-sudo"),
    ("MiroShark/MiroShark", "eyeinthesky6/MiroShark", "eyeinthesky6"),
    ("MiroShark/MiroShark", "c1490b-code/MiroShark", "c1490b-code"),
    ("MiroShark/MiroShark", "kain205/mirofish-vn-lab", "kain205"),
    ("MiroShark/MiroShark", "veridian69/miroshark", "veridian69"),
    ("MiroShark/MiroShark", "Syanhlu/MiroShark", "Syanhlu"),
    ("MiroShark/MiroShark", "Zarbel974/MiroShark", "Zarbel974"),
    ("MiroShark/MiroShark", "kevinpinscoe/MiroShark", "kevinpinscoe"),
    ("MiroShark/MiroShark", "deepmindru-afk/MiroShark", "deepmindru-afk"),
]

for base, forkrepo, owner in candidates:
    default_branch = "main"
    cmp_spec = base.split("/")[0] + ":" + default_branch + "..." + owner + ":" + default_branch
    try:
        r = subprocess.run(["gh", "api", "repos/" + base + "/compare/" + cmp_spec], capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            print(forkrepo, "COMPARE_FAIL", r.stderr[:150].replace("\n"," "))
            continue
        d = json.loads(r.stdout)
        ahead = d.get("ahead_by")
        behind = d.get("behind_by")
        commits = d.get("commits", [])
        authored_msgs = [c["commit"]["message"].split("\n")[0] for c in commits if "chore(cron)" not in c["commit"]["message"] and "update cron state" not in c["commit"]["message"]]
        print(forkrepo, "| ahead", ahead, "| behind", behind, "| total_commits_shown", len(commits), "| non-cron msgs:", authored_msgs[:5])
    except Exception as e:
        print(forkrepo, "ERROR", str(e)[:150])
