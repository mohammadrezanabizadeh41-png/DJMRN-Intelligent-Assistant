# KB-0017 — R2/M1 pre-G2 shared executor design and Jan-vs-small-GUI go/no-go

**Curated:** 2026-10-22 | **Status:** WQ0010/WA0010 VERIFIED & REVIEWED / G2A PROPOSED ONLY / G3 & Jan ADOPTION HOLD / D-005 STILL NOT DECIDED.
**Original:** [WA0010 full proposed blueprint](../../04-work-research-bridge/responses/WA0010.md), [coordinator independent review](../../04-work-research-bridge/reviews/WQ0010.md), [exact WQ0010](../../04-work-research-bridge/requests/WQ0010.md), Source Register SRC-0019.  
**Parent research:** [KB-0014 sources](../tools-and-integrations/KB-0014-r2-m1-ready-solution-source-atlas.md) (29 discovery endpoints), [KB-0015 candidates](../tools-and-integrations/KB-0015-r2-m1-implementable-candidate-inventory.md) (18 distinct assets/5 app forms), [KB-0016 Stage3 conclusions](KB-0016-r2-m1-three-stage-conclusion-and-decision-gates.md) (8 P0–P7 approaches). TASK-0017 unchanged, decision D-005 unselected.
**Keywords:** WQ0010, WA0010, R2 M1, pre-G2, trusted executor, CAP-006, Jan, direct JSON, MCP stdio, WPF RTL, Win32 file identity, G2A, G2B-A, G2B-B, G3, human approval, file manifest, security HOLD.

## Decision summary in Persian

بررسی متمرکز WA0010 توصیه می‌کند **ابتدا فقط هستهٔ مشترک G2A به‌صورت کد محدود و قابل بازبینی، پس از مجوز جداگانهٔ کاربر طراحی/ساخته شود**؛ بدون انتخاب نهایی میزبان/موتور. سپس تنها در صورت رفع گیت‌های هسته، Jan یک‌بار به‌صورت adapter کوچک MCP بدون fork به‌عنوان **اولین محک آزمایشی** مطرح شود. رابط مستقل کوچک (ترجیح بررسی منبع WPF و BiDi قبل از Tk) فقط پس از مانع مشخص Jan بررسی شود. این ترتیب یک **فرضیهٔ صرفه‌جویی** است، نه نتیجهٔ آزمایش.

| Layer | What EXISTS | What does NOT exist / decision |
|---|---|---|
| CAP-006 | Existing verified bounded per-call deterministic Markdown search with source line+SHA, Persian normalization; real user-run prior smoke on two copies | Authenticated human approval of file IDs; process OS sandbox; stable privileged handle-to-read guarantee; independent local chat UI |
| Shared trusted executor, **G2A proposed** | Source-level plan: exact typed tool `djmrn.m1.search.v1` / `search_approved_documents`, opaque file IDs + trusted 1–2-file session grant, owner/revision/digest, default deny, time/size/error, authentic source card | All this actual code, Win32 handle/race assurance, synthetic tests; future G2A source can be written ONLY on explicit user approval |
| Ready-host **A (Jan)** | Upstream source documents chat/history/model tool call, MCP stdio, approval and raw tool result; Windows release exists | Installed binary matching pinned sources, shell/tool OFF config, reliable raw line/hash rendering, Persian, resource and exact executor permission **NOT TESTED**. Jan hook has shell enabled true by default, **require explicit verified OFF**. Cherry/Conduit are conditional other hosts |
| Small local UI **B** | Official WPF sample supports structural RTL/LTR (MIT); Python/Tk GUI API available | Entire conversational client/history/tool loop/packaging, actual Persian caret/clipboard test, Windows RAM unknown. Do NOT build both complete UIs before quick discriminating check |
| Inference engine/model | Some official API/tool-call paths documented | Model checkpoint+quantization+license+template, quality of Persian function calling, Windows CPU/RAM measured, offline/cost/region; **UNSELECTED** |

## Exact contract proposal — NOT IMPLEMENTED

- Model may only propose `{query:string, file_ids:[id1,id2?], max_matches:integer}`; no root/path/command/URL/approval/recipient/shell. Strict extra-property/duplicate JSON-key refusal, max query512 Unicode codepoints, at most 2 unique IDs, `max_matches=1..8`.
- A separate trusted adapter adds schema_version `djmrn.m1.search.v1`, request_id, manifest_revision, owner/session context. Manifest grants must be approved by a human in independent native control, default inactive, exact file identity+digest, revocable, expiring (15-minute example is a DESIGN assumption), not persisted by Jan `allow-always`.
- CAP adapter gets only already authorized exact file mapping, emits executor-owned original file, line1based, raw excerpt and SHA256 plus matched state; model's Persian explanation is visually separate and not a source of authoritative citations. Status `OK/NOT_FOUND/INVALID/BLOCKED/CANCELLED/TOOL_ERROR/INTERRUPTED`; no optimistic fallbacks/replays, no stderr/stdout protocol leaks.
- Scope is a **control against untrusted model/client inputs**, not an OS sandbox against malicious same-user software. Win32 `CreateFileW` handle identity/share locking and NTFS hardlink/reparse/rename must be validated before G3.
- **BLOCKER:** Current CAP opens a path again, so G2A Win32 handle guard must prove no swap before that reopen, or STOP and seek separate permission for a minimal handle/byte-path CAP refactor; cannot reduce protections just to preserve CAP unchanged.
- Proposed common G2A code files are enumerated in [WA0010 §10](../../04-work-research-bridge/responses/WA0010.md). All under `05-assistants-and-capabilities/src/m1_pilot/`; no source file has been created. Existing `src/document_search_v0/`, project rules, task/decision registers, previous reports and CI untouched. Optional G2B-A adds `adapters/mcp_stdio.py` and Jan profile/launcher with pin/NOTICE; optional G2B-B begins a **WPF static RTL spike**, not full second assistant. Both optional and require separate approval.
- Proposed G3 tests `T01–T13`: 2 synthetic Persian MD files, forbidden third, Unicode normalization variants, prompt-injection line, expired/stale/revoked/grant forgery, traversal/junction/hardlink/replacement, malformed JSON/limits, tool impersonation/shell/web, cancellation, source hash and raw citation, click-only RTL, Windows baseline/cold/idle/peak/post-unload CPU/RAM and egress. All **DESIGNED/NOT_RUN**, no actual fixture SHA; hardware headroom and model parameters must be defined later.

## Only next authorized process

1. Coordinator independently accepts/rejects this WQ0010 result (review linked above) and presents exactly scoped **G2A source-only proposal** with default-deny/Win32 HOLD clauses; **ask user specifically to authorize** before any code is written.
2. If user approves, only then create agreed G2A files in canonical repo, leave CAP-006 source unchanged, maintain sha/diff and reversible commits. Future mock/unit test execution scope should be clarified explicitly; not assume testing means user's Windows. A discovered need to change CAP or use a new runtime/provider = STOP + scope change.
3. G2B-A Jan adapter/source config ONLY after shared gate review and separately scoped approval; G3 installation/model/Windows synthetic user-device test ONLY after later separately explicit permission; G2B-B WPF fallback only if a concrete A blocker exists or user requests it.
4. No new broad Work WQ or vendor discovery required by this report. Research is **READY FOR A LIMITED G2 DECISION**, not `PRODUCT_READY`. Cost/region/provider/licensing unknown is never assumed usable.
