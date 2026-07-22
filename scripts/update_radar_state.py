#!/usr/bin/env python3
import json, shutil

state_path = "memory/topics/competitor-radar-state.json"

with open(state_path) as f:
    state = json.load(f)

new_entries = [
  {"id":"hn:48939662","name":"LM Studio Bionic: the AI agent for open models","url":"https://news.ycombinator.com/item?id=48939662","class":"product","score":330,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48995213","name":"Jack Dorsey launches Buzz: team chat, AI agents and Git hosting","url":"https://news.ycombinator.com/item?id=48995213","class":"product","score":321,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48946692","name":"VulnHunter: Capital One agentic AI code security tool","url":"https://news.ycombinator.com/item?id=48946692","class":"product","score":78,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48996236","name":"AI Agent TRMNL","url":"https://news.ycombinator.com/item?id=48996236","class":"product","score":50,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48919562","name":"LoopGain: Stop agent loops with control theory, not max_iterations","url":"https://news.ycombinator.com/item?id=48919562","class":"product","score":31,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48920888","name":"StyleSeed: design-rules engine so AI agents stop building generic UI","url":"https://news.ycombinator.com/item?id=48920888","class":"product","score":24,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48936491","name":"Ratel: give agents unlimited tools and skills without context bloat","url":"https://news.ycombinator.com/item?id=48936491","class":"framework","score":23,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48939710","name":"Libretto PR agents: Automatically fix failing playwright scripts","url":"https://news.ycombinator.com/item?id=48939710","class":"product","score":22,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48994984","name":"OSS Cross-Harness: self-hosted registry and analytics for AI Agents","url":"https://news.ycombinator.com/item?id=48994984","class":"product","score":21,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48994186","name":"An MCP server that turns async-work practices into tools","url":"https://news.ycombinator.com/item?id=48994186","class":"mcp","score":20,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48978880","name":"The0: self-hosted runtime for trading bots, bring your own language","url":"https://news.ycombinator.com/item?id=48978880","class":"mcp","score":18,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48920681","name":"Aict: Unix coreutils that output XML/JSON, built for AI agents","url":"https://news.ycombinator.com/item?id=48920681","class":"product","score":17,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48947754","name":"On-chain bond market where the issuers are AI agents","url":"https://news.ycombinator.com/item?id=48947754","class":"product","score":15,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48996269","name":"Fractal: recursive agent loops for complex, multi-step work","url":"https://news.ycombinator.com/item?id=48996269","class":"product","score":14,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48998262","name":"Browser Tools SDK: an optimal browser harness for agents","url":"https://news.ycombinator.com/item?id=48998262","class":"framework","score":11,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"hn:48935212","name":"Nous: give GTM agents one context graph across your tools","url":"https://news.ycombinator.com/item?id=48935212","class":"product","score":10,"source":"hackernews","announced_at":"2026-07-22"},
  {"id":"ph:cometchat","name":"AI Agents in Chat (CometChat)","url":"https://www.producthunt.com/products/cometchat","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:remote-openclaw-2","name":"Remote OpenClaw","url":"https://www.producthunt.com/products/remote-openclaw-2","class":"mcp","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:rerun-2","name":"Rerun","url":"https://www.producthunt.com/products/rerun-2","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:diffsmith-code-review-studio","name":"Diffsmith","url":"https://www.producthunt.com/products/diffsmith-code-review-studio","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:createos-sandbox","name":"CreateOS Sandbox","url":"https://www.producthunt.com/products/createos-sandbox","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:manifest-363","name":"Manifest","url":"https://www.producthunt.com/products/manifest-363","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:bolna-2","name":"Bolna Agent Studio","url":"https://www.producthunt.com/products/bolna-2","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:openchatcut","name":"OpenChatCut","url":"https://www.producthunt.com/products/openchatcut","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"},
  {"id":"ph:rex-7","name":"Rex","url":"https://www.producthunt.com/products/rex-7","class":"product","score":None,"source":"producthunt","announced_at":"2026-07-22"}
]

existing_ids = set(e["id"] for e in state.get("announced", []))
fresh = [e for e in new_entries if e["id"] not in existing_ids]

state["last_run"] = "2026-07-22"
state["last_status"] = "COMPETITOR_LAUNCH_RADAR_OK"
combined = state.get("announced", []) + fresh
combined.sort(key=lambda x: x["announced_at"])
state["announced"] = combined[-200:]

shutil.copy(state_path, state_path + ".bak")

with open(state_path, "w") as f:
    json.dump(state, f, indent=2)

print("STATE_OK: " + str(len(state["announced"])) + " entries total, " + str(len(fresh)) + " new")
