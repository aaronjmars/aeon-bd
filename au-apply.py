#!/usr/bin/env python3
import subprocess, os
HEAD="bf33365164c5a8b50d49a0ed64a45521dbe96771"

CLEAN_FROM_HEAD = [
 # CLEAN-ADD
 "scripts/dev-loop-pr.sh","scripts/skill_health_recovery.py","scripts/vuln-poc-gate.sh",
 "scripts/tests/fixtures/vuln-poc-foundry/foundry.toml",
 "scripts/tests/fixtures/vuln-poc-foundry/src/Fixture.sol",
 "scripts/tests/live_vuln_poc_gate.sh","scripts/tests/test_chain_runner_invalid_dispatch.sh",
 "scripts/tests/test_dev_loop_handoff.sh","scripts/tests/test_fleet_scorecard.mjs",
 "scripts/tests/test_llm_gateway.sh","scripts/tests/test_skill_health_recovery.py",
 "scripts/tests/test_vuln_poc_gate.sh",
 # CLEAN-UPDATE
 ".github/workflows/chain-runner.yml","docs/CONFIGURATION.md","docs/ECOSYSTEM.md",
 "docs/skill-integrity.md","plugin/skills/aeon/references/secrets.md",
 "scripts/fleet-scorecard.mjs","scripts/notify-deliver.sh","scripts/skill_mode.sh",
 "scripts/stage-vuln-scanner.sh","scripts/tests/test_notify.sh","scripts/tests/test_skill_mode.sh",
]
CLEAN_MERGE = [
 ".github/workflows/ci-skill-integrity.yml","scripts/llm-gateway.sh",
 "skills/feature/SKILL.md","skills/skill-health/SKILL.md",
]

def writeblob(path):
    r=subprocess.run(["git","show",f"{HEAD}:{path}"],capture_output=True)
    assert r.returncode==0, path
    d=os.path.dirname(path)
    if d: os.makedirs(d,exist_ok=True)
    open(path,"wb").write(r.stdout)

for p in CLEAN_FROM_HEAD:
    writeblob(p); print("wrote HEAD blob:",p)
for p in CLEAN_MERGE:
    src=p+".AUMERGED"
    data=open(src,"rb").read()
    open(p,"wb").write(data)
    print("wrote merged   :",p)
# preserve exec bit on shell/py scripts we added
for p in CLEAN_FROM_HEAD+CLEAN_MERGE:
    if p.endswith((".sh",".py",".mjs")):
        os.chmod(p,0o755)
print("done")
