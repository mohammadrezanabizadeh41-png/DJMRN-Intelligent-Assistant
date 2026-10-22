# DJMRN — Cloud-First Minimum Viable Path after central-router choice and tier-aware quota requirement
**Created:** 2026-10-23 | **Status:** SPECIFICATION/SEQUENCED PROPOSAL ONLY — NO BUILT GATEWAY/CLIENT/PROVIDER/AGENT | **Provenance:** user asked to archive smart tier routing + 2026 coding IDE comparison and give next executable project path. D-016 selects **Maxim Bifrost for gated evaluation**, D-005 full stack still undecided. Security gates G3B/CAP-006 closed; D-009 thin capability first, D-014 chat-first UX and D-015 two surfaces/shared tools remain valid.
**Canonical background:** [Current](../07-operations-and-continuity/CURRENT-STATUS.md), [Project Rules](../PROJECT-RULES.md), [D register](../02-project-management/DECISION-REGISTER.md), [TIER KB-0020](../08-project-knowledge-base/models-engines-and-hosts/KB-0020-capability-tiered-model-routing-and-free-quota-preservation.md), [IDE/API KB-0021](../08-project-knowledge-base/tools-and-integrations/KB-0021-ai-coding-clients-free-hosted-models-vs-reusable-apis-20261023.md), [WA0011/WA0012](../04-work-research-bridge/LEDGER.md).

## Minimal architecture (separation is non-negotiable)
```text
User (Persian chat)    Coding client in existing VS Code (only when needed)
       \                /
        -> DJMRN app / thin client(s)
           -> task labeling and capability requirements (deterministic initially)
              -> authenticated localhost Bifrost compatible API (PINNED OSS; NOT RUNNING)
                 -> free-eligible provider/model allowlist with comparable task capability
                    e.g. direct provider API / Kilo AI Gateway / OpenCode Zen if independently verified
           -> separate local deterministic CAP-006 and future tool executor;
              external language-model replies NEVER grant Windows or file privileges
```
If Bifrost proves inadequate for shared exact daily-free allowance, investigate **swapping** its router or an independently justified tiny policy adapter; do NOT add multiple gateways by default.

## Ordered delivery stages and independent gates
### P0: documentation and contract (NEXT; no runtime needed)
- Pin what each client sends: `task_class` (`lite|standard|reasoning|specialist`), `requires_tools`, `requires_vision`, `context_tokens`, `privacy_class`, `max_retries`, `free_only=true`, request correlation ID, auth scope and approval flag. Determine exact OpenAI-compatible alias/header mapping in target Bifrost build rather than assert it exists.
- Define registry candidate rows (provider/model identity, official free price, RPD/RPM, reset/cooldown, context/tool ability, account validity, privacy, local confidence/evidence date, permitted fallback order, reserved capacity).
- Set explicit errors: `FREE_POOL_EXHAUSTED`, `NO_COMPATIBLE_MODEL`, `PROVIDER_429_COOLDOWN`, `AUTH_REQUIRED`, `STREAM_INTERRUPTED`, `TOOL_APPROVAL_REQUIRED`. No paid provider, unknown price, account cycling, consumer IDE reuse. **Deliverable:** small versioned protocol/acceptance matrix, not giant codebase.

### P1: choose exact OSS artifact and source-only preflight (NEXT AFTER P0)
- Confirm exact `maximhq/bifrost` OSS transport release/Go binary/launcher, supported native Windows deployment vs NPX/Docker/WSL overhead; pin checksum/commit, plugin availability, routing aliases, model allowlists, compatible custom provider URLs, authentication, logging/retention, resource estimates (UNKNOWN until measured).
- Compare smallest no-Bifrost mock harness if Bifrost install footprint/Windows missing; do not silently select alternative. **Deliverable:** exact reproducible install-free test plan and fail/stop gates.

### P2: sandboxed synthetic routing tests (require separate authorization before new executable code/test)
- Offline local fixtures simulate provider A healthy, 429 with reset, 500/timeout, B healthy, both unavailable, malformed tool result, mid-stream break, two clients/concurrent request bursts, restart. Do not call cloud providers.
- Verify endpoint stability, per-tier model compatibility, no high-tier reserve leak, zero paid fallback, tool calls unchanged, structured errors, metrics without payload secrets. Re-evaluate based on actual results; high-tier 'intelligence' must be benchmarked by task, not name or parameter count.
- Device RAM/CPU benchmark **not yet measured**. Only after user-approved real local execution on Windows 11.

### P3: qualify exactly two or three real free HTTP upstreams (separate authorization)
- Candidate sources: official direct free-API providers (e.g., Gemini/Groq/OpenRouter/Cerebras), and **Kilo AI Gateway `kilo-auto/free`**, **OpenCode Zen time-limited free routes** when independent terms, protocol and account evidence allow. **No provider account, signup, API key or usage authorized currently**. In-product Antigravity consumer Claude quota is NOT routable.
- Confirm actual configured account free billing hard-zero or provider enforced no overage, free reset schedule, model capabilities, data policy and task performance. User instruction excludes geographical Iran constraints from *product comparison*; does not waive provider licensing/usage terms. Fail closed if pricing or API access unknown.
- First real test tiny chat only, then tool schema if needed, per model; prefer one light + one standard plus high-tier only after quality evidence.

### P4: first user-visible Persian chat with 1-2 free models + existing safe capability (later)
- Pick one lightweight chat frontend only after P2/P3. Jan is candidate, not a mandatory system dependency or selected deployment. A tiny chat UI may be better if resources show it. Frontend sends to local router; actual CAP-006 read-only document search remains behind exact-file allowlist and explicit approval, separate from model API, no automatic Windows administrative commands.
- User-visible first success: Persian question -> chosen lite/standard free model -> source-grounded local document lookup requested with approved scope -> Persian answer showing source/model/routing reason and error when quota exhausted. Only permitted action type; no real cloud submission of private files without authorization.

### P5: controlled coding-client integration (later)
- Existing VS Code used first; compare exactly **ONE** compatible extension/client (Kilo Code vs Cline/Roo vs OpenCode) on mock Bifrost endpoint and human-approved small synthetic repo. Tool-execution approvals and file guard stay outside model choice.
- Antigravity is independent optional standalone help tool, not an API upstream; don't install parallel IDEs as precondition or proxy Antigravity consumer free login.

### P6: smarter tier assignment (AFTER measured need)
- Start deterministic user/client-supplied label; only if labeled test suite shows accuracy gains add simple low-cost classifier / rules engine. Include periodic capability benchmark, reserve budgets, cross-client single ledger, per-account reset and policy update controls.
- Optional observability map last; zero sensitive prompt/body logging by default.

## Exit criteria and current next action
**RIGHT NOW** write/pin **P0 request-routing contract and deterministic test cases**, then **P1 install-free OSS Windows/version feasibility**. No device access/installation/cloud usage until user expressly authorizes a narrow P2 (and P3 separately). Treat Bifrost as preferred candidate only, not promise production-grade failover or free account availability. Preserve prior completed bounded CAP-006 tests and security G3B status; no need to redo earlier PowerShell steps.

## 2026-10-23 EXECUTION RECORD — P0 specification DONE, P1 source preflight PARTIAL / gate still closed
Following explicit user "ادامه بده", the coordinator performed **documentation and public-source code reading only**:
- **P0 DONE as a documented v0.1 contract**: [P0 request policy and 14 offline acceptance scenarios](DJMRN-CLOUD-ROUTER-P0-REQUEST-POLICY-CONTRACT-20261023.md). Task labels `lite`/`standard`/`reasoning` + orthogonal `specialist`, explicit approved free API allowlists, cross-client/shared account quota, protected advanced reserve, failure and tool/stream exclusions. Proposed JSON metadata are **NOT** native REST inputs to Bifrost; actual mappings must be tested.
- **P1 SOURCE PASS / DEPLOYMENT NOT PASSED**: [Pinned Maxim Bifrost v2.3.2 OSS Windows preflight](BIFROST-OSS-WINDOWS-P1-SOURCE-PREFLIGHT-20261023.md). Release source tag `transports/v2.3.2` -> peeled commit `a05ea20e68bf116a35e9f05b1a3d749624b3935e`. Tagged NPX wrapper **supports Windows/amd64** and may download `bifrost-http.exe`; Windows binary NOT fetched/signed/benchmarked. Source verifies virtual keys, CEL rules, fallback and **Beta built-in Complexity Router** (SIMPLE/MEDIUM/COMPLEX) with additional decision/embedding call and cost risk. Avoid adding standalone classifier now; deterministic policy first.
- **New critical stop:** fresh gateway dashboard/admin API may initially be unprotected; design authenticated loopback and setup-token ceremony BEFORE any start. `Authorization` vs `x-bf-vk` differs by inference auth setting; test. Free provider quota and RPD reset/account-level atomic reserve still NOT automatically proven by Bifrost gateway money budgets.
- **P2 next checkpoint:** first obtain explicit separate user approval for any executable mocked localhost Windows/runtime test; before then only review source and prepare self-contained test package/spec. Real provider/account/API use is separate P3 permission; G3B/CAP-006 unchanged. No code/tests/runtime were executed by these P0/P1 records.
