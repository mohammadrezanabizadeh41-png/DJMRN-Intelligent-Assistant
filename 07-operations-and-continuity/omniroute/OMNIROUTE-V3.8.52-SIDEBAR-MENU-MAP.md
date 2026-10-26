# OmniRoute 3.8.52 — Sidebar Navigation Map
Date captured: 2026-10-26
Evidence: 14 user-provided screenshots of left sidebar. This is a transcription of **visible** labels only, not a verified inventory of every possible submenu. Collapsed nested categories and cut-off scrolling may conceal additional entries. Do not claim features work solely because a menu item exists.

## Global
- Home — Dashboard overview
- Search (sidebar search field)
- Restart; Shutdown (bottom)

## OmniProxy
- Endpoints — Your AI connection URLs
- API Keys — Manage API keys and access
- Providers — Manage AI providers
- Models & Combos — Browse models and combos acr...
- Embedded Services — Optional local services
- Combos — Group providers for failover
- Combo Studio — Live routing cascade
- Provider Quota — Track provider usage limits
- Quota Sharing — Share provider quotas across keys

## Tools (visible)
- CLI Code — Code tools pointing to Om...
- CLI Agents — Autonomous CLI agents
- ACP Agents — CLI spawned by OmniRoute
- Cloud Agents — Manage cloud-based agents
- Conductor — CLI-agent fleet
- Orchestration — Live view of everything run...
- Agent Bridge — Intercept IDE agent traffic
- Traffic Inspector — Inspect request and respon...
- Discovery — Scan providers for free access

## Integrations
- API Endpoints — Expose custom endpoints
- Webhooks — Get notified of events
- Log export — Ship call logs out
- Proxy — HTTP proxy settings

## Analytics
- Usage — Traffic and usage stats
- Combo Health — Combo target reliability
- Utilization — Provider utilization
- Cache — Cache hit rates
- Compression — Token savings stats
- Search — Search tool analytics
- Evals — Eval suite results
- Provider Stats — Latency and performance metrics

## Costs
- Overview — Consolidated cost analysis
- Pricing — Per-model pricing rules
- Budget — Budget limits
- Free-Tier Budget — Monthly free-token allowances
- Free Provider Rankings — Best free providers ranked by m... (subtitle truncated)

## Monitoring
- Activity — Friendly feed of recent events
- Logs > (nested submenu not expanded in screenshots)
- Audit > (nested submenu not expanded)
- System > (nested submenu not expanded)

## Dev Tools
- Translator — Format conversion
- Playground — Test prompts live
- Search Tools — Search tool registry

## Agentic Features
- Memory — Persistent agent memory
- AgentSkills — A2A skill registry
- Chaos Mode — Multi-model parallel execution
- OmniSkills — Sandbox skill registry
- MCP Server — MCP server controls
- A2A Server — A2A protocol server
- Plugins — Plugin marketplace & installs

## Other Features > Batch
- Gamification > (nested submenu not expanded)
- Media — Cached media files
- Batch >:
  - Batch Jobs — Process multiple requests
  - Files — Batch input/output files

## Compression Context
- Compression Settings — Global defaults
- Engine Combos — Combine compression engi...
- Caveman — Prompt compression
- RTK — Output filtering
- Headroom — Tabular compaction
- Session Dedup — Cross-turn deduplication
- CCR — Retrieve markers
- LLMLingua — Semantic pruning
- Lite — Fast whitespace cleanup
- Aggressive — Summary and aging
- Ultra — visible at screenshot bottom, description not visible
- OmniGlyph — Context as images
- Compression Studio — Live engine cascade
- Exclusions — Per-model/endpoint bypass

## Configuration
- Storage — Database and backups
- Appearance — Theme and layout
- AI Settings — AI behavior defaults
- Modality Bridge — Image/audio → text fallback for ... (truncated)
- Global Routing — Global routing rules
- Resilience — Retries and breakers
- Advanced — Power user options
- Security — Auth and encryption
- Access Tokens — Scoped CLI tokens for remote m... (truncated)
- Feature Flags — Toggle system capabilities
- Cache — Model catalog and response cac... (truncated)
- Sidebar — Customize sidebar layout

## Help
- Docs — Documentation
- Issues — Report a bug
- Changelog — Release notes

## Action paths for DJMRN
1. Change admin/login password: **Configuration > Security** (the menu exists; exact controls inside have not been viewed).
2. Add provider credentials: **OmniProxy > Providers**; never save actual keys to repository.
3. Inspect shared models: **OmniProxy > Models & Combos**.
4. Inspect quotas: **OmniProxy > Provider Quota**, **Quota Sharing** and **Costs > Free-Tier Budget**; no claim of actual quota independence without tests.
5. Configure task-aware routing: **Configuration > Global Routing**, **OmniProxy > Combos / Combo Studio**.
6. Inspect failure policy: **Configuration > Resilience**.
7. Test local endpoint and agents: **OmniProxy > Endpoints / API Keys**, **Dev Tools > Playground**, **Tools > Agent Bridge / Orchestration**.

Source fidelity: Visible spelling and subtitle truncations retained. Screen order reflects multiple scroll locations and sections rather than exact global ordering. All controls/behaviors inside these pages remain to be inspected.
