import json

with open("/tmp/tw-mr-miroshark.json") as f:
    data = json.load(f)

tweets = data.get("tweets", [])
print("count", len(tweets), "has_next", data.get("has_next_page"))
for t in tweets:
    author = t.get("author", {})
    print("---")
    print("user:", author.get("userName"))
    print("verified:", author.get("isBlueVerified"))
    print("followers:", author.get("followers"))
    print("created:", t.get("createdAt"))
    print("likes:", t.get("likeCount"), "rts:", t.get("retweetCount"), "replies:", t.get("replyCount"))
    print("url:", t.get("url"))
    print("text:", (t.get("text") or "").replace("\n", " ")[:300])
