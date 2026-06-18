# MCP Ecosystem Tracker

*Last run: 2026-06-18*

## Seed Context (2026-05-18)
- Stainless acquired by Anthropic ~$300M+ (The Information, 5/18/2026). Stainless team now building MCP server generation tooling inside Anthropic. Stainless winding down hosted products — existing customers keep generated SDKs. Previously generated SDKs for: OpenAI, Google, Cloudflare, Meta, Runway, Groq, Cerebras, Modern Treasury, and all official Anthropic SDKs.
- MCP (Model Context Protocol): open protocol Anthropic authored. Standardizes how agents make tool calls to external services. GitHub: modelcontextprotocol/modelcontextprotocol.
- Thesis: MCP becomes the default tool-call rail for agents. Anthropic owns the generation layer → controls the integration layer.

## Key Stats
- npm @modelcontextprotocol/sdk: **39,758,175 weekly downloads** (week of Jun 11–17, 2026) — first recorded baseline
- PyPI mcp: unavailable (429 rate limit on pypistats)
- GitHub modelcontextprotocol org repos: **42 total**
- modelcontextprotocol/servers: 87,416★
- modelcontextprotocol/python-sdk: 23,360★
- modelcontextprotocol/typescript-sdk: 12,691★
- modelcontextprotocol/inspector: 10,125★
- modelcontextprotocol/modelcontextprotocol (spec): 8,424★
- modelcontextprotocol/registry: 6,939★
- go-sdk: 4,699★ | csharp-sdk: 4,335★ | rust-sdk: 3,529★ | java-sdk: 3,480★

## Protocol Extensions (active development)
- **ext-apps** (2,443★): MCP Apps — standard for UIs/HTML interfaces embedded in AI chatbots, served by MCP servers
- **ext-auth** (108★): Extensions to authorization — formal auth hardening in flight
- **experimental-ext-interceptors** (17★): SEP-2624 interceptors — multi-language reference implementation
- **experimental-ext-skills** (151★): Skills discovery and distribution through MCP primitives
- **ext-tasks** (7★): Long-running operations / agent communication (async tasks)
- **mcpb** (1,975★): Desktop Extensions — one-click local MCP server installation in desktop apps
- **conformance** (72★): Conformance test suite for MCP implementations

## Upcoming Spec
- **2026-07-28 RC**: Largest protocol revision since launch. Stateless core (deployable on plain HTTP, no sticky sessions, round-robin load balancer). Mcp-Method/Mcp-Name headers for gateway routing. ttlMs caching for tools/list responses. MCP Apps + Tasks formally included. 10-week SDK validation window open. Tier 1 SDKs expected to ship within window.

## Known Servers
- Official (modelcontextprotocol org): filesystem, git, github, gitlab, google-maps, google-drive, postgres, sqlite, slack, brave-search, puppeteer, fetch, memory, sentry, time, sequential-thinking, everything (test server) — now archived to servers-archived
- Enterprise launches: HubSpot (official remote MCP server), Adobe Marketo Engage (100+ operations, launched April 2026)
- Third-party high-quality: n8n (193k★), trigger.dev (15k★), dagu (3.5k★), TabularisDB/tabularis (2.5k★), vmlx (697★), griddynamics/rosetta (305★)
- Agentic CRM: revfleet/hscli (HubSpot CLI + 1180 endpoints)
- Multi-platform ads: ad-ops-mcp-hub (Google Ads, Meta, TikTok, LinkedIn)

## Adoption Signal
- March 2026: 97M monthly SDK downloads (970x increase in 18 months)
- 41% of surveyed software orgs in limited/broad production with MCP servers (Stacklok 2026 report)
- CIO coverage: "why MCP is suddenly on every executive agenda"
- MCP ecosystem fragmentation visible: MCP Servers Live index (auto-updated every 15 min, linny006/mcp-servers-live)

## Signal Log
- 2026-05-18: Anthropic acquires Stainless. Stainless team pointed at MCP server generation.
- 2026-06-18: 42 org repos / npm 39.75M/wk (baseline) / momentum: breakout / 2026-07-28 RC announced (stateless core); HubSpot + Adobe Marketo official servers confirmed; 41% orgs in production
