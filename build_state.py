import json
import re

def slug(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

stories = [
    {
        "date": "2026-08-30", "title": "WebMCP ships",
        "source": "https://x.com/aaronjmars/status/2093724185994346542",
        "subs": ["r/StartupMind", "r/OpenSourceAI", "r/AIPromptProgramming", "r/AskVibecoders"],
    },
    {
        "date": "2026-09-01", "title": "Miroshark shipped x402aff",
        "source": "https://x.com/aaronjmars/status/2093053679259599283",
        "subs": ["r/MiroFish", "r/Agent_AI", "r/aiecosystem"],
    },
    {
        "date": "2026-09-01", "title": "Aeon vuln-scanner responsible disclosure",
        "source": "https://x.com/aeonframework/status/2094047486222442924",
        "subs": ["r/OpenSourceAI", "r/CLaudeSkills", "r/lovingopensourceAI", "r/CoolGithubProjects"],
    },
    {
        "date": "2026-09-02", "title": "CultOS x402 relay affiliate payouts",
        "source": "https://x.com/thecultos/status/2095166433420292459",
        "subs": ["r/StartupMind", "r/LovingAI"],
    },
    {
        "date": "2026-09-03", "title": "UsePodAI cost lever",
        "source": "https://x.com/aeonframework/status/2095109716636577888",
        "subs": ["r/Agent_AI", "r/AIPromptProgramming", "r/OpenSourceAI"],
    },
    {
        "date": "2026-09-04", "title": "CultOS project stack names Aeon+Miroshark",
        "source": "https://x.com/thecultos/status/2095901737345339655",
        "subs": ["r/MiroFish", "r/aiecosystem", "r/Ollama", "r/CoolGithubProjects"],
    },
    {
        "date": "2026-09-05", "title": "Aeon accepted into OpenAI Daybreak",
        "source": "https://x.com/aaronjmars/status/2095903024946295214",
        "subs": ["r/StartupMind", "r/Agent_AI", "r/lovingopensourceAI", "r/AskVibecoders"],
    },
    {
        "date": "2026-09-06", "title": "eyebrow audited Aeon, 2 PRs merged",
        "source": "https://x.com/eyebrowCC/status/2094475852171956625",
        "archetype": "E",
        "subs": ["r/AgentsOfAI", "r/AI_Agents", "r/LLMDevs"],
        "comment_subs": ["r/cybersecurity"],
    },
    {
        "date": "2026-09-06", "title": "TaskMarket Delegate named in Base roundup",
        "source": "https://x.com/AIonBase_/status/2096295356128698778",
        "subs": ["r/CLaudeSkills", "r/AIPromptProgramming", "r/LovingAI"],
    },
    {
        "date": "2026-09-07", "title": "Capminal credits Aeon security review",
        "source": "https://x.com/Capminal/status/2096968349028872581",
        "subs": ["r/OpenSourceAI", "r/aiecosystem", "r/StartupMind", "r/AskVibecoders"],
    },
    {
        "date": "2026-09-10", "title": "Aeon ships Hook Marketplace",
        "source": "https://x.com/aeonframework/status/2097997668601544919",
        "subs": ["r/CoolGithubProjects", "r/OpenSourceAI", "r/AIPromptProgramming", "r/CLaudeSkills"],
    },
    {
        "date": "2026-09-11", "title": "MiroShark one-click video export",
        "source": "https://x.com/aaronjmars/status/2098061703627886906",
        "subs": ["r/MiroFish", "r/AskVibecoders", "r/StartupMind", "r/aiecosystem"],
    },
    {
        "date": "2026-09-12", "title": "Aeon ships Submit Hook skill",
        "source": "https://x.com/aeonframework/status/2098792766658535737",
        "subs": ["r/CLaudeSkills", "r/OpenSourceAI", "r/CoolGithubProjects", "r/aiecosystem"],
    },
    {
        "date": "2026-09-15", "title": "0x Protocol/Hayden Adams hook-safety debate",
        "source": "https://x.com/haydenzadams/status/2099711270115013085",
        "subs": ["r/Agent_AI", "r/aiecosystem", "r/OpenSourceAI", "r/CoolGithubProjects"],
    },
    {
        "date": "2026-09-17", "title": "Miroshark bankrbot x402 Town Hall launch",
        "source": "https://x.com/svector_eth/status/2100605772610834714",
        "subs": ["r/MiroFish", "r/StartupMind", "r/AIPromptProgramming"],
    },
    {
        "date": "2026-09-19", "title": "CultOS first hard usage numbers on Aeon",
        "source": "https://x.com/thecultos/status/2101048281602146370",
        "subs": ["r/StartupMind", "r/Agent_AI", "r/aiecosystem"],
    },
]

posts = []
for st in stories:
    for sub in st["subs"]:
        key = slug(st["title"]) + "--" + slug(sub)
        posts.append({
            "key": key,
            "title": st["title"],
            "subreddit": sub,
            "archetype": st.get("archetype"),
            "kind": "post",
            "posted": None,
            "drafted": st["date"],
            "status": "unconfirmed",
            "measurements": [],
            "removed_on": None,
            "source_story": st["source"],
        })
    for sub in st.get("comment_subs", []):
        key = slug(st["title"]) + "--" + slug(sub) + "--comment"
        posts.append({
            "key": key,
            "title": st["title"],
            "subreddit": sub,
            "archetype": st.get("archetype"),
            "kind": "comment",
            "posted": None,
            "drafted": st["date"],
            "status": "unconfirmed",
            "measurements": [],
            "removed_on": None,
            "source_story": st["source"],
        })

state = {"posts": posts, "removals": []}
with open("memory/topics/reddit-scorecard-state.json", "w") as f:
    json.dump(state, f, indent=2)

print("total candidates:", len(posts))
