# DJMRN — Dual Conversational Surfaces, One Permissioned Tool Core (PROPOSAL)

**Prepared:** 2026-10-21  
**User-selected product goal:** **BOTH** — control DJMRN through ChatGPT and an independent Windows chat environment in the future.  
**Design/implementation status:** **PROPOSED FOR USER REVIEW / NOT ADOPTED AS TECH STACK / NO BUILD OR DEVICE ACCESS AUTHORIZED**.  
**Decision record:** [D-015](../02-project-management/DECISION-REGISTER.md) captures **only the user's dual-surface requirement**, not adoption of Jan/ChatGPT integration. [TASK-0017](../02-project-management/TASK-REGISTER.md).  
**Research baseline:** [WQ0003](../04-work-research-bridge/requests/WQ0003.md) → [WA0003](../04-work-research-bridge/responses/WA0003.md) → [coordinator review](../04-work-research-bridge/reviews/WQ0003.md), user test [NEW-V0004](../06-tests-and-evidence/logs/NEW-V0004-20261021.md); governing [REQ-012](../02-project-management/CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md) / [D-014](../02-project-management/DECISION-REGISTER.md).

## 1. Exact product decision and recommended PRIMARY chat surface

**Requirement confirmed by user:** ordinary operations should start from Persian natural-language messages to assistants, without recurring user PowerShell. Both **ChatGPT** and a **separate local/independent chat** must be able to invoke the same logical DJMRN capabilities in a later phase. A, B and C are complementary capabilities under these surfaces; different programs/LLMs need not be installed or running per assistant.

**Provisional PRIMARY pilot chat:** **Windows local independent chat via Jan Desktop v0.8.7 (only after safety/model/RAM qualification)**. Why for a first test: documented local MCP stdio host and interactive permission prompts; it can launch a strictly limited child tool without any public network listener or ChatGPT Platform tunnel. Reuse existing CAP-006 backend. **Jan is not yet approved or verified as viable on the actual laptop**. Jan official [MCP docs](https://docs.jan.ai/desktop/mcp), [settings](https://docs.jan.ai/desktop/integrations/mcp-servers), [v0.8.7 release](https://github.com/janhq/jan/releases/tag/v0.8.7) were source-checked in WA0003/review; **Shell ON by default in v0.8.7** and MCP Allow All must explicitly be disabled; remote model egress and local LLM memory require separate acceptance. Having Jan installed historically does not count as verified v0.8.7, correct config or readiness. All other built-in/general Shell/File/Web/Agent tools are disallowed for the initial pilot.

**Secondary future chat:** **ChatGPT Desktop local MCP** if the actual Windows app/account/workflow and permission scope support it. Official [ChatGPT Learn MCP docs](https://learn.chatgpt.com/docs/extend/mcp) describe STDIO/HTTP configuration and sharing with Codex; verify whether it is actually accessible in the intended *ordinary ChatGPT conversation/Work mode* on the user's plan/version before calling it a product capability. A GitHub connector or a web chat tab **does not** give local disk access. This secondary surface must reuse the **same tool schema and policy core**, but may need a **separately launched MCP stdio child**, not necessarily the same process.

**Fallback if Jan fails gates:** Cherry Studio v2.1.7 [official release](https://github.com/CherryHQ/cherry-studio/releases/tag/v2.1.7) + same tool adapter and explicit approval checks, **only if** model/tool/permissions and RAM pass. If local model tool-calling is unusable on 8GiB or provider/free/legal/privacy gates fail, report `BLOCKED` and reconsider host/approach; never silently load a large model, activate an unverified cloud service or default to an unrestricted Shell Agent.

**Optional future ChatGPT Web path:** only after documented eligibility, authorization, privacy/egress and true-Free-First/cost review. [Secure MCP Tunnels](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels) require Platform tunnel ID, runtime API key, workspace and organization permissions and a running client on a host with access to the tools; OpenAI API [supported-country rules](https://developers.openai.com/api/docs/supported-countries) require separate legal compliance review. **NOT an approved backup to local MCP and not a workaround for regional restrictions**.

## 2. Logical architecture and clear execution boundaries

```text
                        USER — Persian message and explicit approval
                                    |
                    +---------------+---------------+
                    |                               |
          LOCAL CHAT (Jan pilot)            ChatGPT Desktop (future,
             MCP stdio host                eligibility-gated local MCP)
                    |                               |
                    +---------- identical TOOL CONTRACT -----------+
                             (each host may spawn its own
                               on-demand stdio process)
                                    |
                  DJMRN TRUSTED CAPABILITY/TOOL CORE
             fixed policy / source-set mapping / approval gate
                input validation / timeout / source integrity
                         no model-controlled Shell
                                    |
                   first: djmrn_document_lookup (A)
                         existing CAP-006 V0
                  later: data_validate/extract (B)
                  later: source_evidence_review (C)
                                    |
                     authorized bounded results
              source file/version/line/raw text/SHA256
                                    |
             host-specific response, citations, error/receipt
```

**One CORE means one shared logical contract/implementation and policy authority**; it does **not** require a new always-running central server or one OS process shared by both UIs. One or both hosts can start a short-lived `stdio` adapter from the same checked code under the same policy. No public listener, tunnel, broker, service, vector DB, manager, duplicated research library or model process is required for the initial vertical. A future HTTP transport is an optional additional adapter, only if its authentication, Origin/Host controls, port binding, key/secret storage, TLS and local/remote boundary are designed and separately approved.

The **model reasons** about intent and evidence, but is **NOT** a permission/identity/root-path authority. A deterministic policy outside prompt/model controls execution rights, file allowlist, subprocess command/argv and denied states. A user's in-chat confirmation is presented by a trusted host; if there is no reliable way to verify host approval at the tool boundary, put the confirmation in a trusted local UI/policy gate before the worker call. MCP alone is neither OS sandbox nor cryptographic proof that a user approved. Never accept `approved: true` supplied by an LLM as a grant. Commands obtained from source files/social posts are data, never instructions.

All calls into existing `docsearch_v0.py` use fixed interpreter and program paths controlled by trusted configuration and structured query arguments, **never** shell command expansion. On-demand `import` or `subprocess(shell=False, argv=[...])` are candidate adapters, not chosen implementations. Harden against path traversal/reparse/TOCTOU to an appropriate bounded threat model; do not claim OS containment just because source_set_id is restricted.

## 3. Tool and result contract — proposed V0

**Tool ID:** `djmrn_document_lookup`  
**LLM-visible user-controlled input, maximum:** 
- `source_set_id` — enum fixed to `djmrn_pilot_docs_2` in FIRST pilot.
- `query` — bounded Unicode string, normalized by existing CAP-006; clarify semantic question→literal query with user if uncertain.
- `requested_limit` — optional capped safe value, default <= existing CAP limit.

**Forbidden LLM fields:** absolute or relative filesystem path, command, interpreter, shell flags, root directory, arbitrary URL, `approved`, environment overrides, executable, server ID, model config, account tokens or write destination.

**Trusted-side hidden fields:** `call_id` fresh per invocation, user/session authority, immutable `source_set_id→root/exact file list/expected SHA` mapping, host-approved grant/deny receipt, timeout, resource budget, cancellation ownership and checked source metadata. Historical CAP `task_id` is deterministic fingerprint, NOT unique execution ID.

**Result envelope:** `call_id, capability, execution_status, input_scope, searched[{file,sha256,encoding,status}], matches[{file,line,text,match_mode,source_sha256}], truncated, limitations, redacted_error, approval_status, local_version`. Model must use **real returned** file/line/source text and never claim reading when adapter failed; no-match means only "no match in those allowed versions". Model-generated summarization is clearly separated from quoted evidence.

**Data egress:** even if the original file never leaves the laptop, sending retrieved snippets and query to ChatGPT or a remote model **is** data transfer and needs specific authorization before secondary interface activation. Local model mode must also test telemetry/offline behavior. Do not copy sources into cloud knowledge bases or automatic sync. GitHub remains canonical for project artifacts, Notion Applied/General for technology research, not model chat history.

## 4. Small-first deployment phases (proposal only)

| Gate | What changes | Proof demanded | Stop/fallback |
|---|---|---|---|
| G0 — **User approves THIS PLAN only** | Adopt two-surface goal and narrow first pilot target; no install/code on device | D-015 intent recorded, source-set and consent boundaries agreed | Remains documentation if user does not approve technical work |
| G1 — **Host readiness, separately authorized READ-ONLY local inspection** | Verify installed Jan version (if any), actual Shell toggle/MCP permissions, host extras, model/candidate access, available RAM and local interpreter. Check ChatGPT Desktop MCP surface/eligibility without invoking tools. No model download or software installation. | Real screenshots/recorded version/host permission controls, current RAM snapshot and eligible configuration. No invented measures | Jan fails → assess Cherry or host-neutral local control before installing anything |
| G2 — **Bounded tool adapter, separately authorized repo code change** | Build one narrow portable `stdio` MCP adapter, policy/config and offline fixtures/tests around **existing CAP-006**. No web service, broad Shell or new canonical DB. Pin explicit package/dependency only after check; prefer built-in where feasible. | Fixed-schema rejects forbidden params; deny/no-match/stale SHA/timeout tests; no arbitrary path/exec; no code downloaded at runtime | Security/compatibility gates FAIL → halt |
| G3 — **First local user-chat pilot, separately authorized Windows run** | Hook exactly **one** allowed `djmrn_document_lookup` to approved host, one model candidate if legally/technically available, no permanent scheduler/Agent. User sends message and approves actual call **in chat**; old two local non-sensitive test-copy docs only. | A real Persian message invokes worker without user terminal, cited real file/line/SHA, meaningful fail-closed denial and offline/error case, before/during/after RAM and time measured. Record source consent and audit. | Jan tool controls/model/RAM/privacy fail → do not force; Cherry or another host after review |
| G4 — **ChatGPT Desktop as second surface, separate account/egress consent** | Verify actual account/product supports local MCP tools and narrow grants in desired UI; configure the same tool contract via approved transport. May launch a distinct stdio adapter process; not duplicate policy engine. | Real permitted chat request→same underlying CAP→cited answer; no unsupported scope expansion, no unauthorized source transfer, clear offline/denied receipts | Not enabled/eligible → leave ChatGPT integration BLOCKED/DEFERRED, first local surface intact |
| G5 — **Future capabilities** | Add B CSV/data and C official-source evidence as separate permissioned tools, optional specialist personas and durable workflows on demonstrated need | Per-tool scopes, provenance and approvals; cost/ram/region measured | No heavy always-resident manager, multiple agents, telemetry, cloud host or vector index by default |

**No user-facing routine PowerShell** in successful G3/G4. A one-time authorized technical developer setup or smoke test may still use a terminal but is not the normal user experience. G1/G2/G3/G4 are individually consent-gated: choosing both surfaces NOW is not blanket approval for Windows checks, downloading/upgrading Jan, installing Python packages, creating code, adding MCP servers, using remote tokens/keys, transferring data or running the first pilot.

## 5. HARD stop / low-RAM / availability criteria

- Historical laptop is Windows 11 Pro, Ryzen 5 3500U/Vega 8, 8GiB physical and ~5.88GiB Windows-visible, with constrained available RAM and not always-on. **NO RAM, context latency, inference quality or tool-call capability of Jan v0.8.7, Cherry or any model on this exact PC was measured in WA0003**. A release installer download size is not runtime RAM. Measure realistically under current browser/desktop load before/after; no invented MB guarantee.
- First pilot permits **one active document lookup**, one chat host, at most one required model active, and on-demand adapter/worker, with timeouts, user cancel and ability to unload. Do not require local model if the permitted inference alternative is better; any remote inference requires actual lawful access, privacy/retention disclosure, quota/overage check and consent.
- If laptop is off, its **local documents and workers are inaccessible** to either chat surface. ChatGPT may converse about general data or previously authorized cloud material, but cannot pretend it searched offline local files. Remote execution or source synchronization is **new later architecture requiring consent and validated privacy/legal cost**.
- Security stop conditions: default Shell ON not safely off; Autoapprove on; broad tools cannot be removed; arbitrary path accepted from model; approval cannot be enforced outside model; surprising network/telemetry; source SHA mismatch; unapproved data egress; machine RAM pressure; untrusted executable/package origin; unknown legal or cost eligibility.
- If full local intelligent chat is infeasible on this device, do not accept an empty chat text box/keyword field as meeting REQ-012. State blocker and compare a lower resource or cloud-eligible surface without silently weakening user goal.

## 6. Decision requested from user AFTER reviewing this proposal

**Suggested user confirmation:** 
> «طرح یک هستهٔ ابزار مشترک برای هر دو محیط را می‌پذیرم؛ برای نخستین پایلوت، گفت‌وگوی مستقل ویندوز با نامزد Jan را به‌صورت مشروط در اولویت بگذار. تا قبل از بررسی ایمنی و RAM روی دستگاه، هیچ نصب یا اجرای عملی انجام نده. اتصال ChatGPT را در مرحلهٔ دوم، با همان قرارداد ابزار و بررسی قابلیت حساب، دنبال کن.»

The user can instead prioritize verifying ChatGPT Desktop first without invalidating the shared-core architecture. **Status until explicit reply: PROPOSED / AWAITING USER APPROVAL OF DUAL-SURFACE PLAN and subsequent specific activity permissions**.

## 7. Sources and evidence classes (not a new vendor research round)

- **User fact:** selected "both ChatGPT and independent chat"; previous explicit instruction forbids PowerShell as daily UX.
- **Prior project verified engineering evidence:** [CAP-006 real two-file test NEW-V0004](../06-tests-and-evidence/logs/NEW-V0004-20261021.md); only the bounded local deterministic search backend passed.
- **Work research:** [WA0003](../04-work-research-bridge/responses/WA0003.md), Work commit `77a52a70d0cda9a510707a26eb2e3cebdface3b6`, blob `7b3178b72a630ddcfe304d936169a31770d76936`; independently [reviewed](../04-work-research-bridge/reviews/WQ0003.md). Live Applied Notion Index v0.48/General/Mission and official Jan/Cherry releases were checked in that review.
- **Current primary docs rechecked 2026-10-21:** [Jan local MCP/permissions](https://docs.jan.ai/desktop/integrations/mcp-servers), [Jan v0.8.7 release](https://github.com/janhq/jan/releases/tag/v0.8.7), [ChatGPT Desktop MCP](https://learn.chatgpt.com/docs/extend/mcp), [Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels), [MCP security and transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports).
- **Engineering inference, not selected or measured:** shared logical tool contract and one source policy used by two independently launched stdio hosts can avoid a new central resident service; whether it minimizes RAM on the specific PC depends on real measured model/host overhead. No external account eligibility was observed and no code/Windows test was performed in this planning turn.

## 2026-10-21 USER G0 DESIGN APPROVAL & PLUS PLAN GATE — critical update

**User response:** `اوکی اما تا جایی که من می دونم ام سی پی چت جی پی تی برای اکانت پرئ هست نه پلاس که من هستم`.

**Interpretation:** User **approved the high-level staged dual-surface architecture (G0)** while explicitly correcting that their present ChatGPT subscription is **Plus, not Pro** and asking us not to assume custom MCP support. This **does not authorize** any of G1 readiness checks on Windows, G2 code/adapter, G3 local program installation/test, G4 custom MCP/plugin/tunnel creation, billing, token generation or upload of source excerpts.

### Official sources checked again 2026-10-21

1. [OpenAI Help — Connecting custom MCP servers in ChatGPT](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt), accessed 2026-10-21: **full custom MCP in ordinary ChatGPT web** (including write/modify) is available under **Business and Enterprise/Edu** permissions; **Pro** can connect custom MCP servers with **read/fetch** permissions; **Plus** is **not listed** in that custom-connection entitlement. Thus `PLUS CUSTOM MCP = NOT DOCUMENTED/NOT VERIFIED`, not a baseline dependency. No reason to claim Plus has Pro's developer features. Do not assume upgrading to Pro yields full write MCP.
2. [OpenAI ChatGPT Learn — Model Context Protocol](https://learn.chatgpt.com/docs/extend/mcp?surface=cli): describes configurable local `stdio` MCP servers in ChatGPT desktop/Codex host with shared configuration; its generic **capability documentation does not establish access for this user's exact Plus app/account and normal chat mode**.
3. [OpenAI ChatGPT Learn — Plugins](https://learn.chatgpt.com/docs/plugins): installed **ready-made/bundled MCP plugins** can be usable in Chat or Work on supported accounts and surfaces, sometimes Desktop-only. **Using an installed plugin is not the same as creating arbitrary custom MCP connections**. It may provide useful ChatGPT interactions and GitHub/Notion/other approved data sources on Plus; it does **not** prove direct local DJMRN CAP-006 access.
4. [OpenAI Help — Connecting custom MCP servers](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt) also notes ChatGPT web custom MCP requires remote endpoint or a supported tunnel; it does not directly read `stdio` Windows user files; a Secure MCP Tunnel requires separate authorization/Platform runtime and is not a substitute for missing plan entitlements.
5. **No account dashboard, plugin-add privileges or Windows ChatGPT Desktop/Codex MCP settings were tested.** Product rollout/workspace rules and plan entitlements change: only actual user-observed UI or authoritative plan-specific official documentation can advance status; do not invent account rights from generic API docs.

### Corrected project gates and priorities

- **G0 — USER APPROVED DESIGN GOAL:** one host-independent shared capability + trusted permission core for **both eventual chat surfaces**; local conversation first, ChatGPT path second. This is an *architecture direction approved*, **NOT** a final Jan/version/model choice.
- **G1 — NOT AUTHORIZED YET:** read-only Windows host readiness and current resource check, with one-time permission; Jan conditional, Cherry fallback. Tool permission control and local tool-call model must be proven before G2/G3.
- **G4 Plus ChatGPT integration — ON HOLD / ENTITLEMENT-DEPENDENT:** do **not** presume custom self-created MCP servers/connectors in Plus work in regular ChatGPT chat. Only non-invasive capability inspection may be **proposed**, including whether *the actual Plus desktop/Codex or already-available plugins* expose a suitable authorized tool path. Any real local bridge, plugin creation/config, tunnel or remote activation awaits separate entitlement/security/privacy approvals.
- **Portable core remains valid even if ChatGPT Plus has no custom MCP path**: it exposes a fixed typed tool contract, not a proprietary Jan extension; a future eligible ChatGPT/plugin surface could use its own transport without rebuilding A/B/C. ChatGPT can still help as a separate research/planning conversational interface through its **available** supported tools, while direct user-local CAP-006 access stays `BLOCKED` until demonstrated.
- **Free-first / no automatic Pro upgrade:** do not recommend purchase solely for anticipated MCP, since Pro grants read/fetch custom connections, not full unrestricted MCP; Business/Enterprise/Edu availability also depends on workspace administration and eligibility, and plan upgrades have financial and regional costs. The project should still progress with independent local host if lawful and the actual RAM/model security gates pass.

**Next explicit user authorization still needed:** permission for **read-only G1 inspection of Jan/Windows resource and MCP/ChatGPT Plus feature availability**, no install/upgrade. No new evidence of running a tool or connecting Plus was created by this documentation update.
