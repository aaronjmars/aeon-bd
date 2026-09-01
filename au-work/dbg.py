import json
d = open('catalog/skills.json').read()
marker = ',"skills":['
arr = d.index(marker) + len(marker)
depth = 0
start = None
entries = []
for j, ch in enumerate(d[arr:], arr):
    if ch == '{':
        if depth == 0:
            start = j
        depth += 1
    elif ch == '}':
        depth -= 1
        if depth == 0:
            entries.append(d[start:j+1])
for e in entries:
    try:
        json.loads(e)
    except Exception as ex:
        print('BAD', ex)
        print(e[:400])
        break
else:
    print('all entries parse:', len(entries))
