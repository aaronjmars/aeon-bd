import subprocess, json

repos = ["aeonfun/aeon", "aaronjmars/aeon-agent", "aaronjmars/miroshark-aeon", "MiroShark/MiroShark"]

for repo in repos:
    slug = repo.replace("/", "-")
    for kind, path in [("forks?sort=newest&per_page=40", "forks"), ("issues?state=open&per_page=40", "issues")]:
        out_path = "/tmp/bd-" + path + "-" + slug + ".json"
        try:
            r = subprocess.run(["gh", "api", "repos/" + repo + "/" + kind], capture_output=True, text=True, timeout=60)
            if r.returncode == 0 and r.stdout.strip():
                data = r.stdout
            else:
                data = "[]"
        except Exception as e:
            data = "[]"
        with open(out_path, "w") as f:
            f.write(data)
        print(repo, path, "written", len(data), "bytes")
