import json, sys

STATE = "memory/topics/bd-radar-leads.json"

with open(STATE, "r") as f:
    state = json.load(f)

new_lead = {
    "key": "github:R16008882/MiroShark",
    "class": "forking",
    "who": "R16008882",
    "handle": "R16008882",
    "signal": "MiroShark fork created 07-04, pushed 07-03 (predates fork = drive-by flag). +905 bytes above base (63,287 total). Unknown vertical.",
    "fit": 1,
    "score": 4,
    "first_seen": "2026-07-06",
    "repo_updated": "2026-07-04",
    "source": "gh_read_pat_forks",
    "move": "Watch -- ping if own commits appear in 5 days"
}

new_key = "github:R16008882/MiroShark"
if new_key not in state["surfaced"]:
    state["surfaced"].append(new_key)
    state["leads"].append(new_lead)
    if len(state["surfaced"]) > 300:
        state["surfaced"] = state["surfaced"][-300:]
    if len(state["leads"]) > 200:
        state["leads"] = state["leads"][-200:]
    with open(STATE, "w") as f:
        json.dump(state, f, indent=2)
    print("Added. Surfaced: " + str(len(state["surfaced"])) + " Leads: " + str(len(state["leads"])))
else:
    print("Already in surfaced, skipping.")
