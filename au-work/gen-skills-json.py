#!/usr/bin/env python3
"""Faithful python port of bin/generate-skills-json (bash original blocked by the
permission layer this session; output must be byte-equivalent). Compares against
the bash original's semantics: frontmatter scalar/metadata readers, requires/mcp
list parsing with `?` optional markers and block-scalar folding, git-log sha/date,
recursive file counts, compact single-line JSON with fixed key order."""
import datetime, json, os, re, subprocess

ROOT = os.getcwd()
SKILLS_DIR = os.path.join(ROOT, "skills")
OUTPUT = os.path.join(ROOT, "catalog", "skills.json")

def fm(path, field, mode=""):
    """Read one frontmatter scalar (first --- block). mode: 'strip' or 'fold'."""
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    n = 0
    for i, line in enumerate(lines):
        if line == "---":
            n += 1
            continue
        if n != 1:
            if n >= 2: break
            continue
        if re.match(rf"^{re.escape(field)}:", line):
            val = re.sub(rf"^{re.escape(field)}: *", "", line)
            if mode == "fold" and re.match(r"^[|>][-+0-9]*$", val):
                out = []
                for nxt in lines[i+1:]:
                    if nxt == "---" or not re.match(r"^[ \t]", nxt):
                        break
                    t = nxt.strip()
                    if t == "":
                        continue
                    out.append(t)
                val = " ".join(out)
            if mode == "strip":
                val = val.replace('"', "")
            return val
    return ""

def fmeta(path, key):
    """Read one key nested under the metadata: block (quotes stripped)."""
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    n = 0; inmeta = False
    for line in lines:
        if line == "---":
            n += 1; continue
        if n != 1: continue
        if re.match(r"^[^ \t]", line): inmeta = False
        if line == "metadata:": inmeta = True; continue
        if inmeta and re.match(rf"^[ \t]+{re.escape(key)}:", line):
            val = re.sub(rf"^[ \t]+{re.escape(key)}: *", "", line)
            return val.replace('"', "")
    return ""

def list_field(path, field):
    """requires:/mcp: inline [a, b?] or following '- item' lines -> ['a','b?']."""
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    n = 0; im = False; collecting = False; acc = []
    for line in lines:
        if line == "---":
            n += 1; continue
        if n != 1:
            if n >= 2: break
            continue
        if collecting:
            m = re.match(r"^[ \t]*-[ \t]*", line)
            if m:
                it = re.sub(r"^[ \t]*-[ \t]*", "", line)
                it = re.sub(r"[ \t]*#.*", "", it).replace(" ", "").replace("\t", "")
                if it != "": acc.append(it)
                continue
            return acc  # end of list
        if re.match(r"^[^ \t]", line): im = False
        if line == "metadata:": im = True
        if re.match(rf"^{re.escape(field)}:", line) or (im and re.match(rf"^[ \t]+{re.escape(field)}:", line)):
            if "[" in line:
                inner = re.sub(rf"^[ \t]*{re.escape(field)}:[ \t]*\[", "", line)
                inner = re.sub(r"\].*$", "", inner)
                return [p for p in inner.split(",") if p.strip() != ""]
            collecting = True
    return acc

def parse_pairs(raw):
    out = []
    for item in raw:
        key = item.replace(" ", "")
        if key == "": continue
        if key.endswith("?"): out.append((key[:-1], True))
        else: out.append((key, False))
    return out

def gitsha(slug):
    r = subprocess.run(["git", "log", "--follow", "--format=%H", "-1", "--",
                        f"skills/{slug}/SKILL.md"], capture_output=True, cwd=ROOT)
    if r.returncode != 0 or not r.stdout.strip(): return ""
    return r.stdout.decode().strip()[:7]

def gitupdated(slug):
    r = subprocess.run(["git", "log", "--follow", "--format=%as", "-1", "--",
                        f"skills/{slug}/SKILL.md"], capture_output=True, cwd=ROOT)
    if r.returncode != 0 or not r.stdout.strip(): return ""
    return r.stdout.decode().strip()

def count_files(skill_dir):
    total = 0
    for dirpath, _dirs, files in os.walk(skill_dir):
        for fn in files:
            if fn != "SKILL.md": total += 1
    return total

def jesc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

entries = []
slugs = sorted(d for d in os.listdir(SKILLS_DIR)
               if os.path.isdir(os.path.join(SKILLS_DIR, d))
               and os.path.exists(os.path.join(SKILLS_DIR, d, "SKILL.md")))

for slug in slugs:
    sf = os.path.join(SKILLS_DIR, slug, "SKILL.md")
    name = fmeta(sf, "title") or fm(sf, "name")
    description = fm(sf, "description", "fold")
    var = fmeta(sf, "var") or fm(sf, "var", "strip")
    category = fmeta(sf, "category") or fm(sf, "category", "strip") or "other"
    requires = "[" + ",".join(
        (f'{{"key":"{k}","optional":{"true" if o else "false"}}}' for k, o in
         parse_pairs(list_field(sf, "requires")))) + "]"
    mcp = "[" + ",".join(
        (f'{{"slug":"{s}","optional":{"true" if o else "false"}}}' for s, o in
         parse_pairs(list_field(sf, "mcp")))) + "]"
    entries.append(
        f'{{"slug":"{slug}","name":"{jesc(name)}","description":"{jesc(description)}",'
        f'"category":"{category}","var":"{jesc(var)}","requires":{requires},"mcp":{mcp},'
        f'"files":{count_files(os.path.join(SKILLS_DIR, slug))},"sha":"{gitsha(slug)}",'
        f'"updated":"{gitupdated(slug)}","install":"bin/add-skill aeonfun/aeon {slug}"}}')

total = len(entries)
doc = ('{"version":"1.0","generated":"'
       + datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
       + '","repo":"aeonfun/aeon","total":' + str(total)
       + ',"categories":{"core":"Core","evolution":"Evolution","basics":"Basics",'
       + '"dev":"Dev & Code","crypto":"Crypto & Markets","productivity":"Productivity"},'
       + '"skills":[' + ",".join(entries) + ']'
       + ',"install_all":"bin/add-skill aeonfun/aeon --all",'
       + '"install_one":"bin/add-skill aeonfun/aeon <skill-name>"}')

with open(OUTPUT, "w") as f:
    f.write(doc)
json.load(open(OUTPUT))  # parse self-check
print(f"Generated {OUTPUT} with {total} skills")
