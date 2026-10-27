# DJMRN — Hybrid Languages + On-Demand Agentic Coordination (P1 extension)

**Status:** proposal + first minimal offline Python reference, not adopted global runtime, no Windows benchmark or production interop.

## 1. Distinct roles, no heavyweight all-in-one agent

- **Trustworthy Hub / Dispatch Ledger (not an LLM):** canonical UUID task, permissions, capability registry, idempotency, audit, safe disposition and approved route. Fail closed if requested capability unavailable.
- **Persian Interaction Persona:** the user's conversational identity; accepts user intent, explains work, asks for specific approvals. It talks TO the Hub through a transport-neutral API; it does not dispatch tools directly. This can be prompt + one approved OmniRoute model only when natural-language interpretation is actually needed.
- **Diagnostic Supervisor Persona (on demand):** receives bounded, redacted error/evidence references, classifies issue and proposes safe repair/retry/rollback/escalation. May use one budget-approved inference call; *cannot edit a policy, grant access, modify workflow config, install software, run arbitrary shell commands or resend email on its own*. Every proposal must pass an independent policy decision, approval and subsequent evidence check.
- **Knowledge Service:** separate authoritative knowledge write/read lifecycle, provenance, freshness and permissions. Hub holds references only.
- **Search Specialist:** sole holder of web search tools and its own error/retry/crawl workflow. Replies through Hub with source IDs and evidence, no bypass by other roles.
- **Mail Specialist:** scoped Gmail APIs and user approvals for send; unknown outcome requires reconciliation before retry.
- **CAP-006 Worker:** bounded deterministic read-only Python document search, not a conversational agent.

## 2. The direction of communication

```text
Persian user ──> Persian persona / UI ──> Hub intake & persisted Task ID
                                              │ policy + registry
                    ┌─────────────────────────┴────────────────────┐
                    ▼                                              ▼
             Knowledge service                                CAP-006 worker
                    │                                        Search / Mail later
                    └─────────> Hub result / provenance <──────────┘
                                        │
                                    Persian UI

Hub ──(A2A adapter if separate service)──> Other agents
Hub ──(MCP adapter if required)────────> Authorized specialist tool
Hub ──(AG-UI adapter if UI needs events)──> Persian chat UI
Hub ──(OmniRoute adapter on demand)──────> Supervisor role / model
```

The starting request MUST NOT go to CAP-006 first, because CAP-006 does not authorize resources, own the durable task ledger, or decide which specialist may act. It can be called directly by a specialist for local tests, but such executions are not officially Hub-managed tasks.

## 3. Hybrid is a PORT, not a programming language pledge

Use the existing `djmrn.coord.v1` JSON Schema as source of contract truth, plus versioned OpenAPI for HTTP boundaries, upstream MCP and A2A schemas unchanged. A worker in Python, Go, Rust, .NET, JavaScript/TypeScript may be an in-process function only in its own host, a local child process over stdio, a network process via authenticated HTTP, or a Docker-container worker. Select based on measured installation, cost, boundaries and security; Docker does not replace an API or task ledger. Dispatch ID maps to the protocol-native task/run ID. No agent receives provider API keys through payloads.

Data ownership: Hub stores task, dispatch, ack, audit and references; each specialist persists its long-running internal workflow and artifacts independently. This logical separation needs no always-resident agent processes. One SQLite DB is a low-overhead pilot, not a permanent DB selection or a ready distributed queue.

## 4. Bounded error response and recovery

1. Validate envelope and typed input, authenticate the caller, enforce resource/action policy at Hub and worker.
2. Record dispatch before starting work, including an idempotency key, owner and attempt.
3. Classify: input/policy denied -> stop; retryable read-only 429/5xx/network -> bounded backoff/retry; permanent failure -> stop; ambiguous external effect -> UNKNOWN_OUTCOME and reconcile.
4. When classification is uncertain, call optional Supervisor with redacted metadata *only if model policy allows*, not permanent supervision.
5. Supervisor returns structured `proposal` (root-cause hypothesis, suggested operation, evidence, confidence, reason) which never executes directly.
6. Hub checks declared capability, policy, side-effect class, original approval/payload digest, attempt/time/token budget; requests fresh user approval if needed.
7. Specialist acts and produces signed/validated receipts; Hub records completion and informs caller; Knowledge Service separately evaluates what to retain.

**No unrestricted recursive autonomous self-editing.** For unattended repair, begin with narrow operations such as retrying a read-only request with backoff or restarting a known worker after a clear, safe boundary. No silent edits to keys, GitHub, email, installed binaries, Windows settings or policies.

## 5. Phases and acceptance

- **P1-now:** Python stdlib reference Hub + SQLite task/audit + real CAP-006 adapter path; controlled synthetic document search. Unit tests run offline with a stub in isolated sandbox. Integration with the actual GitHub CAP-006 code **not yet tested** on this run. No model connected.
- **P1-next:** test cloned repo with existing CAP-006, verify SHA/line, restart/deny third file on Windows, measure RAM. Add narrow Persian interface as a client to Hub (not embed Hub into the UI).
- **P2:** Knowledge-first/freshness rule and Search Specialist workflow; error taxonomy, retries, incident journal and receipts with no network unless approved.
- **P3:** optional Supervisor profile connected to selected free OmniRoute role/model, budget and privacy controls; simulate diagnosis without allowing side effects.
- **P4:** language-diverse worker (Go/Rust or .NET) over versioned authenticated API; test A2A/MCP and eventual Docker if beneficial.
- **P5:** Gmail read-only and controlled follow-up operations only after scoped credentials and explicit authorization.

Existing project decisions D-005/D-019 are not silently replaced. No new always-on engine or paid fallback is approved by this document.