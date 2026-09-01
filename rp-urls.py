import urllib.parse
from datetime import date

subs = {
    'MiroFish': 'x402aff shipped - any x402 endpoint goes affiliate-ready in one line, payouts locked onchain',
    'Agent_AI': 'Agents that pay and get paid - we shipped an onchain affiliate rail for x402 endpoints',
    'aiecosystem': 'Miroshark crossed 100k agent actions and shipped an onchain affiliate layer for x402',
}
for s, t in subs.items():
    url = 'https://www.reddit.com/r/' + s + '/submit?title=' + urllib.parse.quote(t, safe='')
    print(s + ' -> ' + url)

print('days_since_last_promo:', (date(2026, 9, 1) - date(2026, 8, 30)).days)
