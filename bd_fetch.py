import urllib.request, json, os, sys

pat = os.environ.get('GH_READ_PAT','')
headers = {'Authorization': f'Bearer {pat}', 'Accept': 'application/vnd.github+json'}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read())
    except Exception as e:
        return {'error': str(e)}

mode = sys.argv[1] if len(sys.argv) > 1 else 'forks'

if mode == 'aeon_forks':
    data = fetch('https://api.github.com/repos/aaronjmars/aeon/forks?sort=newest&per_page=40')
elif mode == 'miroshark_forks':
    data = fetch('https://api.github.com/repos/aaronjmars/MiroShark/forks?sort=newest&per_page=40')
elif mode == 'aeon_issues':
    data = fetch('https://api.github.com/repos/aaronjmars/aeon/issues?state=open&per_page=40')
elif mode == 'miroshark_issues':
    data = fetch('https://api.github.com/repos/aaronjmars/MiroShark/issues?state=open&per_page=40')
else:
    data = {'error': 'unknown mode'}

if isinstance(data, list):
    print(f'count={len(data)}')
    for item in data:
        if mode.endswith('forks'):
            print(json.dumps({
                'full_name': item.get('full_name'),
                'owner': item.get('owner',{}).get('login'),
                'created_at': item.get('created_at','')[:10],
                'pushed_at': item.get('pushed_at','')[:10],
                'size': item.get('size',0),
                'description': item.get('description','')
            }))
        elif mode.endswith('issues'):
            if not item.get('pull_request'):
                print(json.dumps({
                    'number': item.get('number'),
                    'title': item.get('title'),
                    'user': item.get('user',{}).get('login'),
                    'created_at': item.get('created_at','')[:10],
                    'body': (item.get('body') or '')[:300]
                }))
else:
    print(json.dumps(data))
