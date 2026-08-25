#!/usr/bin/env python3
import subprocess, hashlib, os, base64
UPSTREAM="aeonfun/aeon"
BASELINE="b7a909aa412d8e654df15417fcff0682dac39682"
HEAD="8b8d719715ec9bb68fb858a1e334d23209047d82"
def sh(a): return subprocess.run(a,capture_output=True,text=True)
def fetch(path,ref):
    r=sh(["gh","api",f"repos/{UPSTREAM}/contents/{path}?ref={ref}","--jq",".content"])
    if r.returncode!=0 or not r.stdout.strip(): return None
    try: return base64.b64decode(r.stdout)
    except: return None
def sha(b): return hashlib.sha256(b).hexdigest() if b is not None else "NONE"
def loc(p):
    if not os.path.exists(p): return None
    return open(p,"rb").read()

# real conflicts: confirm base fetch worked and local != base != head
conf=[".github/README.md",".github/workflows/aeon.yml","CHANGELOG.md","docs/skill-packs.md","llms.txt"]
print("=== CONFLICT verification (local / base / head) ===")
for p in conf:
    lb=loc(p); bb=fetch(p,BASELINE); hb=fetch(p,HEAD)
    print(p)
    print("   local=",sha(lb)[:12]," base=",sha(bb)[:12]," head=",sha(hb)[:12],
          " | local==base:",sha(lb)==sha(bb)," local==head:",sha(lb)==sha(hb))

# carried pending not in this delta: still divergent from HEAD blob?
carry=[".github/workflows/ci-tests.yml","skills/heartbeat/SKILL.md","skills/memory-flush/SKILL.md","skills/skill-health/SKILL.md"]
print("\n=== carried PENDING re-verify (keep if local != HEAD blob) ===")
for p in carry:
    lb=loc(p); hb=fetch(p,HEAD)
    still = sha(lb)!=sha(hb)
    print(p," local==head:",sha(lb)==sha(hb)," -> ",("KEEP pending" if still else "RESOLVED drop"))
