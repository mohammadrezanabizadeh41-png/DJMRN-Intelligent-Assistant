# DJMRN — Work Research Mission 02: Ready-made Intelligent Cores & Agent OS

**Mission ID:** DJMRN-READY-INTELLIGENCE-PLATFORM-DISCOVERY-002  
**Source:** User-supplied complete ChatGPT Work report on 2026-10-27, Work duration reported 8m18s.  
**Artifact status:** Structured comprehensive archive of the Work findings, NOT a word-for-word transcript; no independent reproduction of all third-party source audits. The user's full Persian text remains in the origin chat.  
**Research status:** COMPLETE WITH TARGETED EVIDENCE / REAL WINDOWS INTEGRATION, RAM AND PROVIDER TESTS PENDING.  
**Scope:** Research only, no install, execution, model call, settings changes, database migration, external action or secret use. Work originally wrote NOTHING to GitHub or Notion. This archive is a later user-authorized repository recording by coordinator; it is not a Work WA file.
**Authoritative destination:** same project repository mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant, main. **Preserve** the 2025-10-25/26 hybrid architecture, and the first Work research ID DJMRN-CORE-ARCHITECTURE-RESEARCH-001. D-019 remains a conditional research-review decision, not approved software adoption.

## 1. Executive summary — Adopt + Thin Custom Core (conditional)

Work's recommendation: use **Agno/AgentOS** as the leading ready-made agent runtime/API candidate with **a thin DJMRN-specific trusted core** owning policy, capability/permission contracts, task identity, authorized tools and evidence. The preference is NOT based merely on previous Agno installation. Source evidence cited by Work includes actual API, team/agent/workflow runtime, SQLite schemas, queue path and observability capabilities. Yet Agno does **not** deliver a complete private DJMRN Windows desktop assistant without system definition/integration/security policy.

**Strong alternatives:** Langflow for a ready visual builder/UI and APIs; Dagu for script/event workflow execution (not a personal intelligence brain); DBOS for durable Python steps; Letta Code for persistent identity/memory; OpenFang for a potentially lightweight integrated host (needs recovery/maintenance checks). No single contender was proven to satisfy all DJMRN requirements with low complexity on this laptop.

**Build only** DJMRN task contracts, authorization/approval, provenance, capability mapping, real task DONE evidence, model quota admission policy and necessary adapters. **Reuse** SDK/runtime, standard API, model drivers, reliable persistence/workflow machinery wherever possible. Do not preinstall a second workflow engine or broker and do not assume a named multi-agent persona requires a resident model.

## 2. Search and evidence method as reported by Work

- Three sources: live Notion Applied/General catalogs, exact current main repository with existing architecture and test receipts, then independent current official GitHub/document/code/release searches.
- Work reported **30 candidate families screened; 10 deep-screened**. Deep screened = relevant architecture/API/DB/code subset inspected, not complete code audit, security verification or actual local execution.
- Evidence tags: C=code inspected; D=official documented; E=extension needed; ?=unverified; TEST PENDING=actual local operation not tried.
- Example independent phrases: self-hosted agent OS persistence tools workflow; local-first multi-agent server memory; agent worker orchestration durable messaging; shared AI workspace knowledge API; capabilities/task delegation/SQLite.
- Sampling of Issues and PRs was targeted; full CVE/dependency/CI audit NOT conducted. Don't promote README promise into verified functionality.

## 3. Candidate longlist (30; as included in the user-supplied Work result)

| No. | Candidate | Architectural family | Work disposition |
|---:|---|---|---|
| 1 | Agno | AgentOS/backend/team (B/C/H) | Deep review; leading runtime candidate |
| 2 | AGNT | Desktop/backend (A/B/G) | Deep review; source-available restrictive license |
| 3 | OpenFang | Local runtime/UI (A/B/F) | Deep review; durability and maintenance gates |
| 4 | Aether / AetherLite | Agent/worker messaging (C/H) | Deep review; fabric, not a complete brain |
| 5 | AgentScope | Framework/app server (B/C/H) | Deep review; composition needed |
| 6 | Dify | Workflow platform/UI (A/G) | Deep review; multiple services/licensing |
| 7 | Langflow | Visual flow/API (A/G/H) | Deep review; principal visual comparator |
| 8 | Letta Code | Agent identity/memory (B/D/F) | Deep review; persistence-centric |
| 9 | Dagu | Script/workflow orchestration (E/H) | Deep review; deterministic workflow |
| 10 | DBOS Python | Durable workflows (E/H) | Deep review; library, not agent chat |
| 11 | LangGraph | Stateful orchestration SDK (C/E/H) | Comparator |
| 12 | CrewAI | Multi-agent framework (C/H) | Comparator |
| 13 | Pydantic AI | Typed agent SDK (B/H) | Comparator |
| 14 | AutoGen | Legacy multi-agent (C) | Work reports official maintenance-ending notice; don't greenfield by default |
| 15 | Microsoft Agent Framework | Agents/workflows (B/C/E) | Successor architecture candidate |
| 16 | n8n | Automation builder (E/G) | Complement; Sustainable Use license constraints |
| 17 | Activepieces | Visual automation (E/G) | Not deeply reviewed |
| 18 | Windmill | Script/job workflows (E/G) | Not deeply reviewed |
| 19 | Conductor | Durable enterprise orchestration (E) | Later scale |
| 20 | Sim | Visual agents (A/G) | Not deeply reviewed |
| 21 | Flowise | Legacy visual flow (G) | Work reports official end-of-support 2026-08-31 |
| 22 | Open WebUI | Local GUI + knowledge (D/F) | Not a complete shared control plane proven |
| 23 | AnythingLLM | Knowledge workspace (D/F) | Not control plane |
| 24 | Agent Zero | Execution assistant (B/F) | Needs deeper audit |
| 25 | Hermes Agent | Agent backend (B/F) | Needs deeper audit |
| 26 | Mem0 | Memory (D) | Not task control |
| 27 | Graphiti | Knowledge graph (D) | Not task control |
| 28 | Localmem | Shared local memory (D/H) | Optional memory layer |
| 29 | Memento Multiagent | Agent memory/skills (C/D/H) | Optional candidate |
| 30 | Zeta | Ambient agent (B/F) | Dependencies need audit |

Work also encountered **Motia** and **LibreChat** as search leads but lacked robust retrieved metadata; NOT included in the 30. A later separate architecture research must follow these leads independently.

## 4. Deep shortlist — dated snapshot reported by Work (2026-10-27)

| Project / developer | Type | Release Work observed | License described by Work | Base deployment |
|---|---|---|---|---|
| Agno / agno-agi | Python SDK+AgentOS server | 3.1.10 (Oct23) | Apache-2.0 | Python, possible SQLite |
| AGNT / agnt-gg | Electron desktop+backend | 0.6.7 (Oct9) | custom restrictive; NOT ordinary OSS | Electron/Node/SQLite |
| OpenFang / RightNow-AI | integrated Rust runtime+UI | 0.6.9 (May12) | MIT/Apache file-level | Rust binary |
| Aether / Scitrera | task/message fabric | 0.2.4 (Sep12) | Apache-2.0 | Lite binary, SQLite/Badger |
| AgentScope / agentscope-ai | framework+app server | 2.0.10 (Oct12) | Apache-2.0 | Python |
| Dify / LangGenius | visual full-stack | 1.18.0 (Oct23) | additional conditions on Apache base | Compose multi-service |
| Langflow / langflow-ai | visual flow+API | 1.13.0 (Oct22) | MIT | Windows Desktop/Python |
| Letta Code / letta-ai | local assistant+memory server | 0.34.24 (Oct25) | Apache-2.0 | Node, Windows path |
| Dagu / dagucloud | job/workflow UI+API | 2.23.0 (Oct26) | GPL-3.0 and commercial features | Go binary |
| DBOS / dbos-inc | durable Python library | 3.3.0 (Oct15) | MIT | Python + SQLite/Postgres |

**Version caveat:** Main-branch code findings must NOT be attributed to release binaries without tag cross-check. All releases/labels above were stated by Work; not independently revalidated as current by this archive.

### Agno technical findings
- SQLite schema tracks session/run and agent/team/workflow identities, not just chat text.
- DB queue exists as selectable functionality; not guaranteed enabled. AgentOS session/memory persistence does not automatically equal DJMRN task authoritative state.
- User isolation disabled by default in Work's pinned-source inspection; permission/authorization must be configured and enforced at executor.
- API, tools, runtime are available; DJMRN must still supply profile/capability/approval/task contracts.
- "Local Control Plane free" differs from availability/licensing of self-hosted Control Plane/UI features; verify pricing and deployment license exactly before deciding.

### AGNT
- Features observed: Electron UI, local backend, SQLite, workflows, model custom endpoint.
- Full replay after crash was not established. Restrictive source-available license may constrain commercial resale/hosted third-party services; don't call it permissive OSS.

### OpenFang
- Rust binary, integrated API/UI, OpenAI-compatible driver and SQLite memory; self-published idle memory ~40 MB and binary ~32 MB are claims, NOT Windows measurement.
- In-memory Workflow registry observed in source area checked; run/restart durability not demonstrated.
- Pre-1.0 and apparently lower main activity as of snapshot; latest relevant pull requests not evidence of merged fixes.

### AetherLite
- A2A-like inter-worker contract for IDs, ACLs, task lifecycle, checkpoints, delegation and gRPC; not a model inference runtime.
- Lite persistence uses SQLite/Badger components; quotas reportedly not restart-durable; Windows real deployment pending.

### AgentScope
- App Server, team/session/API and delegation supported; Work inspected a TeamPipeline code path where delegation was ALWAYS_ALLOW, meaning separate project authorization required.
- Redis seen in examples, not proven mandatory in every deployment.

### Dify
- API and workflow/run/node models in code; Docker Compose uses API, workers, Redis, DB, sandbox, other services. Do not add all vector DB alternatives simultaneously.
- Vendor minimum 2 CPU and ~4 GB RAM as of report; not "impossible with 8 GB" but poor initial fit absent measured headroom. License additional conditions.

### Langflow
- UI/API/components, job/checkpoint/session DB; a checkpoint is not automatically exactly-once external side effects.
- Vendor docs caution that custom Python execution has host privileges and does not isolate file/network per tenant; use trusted local environment + external policy if tested.

### Letta Code
- Repository/identity changed relative to historical Letta. Local backend examined uses JSON/JSONL, not presumed old PostgreSQL design. App server/local identity & memory; output to OmniRoute unverified.

### Dagu
- UI/OpenAPI, run history, cron/script/HTTP/human task and model provider BaseURL in code/docs; no external broker/DBMS required for basic local workflow.
- Is NOT intelligent shared knowledge store, agent group discussion manager or necessarily free enterprise RBAC/SSO/Audit.

### DBOS
- Python-library durability with SQLite and DB schema; not chat desktop nor agent team framework.
- Work identified mismatch between older README emphasis on PostgreSQL and newer code/SQLite, and upstream Issue #922 / PR #923 about SQLite startup race; a proposed fix is not a proven release fix.

## 5. Critical feature comparison, interpreted conservatively

Legend: YES-DOC/CODE = documented or code inspected by Work only; NOT proven on DJMRN; EXT = extension needed; CHECK = insufficient proof.

| Option | API/UI | Roles/dialogue | Durable state | Deterministic tasks | Shared knowledge | Main risk |
|---|---|---|---|---|---|---|
| Agno | API yes, Control Plane separate | teams/delegation | sessions DB; specific task replay TEST | tools/workflows | optional knowledge/memory | defaults/config, UI deployment, double state owners |
| Langflow | visual UI+API | flow-mediated, not necessarily unconstrained interagent mesh | DB/jobs; workflow crash guarantees CHECK | flow/tool components | components | Python execution host trust, RAM |
| Dagu | job UI+OpenAPI | Agent dialogue EXT | run state | YES main purpose | semantic memory EXT | orchestration duplication |
| DBOS | build your API/UI | Agent framework separate | durable workflow state | YES | EXT | workflow semantics, data serialization/versioning |
| AgentScope | server/app/API | teams, delegation | selected DB/backend | tools/workflows | optional | team delegation boundary |
| Letta Code | CLI/app server | persistent agent persona | local conversation/memory | generic task control EXT | strong focus | provider, source evolution, portability |
| OpenFang | integrated UI/API | agents supported | conversation persistence; active workflow recovery CHECK | tools possible | memory | pre-1.0, reboot |
| AetherLite | proto/API | cross-worker messaging/delegation | task store; quota volatile | executes via workers | EXT | another service/broker without work owner |
| Dify | visual UI+API | flow-mediated | workflow storage | workflows | built-in resources | resource footprint/license |
| AGNT | integrated desktop | workflow/plugins | SQLite | tools | features | restrictive license |

Distinguish shared knowledge from mailbox, role-to-role chat, and task orchestration: none entails the others by itself. The user wants all four eventually, with one coherent authority contract.

## 6. Recommended architecture patterns from Work's second report

**All-in-one:** Langflow/Dify/AGNT. Faster ready UI, but project-specific permission/approval/evidence and lock-in remain.

**Composable:** Agno/AgentOS + thin trusted DJMRN layer + authorized deterministic Python workers + SQLite operational state + OmniRoute as one inference gateway. This is Work's leading conditional fit, subject to exact security, version and storage behavior.

**Minimal custom:** small Python (or .NET) API + SQLite + typed roles/tool adapters. Most control, more first-party maintenance.

**Never add both Dagu + DBOS at day one**, or build multiple authoritative independent task retry layers. Later choose Dagu if script/cron observability dominates; DBOS if crash-resume of Python functions dominates; Aether if agent/worker processes are distributed and protocol/ACL becomes a measured need.

## 7. Model, memory and agent communication integration

- Existing gateway evidence: OmniRoute on local http://127.0.0.1:20128; Work 02 made no API call to it. Merely supporting OpenAI-compatible BaseURL is not proof of actual response/tool calling/streaming or free-only fallback.
- Single serial shared inference route can support multiple logical personas; avoid 1 resident model/process per persona.
- Future typed task envelope: task_id, parent_task_id, correlation_id, sender_role, recipient_role, capability, scoped input_refs, deadline, status, result_refs and error. No freeform LLM instruction is authorization.
- A first review cycle A→B→A passes a *source-linked artifact*, not unrestricted private transcript and tool credentials.
- Shared operational identifiers, evidence, accepted decisions and narrow capabilities; persona memory/private transcripts scoped and not universal. Notion remains research governance; GitHub project evidence; product runtime DB maintains task state; indexes are rebuildable derived views.
- Memory pipeline: original file+revision/hash → lexical search/normalized Persian → tested provenance → optional embeddings only on demonstrated retrieval failure; Graphiti/Mem0/vector graph not day-one authority.

## 8. Evidence-based first vertical and candidate PoC

Prompt: "این دو فایل مجاز را بررسی کن، تفاوت‌های مرتبط را با منبع گزارش بده و نتیجه را برای نقش بازبین بفرست."

**Phase 0:** exact task & permission/evidence contract, before framework activation.

**Phase 1:** Persian message → durable task_id/RECEIVED, validation, two allowed non-sensitive files, CAP-006 deterministic read/search, correct file hash + line, persisted state and result. Third file DENIED. No model call.

**Phase 2:** reopen application; verify task+refs survive; distinguish restart after COMPLETED and restart mid-RUNNING; explicit retry/UNKNOWN_OUTCOME.

**Phase 3:** one *already verified and free-admitted* OmniRoute route, GPT-compatible endpoint/alias UTF-8, streaming if needed, structured output/tool-call capability tested separately, 429/500/timeout handled without paid fallback.

**Phase 4:** A analyst hands scoped task to B reviewer and B returns linked verdict, bounded depth/turns/tokens. Measure quality, tokens and latency against direct single-agent answer.

**Phase 5:** user-facing Persian GUI, no manual PowerShell daily; real opportunity processing in READ-ONLY/DRAFT mode when independently approved.

**Required measurement:** working set/peak/total RAM with Chrome open/closed and gateway active, Windows startup/service behavior, exact bytes persisted, files unchanged, export+restore, version pin, license, secret/telemetry policies. No result in these gates has been run by Work 02.

## 9. Project and original-source receipts as reported by Work

**APPLIED_LIBRARY_READ_RECEIPT:** PARTIAL TARGETED; Operating Memory 25 Oct, Tool Governance 17 Oct, Applied Index title v0.48 (20 Oct), Applied Mission (20 Oct), General Discovery (18 Oct), relevant branches only. Old AGNT/Letta/Flowise/AutoGen/Agno/Dify/Langflow/Dagu were already cataloged; OpenFang/Aether NEW-EXTERNAL only relative to targeted scans. Applied Index title/checkpoint mismatch persists.

**PROJECT_REPOSITORY_READ_RECEIPT:** exact main at b21c1a5e9973e284b91c35d0773e79c4a3123d6b; first Work report commit 1819338c93d4b64407284bfd9a0a1d7730be723a, blob c38880ad3329db15014edac5584a9034dafe354a. Work reported blobs PROJECT-RULES acff165a37ce7176e6973bc506fe6915e5cc5092; CURRENT d1262533461f3ee866c93c609b0225120ee801de; architecture synthesis 989ff696021df3d6606a95371aa6fc68401f778b; master roadmap 1dc1909d102f1cd8691ea79d712a97bd9549edc3; research bridge README fa5fdf56ad50714e6e4479fe5111ec6f1036be27; lock 231778be56580deedcd1d5c0c5de54bc093552fc. No WQ/WA assignment, originally NO WRITE.

**INDEPENDENT_SEARCH_RECEIPT:** Work states 30 families + 10 deep; GitHub commits, selected source files, Releases, docs, targeted Issues/PRs and official pricing/licenses. No full dependency/CVE/CI security, no account fee/free-tier eligibility and no Windows runtime benchmark.

### Precise commit snapshots Work reported (do not interpret as local versions)

| Project | inspected main SHA, as reported |
|---|---|
| Agno | ffe47567920e5a5c5d5d416c2b366f8c32c62f31 |
| AGNT | 8487ca46875691945e5f1dc66d038e50b5e9cb88 |
| OpenFang | acf2587e46be174c10200489c9a2d23a39a98aeb |
| Aether | 610aaff663536090136403d46a4140d645ffa271 |
| AgentScope | 44b5d5208f093ae2f5309f42653813801c2ea8cf |
| Dify | adb27d0d016f372fb643fb53c38de91c014be034 |
| Langflow | aeb10d96bb2ea797696613af931e91ddf51f3320 |
| Letta Code | b995585d42313c9ddb8873986de05e01a595d52a |
| Dagu | 0082d03f66b87311846c2cf7f2c6292dce1e88d9 |
| DBOS | 2873b8c22ba21f9ff7e52acbd54285b3472242ac |

### Core source blobs Work reported

| Project | File | Blob |
|---|---|---|
| Agno | libs/agno/agno/db/sqlite/schemas.py | e172ddec17502fc2e6be9862482425cb161687cc |
| Agno | libs/agno/agno/os/app.py | 6564f18ddb82522934d2f506ec68a3c93b986081 |
| Agno | libs/agno/agno/job_queue/config.py | 630dc16ecb164c334dbcb36ceb7da94e098d6f6 |
| AGNT | backend/src/models/database/index.js | 0c4172d75a7ac3c7de43b3e40ac17f5debd2ac81 |
| AGNT | LICENSE | 9ae035c7e45ca0c706ca18cb02fde7c0fdbbcf92 |
| OpenFang | crates/openfang-kernel/src/workflow.rs | a40f544a500a0f7ff388a5cd63cd917cafee0ac2 |
| OpenFang | crates/openfang-api/src/routes.rs | cebb1f599a4695fd0d8a19f3444cf822d70a6417 |
| Aether | api/proto/aether.proto | 6e39e14c83cbc6275a19fe025d5d82bc389b9ff4 |
| Aether | tasks/sqlite/store.go | 0710d26f81eec6f63040d1615aaaf4cae94c60e7 |
| AgentScope | src/agentscope/pipeline/_team_pipeline.py | c4c6bada1c97d46608f4d09812e5e5dd4c790035 |
| Dify | api/models/workflow.py | 3653a3f30ab215b0a09b40a525106fdd5593aee3 |
| Dify | docker/docker-compose.yaml | bfc96bcd0ed84035046882a738de3c63804bf61a |
| Langflow | src/backend/base/langflow/services/database/models/jobs/model.py | ca56535f702ad16275e15901be840514a757a15c |
| Langflow | src/backend/base/langflow/services/database/service.py | e0aa9ac95ea3e91912321ecafa0a5c5939c64755 |
| Letta Code | src/backend/local/local-store.ts | 47fb6ce599ae9a7bec3e7cac8292371bdc415ecb |
| Dagu | api/v1/api.yaml | 80a14d33b2e4cf1572cd3b63f2234378cd8ac47f |
| DBOS | dbos/_sys_db_sqlite.py | 1b29c512b4106638239bd6c7096ea25cb0305707 |
| DBOS | dbos/_schemas/system_database.py | e022b055973e6b0fb68bc37203748e96a76c69ba |

**Crosswalk classifications:** BOTH PROJECT+LIBRARY = Agno/Dagu/DBOS/Langflow/Dify and prior tools; new enrichment = actual code/license/defaults/version findings; narrow NEW-EXTERNAL = OpenFang/Aether; NOT PROVEN = all real DJMRN integrations/RAM/safety/multiagent recovery. Work's reported Flowise/AutoGen deprecation should be rechecked by official source at the time of actual choosing.

## 10. Comparative conclusion and explicitly deferred step

Original Work 02 voted conditional leading PoC: Agno/AgentOS + SQLite + existing permissioned CAP-006 + thin DJMRN policy/evidence/task shim + OmniRoute only for admitted model calls. Langflow for visual alternative; Dagu for workflow-first. User has **not approved** any architecture adoption or runtime installation based on these reports.

**Subsequent independent architecture research must NOT anchor on this winner**. Explicitly compare actor/event-bus, modular-monolith, durable-workflow-first, agent-framework-first and worker registry approaches, including candidates not discovered by Work 02, and register a falsifiable decision tree before coding.

**No task in this archival authorizes writing to Notion/Research-Bridge, installing code, connecting secrets, editing user files, invoking cloud accounts, creating model groups, or spending funds.**
