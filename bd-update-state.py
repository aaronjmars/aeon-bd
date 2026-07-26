#!/usr/bin/env python3
"""Update bd-radar-leads.json with today's new leads"""
import json
from datetime import datetime

with open('memory/topics/bd-radar-leads.json') as f:
    state = json.load(f)

today = "2026-07-26"

new_leads = [
    {
        "key": "github:amir-rezaei/aeon",
        "class": "forking",
        "who": "amir-rezaei/aeon",
        "signal": "142-repo dev (since 2017), forked Aeon 07-23, drive-by",
        "score": 3,
        "surfaced": today
    },
    {
        "key": "github:binyangzhu000-sudo/MiroShark",
        "class": "forking",
        "who": "binyangzhu000-sudo/MiroShark",
        "signal": "219-repo account, forked MiroShark today, probable scraper",
        "score": 2,
        "surfaced": today
    },
    {
        "key": "github:capemeta/genesis-agent",
        "class": "adjacent",
        "who": "capemeta/genesis-agent",
        "signal": "Go agent framework inspired by Claude Code, MCP/skills, enterprise RBAC, pushed 07-25",
        "score": 2,
        "surfaced": today
    }
]

# Add to surfaced LRU (cap 300)
for lead in new_leads:
    key = lead["key"]
    if key in state["surfaced"]:
        state["surfaced"].remove(key)
    state["surfaced"].append(key)

state["surfaced"] = state["surfaced"][-300:]

# Add to leads list (cap 200, newest first)
for lead in new_leads:
    # Remove existing entry with same key if present
    state["leads"] = [l for l in state["leads"] if l.get("key") != lead["key"]]
    state["leads"].insert(0, lead)

state["leads"] = state["leads"][:200]

with open('memory/topics/bd-radar-leads.json', 'w') as f:
    json.dump(state, f, indent=2)

print(f"leads: {len(state['leads'])}, surfaced: {len(state['surfaced'])}")
print(f"New keys added: {[l['key'] for l in new_leads]}")
