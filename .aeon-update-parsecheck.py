import yaml, json
files_yaml = ['.github/workflows/aeon.yml','.github/workflows/chain-runner.yml']
files_json = ['apps/webhook/package.json','apps/webhook/package-lock.json']
ok = True
for f in files_yaml:
    try:
        yaml.safe_load(open(f)); print('OK  ', f)
    except Exception as e:
        print('FAIL', f, e); ok = False
for f in files_json:
    try:
        json.load(open(f)); print('OK  ', f)
    except Exception as e:
        print('FAIL', f, e); ok = False
print('ALL-OK' if ok else 'HAS-FAILURES')
