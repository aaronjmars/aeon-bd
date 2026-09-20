import json

d = json.load(open("/tmp/tw-mr-aeon2.json"))
with open("cursor_aeon.txt", "w") as f:
    f.write(d.get("next_cursor", ""))
print("done")
