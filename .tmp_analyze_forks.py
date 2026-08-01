import json
from datetime import datetime

def analyze(path, baseline):
    with open(path) as f:
        data = json.load(f)
    print(path, 'total forks:', len(data))
    for r in data:
        created = r['created_at']
        pushed = r['pushed_at']
        size = r['size']
        full_name = r['full_name']
        c = datetime.fromisoformat(created.replace('Z','+00:00'))
        p = datetime.fromisoformat(pushed.replace('Z','+00:00'))
        gap_hours = (p-c).total_seconds()/3600
        size_dev = abs(size-baseline)/baseline*100
        if gap_hours > 3 and size_dev > 2:
            print(' ', full_name, 'gap_hours=%.1f'%gap_hours, 'size=%d'%size, 'dev=%.1f%%'%size_dev, 'stars=',r['stargazers_count'], 'lang=',r['language'])

analyze('/tmp/bd-forks-miroshark.json', 62000)
print()
analyze('/tmp/bd-forks-aeon-agent.json', 20000)  # rough, will inspect manually
print()
analyze('/tmp/bd-forks-miroshark-aeon.json', 12000)
