# OmniRoute 3.8.52 — Sidebar Navigation Inventory
Captured from 14 user-supplied screenshots on 2026-10-26. **Visible labels only**; some sections and nested items may not be shown because of scrolling. This is a navigational map, not confirmation that each feature is configured or working. Labels preserved in English for easy UI matching.

## Home
- Home — Dashboard overview

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

## Tools
- CLI Code — Code tools pointing to Om...
- CLI Agents — Autonomous CLI agents
- ACP Agents — CLI spawned by OmniRoute
- Cloud Agents — Manage cloud-based agents
- Conductor — CLI-agent fleet
- Orchestration — Live view of everything run...
- Agent Bridge — Inspect IDE agent traffic
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
- Free Provider Rankings — Best free providers ranked by m...

## Monitoring
- Activity — Friendly feed of recent events
- Logs — submenu not expanded in screenshots
- Audit — submenu not expanded in screenshots
- System — submenu not expanded in screenshots

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

## Other Features
- Gamification — submenu not expanded
- Media — Cached media files
- Batch
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
- Ultra — item visible near lower edge, description not visible
- OmniGlyph — Context as images
- Compression Studio — Live engine cascade
- Exclusions — Per-model/endpoint bypass

## Configuration
- Storage — Database and backups
- Appearance — Theme and layout
- AI Settings — AI behavior defaults
- Modality Bridge — Image/audio → text fallback for ...
- Global Routing — Global routing rules
- Resilience — Retries and breakers
- Advanced — Power user options
- Security — Auth and encryption
- Access Tokens — Scoped CLI tokens for remote m...
- Feature Flags — Toggle system capabilities
- Cache — Model catalog and response cac...
- Sidebar — Customize sidebar layout

## Help
- Docs — Documentation
- Issues — Report a bug
- Changelog — Release notes

## Persistent bottom actions
- Restart
- Shutdown

## Navigation for DJMRN next steps
1. **Change login password:** Configuration → Security (visible in screenshots; actual controls inside not yet inspected).
2. **Register existing Gemini API credential:** OmniProxy → Providers; avoid pasting secret in chat or repo.
3. **Gateway keys for clients:** OmniProxy → API Keys; distinguish gateway-issued keys from upstream provider keys.
4. **Find connection address:** OmniProxy → Endpoints.
5. **Free quota/routing:** Provider Quota, Quota Sharing, Combos, Combo Studio, Configuration → Global Routing and Resilience, Costs → Free-Tier Budget.
6. **Verify requests:** Dev Tools → Playground; Analytics → Usage; Monitoring → Logs.
7. **Agent integration:** Tools → Agent Bridge/Orchestration and Agentic Features → MCP Server/A2A Server, if applicable.

## Provenance and limitations
- Screenshot-based extraction, not tested feature behavior.
- Some captions visibly truncated with ellipses; do not invent hidden words.
- Top-level menu order in this document is grouped for lookup; actual on-screen sequence may differ.
- UI could change with app updates. Version observed: v3.8.52.
- Do not store any password or API secret in this document.
