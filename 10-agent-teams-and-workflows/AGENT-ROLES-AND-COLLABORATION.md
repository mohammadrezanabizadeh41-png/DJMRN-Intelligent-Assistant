# نقش‌ها، گفتگو و بازبینی متقابل — DJMRN-AGTEAM-001

**Status: SPECIFICATION / NOT PROVISIONED**

## 1. پروفایل استاندارد هر ایجنت
`agent_id` (immutable), display name, mission, competencies, personality (tone and reasoning preferences), assigned skills, allowed tools and resources, model role/fallback, private memory namespace, shared read scope, task subscriptions, schedule ownership, supervision contract, decision authority, risk level, review duties, budget/quota cap, stop conditions, state, provenance.

**شخصیت ≠ Agent Runtime.** استقلال واقعی با Agent ID + session/state boundaries + Tools/Permissions + messaging + evidence سنجیده می‌شود؛ چهار prompt روی یک چت برای پذیرش کافی نیست. مدل‌ها می‌توانند مشترک و on-demand باشند.

## 2. تیم اولیه و توسعه مشروط
| ID | Responsibility | Allowed | Requires review / approval |
|---|---|---|---|
| DJMRN-PM-01 | Coordinator: receive goals, allocate tasks, collect evidence, assess reviews and conflicts, report | assign bounded read-only tasks, request peers, summarize | no self-approval of sensitive writes/deploy/payments |
| DJMRN-ARCH-01 | systems architect: compare design with actual code, risks, simplicity, costs, reversible plan | read docs/code, research, seek specialists | proposed architectural change needs evidence + owner gate |
| DJMRN-RESEARCH-01 | independent research: official sources, counterexamples, licensing, quota and availability | internet/approved docs read only | unsupported vendor claims must be tagged UNVERIFIED |
| DJMRN-REVIEW-01 (optional) | independent critic / test/security reviewer | review evidence, raise blockers and test gaps | distinct review policy and enough independence; not automatic agreement |
| DJMRN-DEV-01 (future) | implementation/testing under approved scoped task | isolated test workspace only after approval | no unapproved production writes |

## 3. Peer-to-peer interaction protocol (concept, NOT shipped API)
For each consultation, store/log minimum fields:
`task_id, correlation_id, source_agent_id, target_agent_id, role_requested, question, evidence_refs, context_digest, permission_scope, deadline, token_budget, status, response_refs, review_outcome`.
States: `NEW → ASSIGNED → IN_PROGRESS → REVIEW_REQUESTED → REVISION/RESEARCH → ACCEPTED/REJECTED/ESCALATED → COMPLETED`; failure: `FAILED/TIMED_OUT/BLOCKED`.

### Peer review and conflict
- Reviewer must inspect evidence or tests; **no agreeing because another Agent said so**.
- Explicit critique: reproducibility, alternatives, risks, potential counterexample and confidence.
- Conflict: isolate disputed claims; research authoritative sources; propose falsifiable test; record unresolved dissent; ask PM to synthesize.
- A security/reliability blocker must prevent automatic promotion to acceptance; PM may not override tool-level denied actions by prompt.
- Limit consultation depth (pilot ≤2 handoffs), fanout (pilot ≤2 peers), loops/retries (≤1 per failure) and context size.
- Doer/Reviewer should not share exactly the same unsupported claims without independent verification.
- All important conclusions link to actual source code/test output/official docs; distinguish OBSERVED/INFERRED/PROPOSED/APPROVED.

## 4. Absence-of-user operation
- Timer fires on a host that remains awake; assigned agent runs and consults other agents through permitted inter-agent messaging.
- PM receives structured result or escalation.
- Low risk + preapproved: continue automatically; missing approval/cost/permission: stop at `PENDING_USER_APPROVAL`.
- When user returns, show summary, consulted agents, disagreement, evidence, risks, queued approvals and cost/quota consumed.
- User can pause/stop; no agent may secretly disable approval gates.

## 5. Example (illustrative, NOT evidence of run)
1. 08:00 ARCH detects design/code drift in read-only repository scan.
2. ARCH asks RESEARCH for 2 official alternatives and a negative finding.
3. RESEARCH returns citations, eligibility caveats and pending questions.
4. ARCH asks REVIEW if available; REVIEW rejects unsafe assumption.
5. ARCH revises plan, identifies a validation test.
6. PM records accepted proposal vs unresolved objection, requests owner sign-off before write.

## 6. Traceability
A collaborative thread is useful UX, but the real proof is: **different agent IDs, different sessions, an actual peer send/receive log, a changed recommendation after peer input, and no manual copy-paste**. Workspace shared message ≠ proof of `sessions_send`.
