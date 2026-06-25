# MCP Ecosystem Tracker

*Last run: 2026-06-25*

## Seed Context (2026-05-18)
- Stainless acquired by Anthropic ~$300M+ (The Information, 5/18/2026). Stainless team now building MCP server generation tooling inside Anthropic. Stainless winding down hosted products — existing customers keep generated SDKs. Previously generated SDKs for: OpenAI, Google, Cloudflare, Meta, Runway, Groq, Cerebras, Modern Treasury, and all official Anthropic SDKs.
- MCP (Model Context Protocol): open protocol Anthropic authored. Standardizes how agents make tool calls to external services. GitHub: modelcontextprotocol/modelcontextprotocol.
- Thesis: MCP becomes the default tool-call rail for agents. Anthropic owns the generation layer → controls the integration layer.

## Key Stats
- npm @modelcontextprotocol/sdk: **40,125,385 weekly downloads** (week of Jun 18–24, 2026) — up +367,210 (+0.9%) vs last week
- PyPI mcp: unavailable (429 rate limit on pypistats — consistent)
- GitHub modelcontextprotocol org repos: **42 total** (unchanged from last run)
- modelcontextprotocol/servers: 87,692★ (↑+276 this week)
- modelcontextprotocol/python-sdk: 23,442★ (↑+82)
- modelcontextprotocol/typescript-sdk: 12,723★ (↑+32)
- modelcontextprotocol/inspector: 10,192★ (↑+67)
- modelcontextprotocol/modelcontextprotocol (spec): 8,465★ (↑+41)
- modelcontextprotocol/registry: 6,954★ (↑+15)
- go-sdk: 4,722★ | csharp-sdk: 4,349★ | rust-sdk: 3,561★ | java-sdk: 3,492★
- php-sdk: 1,542★ | use-mcp: 1,029★

## Protocol Extensions (active development)
- **ext-apps** (2,485★ ↑+42): MCP Apps — standard for UIs/HTML interfaces embedded in AI chatbots, served by MCP servers
- **ext-auth** (132★ ↑+24, +22% in one week): Extensions to authorization — formal auth hardening. Star velocity spike signals real developer interest
- **experimental-ext-interceptors** (18★): SEP-2624 interceptors — multi-language reference implementation
- **experimental-ext-skills** (153★ ↑+2): Skills discovery and distribution through MCP primitives
- **ext-tasks** (7★): Long-running operations / agent communication (async tasks)
- **mcpb** (1,996★ ↑+21): Desktop Extensions — one-click local MCP server installation in desktop apps
- **conformance** (73★): Conformance test suite for MCP implementations

## Upcoming Spec
- **2026-07-28 RC (active)**: Largest protocol revision since launch. Stateless core (deployable on plain HTTP, no sticky sessions, round-robin load balancer). Mcp-Method/Mcp-Name headers for gateway routing. ttlMs caching for tools/list responses. MCP Apps + Tasks formally included. 10-week SDK validation window open. Tier 1 SDKs expected to ship within window.
- RC announced May 21, 2026. Window closes ~late July. Auth hardening (OAuth 2.1/PKCE, SAML/OIDC) live in Q2 2026.

## Known Servers
- Official (modelcontextprotocol org): filesystem, git, github, gitlab, google-maps, google-drive, postgres, sqlite, slack, brave-search, puppeteer, fetch, memory, sentry, time, sequential-thinking, everything (test server) — now archived to servers-archived
- Enterprise launches: HubSpot (official remote MCP server), Adobe Marketo Engage (100+ operations, launched April 2026), AWS MCP Server (GA May 6, 2026, IAM guardrails + CloudWatch + CloudTrail), Microsoft MCP Server for Enterprise (Preview — Entra ID natural-language access for AI agents)
- Planned: Zendesk MCP Server early access (summer 2026, announced May 21)
- Third-party high-quality: n8n (194k★), trigger.dev (15k★), dagu (3.5k★), TabularisDB/tabularis (2.5k★), vmlx (697★), griddynamics/rosetta (308★ ↑+3), christinminor459/OnionClaw (215★ — Tor network access for agents, interesting OSINT angle)
- Agentic CRM: revfleet/hscli (HubSpot CLI + 1180 endpoints)
- Multi-platform ads: ad-ops-mcp-hub (Google Ads, Meta, TikTok, LinkedIn)

## Adoption Signal
- March 2026: 97M monthly SDK downloads (970x increase in 18 months)
- 41% of surveyed software orgs in limited/broad production with MCP servers (Stacklok 2026 report)
- 5,000+ MCP servers now available; every major AI coding tool supports them
- CIO coverage: "why MCP is suddenly on every executive agenda"
- MCP donated to Agentic AI Foundation (AAIF) / Linux Foundation (Dec 2025) — vendor-neutral open standard
- MCP Dev Summit North America 2026 held — "MCP is now enterprise infrastructure" framing
- MCP ecosystem fragmentation visible: MCP Servers Live index (auto-updated every 15 min, linny006/mcp-servers-live)
- The New Stack: "Why the Model Context Protocol Won" — mainstream dev media declaring victory

## Signal Log
- 2026-05-18: Anthropic acquires Stainless. Stainless team pointed at MCP server generation.
- 2026-06-18: 42 org repos / npm 39.75M/wk (baseline) / momentum: breakout / 2026-07-28 RC announced (stateless core); HubSpot + Adobe Marketo official servers confirmed; 41% orgs in production
- 2026-06-25: 42 org repos (no new) / npm 40.1M/wk (+367k, +0.9%) / momentum: building (5 pts) / ext-auth +22% star velocity; Microsoft Enterprise MCP Preview; RC validation window active; mainstream "MCP won" coverage
