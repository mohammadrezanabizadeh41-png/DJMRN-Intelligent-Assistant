# DJMRN — Foundational Architecture Alternatives for a Shared Intelligent Assistant Ecosystem

**Research ID:** DJMRN-FOUNDATIONAL-ARCHITECTURE-COMPARISON-003  
**Research date:** 2026-10-27 (UTC); user explicitly requested independent, broad architectural research and persistence in the existing main project's research archive.  
**Status:** INDEPENDENT SOURCE RESEARCH + COMPARATIVE PROPOSAL; **NOT APPROVED / NOT DEPLOYED / WINDOWS TEST PENDING / NO BENCHMARK**.  
**Repository authority:** mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant (main); research folder is 03-architecture-and-tools; do not write to the separate Applied Research Bridge.  
**Privacy:** Repo metadata last read showed PUBLIC visibility; no credentials/private payloads/data were saved.  
**Linked reports:** [First Work foundational architecture](DJMRN-CORE-ARCHITECTURE-RESEARCH-001-20261027.md); [Second Work ready-made discovery](DJMRN-READY-INTELLIGENCE-PLATFORM-DISCOVERY-002-20261027.md); [2022 master system roadmap](../02-project-management/MASTER-SYSTEM-ROADMAP-20261022.md); [Current/earlier hybrid design](../07-operations-and-continuity/CURRENT-STATUS.md); D-019 in [Decision Register](../02-project-management/DECISION-REGISTER.md).

## 0. Exact research question, independent of model grouping

What **professional architecture and first implementable foundation** best accommodates a local-first Persian-chat assistant, *one trusted center*, interoperating specialized personas/assistants that can converse/delegate/review each other's tasks, internal APIs, reusable Python and other-language workers, shared provenance-aware knowledge, recoverable business task state, free-first cloud model inference via OmniRoute, user approvals and extensions to future local/cloud/on-demand workloads on a **Windows 11 Ryzen 5 3500U laptop with 8 GB physical RAM**?

This question is DISTINCT from model group naming and primary/fallback LLM selection. The model gateway is just one infrastructure port. Do not assume the existing installed Agno must win. Preserve the Oct25/26 HYBRID architecture, which defines deterministic tools and workflows, scoped memory/approvals, Agent runtime candidates, shared workers and on-demand inference. Its actual deployment remains unproven. Preserve the 2026-10-27 Work Research 001 and 002 as evidence, not final decisions.

## 1. Method and levels of proof

Three bounded streams:
1. **Known project:** Actual repository rules, CURRENT, D-019, Work001, Work002, earlier architecture, prior CAP-006 / OmniRoute / Agno receipts as summarized therein. Prior user-generated Work-source version/issue claims are labeled **WO2**, not a new live independent audit.
2. **Independent live search:** Search problem-first for control plane patterns, event-driven architecture, actor model, durable workflows, agent group discussions, handoffs, capability/memory protocols, ports & adapters and real ready runtimes. Read official Microsoft/Azure/MAF/Orleans, Dapr, Agno, LangGraph, A2A, MCP, DBOS/Pydantic, Mastra and iii sources. These official vendor docs support described *capabilities/patterns*, not local performance or security guarantees.
3. **Actual code identity and license snapshots via GitHub connector:** Verified current repo metadata/fetched README or licenses for iii-hq/iii, agno-agi/agno, microsoft/agent-framework and mastra-ai/mastra. Particularly noteworthy: repository lookup **MotiaDev/motia resolves to iii-hq/iii** in this current lookup; do NOT conflate older Motia Step docs with currently installed/configured iii without testing and migration/version checks.

Evidence shorthand:
- **EXT-DOC:** live official external technical documentation or specification read on 2026-10-27.
- **EXT-CODE:** source file text or GitHub repo metadata independently fetched on 2026-10-27 (but no local execution).
- **WO1/WO2:** user's supplied Work research, valuable but its vendor audits not independently fully replicated.
- **INFERENCE:** engineering synthesis and conditional preference, not an experimentally proven architecture.

Negative evidence: Exa Search app returned **HTTP 402 credits exhausted** during the query pass; no Exa results, no paid top-up, and no claims based on it. Independent web/official-source access and GitHub connectors were successful and are reported separately. Official search coverage is targeted, not a comprehensive audit of every existing project, license or CVE. No candidate was installed/executed or benchmarked on the laptop.

## 2. Fundamental conceptual architecture: stable seams, not fixed vendor lineup

**Professional architecture must separate at least seven *logical* boundaries. These are NOT seven mandatory processes/services/DBs.**

1. **Conversation & user surfaces (inbound ports):** native/light web UI now, optional ChatGPT connector/mobile later. UI does not own canonical state or tool permissions.
2. **Trusted Task/Policy Control:** identity, accepted task, state machine, consent, budget, capability allowlist, routing to deterministic versus inference versus collaborative paths; this is the **stable DJMRN integration seam**.
3. **Operational durability:** one authoritative task/correlation/action/outcome record and transactional event/outbox where required; conversation session state may be owned by an agent runtime separately only with explicit reference/mapping. Avoid duplicate canonical owners for one business state.
4. **Worker & Tool Fabric:** typed deterministic Python/Go/.NET/Node functions for files, documents, web APIs, safe scraping, parsing, schedules, validation, receipts. Not all workers are agents; by default one sequential permitted executor. Any internal RPC is optional until a process boundary appears.
5. **Agent/Persona Runtime:** intelligent analysis, delegation, review, controlled multi-turn collaboration, memory context, role-specific scopes; reuse an existing framework. Persona is logical identity/prompt/tools/permissions, not necessarily a continuously running process or separately loaded model.
6. **Inference Gateway:** OmniRoute/OpenAI-compatible adapter with explicit free-only/approved-model quota admission, bounded retries and fallback. This is NOT the task authority. Separate management token, gateway token and upstream keys; no secrets in code/repos.
7. **Evidence/Knowledge:** source documents (GitHub/Notion/file authorities) vs derived indexes (FTS/vector) vs scoped agent/session memory vs approved project decisions; provenance, hash, time, revision, access scope and reclaimable indexes.

**What becomes “intelligent”?** A combination of learned reasoning in *selective* model calls, deterministic routing/business policy, durable state, verified evidence and controlled cooperative agents. A permanent live LLM daemon is not the center.

## 3. Architecture paradigms compared — alternatives to the previous Agno-centric draft

| ID | Architecture | Core pattern / independent source | Strongest potential benefit | Weakness / operational cost | DJMRN current viability |
|---|---|---|---|---|---|
| A | **Modular monolith with ports/adapters and plugin-bound agent runtime** | One trusted process with Task/Policy/Tool/Evidence/Agent interfaces; incremental service extraction per Microsoft architecture guidance | Stable API ownership and low process/RAM overhead; agents/worker engines replaceable | DJMRN implements small contracts & task durability; discipline required | **Leading structural pattern (INFERENCE), framework neutral** |
| B | **Agent-runtime-centric Agno/AgentOS** | Agents/Teams/Workflows + FastAPI/SSE/sessions/SQLite/tracing/approvals; Agno docs and source | Reduces code for agents, team conversations, server/API; already partially installed | Session != all task state; GUI hosted vs runtime distinction; config security, telemetry, fallback; overdependence on version | **Leading trial for runtime adapter, not automatic owner of DJMRN data** |
| C | **Durable-workflow-first Python (DBOS + typed agent)** | DBOS steps/checkpointing; Pydantic AI+DBOS officially integrated; agent calls are durable steps | Strong resume/retry/idempotency vocabulary, useful when human approval and long operations matter; minimal no-LLM tasks | UI/group-chat/team coordination must be composed; replay/serialization/upgrade/retry pitfalls | **Strong independent alternative** if state recovery outranks prebuilt teams |
| D | **Graph/workflow-first with LangGraph** | Explicit state graph, checkpointer per thread, store across threads; official docs | Explicit routing, branching, state/time-travel, finer orchestration control | Chat product/API, permissions and operational authoritative state still required; graph evolution and checkpoint semantics | **Good if complex dynamic control graph proven** |
| E | **Microsoft Agent Framework multi-agent application** | .NET/Python source with sequential, parallel, handoff, group chat, magentic plus workflow/HITL; official docs | **Directly addresses user’s persona-to-persona conversation** without inventing own group manager; alternative to Agno in Python or .NET | Need application backend/storage/config/UI; released vs experimental feature maturity pin/test | **Primary fair challenger to Agno** for bounded group-chat/HITL |
| F | **Event-driven worker/trigger/function registry (iii, formerly Motia lead)** | Central engine with dynamic worker registration, function IDs, HTTP/queue/cron/state/stream triggers; Python/TypeScript/Go/Rust SDKs | Especially close to **shared internal API for heterogeneous Python workers**, dynamic capability catalog and observed invocation; agent runtime can be worker | iii engine **Elastic License 2.0**, not permissive open source; runtime/migration, Windows packaging, persistent task security and RAM untested; still need agent intelligence/persona | **New serious conditional infrastructure candidate, not day-one winner** |
| G | **TypeScript unified AI backend (Mastra)** | Server, agents, workflows, memory, harness, subagents, tool connectors; docs/source | Attractive if one Node-centered stack/API/UI integration valued, alongside Python workers by RPC | Adds JS/Node maintenance; some enterprise-only parts; exact OmniRoute, Windows resources and multi-agent behavior untested | **New alternate integrated stack; compare selectively** |
| H | **Actor/virtual-actor model (Orleans or Dapr Actors)** | State-encapsulated, addressable actors exchange asynchronous messages; Orleans Grains and Dapr actors | Scales independent identities/mailboxes across processes/hosts later; strong conceptual fit to persona communities | Actor != language reasoning agent, need separate agent logic, persistence provider and host complexity; Dapr sidecars/Orleans silo increase ops | **Useful later architecture boundary, not forced runtime now** |
| I | **Dapr multi-service/workflow infrastructure** | Durable workflows, service invocation, state, pub/sub, ACL and independent service workers | Strong future multi-language service fabric, retries, scheduling, service auth and resilience | Additional sidecar and state component; deployment complexity; overkill for two files and one laptop | **Later if actual independent host/process fan-out** |
| J | **UI-centric Langflow/Dify** | Visual flow editor and API, workflow nodes/KB | Quick visual experience or hand-editable pipelines | Graph flow != general task authority; CPU/RAM/license/security and extension limits | **Comparator for UI, not mandatory core** |
| K | **Knowledge/persona-memory-first (Letta Code/Mem0/Graphiti)** | Long-lived persona memory/retrieval | Strong when knowledge continuity is principal problem | Does not alone perform lifecycle/permissions/dispatch; possible duplicate knowledge authority | **Optional specialized layer after retrieval evaluation** |
| L | **Microservices/Event Bus first** | Independent services, broker, pub/sub/outbox, distributed tracing; Azure/Dapr | High scalability/independent deployments | At 8GB local first, network, retries, distributed consistency, high integration count before useful task | **Defer until explicit demand** |

These options are not necessarily mutually exclusive: **A is a structural style**, B/E are candidate inference/agent runtimes, C/D are execution/orchestration models, F/H/I are service-fabric topologies. The wrong question is “which one replaces all others?” The right question is “which owns each specific responsibility, and when is an extra runtime warranted?”

### New external findings which Work 02 did not put in its finalist matrix

**iii identity / license (EXT-CODE):**
- lookup for MotiaDev/motia returned canonical **iii-hq/iii**, branch main, not archived.
- README Git blob **0de4c9c716bceaa88a61148f212f8cfd9d7d3557**, current repo https://github.com/iii-hq/iii .
- iii primitive: Workers register named Functions and Triggers; reusable interfaces can be HTTP, queue, cron, state, streams; Python/Node/Rust/Go SDKs; dynamic catalog/discovery/tracing. This **could** directly cover DJMRN shared tools/worker registry.
- engine license at engine/LICENSE, Git blob **23b3a1fadcaa5d29bd09158e08b31e181a780ce2**, is **Elastic License 2.0**, which restricts providing the software to third parties as a hosted/managed service exposing substantial features; SDK/docs are Apache-2.0. This is source-available, **not blanket permissive OSS**; the service-business scenario requires careful legal assessment. No private machine deployment performed, no assumed direct backward compatibility with Motia-era docs.

**Mastra alternate (EXT-CODE + DOC):**
- https://github.com/mastra-ai/mastra, main; fetched LICENSE.md blob **e1b6e4b6455a882dbbf66ee0b13101ec584d5e63**; most code Apache-2.0, specific ee/ directories subject to another license. Do not label all UI/auth/editor enterprise functionality free.
- Official https://mastra.ai/docs/workflows/overview describes typed steps, built-in workflow engine, suspend/resume and optional runner; product https://mastra.ai/ lists agents, harness, memory, server. Windows/RAM and direct OmniRoute adapter not verified.

**Microsoft Agent Framework alternative (EXT-CODE+DOC):**
- https://github.com/microsoft/agent-framework , README Git blob **bc9a8b080aeca9b3c5a25f216f8f96f61ffc012c**; public code + Python/.NET source, workflows, checkpoint and DevUI patterns. Official https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/ lists sequential/concurrent/handoff/group-chat/magentic with HITL.
- Unlike a basic agent SDK, group-chat orchestrator chooses speaker turns and synchronizes history across *separate* agent sessions. See https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/group-chat . This is immediately relevant to user-requested *personality-based dialogue*. Whether pinned release is stable/fully local/free/efficient must be tested.

**Agno source current and prior pinned-source gap:**
- Fetched https://github.com/agno-agi/agno README at blob **0524dec2b4ffe026c353fcd11d24a86e98859ab7** (current main, NOT necessarily same as installed 3.1.10).
- https://docs.agno.com/features/runtime describes AgentOS API, durable sessions, scheduling and observability, enable auth by explicit configuration.
- https://docs.agno.com/agent-os/studio/teams documents modes Coordinate/Route/Broadcast/Tasks and agent/team orchestration. Team functionality may address conversation/handoff; exact mode semantics must be pin-checked before adoption.
- Prior 3.1.10 Work001 reported authorization False, user isolation False, auto DB provision True, telemetry True. Never assume current docs and older version defaults coincide without local inspect.

**Pydantic AI + DBOS combination:**
- https://pydantic.dev/docs/ai/capabilities/durable_execution/dbos/ documents durable model calls and steps, replay, SQLite/Postgres; custom tools may need explicit wrapping, and cumulative client+transport+workflow retries can multiply API spending. This is a first-class **workflow-first alternative** that did not lead Work 02's rankings.

**Non-LLM actor pattern:**
- https://learn.microsoft.com/en-us/dotnet/orleans/overview virtual Actor/Grain identity, messages and state, Windows/.NET possible. Orleans is a framework, not a ready GUI or personal assistant product; one-machine hosting possible per Microsoft.
- https://docs.dapr.io/developing-applications/building-blocks/actors/actors-overview/ explains stateful actors and one-message-at-a-time behavior; https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/ describes durable steps/HTTP+gRPC orchestration with sidecar. Both can later host independent persona/worker processes, but no additional model intelligence automatically.

## 4. Real persona dialogue vs task handoff vs worker API: three orthogonal patterns

**A. Deterministic tool/workflow:** A receives request, authorized code finds file metadata, task status updated, final result. ZERO LLM. No second agent needed.

**B. Delegation/handoff:** Agent A hands a *bounded task* to role B, B returns sourced artifact, A resumes. Requires structured task IDs, role-specific capability permissions, parent/deadline/status/result refs; may reuse one model serially.

**C. True controlled group conversation:** Coordinator defines a bounded dialogue thread; A proposes analysis, B critiques, coordinator selects next speaker, passes only permitted context, validates stop criterion/turn/time/model budget and consolidates to a task artifact. A conversation transcript isn't automatically operational truth. Microsoft explicitly documents group-chat and maker-checker patterns; its docs caution loops and suggest small groups: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns/ ; https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/group-chat .
   
An optional “personality” is a versioned **Role Profile**: role_id, function/mission, system prompt/instructions, allowed tools/data, model capability family, context selection, retention, escalation, max turns/tokens, persona voice/style, quality rubric. It is **not** authentication, a model partition, a new always-running process, or proof of different expert independence.

For a first conversational collaboration, recommend an **A→B→A maker-checker** task chain, with a 2–3 turn managed dialogue only if maker-checker quality is insufficient. Later optional group chat; do not activate free-for-all agent conversations by default. Each model call subject to the same free-only quota admission controls.

## 5. Standards and future-proof interoperability

| Interface | Actual responsibility | Entry gate |
|---|---|---|
| Typed Python (or .NET) internal call | Same-process CAP-006/tools, role handlers, policy, storage interfaces | Day one |
| Local HTTP REST + OpenAPI | Local chat UI, future separate tool-host clients and external app integration; contract tests | First local chat boundary |
| JSON stdin/stdout | Isolated process worker with exact input/output | When process separation required |
| SSE | UI progress streaming | When beneficial |
| MCP (host-client-server) | Exposes approved tools/resources to compatible agent hosts | Consumer/capability/auth exists; not itself a task bus. Official: https://modelcontextprotocol.io/docs/learn/architecture |
| A2A (Agent Card / Task / Message / Artifact) | Interoperability between *independent* agent services/runtimes | Cross-framework/host requirement confirmed. Official: https://a2a-protocol.org/latest/specification/ |
| Event bus / outbox | Durable async event delivery, fanout, disconnected workers | Measured independent consumer/recovery case; avoid queue plus model-run retry loops. Microsoft: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven ; https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs |
| Dedicated actor runtime (Orleans, Dapr) | Stateful identities/mailboxes at distribution/concurrency scale | Real multi-process/host service need |

**Note:** MCP/Agent2Agent do not replace access policy or business persistence, and a tool's untrusted data must not grant authority. Do not build a custom MCP server just to simulate two local functions.

## 6. Logical domain contracts and data ownership (vendor-neutral)

**Proposed minimal canonical entities, NOT required one-per-table:** 
- Request (human UI input, caller, idempotency token, intent),
- Task (task_id, owner, status, correlation, deadlines, authorized refs, result),
- Step/Attempt (one step's checkpoint/trace/retry),
- Capability (name, input/output schema, side effects, authorization scope, worker binding),
- Role Profile (persona name, model family, tools, scope, budget),
- Message/Exchange (sender, recipient, task/correlation reference, visible fragments, reply-to),
- Evidence/Artifact (source URI or file_id, sha256/revision/line, time, sensitivity, derived conclusion flag),
- Approval (actor, exact payload hash, target, expiry, receipt),
- Model Usage (actual provider/project/model, token/quota/cost known vs unknown).

**State machine:** RECEIVED → VALIDATED → READY → RUNNING → SUCCEEDED with FAILED, DENIED, NEEDS_CLARIFICATION, WAITING_APPROVAL, RETRY_WAIT, CANCELLED, UNKNOWN_OUTCOME as applicable. A task is finished only when result/artifact/event commit is durable, not when UI shows text. External side effects require idempotency or reconciliation before retry.

**Single business task-state authority:** choose either a thin DJMRN state machine stored in its own reviewed schema, **or** delegated authoritative orchestration to a framework's DBOS/AgentOS workflow record through an adapter. Never maintain two independent writers each saying "this exact task succeeded." If AgentOS separately stores conversation/session state, map to task references; that's a different fact owner, not automatically a conflict. GitHub project docs, Notion research source and runtime DB remain distinct authorities.

Knowledge: source originals remain in approved files/GitHub/Notion; the application stores source IDs, revisions and search projections. CAP-006 / simple lexical FTS for initial tests; Persian normalization, exact source line/hash; vector search added for measured recall misses, not default.

## 7. Reference layout — framework-neutral architecturally, minimal runtime physically

    Persian UI / future second chat surfaces
                      |
                 Local HTTP API
                      |
              DJMRN Trusted Seam
     Request | Task | Policy | Evidence | Approval
                 |             |
           Capability Router  Scoped Knowledge
           /       |        \
    Deterministic   |     Role Engine Port
    Python Tools    |       |
       CAP-006      |    Agno / MAF / Pydantic / LangGraph
                    |       |
                   Model Adapter
                        |
                 OmniRoute gateway
                      |
                  Free model APIs

         One authoritative durable Task/Artifact store
         Scoped conversation/agent memory where justified
         Auditable exchanges between role profiles

**Physical P0 deployment:** may be one light process plus existing OmniRoute and a small DB file. The role engine doesn't need to be live if executing pure deterministic tasks. No message broker or network between roles. Optional separate orchestration/worker processes are future adapters; the architecture can expose an internal API before needing separate hosts.

## 8. Evaluation matrix for choosing first runtime without anchoring bias

Score real equal-workload PoCs qualitatively and measure actual metrics before selection:

| Criterion | Agno/AgentOS + thin seam | Microsoft Agent Framework + thin seam | Pydantic AI + DBOS + thin seam | iii worker hub + agent runtime | Modular direct Python |
|---|---|---|---|---|---|
| Agent/team dialogue supported in vendor docs | Yes, teams/modes; actual semantics verify | Yes, explicit group chat/handoff | Compose manually using role calls | Only by connected agent worker | Build bounded coordinator yourself |
| Ready local API | AgentOS provides API | Host/API glue required | API glue required | Engine provides function/trigger surface | API glue required |
| Non-LLM deterministic Python tools | Yes via tools | Yes via functions/executors | Yes via steps | Yes via Python worker | Yes directly |
| Restart/durable task ownership | Agent DB, exact semantics test | Checkpoints, DB contract test | DBOS durability, semantics test | Function delivery/storage semantics test | Implement/reuse minimal transactional task |
| Existing Windows install | Agno imports PASS historically | NOT TESTED | NOT TESTED | NOT TESTED | Python + CAP-006 partially passed |
| License / future services | Apache SDK; Control Plane terms separate | Repo open/MIT as reported in source | Pydantic/DBOS license recheck at activation | **ELv2 engine restriction** | Own code + dependencies |
| Real RAM/performance on this laptop | NOT MEASURED | NOT MEASURED | NOT MEASURED | NOT MEASURED | NOT MEASURED |
| Real OmniRoute inference/tool-call | NOT END-TO-END VERIFIED | NOT TESTED | NOT TESTED | NOT TESTED | Existing direct combo HTTP200 only |
| Custom governance/evidence layer | YES | YES | YES | YES | YES |
| Lock-in concern | Medium if internal schema leaks | Workflow adapter semantics | Durable step ID/replay compatibility | Worker protocol + licensing | Maintain more own code |

**No numeric winner.** At this evidence level, assigning scores like “Agno 9/10” would fabricate measurements. An equal-workload comparison should include **A: no-Agent baseline**, **B: Agno**, **E: MAF** (explicit group chat), and **C: DBOS/Pydantic** if durable waits are necessary. iii can be a separate third-phase fabric benchmark if cross-language worker registry truly is urgent and licensing acceptable.

## 9. Falsifiable first-milestone and gate sequence

### Gate G0 — architecture and permission contract (read-only design)
- Locate accurate CAP-006 code paths; verify existing Windows HOLD and file reader contract, *never bypass* reported require_verified_read().
- Lock one user action: Persian request to compare/search two individually approved nonsensitive markdown files, no third file/no untrusted shell/network.
- Define task/provenance schema **logical contract only**; decide ONE operational state owner for a given task.
- Define fake/real no-LLM baseline and a model-adapter independent interface. Record Windows resource baseline.
- **PASS:** no ambiguous state ownership, no unauthorized executor edge, independent persona/tool contracts visible.

### Gate G1 — minimal deterministic vertical
- Bounded task ID persisted, check allowlist, execute previously proved CAP-006 function using exact verified file reference, return line+hash, save evidence.
- Invalid or third file -> DENIED, not fallback to general read. Reopen app -> task and artifact still available. Input duplicate semantics checked. No model calls.
- **PASS:** readback of evidence across restart, clear error/recovery; source docs unchanged.

### Gate G2 — model adapter + runtime comparison
- One previously admitted free route through OmniRoute from Agno (original PowerShell quoting error must be bypassed by correct Python script, not by claiming pre-existing success). Compare identical task with no-Agent handler and at least one serious alternative only if warranted.
- Test model UTF-8, tool call, structured output, timeout 429/500, cost admission; pin exact runtime version/config/auth/telemetry/DB behavior. Do not select Gemma 4 31B currently upstream HTTP500.
- **PASS:** valid response with source IDs, no paid fallback, no secret leaks, repeatable startup/RAM within measured device headroom.

### Gate G3 — persona-to-persona exchange
- Distinct role profile Analyst A and Reviewer B, one shared model sequential if suitable. Create child task with parent/correlation refs; each receives only permitted context; create new review artifact, don't overwrite.
- Group-chat alternative from MAF/Agno only after basic A→B→A proven; cap rounds/time/requests, require coordinator stop condition and user approval for side effects.
- **PASS:** traceable A→B→A dialogue/decisions, bounded cost, and measured improvement over single-role baseline.

### Gate G4 — user-facing daily product and first economic workflow
- Local Persian chat UI starts in one click, no user daily PowerShell, optional no-LLM route when gateway unavailable.
- Approved batch of opportunity/email data -> extract/dedupe/rank/draft (READ-ONLY initially); external sending only with per-action user approval.
- **PASS:** real utility and reversible deployment, export/restore with no duplicate writes.

### Gate G5 — grow only when justified
- Add memory/vector/knowledge graph on documented FTS recall miss; add DBOS/Dagu on proven long-running recovery gap; add iii/Aether/Dapr/Orleans or event bus on proven cross-process/host messaging; add A2A on cross-framework independent agent; add cloud uptime only on specified when-laptop-off requirement and verified pricing/region/billing policy.

## 10. What would change the provisional recommendation?

- **Choose Agno-first implementation** if pinned 3.1.10 (or explicitly approved updated version) starts safely, supports actual DJMRN evidence+policy integration, returns real OmniRoute Persian response, restart recovery and two-role collaboration with acceptable latency/RAM. Built-in team/workflow reduces genuine code.
- **Prefer Microsoft Agent Framework** if its group-chat/handoff/typed workflow and host portability demonstrably remove collaboration code while Agno requires heavy custom coordination or UI/permissions; compare real Windows process count and data interoperability.
- **Prefer Pydantic AI + DBOS** if multiple human approval waits/restarts or robust durable steps are urgent and Agno task recovery semantics do not meet requirements, while UI/team orchestration is comparatively simple.
- **Prefer Mastra** if a cohesive TypeScript + backend/frontend stack and durable workflows reduces actual effort and enterprise restrictions are acceptable, with proven Python worker interoperability.
- **Prefer iii (worker-centric)** if future **many heterogeneous independent internal Python/Go/Node workers** and a discoverable shared API/event/trigger bus are urgent now, AND Windows RAM, durability, auth and ELv2 commercial use check PASS. It must be paired with a role/agent reasoning layer; SDK ≠ personal AI supervisor.
- **Prefer actor/event bus infrastructure** if independent stateful actors with true concurrency/remote deployment must run, not simply because there are many logical personas.
- **Prefer minimal direct core without new runtime** if a narrow reusable CAP-006+task/permission API meets the near-term needs and full framework adds more moving parts than value.

## 11. Open risks, tests and stop conditions

- **Windows privacy and file boundary:** exact normalized handles, traversal/symlink race, third-file rejection, safe mounts; role prompt NEVER grants new permission.
- **Single authority:** do not conflate Agno session DB with source evidence DB, but avoid duplicate business task authority.
- **Approval:** exact action target/payload hash/idempotency key and receipt. 2 roles / 2 keys do NOT create independent model quota.
- **Retry multiplication:** agent transport + gateway fallback + durable step retry can multiply costs, especially free providers; disable duplicate retries/select one owner per boundary. Pydantic source explicitly warns about this.
- **Crash-recovery:** after external email/payment call when outcome unknown, don't blind retry; mark UNKNOWN_OUTCOME until reconciliation.
- **Message routing:** timeout/correlation and ACL; internal in-process task event registry suffices first. Event outbox needed only when event delivery across process boundaries truly matters.
- **Data export/version migration:** pinned framework version and DB schema migration, standalone export JSON/SQLite, recover from upgrade/rollback after snapshot.
- **Infrastructure footprint:** quantify working-set/private bytes, page faults, peak, total Windows memory with Chrome open vs closed, gateway active; no unsupported low-RAM promises.
- **Agent conversation quality:** same model with two personas doesn't guarantee independent verification; benchmark A/B against single-agent result with equal task and capped model budget.
- **Source freshness:** report may contain current-main code features not present in Agno installed 3.1.10 or other pinned versions; require release-tag-specific checks.
- **Vendor lock and legal:** iii engine ELv2; Mastra ee/ exception; various Work02 licenses/availability are snapshots, not legal advice.

## 12. Source ledger (checked 2026-10-27) — official docs and GitHub, with limitations

Primary architectural sources, in directly usable URL form:

1. Microsoft/Azure, **AI agent orchestration patterns** (sequential, concurrent, group chat, handoff, magentic, applicability, failure/cost): https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns/
2. Microsoft Agent Framework **built-in workflow patterns**: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/
3. Microsoft Agent Framework **group chat and session synchronization**: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/group-chat
4. Microsoft **multi-agent interoperability** (native inside, MCP tools, A2A cross-agent): https://learn.microsoft.com/en-us/agents/architecture/multi-agent-patterns
5. **Microsoft Agent Framework source**, main README blob bc9a8b080aeca9b3c5a25f216f8f96f61ffc012c: https://github.com/microsoft/agent-framework
6. **Agno Agent Runtime** API/storage/auth/scheduler: https://docs.agno.com/features/runtime
7. **Agno Teams** team modes and scoped memory: https://docs.agno.com/agent-os/studio/teams
8. **Agno source**, main README blob 0524dec2b4ffe026c353fcd11d24a86e98859ab7: https://github.com/agno-agi/agno
9. **LangGraph persistence** checkpointer/thread vs cross-thread store; in-memory not persistent after restart: https://docs.langchain.com/oss/python/langgraph/persistence
10. **Pydantic AI + DBOS** durable agent/step, retries/serialization: https://pydantic.dev/docs/ai/capabilities/durable_execution/dbos/
11. **DBOS official Pydantic agent integration**: https://docs.dbos.dev/integrations/pydantic-ai
12. **Dapr architecture building blocks**: https://docs.dapr.io/developing-applications/building-blocks/
13. **Dapr Actors** virtual actors, message-by-message state: https://docs.dapr.io/developing-applications/building-blocks/actors/actors-overview/
14. **Dapr Workflow** durable state, child workflow, HTTP/gRPC: https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/
15. **Microsoft Orleans** virtual actor framework, Windows/.NET: https://learn.microsoft.com/en-us/dotnet/orleans/overview
16. **Microsoft Orleans persistence**: https://learn.microsoft.com/en-us/dotnet/orleans/grains/grain-persistence
17. **iii source** worker-function-trigger registry, main README blob 0de4c9c716bceaa88a61148f212f8cfd9d7d3557: https://github.com/iii-hq/iii
18. **iii official docs**: https://iii.dev/docs
19. **iii ENGINE LICENSE** ELv2, Git blob 23b3a1fadcaa5d29bd09158e08b31e181a780ce2: https://github.com/iii-hq/iii/blob/main/engine/LICENSE
20. **Mastra docs** workflows/suspend/resume/typed steps: https://mastra.ai/docs/workflows/overview
21. **Mastra source** with license per directory, LICENSE.md blob e1b6e4b6455a882dbbf66ee0b13101ec584d5e63: https://github.com/mastra-ai/mastra
22. **A2A specification** Task/Message/Artifact/Agent Card (inter-agent platform boundary): https://a2a-protocol.org/latest/specification/
23. **MCP architecture** Host/Client/Server, tools/context — not automatic dispatch brain: https://modelcontextprotocol.io/docs/learn/architecture
24. **Event-driven architecture style** and tradeoffs: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven
25. **CQRS** and transactional outbox placement: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
26. **Microsoft .NET common architectures** warning on premature microservices: https://learn.microsoft.com/en-us/dotnet/standard/modern-web-apps-azure-architecture/common-web-application-architectures
27. **Microsoft architecture styles** tradeoffs including Web-Queue-Worker: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
28. **Microsoft Orleans FAQ** framework vs ready product: https://learn.microsoft.com/en-us/dotnet/orleans/resources/frequently-asked-questions
29. **Motia-era Steps** technical lead (historical website; identity redirects to iii; do not silently mix): https://motia.tech/docs/concepts/cli
30. **Wikipedia/paper/blog posts** were not taken as product operational evidence; official project code and docs have precedence.

**Fetch gaps:** specific old LangGraph multi-agent URL returned 404; DBOS old tutorial URL did not open; use official alternative persistence and integration pages. Exa credits exhausted/HTTP402; NOT READ through Exa. Research sources are selected and cited, NOT a total exhaustive code line/CVE/Windows benchmark.

## 13. Research recommendation and decision state

**Conditional synthesis, no user adoption:** Architecture **A (modular core / typed ports)** is the best *long-term structural boundary*, while **Agno/AgentOS is the first ready agent runtime adapter to trial**, not inherently the central source of all task truth. Compare **Microsoft Agent Framework** for rich persona dialogue and **Pydantic AI+DBOS** for durable workflow-first path on the **same initial two-file workload**. Consider **iii** as an important newly found worker fabric candidate, not automatically an OSS replacement, because of ELv2 and unmeasured local effects. Mastra is an optional TypeScript stack candidate. Favor smallest verified dependency set for 8GB Windows.

This is a refinement of D-019 and existing hybrid architecture; it does **not** supersede approved policy, commit to Python, install a service, create a database, model Combo or run agents. **Next only with separate user approval:** design the P0 contract and run bounded, version-pinned equal-workload trials on user's laptop, choosing technology from observed evidence.

**Persistent archive write effects:** documentation in existing main GitHub repository only. No Notion, external Research-Bridge, Windows, runtime, account, provider, secret, cloud, paid or production changes.
