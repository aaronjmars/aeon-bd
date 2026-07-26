#!/usr/bin/env python3
"""BD Radar — GitHub data fetcher"""
import os, urllib.request, json, sys

pat = os.environ.get('GH_READ_PAT', '')
if not pat:
    print("BD_RADAR_SOURCE_MISS: github-forks-issues (no GH_READ_PAT)")
    sys.exit(0)

headers = {
    'Authorization': f'Bearer {pat}',
    'Accept': 'application/vnd.github+json',
    'User-Agent': 'aeon-bd-radar/1.0'
}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception as e:
        return {'error': str(e)}

# Aeon forks
forks_aeon = fetch("https://api.github.com/repos/aeonfun/aeon/forks?sort=newest&per_page=40")
# MiroShark forks
forks_shark = fetch("https://api.github.com/repos/MiroShark/MiroShark/forks?sort=newest&per_page=40")
# Aeon issues
issues_aeon = fetch("https://api.github.com/repos/aeonfun/aeon/issues?state=open&per_page=40")
# MiroShark issues
issues_shark = fetch("https://api.github.com/repos/MiroShark/MiroShark/issues?state=open&per_page=40")

if isinstance(forks_aeon, list):
    print(f"aeon_forks: {len(forks_aeon)}")
    for f in forks_aeon:
        pushed = f.get('pushed_at', '')[:10]
        created = f.get('created_at', '')[:10]
        # Only active forks (pushed after created by more than a day)
        active = pushed > created if pushed and created else False
        print(f"  FORK name={f.get('full_name')} created={created} pushed={pushed} size={f.get('size',0)} active={active} owner_login={f.get('owner',{}).get('login','?')}")
else:
    print(f"aeon_forks error: {forks_aeon}")

print("---")

if isinstance(forks_shark, list):
    print(f"miroshark_forks: {len(forks_shark)}")
    for f in forks_shark:
        pushed = f.get('pushed_at', '')[:10]
        created = f.get('created_at', '')[:10]
        active = pushed > created if pushed and created else False
        print(f"  FORK name={f.get('full_name')} created={created} pushed={pushed} size={f.get('size',0)} active={active} owner_login={f.get('owner',{}).get('login','?')}")
else:
    print(f"miroshark_forks error: {forks_shark}")

print("---")

if isinstance(issues_aeon, list):
    real = [i for i in issues_aeon if not i.get('pull_request')]
    print(f"aeon_issues: {len(real)}")
    for i in real:
        print(f"  ISSUE #{i['number']} user={i['user']['login']} created={i['created_at'][:10]} title={i['title'][:80]}")
else:
    print(f"aeon_issues error: {issues_aeon}")

print("---")

if isinstance(issues_shark, list):
    real = [i for i in issues_shark if not i.get('pull_request')]
    print(f"miroshark_issues: {len(real)}")
    for i in real:
        print(f"  ISSUE #{i['number']} user={i['user']['login']} created={i['created_at'][:10]} title={i['title'][:80]}")
else:
    print(f"miroshark_issues error: {issues_shark}")
