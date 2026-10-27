# DJMRN P1 — Language-neutral coordination hub pilot, Python reference

**Status:** Experimental pilot, read-only synthetic fixtures, not a production service, user device not tested. **Does not adopt Python as the project-wide implementation language.**

## Why this boundary?

The trusted hub owns Task ID, state, dispatch, idempotency and audit. A Persian assistant UI/persona submits a request to the hub; CAP-006 is a specialist worker and cannot grant permissions or own the authoritative Task ID. A supervisor LLM can later review errors or suggest routes, but must never self-approve permissions or external effects.

The JSON submission is the existing `TASK_SUBMISSION` record from `DJMRN Coordination Contract v1.0`. The **capability-specific** `query` travels separately so the generic task envelope remains compatible with the existing Schema (no `additionalProperties` bypass). Only `documents.search.v0` and at most **two trusted file IDs** can run in P1. `research.web`, Gmail, and other capabilities fail closed until their own specialist is added.

## Boundaries, transport, hybrid development

- Code is a Python standard-library **reference implementation**, not a permanent architectural lock. No mandatory Python worker for Go, Rust, TypeScript, .NET or Docker later.
- The current interface is a trusted in-process function, **not an HTTP, MCP, A2A or AG-UI server**; OpenAPI in the contract describes the future language-neutral edge. All those protocol adapters must be tested separately.
- Docker is optional *packaging/deployment*, not a programming language. A future Go/Rust/.NET worker accepts typed JSON or MCP/A2A through a Hub-owned adapter with its own identity/authorization; no direct user-facing privilege escalation.
- Knowledge specialist and Search specialist keep their own workflows. Hub stores official dispatch, receipts and limited read-only results for this demo. Move bulky/private contents to separate knowledge/artifact storage later; keep scoped evidence refs in hub.
- No web access, OAuth, Gmail, secrets, OmniRoute, LLM, self-installation, automatic patching or extra background process in this pilot.

## First run (synthetic data only, after local approval)

From a clone of the **main DJMRN-Intelligent-Assistant repository**:

```sh
python 05-assistants-and-capabilities/src/coordination_hub_p1/hub_p1.py demo pilot.sqlite3
python -m unittest discover -s 05-assistants-and-capabilities/src/coordination_hub_p1 -p 'test_*.py' -v
```

`demo` uses *only* the existing sibling `document_search_v0/fixtures/sample_alpha.txt` and `sample_beta.md` under CAP-006, whose contents are synthetic. Local SQLite stores a real Hub UUID task separately from CAP-006's deterministic fingerprint. `Hub.get()` emits a schema-compatible `TASK_RECORD` with versioned state; `Hub.get_result()` retrieves the locally persisted capability receipt separately (no network/API endpoint is exposed). Running `demo` again returns the existing task because its idempotency key is the same. The results are durable across closing/reopening SQLite. Do **not** use this for real private files or multiuser/remote endpoints yet. Do not run on the user's Windows without explicit scoped approval and path review.

## First-persona workflow (planned, NOT implemented)

`Persian UI/persona → Hub submit/authorize → Registry → optional knowledge lookup → CAP-006/Search Specialist → Hub result/evidence/audit → Persian UI`.

The `Persona` is a role/profile and optional model invocation, not an always-on second process. When a specialist reports an error: deterministic classifier checks retryable read-only vs. non-retryable; optional supervisory LLM reviews a redacted error, proposes an action; validated policy+scope gates any retry, config edit, repair or human approval. Unknown side effects (Gmail sending, purchases) must never be blindly retried.

## Limitations of P1

No agentic routing, no interpretation of arbitrary Persian intent (the `query` parameter is explicit), no HTTP authentication, no durable async multi-worker queue, no cross-process dispatch, no concurrency guarantee across a real web server, no full OpenAPI compatibility, no hard OS sandbox, no real file approval system. SQLite state and append-only logical audit are a focused proof, not a security certification. On crash, `reconcile_readonly()` can requeue *only* bounded explicitly read-only CAP-006 work for manually triggered execution. Production idempotency, crash-recovery and filesystem race safety need stronger host-level protections and real stress tests.