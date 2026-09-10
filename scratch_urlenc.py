import urllib.parse as up

titles = {
    "CoolGithubProjects": "Aeon - open-source agent framework that just shipped a Uniswap v4 hook registry deploying to 7 chains",
    "OpenSourceAI": "Shipped a multi-chain hook marketplace with a framework that has no approval loop between runs - here's how the pipeline works",
    "AIPromptProgramming": "An agent framework where shipping a feature means a scheduled markdown file writes code and opens a PR",
    "CLaudeSkills": "A skill whose entire job is drafting Reddit promo posts from another skill's output - here's the shape",
}
for sub, t in titles.items():
    print(sub, "->", "https://www.reddit.com/r/" + sub + "/submit?title=" + up.quote(t))
