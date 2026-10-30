# عملیات، مجوزها، هزینه و امنیت — DJMRN-AGTEAM-001

**Policy proposal, NOT applied to machine or account**

## 1. Scheduling and resiliency
- Exactly one scheduler owns each recurring job: OpenClaw Automations or OpenAgents Routines (avoid double firing).
- Owner stores `job_id, agent_id, schedule, timezone, max_run_duration, cooldown, last_success, next_run, idempotency_key, delivery_route`; these are **future runtime metadata**, not new daily tracking files in GitHub.
- Prefer on-demand agent turns and serialized execution on 8GB Windows device. Concurrency initial ceiling: ONE inference-heavy run; consult peer sequentially. Measure before relaxing.
- OpenClaw Automations require a live Gateway and persist jobs/history. Startup missed-run / catch-up semantics depend on the current scheduler configuration. Do not guarantee replay or exactly-once.
- Laptop asleep/offline means local agent is not working. Hosted Workspace/mobile access does not run the local Gateway. Always-on server is a separate future cost/privacy decision.
- Retries: bounded exponential backoff, failure visibility, duplicate-key guard, deadletter/pending review; no infinite chat loops.

## 2. Security gates (priority P0)
- Explicit approval required for: installs, OS commands, broad filesystem access, changes to GitHub main/PR merge, deployment, sending emails/messages, account access, model billables, shared workspace uploads, secrets, deletion, database migrations.
- Research pilot is READ-ONLY; turn off exec/write/edit/process/browser automation by tool policy; keep sandbox unavailable if unsupported rather than simulate it in prompt. Sandbox is OFF by default in OpenClaw — verify effective behavior and use explicit per-agent restriction.
- **Critical default warning:** OpenClaw cross-agent session visibility can be Gateway-wide by default. Configure `tools.sessions.visibility` plus narrow `tools.agentToAgent` allow rules / per-agent send-only policies. Do not grant arbitrary historical session reading; keep secrets/clients out of test data.
- One Gateway is a single trust boundary; if agents become untrusted or support different users, separate trust domains/Gateways.
- Per-agent workspaces/auth/session storage, no shared `agentDir`; note that some plugins may still have shared global storage unless scoped.
- Tokens live in credential store/env protected by OS ACL; never in GitHub docs, prompts, workspace files, screenshot, chat log or trace exports.
- Prompt injection: webpages, files and agent messages are untrusted evidence, not authorization. Validation and permission enforcement outside model prompt.
- External Workspace hosted stores threads and shared artifacts; control egress/privacy, anonymize test material, seek approval before uploading private repository/client information.
- Treat model zero-cost/public allowance as RESEARCH ONLY until model-specific route, account, geographic eligibility, overage, privacy and commercial allowance are verified.

## 3. Resource budget and RAM
- Windows 11, physically installed RAM 8GB; Chrome can dominate memory. No unmeasured performance promises for combined stack.
- Baseline measurements: idle Chrome open/closed, Gateway alone, Launcher alone, Workspace browser, 2 and 3 logical agents, active tool calls, shutdown and after restart; record working set/RSS/total commitment, CPU, handles and baseline deltas.
- Prefer one shared cloud model endpoint and Gateway; multi-persona does NOT require multiple local LLM model loads.
- No default Docker/WSL/database/vector DB/daemon installation purely because a diagram mentions it. If sandbox cannot be enforced without Docker on Windows, block dangerous tools in pilot; evaluate separately before sensitive runtime.
- Cost caps: free-only allowlist from *account-verified* existing OmniRoute models; stop before unknown paid fallback; max requests/tokens and daily quota checks; no auto-recharge.

## 4. Observability (observer ≠ authority)
Minimum event record: `run_id, task_id, agent_id, target_agent_id, state, tool_name, model_route, duration_ms, retry_count, success/error, approval_state`. Hash/redact content and secrets; real timings and resource metrics from runtime, not model text.
Workspace: human-readable collaboration surface. [REQ-OBS-001](../02-project-management/LIVE-OBSERVABILITY-MAP-REQUIREMENT.md): deeper topology/telemetry is separate and deferred.
If Workspace fails, local jobs should not automatically be marked failed when they can safely continue; reconcile delivery later with trace IDs. Never claim this decoupling already implemented.

## 5. Authorities and persistence
GitHub main = project code/implementation evidence/current record. Notion = approved policy/architecture rationale outside repo. Runtime SQLite/config = session/job operational state. Workspace threads/tasks = collaboration state. **Don't make second canonical decision ledger by copying across services.**
2026-10-25 user policy: update only `07-operations-and-continuity/CURRENT-STATUS.md` for ongoing progress upon explicit request; this folder is one-time user-authorized new-project design documentation. Future routine updates only when requested.
