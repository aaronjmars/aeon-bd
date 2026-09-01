import json

with open('/tmp/bd-xai-response.json') as f:
    data = json.load(f)

for out in data.get('output', []):
    if out.get('type') == 'message':
        for part in out.get('content', []):
            if part.get('type') == 'output_text':
                print(part.get('text', ''))
