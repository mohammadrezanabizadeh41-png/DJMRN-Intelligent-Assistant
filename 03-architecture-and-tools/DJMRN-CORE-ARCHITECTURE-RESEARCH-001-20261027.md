# DJMRN — Foundational Hybrid Intelligence Architecture | Work Research 001

**Research ID:** `DJMRN-CORE-ARCHITECTURE-RESEARCH-001`  
**Research / user-submitted Work response:** 2026-10-27 (Work reported duration 3m43s)  
**Archive entry:** 2026-10-27; reproduced as a detailed, structured evidence-preserving synthesis of the user's Work response, **not a verbatim transcript**. The full originally shared Work narrative remains in the originating conversation.  
**Status:** RESEARCH COMPLETE WITH EXPLICIT EVIDENCE GAPS / **RESEARCH ONLY** / CONDITIONAL RECOMMENDATION, **NOT an approved global technology decision, implementation, test or deployment**.  
**Repository:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, branch `main`.  
**Independent coordinator check at archive time:** live Notion Operating Memory / Tool Governance, project repo metadata, project rules, current status, master roadmap, architecture synthesis and decision register read. Exact three `m1_pilot/core/` code paths cited by Work were *not resolved* by the coordinator's initial direct path attempts; do not upgrade Work's source-code claims to a second independent audit. Original Work cited exact blob SHAs for those files. Some source pages returned `verification=unverified`.

## 0 — Why this entry exists; relationship to earlier architecture

User explicitly requested preservation of the first Work architecture research and analysis of the practical first milestone. **Do not remove, replace, rename, or silently supersede** the earlier hybrid architecture in `07-operations-and-continuity/CURRENT-STATUS.md`:
- `2026-10-25 — DJMRN-HYBRID-AGENT-WORKFLOW-AND-PREREQUISITE-INSTALL-PACKET-001`
- `2026-10-26 — FUTURE ARCHITECTURE RESEARCH: HYBRID MULTI-AGENT + COMPLEMENTARY SOFTWARE`
- Commit preserving the 26 Oct architecture: `49a01d7608cdce4573683c5113dc046674962d89`
- Project-level proposal: `02-project-management/MASTER-SYSTEM-ROADMAP-20261022.md`
- Comparative review: `03-architecture-and-tools/ARCHITECTURE-RESEARCH-SYNTHESIS-20261022.md`
- Model routing/admission policy: `02-project-management/FREE-CLOUD-MODEL-QUOTA-AND-ROLE-ROUTING-POLICY-20261025.md` (D-018).

**Interpretation:** This research specifies a feasible first *vertical slice* and evolution path **inside** the pre-existing hybrid vision. It does not demote or prohibit future Agno/AgentOS, OmniRoute family routing, shared tools, agent collaboration, knowledge services, browser, email, n8n, Docker, DBOS/Dagu or conditional cloud execution. These stay on-demand; their need must be proven.

## 1 — Executive conclusion: Where to start?

**Work's conditional recommendation:** begin with one real, bounded workflow:
`Persian user message → persistent task → authorized deterministic tool → source-grounded answer → persistent result → optional second-role review`.

A central intelligence system is **not** one permanent LLM and is **not** merely a knowledge database. Separate:
1. Semantic understanding/reasoning, using a model only when necessary.
2. Execution authority, policy, ordering, permissions and budget in trusted code.
3. Task and conversation state in a durable operational store.
4. Source knowledge, evidence and rebuildable search projections in their appropriate authority domains.

Compare starting orders: **Smallest Working Vertical First** best fits DJMRN's unproven end-to-end link; **Knowledge Store First** only when search itself is the product; **Agent/Control Plane First** risks building unused infrastructure. Use a minimal modular-monolith-shaped application from the outset, but implement only actual needed capabilities.

## 2 — What is the shared intelligence core?

**Work-derived definition:** A small set of trusted execution policies, typed contracts, durable state and interfaces to knowledge, models and tools, coordinating multiple capabilities with explicit identity, authorization and evidence. It can start and stop with the chat app. It is **not** inherently a permanent daemon, message broker, autonomous agent, full data warehouse or vector database.

Key responsibilities and distinction:
- **Task control:** accept/validate work, assign owner, run policy, record transitions/results, dispatch permitted steps.
- **Workflow:** explicit ordering/retry/recovery, often entirely no-LLM.
- **Tool/worker:** bound action on allowed files, data or endpoints; executes real I/O.
- **Model adapter:** optional LLM call through OmniRoute or alternative; model proposes text/structured reasoning, never authority.
- **Knowledge interface:** fetch source-grounded, permissioned fragments; FTS first, vectors/graph if measured relevance gaps.
- **Agent/role interface:** role-scoped reasoning/delegation; collaboration becomes useful only when it improves outcomes.
- **Observation:** task/step/request IDs, errors, provenance, budgets, latency, optional later tracing.

**Important non-equivalences:** shared memory does not create coordination; messaging does not create reasoning; agent discussion does not guarantee independent verification; workflow orchestration needs no agent or LLM by default.

## 3 — Actual project findings reported by Work and operational gaps

**Work GitHub reading baseline:** `main` at `44e955799f81de60779752f67b0b0418d9bfa544`. Work explicitly reported targeted reads, not a complete audit of giant Notion archives or all history.

- 25 Oct hybrid execution design includes code-based deterministic workers, workflows, model inference and human approval.
- 26 Oct hybrid multi-agent design separates OmniRoute inference/data plane, Agno/AgentOS candidate control plane, shared tools, scoped operational state, and optional n8n/Playwright/Docker/PostgreSQL/Redis.
- Agno `3.1.10` plus Python `3.12.15` isolated environment and AgentOS imports were reportedly installed/passed; **Agno → OmniRoute real end-to-end call was not verified**, prior PowerShell command failed before inference.
- `DJMRN-Persian-L1` has a prior actual HTTP 200 Persian combo receipt; **do not change or delete**.
- Gemma 4 26B gateway text+inline image passed; Gemma 4 31B failed with Google and gateway HTTP 500 later; 31B must not be auto-admitted from older smoke-success summaries.
- CAP-006 read-only bounded document search had a user-run Windows technical PASS on two allowed files with source lines and hashes, **but is not a daily chat product**.
- Work examined `session.py`, `windows_guard.py`, `cap006_adapter.py`; reported RAM-only session `_seen` (not durable task state), an intentionally blocking `require_verified_read()`, and a not-yet-proven end-to-end authorized file-to-chat tool bridge. Exact paths unresolved in the coordinator's initial attempted fetches; use Work's supplied blob identifiers pending accurate path lookup:
  - `session.py`: `2f04a2c5b7ab650211d85577c56faebfb87c0707`
  - `windows_guard.py`: `2ad992932489b1f12417c9e5e5eb4a1d2c40d12a`
  - `cap006_adapter.py`: `c4c775428e4715b9f4c220add7ebdcd2405019b0`
- D-005 global language/runtime/database/agent-host decision remains **NOT DECIDED**. Existing D-009 thin contract + no-Agent first, D-013 bounded CAP-006 real pass, D-014 chat-first, D-015 dual-surfaces/shared trusted core G0 remain scoped.

**Critical gap:** prove one usable chain `Persian chat → authorized tool → result with sources → durable task state/reopen`, *before* adding many agents, service layers or OmniRoute Combos.

## 4 — Architecture candidates (not mutually exclusive)

| Candidate | Advantage | Failure/complexity | Fit now |
|---|---|---|---|
| A. Minimal Python core + SQLite/FTS + typed capabilities | Lightweight, deterministic, low dependency, reversible | Must implement small UI/task/recovery/policy correctly | **Best baseline** |
| B. Modular monolith with optional Agno/AgentOS agent adapter | Scalable logical roles and reusable contracts in one deployment | Framework defaults/DB/telemetry/security require explicit validation | **Evolution target, conditional** |
| C. Durable workflow first (DBOS/Dagu etc.) | Retry, waits, restart/recovery | Another owner of state/replay/operation contracts | When real long-running work requires it |
| D. Knowledge-first | Good for search-centric products | Does not solve authorization/task execution | Bounded capability only |
| E. Distributed services/Temporal/broker | Separate workers/always-on scale | Operations/network/migration overhead | Not yet justified |
| F. .NET/Go/Node alternative | Better fit to specific packaging/runtime constraints possible | Toolchain/maintenance trade-offs | Fair alternatives; no benchmark winner |
| G. No-Agent baseline | Predictable, low model usage | Limited dynamic exploration | **Required comparison baseline** |

Conditional preference: **build A with good seams that allow B**, not A as an irrevocable technology commitment. Do not install a second workflow engine if the existing selected runtime covers measured needs.

## 5 — Evaluated components: Build versus framework versus workflow

- **Python stdlib + SQLite:** simple control + one-step or short deterministic workflow; implement policy, lifecycle, recovery and UI for required use only.
- **Agno/AgentOS:** documented agent/team/workflow/API/persistence candidate; existing installed environment is useful for comparison but not proof of production security or runtime integration.
- **Pydantic AI:** lighter typed-agent candidate; full system state must be owned outside SDK.
- **LangGraph:** checkpoint/thread state distinct from cross-thread store; `InMemory` does not provide restart durability.
- **DBOS:** durability/checkpoints; SQLite/Postgres configurations/semantics must be verified for the real workload.
- **Dagu:** script/runbook orchestration with built-in UI, documented Windows use; licensing tiers must be checked.
- **Microsoft Agent Framework:** .NET/Python comparator; no global selection.
- **Temporal:** more operations for larger service topology; no current need demonstrated.
- **Graphiti:** knowledge graph with graph DB/model/embedder dependencies; defer until real relational recall tests.
- **Edda:** independent discovery lead; official README suggests SQLite single-process, multi-process needs another DB; investigation incomplete (`LEAD ONLY`).
- **.NET Generic Host:** Windows service lifecycle/logging without agent framework, candidate if real packaging/supervision need.
- **OmniRoute:** inference routing; not canonical task store, not autonomous planner, and no free quota of its own.

**Reported Agno 3.1.10 pinned-source research** at `04330571dc84b15d03dd3c2b598f8f01d4a239e0`: in the inspected AgentOS constructor defaults reportedly `authorization=False`, `user_isolation=False`, `tracing=False`, `auto_provision_dbs=True`, `telemetry=True`, `scheduler=False`, `queue=None`. These are **Work-reported pinned-source findings requiring same-version validation before execution**. Do not start default AgentOS with silent schema provisioning or telemetry: explicit configuration and user approval required.

Language trade-off: Python good for initial document/AI integration; .NET suited Windows lifecycle/UI; Node for web/network frontend/backend but inspect exact installed version's SQLite maturity; Go for service/CLI distribution. No independently measured RAM superiority asserted.

## 6 — State, knowledge, internal API and agent collaboration

**Logical responsibilities; not instruction to create eight physical tables:** `Task`, `Step/Attempt`, `Message`, `Evidence/Artifact reference`, `Conversation`, `Approval`, `Model usage`, `Memory item`. First vertical can use a few simple SQLite tables/payloads, with explicit schema review before any migration.

Task states: `RECEIVED → VALIDATED → READY → RUNNING → SUCCEEDED`, with `NEEDS_CLARIFICATION`, `WAITING_APPROVAL`, `RETRY_WAIT`, `FAILED`, `CANCELLED`, `UNKNOWN_OUTCOME` as relevant. One idempotency identity per intended action; a repeated identical payload is not necessarily the same user-intended operation.

**Authority:** Notion = cross-project governance/architecture decisions; GitHub = code/project evidence; selected DB = runtime state; source documents remain source truth. Local search/embedding caches are rebuildable projections, not silent duplicate authorities. Separate raw evidence from derived model summaries. Namespace/owner/scope and provenance mandatory.

**Initial knowledge**: two explicitly allowed non-sensitive text files with file/revision/hash/line references; preserve originals; optionally normalize Persian ی/ي، ک/ك, ZWNJ for FTS5 index; test actual queries; embedding/knowledge graph when lexical recall demonstrably fails. Do not mix different embedding vector spaces solely due to equal dimension.

**Internal communications evolution:** typed functions now; JSON stdin/stdout when subprocess boundary justified; REST/OpenAPI if lightweight web UI or separate process; MCP when a real interoperable tool-host consumer exists; A2A when truly independent heterogeneous agents need it; SSE/WebSocket/event bus only for concrete streaming/concurrency requirements.

Proposed future contract only (NOT built): `POST /v1/tasks`, `GET /v1/tasks/{id}`, `GET /v1/tasks/{id}/events`, `POST /v1/tasks/{id}/reviews`, `POST /v1/tasks/{id}/cancel`, `GET /v1/capabilities`. Envelope: `task_id`, `parent_task_id`, `correlation_id`, trusted `actor_id`, `capability_id`, `schema_version`, `input_refs`, deadline, attempt, idempotency key. Model-supplied claims of actor identity, tool permission or approval are not authority.

Second role: A creates scoped draft artifact; core authorizes B's review subtask; B reads only evidence/draft; returns *new* review artifact; A or coordinator reconciles; bound recursion/turns/time/tokens. **Two logical roles can call one model sequentially.** Same model doing both is not intrinsically independent verification; compare against one-role baseline.

## 7 — First real vertical and phase plan

**Vertical V0:** Persian prompt about 1–2 authorized non-sensitive DJMRN files → a task ID → allowed read/search (reuse existing CAP-006 when safe) → source/line/hash answer → persisted result → reopen after app restart. Initial deterministic path does **not** call an LLM; then add one optional OmniRoute summarizer and an optional scoped second reviewer.

| Gate | Minimal work | Proof / exit | Not yet required |
|---|---|---|---|
| P0 reuse/approval | Locate exact existing CAP-006 contracts/HOLD; enumerate 2 allowed test docs; define one UX action, policy & baseline | Bounded acceptance case + validated reuse design | New framework/DB installation |
| P1 deterministic core | Task handler, narrow capability, minimal local SQLite state; no unsafe bypass of `require_verified_read` | Real two-file query, provenance and persistent task | Agent/LLM |
| P2 recovery | Close/reopen; duplicate request; disk/tool failures; no blind replay | Same task/result found; interrupted attempt has explicit state | Broker/queue engine |
| P3 chat-first UI | Minimal Persian text chat using task handler; no daily PowerShell | `message → result + sources + task ID` in UI | Heavy frontend |
| P4 inference seam | Opt-in one admitted OmniRoute route via model adapter; model receives scoped/sanitized context | Measured live request; 429, timeout, cost/error policies | Several model Combos |
| P5 review role | A analysis + B review on same stored task; optional Agno adapter A/B tested | Artifact chain and measured quality vs simpler baseline | Resident multi-agent swarm |
| P6 economically useful workflow | Approved file/batch of work opportunities → parse/dedupe/rank/draft | Evidence-backed useful draft, no unsanctioned send | Browser/email production write |
| P7 optional durable engine | DBOS/Dagu/AgentOS mechanisms only if wait/restart complex | Reliable replay with tested semantics | Additional workflow layer by default |
| P8 conditional hybrid | Only jobs requiring always-on server | Official free/region/privacy and explicit deployment approval | Cloud always-on by default |

Phase order is **proposed**, not approved deployment. A minimal local file/folder for product code belongs inside the existing repository and may use existing CAP-006 modules; no second repo, new canonical architecture truth, or grand platform refactor.

**Acceptance failure modes:** unknown input must stop or ask; a third file must be denied; modified file changes revision/invalidates evidence; model outage must not erase deterministic result; task survives restart; no accidental external writes; duplicate handling is explicit; first useful user path avoids PowerShell. Measure local RAM/latency with Chrome open/closed and OmniRoute active; do not present Work's RAM targets as observed.

## 8 — Hardware, cost and operational constraints

User-reported hardware: Windows 11 Pro, Ryzen 5 3500U, 8 GiB RAM. Older Windows snapshot ~5.88 GiB usable; Chrome closed may release ~2–3 GiB (user estimate). Not a benchmark for the new combined system. Work supplied **design test targets only**, not measurements: baseline A idle <~200 MiB, peak core <~400 MiB; modular B idle <~350 MiB, peak core <~600 MiB, excluding OS/Chrome/OmniRoute/model/browser. Overages above goals require diagnosis, not automatic reject.

Free-first: local deterministic Python/SQLite avoids paid inference; software licenses do **not** guarantee third-party API free tier; provider account/eligibility/quota/project-shared limits, remaining credit and overage must be verified separately. No unauthorized payment, paid fallback or cloud data export. Local tasks stop when laptop is off; an approved, independently online remote runtime would be needed for offline continuation.

## 9 — Failure/security/reversibility checklist

Test duplicate command and idempotency; crash after an external side effect (`UNKNOWN_OUTCOME` and reconcile before retry); disk-full/WAL backup/restore; file symlink/path races; injected instructions inside retrieved text; invalid LLM JSON; 429/500 and bounded retry; A→B delegation loops; stale task leases; telemetry secret leakage; two canonical state stores; code+DB migration rollback.

Permissions are enforced at the tool executor, **not** inside a prompt. Localhost alone is not authentication; read-only narrow file root first, no arbitrary shell, no external send, no unapproved Gmail/browser account. Gateway bearer, management token, upstream key separate. MCP/A2A compatibility is not a security boundary. Start with structured task logs and correlation IDs; later evaluate OpenTelemetry only with a measured need.

## 10 — Research gaps and evidence receipts (as reported by Work)

**APPLIED_LIBRARY_READ_RECEIPT:** `READ—TARGETED / PARTIAL ARCHIVE COVERAGE`; Operating Memory (last edited 25 Oct), Tool Governance (17 Oct), Applied Index (title v0.48 but appendix v0.42 inconsistency), Applied Mission (20 Oct), General Discovery054 / CURRENT v52 (18 Oct), Design015, Design018, Intelligence Fabric proposal; NOT a full read of every branch/archival line. Several Notion pages `verification=unverified`.

**PROJECT_REPOSITORY_READ_RECEIPT:** Work reported repo `main` `44e955799f81de60779752f67b0b0418d9bfa544`; project and architecture file blob SHAs:
- `PROJECT-RULES.md`: `acff165a37ce7176e6973bc506fe6915e5cc5092`
- `07-operations-and-continuity/CURRENT-STATUS.md`: `84cd62713bf6e2ba64230ecf8dca581a65a8742a`
- `02-project-management/MASTER-SYSTEM-ROADMAP-20261022.md`: `1dc1909d102f1cd8691ea79d712a97bd9549edc3`
- `03-architecture-and-tools/ARCHITECTURE-RESEARCH-SYNTHESIS-20261022.md`: `989ff696021df3d6606a95371aa6fc68401f778b`
- `04-work-research-bridge/README.md`: `fa5fdf56ad50714e6e4479fe5111ec6f1036be27`
- Decision/Task/Test/KB/Source registers also Work-reported read; source code `session.py`, `windows_guard.py`, `cap006_adapter.py` with the three blobs above.
- Work reported **no authorized exact WQ/WA pair for this mission**; its output was chat-only, `write=NONE; commit=NONE`. This is the subsequent user-authorized archival, **not a fabricated Work WA write**.

**INDEPENDENT_SEARCH_RECEIPT:** Work reported targeted official/primary-source analysis of agent/workflow distinctions, embedded SQLite durability, Dagu, DBOS, .NET/Go/Node alternatives, MCP, A2A, FTS5/WAL, Google shared quotas, Agno pinned tag, OmniRoute 3.8.52 and negative cases. Work did not include full URLs for every external source in its pasted bibliographic table; **DO NOT fake links or treat summaries as independent official verification**. Work marked `Restate` doc URL, `Letta` memory URL and LM Studio TTL page `NOT_READ` (timeout/unavailable); account entitlement, exact current software RAM, local integration benchmarks `NOT_RUN`.

**MERGED_CANDIDATE_MATRIX condensed:** Both known/proposed: Python+SQLite, modular monolith, Agno/AgentOS, LangGraph, DBOS, Dagu, OmniRoute, .NET; existing enrichment: Pydantic AI, Node, Go, Microsoft Agent Framework; later-only: Graphiti, Temporal; new external limited lead: Edda; no-new-tool is a legitimate option. `LiteLLM` is alternative gateway, not justification to replace working OmniRoute.

## 11 — Next decision, conditional and reversible

**Recommendation for review, not architecture finalization:** keep earlier DJMRN hybrid design as target; adopt **Architecture A as first bounded slice of modular Architecture B** if the user separately authorizes implementation after ready-platform research. Core tasks and authoritative state stay framework-neutral. Demonstrate CAP-006+task persistence+Persian chat first; integrate OmniRoute as adapter next; compare Agno to no-Agent baseline using identical work; attach a second role only for measured benefit. Decide workflow/durable engine only when real failure cases show need.

**Second independent research still pending:** `DJMRN-READY-INTELLIGENCE-PLATFORM-DISCOVERY-002` (ready-made, open-source, low-code and composable alternatives). Findings may supersede *recommendations*, but must **not erase** the preserved hybrid architecture or Work 001 research history.

**Changes made by this archival:** GitHub documentation only. **No** user Windows process, credentials, OmniRoute Combo/group, agent, database/schema, deploy, external API, paid usage or GitHub code was changed.
