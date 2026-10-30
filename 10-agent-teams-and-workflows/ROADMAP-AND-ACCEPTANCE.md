# نقشه راه مرحله‌ای و آزمون پذیرش — DJMRN-AGTEAM-001

**Current stage: R0 — RESEARCH DOCUMENTED ONLY. No account, install, connection, payment or runtime test authorized by this record.**

## Stages
| Stage | Deliverable | Exit criterion | Gate |
|---|---|---|---|
| R0 | Project charter, research, architecture and known unknowns | docs linked and read-back on GitHub | current explicit documentation approval |
| R1 | Live recheck: exact versions, Windows install, privacy, zero-cost, OpenAgents→OpenClaw multi-persona mapping, OmniRoute endpoint, alternatives | evidence matrix with unresolved risks, go/no-go | fresh research authorization |
| P0 | Disposable read-only smoke on ONE gateway + TWO agent identities, no sensitive project files | each has separate state and tools, no unintended write | explicit install/connection consent |
| P1 | Direct peer consultation ARCH→RESEARCH and PM synthesis | peer send/receive trace, outcome changes after critique, no manual relay | test permission and quotas |
| P2 | Connect OpenAgents Workspace with Launcher/agn, verify separate participants (P0 BLOCKER) | each Agent individually selectable/traceable and role targeting correct OR fallback documented | sign-in/data egress consent |
| P3 | Single scheduled low-risk job + peer review + unattended delivery | run while user absent, hard time/token bounds, trace and visible result | scheduling consent |
| P4 | Failure/restart/security/quota/RAM tests | evidence-based policy and rollback, stop under budget or permission | permission for diagnostics |
| P5 | Optional production-ish limited pilot, human approval gates | measurable reliability/value over several runs | separate human promotion approval |

**Do not skip P2 on marketing claims.** If a one-Gateway many-persona mapping fails, alternative architecture must be evaluated, not disguised as success. P2 may be performed ahead of P1 if this determines feasibility before any additional investment.

## Acceptance tests
- **T01:** each logical agent possesses unique stable ID and distinct workspace/session, without a second local inference service per role.
- **T02:** independent agent A sends to B via actual tool/event; B responds, A consumes answer and revises output; no user relay.
- **T03:** reviewer challenges a factual claim with an independent source; PM reports both positions and reconciles or marks unresolved.
- **T04:** self-reference/circular delegation limited; bounded fanout/steps and stop.
- **T05:** Workspace shows each target agent separately, not one composite generic bot, OR is transparently labeled FAILED for the user's dual-interface requirement.
- **T06:** identity, permissions and trace/correlation preserved from dashboard task through runtime and back.
- **T07:** scheduled run starts on live awake device without user, peer consult occurs and final result is delivered; no duplicate jobs.
- **T08:** restart/offline/reconnect handling accurately reports missed, pending and failed; no false success.
- **T09:** forbidden write/exec/paid model attempt is denied by effective tool enforcement, not merely a prompt refusal.
- **T10:** API gateway no-card/no-charge allowed model route verified with Tool Calling, rate/usage caps and zero paid fallback.
- **T11:** measured RAM/CPU idle/run/restart on actual Windows device within user-approved resource budget.
- **T12:** dashboard telemetry redacted; no secrets, client documents or sensitive GitHub data leaked to hosted workspace.
- **T13:** stop/pause/approval works end-to-end; no autonomous modification of repository main or external services.
- **T14:** comparison with OpenClaw-only baseline: added Workspace benefits exceed added RAM/privacy/complexity.

## Evidence rule
Each test requires date, exact version, device, chosen model/provider route, inputs (sanitized), tool traces, result, measured numbers where appropriate, PASS/FAIL/BLOCKED, and source refs. Testing a mock ≠ real end-to-end PASS.

## Minimum success before migration
T01, T02, T03, T04, T05, T06, T09, T10 all PASS; then timed autonomous and resource tests T07–T14. AGNT preservation/retirement decision comes last. No account/install/machine changes are implicit in this plan.
