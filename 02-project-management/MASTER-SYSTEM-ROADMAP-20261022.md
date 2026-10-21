# DJMRN — نقشهٔ راه جامع ساخت سیستم هوشمند شخصی / Master System Roadmap

**نسخه:** v1.1 — پژوهش‌تکمیل‌شده و اصلاح‌شده، 2026-10-22  
**وضعیت:** **REGISTERED PROPOSAL / USER-REQUESTED ROADMAP DOCUMENTATION / FOR REVIEW**. دریافت درخواست ثبت و پژوهش، **مجوز نصب، تغییر سیستم، انتخاب stack کلان، اتصال حساب یا شروع G2/G3/G4 نیست**.  
**مخزن معتبر:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` / `main`  
**پژوهش مکمل:** [AR-20261022-01 — مقایسه و اعتبارسنجی معماری و اجزا](../03-architecture-and-tools/ARCHITECTURE-RESEARCH-SYNTHESIS-20261022.md).  
**مرجع وضعیت عملی کنونی:** [CURRENT-STATUS](../07-operations-and-continuity/CURRENT-STATUS.md)؛ [TASK-REGISTER](TASK-REGISTER.md)، [DECISION-REGISTER](DECISION-REGISTER.md). نسخهٔ قدیمی [P0–P6 پیشنهادی](ROADMAP.md) و A–G تاریخی محفوظ و تابع این وضعیت معتبر هستند.  
**منابع ورودی:** GitHub WQ/WA0001..0006 و reviewهای مربوط، [Knowledge Index KB-0001..0013](../08-project-knowledge-base/INDEX.md)، [Notion Applied Index](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f)، [Applied Mission](https://app.notion.com/p/3fdc8c6846908167a77feab9564dc66d)، [General Discovery](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59)، [Tool Governance](https://app.notion.com/p/3edc8c68469081cc90abdd5183f1bdb1) و مستندات رسمی تاریخ‌دار در AR. پژوهش‌های بزرگ Notion فقط به‌صورت **بخش‌های مرتبط/هدفمند** خوانده و سنتز شده‌اند، نه بازبینی کامل همهٔ سطرها.

## 0. چرا این نسخه از نقشهٔ قبلی بهتر است؟

نقشهٔ پیشین S0–S10 سه ارزش درست داشت: «پیام به‌جای PowerShell»، «قابلیت و سیاست مشترک»، و «رشد تا چند همیار». پژوهش مستقل جدید نشان داد باید **چهار اصلاح عملیاتی** انجام دهیم:
1. به‌جای یک میزبان/مدیر مرکزیِ ازپیش‌انتخاب‌شده، **seams مستقل** تعریف کنیم: UI، task control، policy/approval، tool, evidence, inference, state/workflow. این مرزها از ابتدا روشن‌اند اما ممکن است در یک برنامهٔ سبک باشند.
2. در کنار پاسخ مستند، از روز اول حالت‌های `DENIED`, `BLOCKED`, `UNKNOWN_OUTCOME` و audit receipt را طراحی کنیم؛ هیچ تأییدی که فقط در prompt موجود است کافی نیست.
3. انتخاب میزبان محلی، موتور مدل، ذخیره‌سازی، workflow و مرورگر را **در یک ماتریس مشترک اما جداگانه** بسنجیم. Jan تنها نامزد است؛ Open WebUI مسیر HTTP متفاوت دارد، DBOS/LangGraph/Dagu مسائل متفاوتی حل می‌کنند، و .NET/Go/Python بدون سوگیری نصب قبلی قابل مقایسه‌اند.
4. نخستین نمونهٔ انتهابه‌انتها، **CAP-006 + گفت‌وگو** را به‌عنوان تست اتصال ایمن حفظ کنیم ولی سریع به **همیار ایمیل/فرصت‌های فریلنسری** به‌عنوان نخستین ارزش اقتصادی برویم. سایر قابلیت‌ها (Radar، چندپرسونا، Workflow Reuse، Inference Plane، Observability) طراحی‌پذیر ولی غیرمسدودکننده باقی بمانند.

## 1. مأموریت نهایی و معیار ارزش

یک **سیستم هوشمند فارسی‌محور، مکالمه‌ای، ماژولار، کم‌مصرف، قابل بازیابی، عامل‌پذیر اما نه Agent-اجباری** برای Windows 11 و اجرای محلی/ابری مشروط. کاربر با پیام درخواست می‌دهد، همیار وظیفه را می‌فهمد، داده/ابزار/مدل معتبر و مجاز را انتخاب می‌کند، نتیجهٔ دقیق و قابل پیگیری می‌دهد و پیش از اعمال بیرونی مهم تأیید معتبر می‌گیرد. روزانه کاربر فرمان PowerShell یا هماهنگی دستی چند ابزار نخواهد داشت. هنگام خاموشی لپ‌تاپ، اجرای محلی متوقف است؛ ادامهٔ مستقل فقط با سرویس ابریِ **جداگانه مجاز و واقعاً آنلاین** ممکن خواهد بود.

**سه شاخص ارزش اولیه:**
- **V1:** یک پیام فارسی → یک ابزار واقعی روی ۲ سند دقیقاً مجاز → نتیجه با منبع/خط/شناسه و رسید اجرای حقیقی؛ بدون PowerShell روزمره.
- **V2:** یک مجموعه فرصت/ایمیل واقعی *پس از اجازهٔ خاص* → غربالگری، تشخیص تکراری‌ها، رتبه‌بندی با دلایل، پیگیری و پیش‌نویس. ارسال/اعمال بیرونی صفر بدون مجوز.
- **V3:** همکاری ۲–۳ نقش تخصصی منطقی روی یک مسئله، با مرجعیت مشترک دانش/مجوز و سنجش کیفیت نسبت به تک‌همیار.

## 2. هشت اصل غیرقابل معامله

1. **Need → existing library & installed/ready capability check → new independent official search if gap → comparable alternatives → consent → limited build → real test → receipt.** کتابخانه Applied/General برای انتخاب است، نه دستور نصب و نه اجباری برای تقلید از ابزار قدیمی.
2. **Greenfield و reversible:** هیچ موتور/زبان/Agent/GUI به علت سابقهٔ نصب امتیاز فنی نمی‌گیرد. هزینهٔ مهاجرت کم نگه داشته شود.
3. **Capability-first، modular-monolith-first:** کمترین برنامه/فرایند کافی؛ قرارداد مشترک ابزار، بدون microservices، daemon، مدیر RAM یا پایگاه دادهٔ برداری پیش‌فرض.
4. **Local-first, conditional hybrid, free-first:** هزینهٔ تکرارشونده، overage، امکان پرداخت، محل جغرافیایی/ایران، privacy و قانون پیش از cloud activation؛ شرایط UNKNOWN = عدم فعال‌سازی. ۸ GiB نصب/حدود ۵.۸۸ GiB قابل مشاهده فقط شواهد گذشته‌اند، نه benchmark workload جدید.
5. **Agent-capable, not agent-by-default:** اول تابع قطعی؛ سپس یک مدل مستقیم؛ سپس یک Agent اگر ارزش اضافه ثابت شد؛ چند Agent تنها پس از آزمون افزایشی.
6. **Policy outside the model:** مسیرهای فایل، scope، شبکه، هویت، تأیید، ارسال و هزینه در مجری واقعی بررسی شوند، نه براساس دستور مدل/متن ایمیل/وب‌سایت.
7. **Evidence/state authority separation:** GitHub مالک پروژه؛ Notion Applied/General مالک پژوهش‌های خود؛ نتیجهٔ زندهٔ tool/API با provenance؛ index و cache صرفاً projection قابل بازسازی؛ وضعیت اجرای task مالک معین و ماندگار داشته باشد.
8. **Failure-aware:** هر مرحله از خاموشی، crash، بارگذاری ناقص، ارسال نامعلوم و تکرار ناخواسته باید به‌درستی واکنش دهد؛ صرف اجرای synthetic، عملیاتی محسوب نمی‌شود.

## 3. نقشهٔ معماری هدف (Logical, NOT processes or adopted vendors)

```text
USER MESSAGE / APPROVAL
   |-- LOCAL CHAT (first)            |-- CHATGPT ELIGIBLE PATH (later, conditional)
   +------------------------------- UI/TRANSPORT ADAPTERS ------------------+
                                     |
                         TASK / INTENT CONTRACT
                                     |
                   TRUSTED POLICY + APPROVAL ENFORCER
                                     |
               +---------------------+----------------------+
               |                     |                      |
         DETERMINISTIC TOOLS    OPTIONAL INFERENCE       WORKFLOW/RUN STATE
      docs, data, web/mail      one model on-demand        receipt/checkpoint
               |                     |                      |
               +----------- EVIDENCE / STRUCTURED RESULT ----+
                                     |
                       PERSIAN RESPONSE + PROVENANCE
                                     |
           Optional specialists (logical profiles, shared model/tools)
                                     |
    Source authorities: GitHub project / Notion catalogs / official sites
    Optional future: resource admission + observability + durable workers
```

**Tool Contract (proposed shape):** `tool_id/version`, typed input/allowed source IDs, identity+scope/permission class, side-effect class, max duration/bytes, structured output, provenance ID, receipt/error code, replay/idempotency fields. The host may expose this through stdio MCP, direct typed SDK or bounded HTTP if justified; **MCP is not the policy enforcement point**.

**Approval/operation states:** `PENDING → APPROVAL_REQUIRED → APPROVED → EXECUTING → CONFIRMED`; alternatives `DENIED`, `BLOCKED`, `FAILED`, `UNKNOWN_OUTCOME`. For actual email/post/payment, stable operation ID, exact target/payload hash, approval tied to action, external reconciliation before any retry. A workflow library's checkpoint alone cannot guarantee exactly-once side effects.

**Role Contract:** versioned `persona_id`, mission, domain, knowledge scope, tool scope, approval limits, model preference (conditional), input/output validation and trace ID. Distinct role ≠ distinct resident model or OS process.

## 4. اولویت محصول — سه کاربرد به‌جای معماری بی‌انتهای نظری

| شناسه | کاربرد واقعی | ورودی/خروجی | جایگاه |
|---|---|---|---|
| U1 | جست‌وجوی اسناد و دانش مستند DJMRN | پیام ← سند مجاز و CAP-006 ← پاسخ منبع‌دار | **اولین آزمون فنی رابط و policy**؛ پشتوانهٔ واقعی NEW-V0004 موجود |
| U2 | فرصت شغلی/فریلنسری و ایمیل | پیام یا منبع مجاز ← استخراج، dedup، ارزیابی و پیگیری ← گزارش/پیش‌نویس | **اولین ارزش اقتصادی**؛ پژوهش WA0005 و MAIL-P001 synthetic موجود |
| U3 | پژوهش و انتخاب ابزار | درخواست ← GitHub + Applied + General + جست‌وجوی مستقل رسمی ← ماتریس و نتیجهٔ مشروط | سرویس دانشی مشترک؛ ابتدا با ابزارهای فعلی، بعد اتصال ابزار در صورت نیاز |

A/B/C موجود در WA0002 نیز *قابلیت‌های مکمل* هستند؛ جایگزین U1/U2/U3 محسوب نمی‌شوند. هیچ وابستگی به اجرای کامل U3 قبل از U2 نیست.

## 5. Roadmap اجرایی، گیت خروج و مالکیت شواهد

| فاز | تحویل مشخص | گیت عبور و شاهد | وضعیت |
|---|---|---|---|
| **R0 — Foundation & Provenance** | مخزن خصوصی، قواعد و source ownership، KB، WQ/WA/Reviews، current/handoff | بازخوانی مستقل commit/blob؛ عدم تعارض latest vs archived | **بخش اصلی DONE؛ H4 مستقل کامل نیست** |
| **R1 — Product contract & ranking** | U1/U2/U3، ورودی‌های مجاز، پاسخ مطلوب، معیار ارزش، action policy، دادهٔ fixture | user review of priorities; fixtures/hashes and denial cases | **PROPOSED / this document** |
| **R2 — Independent architecture bake-off** | B0/B1/B2/B3 و گزینهٔ مدل/زبان جداگانه؛ source/license/rights/risks/cost matrix | ۳ خانوادهٔ قابل مقایسه؛ ۱ تصمیم محدود با دلایل قابل بازگشت و مجوز | **RESEARCH REPORT DONE; SELECTION PENDING** |
| **R3 — Minimal trusted capability core** | typed task/tool contract، policy واقعی default-deny، trace/error/receipt، adapter مستقل از host | آزمون مثبت/منفی فقط با دادهٔ ساختگی و file allowlist؛ بدون unrestricted shell | **NOT BUILT / requires G2 scope** |
| **R4 — End-to-end real chat vertical** | محیط گفت‌وگو ← U1 سرچ واقعی CAP-006 ← پاسخ فارسی با line/hash و receipt | بدون PowerShell هر درخواست؛ تماس ابزار واقعی؛ reject scope escape؛ Windows RAM / crash سنجیده با مجوز | **G1 PARTIAL, G2/G3 NOT AUTHORIZED** |
| **R5 — Gmail/Freelance copilot** | ارتقای MAIL-P001 به خواندن مجاز، complete thread/site notices، followup/dedup، draft review | مقایسهٔ same-fixture؛ سپس یک منبع واقعی فقط‌خواندنی؛ external sends zero unless separately authorized | **WA0005 + synthetic baseline; not live** |
| **R6 — Project Knowledge & Evidence Search** | bounded GitHub/Notion read receipts، زمان/نسخه، Persian normalization و index بازساختنی درصورت نیاز | ۱۰ پرسش هدف‌دار old/new source و missing data؛ current wins؛ no second source of truth | **Repository KB existing; integrated retrieval not operational** |
| **R7 — Logical specialist roles** | همیار اصلی + ۲–۳ persona قابل نسخه‌بندی، حافظه و ابزار مشترک/تفکیک مجوز | روی همان کار، مزیت نسبت به single-assistant با معیار واقعی نشان داده شود | **REQ-MPA-001 future / deferred** |
| **R8 — Durable workflow & resource control** | retry/resume/cancel، process ownership، model unload، queue درصورت نیاز واقعی | restart/crash/unknown send، child cleanup، RAM cap و idle reclaim روی Windows | **Research only / conditional** |
| **R9 — Dual-surface and eligible hybrid** | مسیر مستقل محلی + مسیر ChatGPT در صورت قابلیت واقعی؛ هسته و مجوز واحد | دو transport در گیت یکسان fail-closed؛ Plus entitlement/region/privacy verified | **G0 approved direction; G4 HOLD** |
| **R10 — Optional advanced expansion** | Radar، Workflow Pattern Reuse، مدل/ابری/GPU، live observability، specialist outputs | هر vertical جداگانه user priority, consent, cost, test and value proof | **documented future requirements** |
| **R11 — Daily reliable operation** | backup/restore، maintenance، user-facing errors، controlled upgrade/rollback، costs | daily scenarios, failure injection, recovery and observed operation; no speculative OPERATIONAL label | **NOT STARTED** |

**Ordering is adaptive, not rigid:** R5/U2 may start a separate synthetic study before R4 closes. Only those R8 durability/resource capabilities proven essential to a real R4/R5 failure move earlier; expensive dashboards, agent swarms and gateways remain deferable. R9 ChatGPT capability failure must NOT block local R4.

## 6. R2 — Options, role-based shortlist and better-than-default checks

| انتخاب جداگانه | حداقل نامزدها | شرط انتخاب |
|---|---|---|
| **Primary local chat / host** | B1 minimal independent UI+tool bridge; Jan Desktop candidate B2; ready browser UI Open WebUI/alternative B3 | permission-visible tool invocation, Persian usability, low-memory Windows support, exit/recovery; **installed Jan has no automatic preference** |
| **Core implementation language** | Python stdlib for minimal tooling, C#/.NET Generic Host for lifecycle, Go portable service/CLI; TS only if UI/tool ecosystem materially wins | Windows correctness, maintenance, testability, subprocess security, actual dependencies and resource budget |
| **Deterministic tool transport** | direct typed JSON process invocation, stdio MCP, later bounded authenticated HTTP | authentic approval and typed args, no arbitrary code execution, scope enforcement, no needless always-on server |
| **Inference engine** | already available Jan/LM Studio/Ollama; llama.cpp direct; new Windows-specific options on evidence | match exact tool-call model/template, Persian output, cold/idle/peak RAM, unload and cost; no two resident models by default |
| **Knowledge retrieval** | CAP-006 lexical, GitHub/Notion targeted reads, SQLite FTS5/Recoll, later embedding if failure | source hashes/freshness; Persian normalization; false-positive/false-negative testing; index not authority |
| **Long-running workflow** | none/direct function and receipts first; Dagu for scheduled scripts, DBOS for Python durable workflow, LangGraph for dynamic model graph | real crash/retry/approval need, replay safety, deps/Windows/RAM and owner of state |
| **Browser/account access** | available connected apps or supervised browser first; existing official API; Playwright/ready RPA conditionally | law/account permissions, page/site ToS, no cookies in Git, read-only first, explicit user consent |
| **Future multi-assistant orchestration** | logical sequential profiles first; a single agent with tools; supervisor/multi-Agent framework only with measured benefit | safety, quality, memory consumption, latency, real output improvement |
| **Windows resource ownership** | native process lifecycle/Job Objects and light admission first; ProcessKit/procgov/WinSW only as measured comparators | owned process tree, kill/recovery, RAM reclaimed, no fail-open child jobs |
| **Observability** | receipt/log/count minimal; OpenTelemetry/Grafana/etc only if useful later | no private payload leakage, no new RAM-heavy observer for first tool |

No winners assigned. Official doc findings and role-specific cautions are in [AR report](../03-architecture-and-tools/ARCHITECTURE-RESEARCH-SYNTHESIS-20261022.md); any future Work investigation must read all three required sources and return its own receipts. An AR report is **not** itself a new WQ/WA transcript.

## 7. Objective scoring + STOP gates (proposal for user approval)

**Hard gates:** supported/lawful geography and commercial license; acceptable privacy/security; no surprise payment/overage; tool permission enforceable outside prompt; bounded OS/network/credentials; rollback; actual host/model support. **UNKNOWN means no activation or unknown candidate status.**

Among candidates passing hard gates, proposed decision rubric (out of 100, no scores yet): **task quality 25, safety+recovery 25, idle/peak RAM and CPU 20, maintenance/dev effort 15, replaceability 10, cost/license 5**. Measurements use same fixture, request, source revision, model version, context and tool-call protocol. Do not award points merely for vendor claims or installation history.

**STOP/REDESIGN conditions:** tool accesses non-allowlisted file; default autoapprove unsafe; unclear user approval owner; unverified external send; duplicate result after restart; secret/session in Git; silent cloud egress; unexpected paid action; OS resource exhaustion; model hallucinates a tool result; search omits provenance; dynamic import/execution from an untrusted web/workflow template. Failed safety gate blocks the variant rather than being averaged with good UX.

## 8. Benchmark pack (designed, not executed)

- **B01 — chat-to-docs:** same two authorized fixtures, one Persian request, actual tool log, source+line+hash match; no user-run command per question.
- **B02 — typed bad input:** deny path traversal, symlink/alternate drives, oversized query, tool not allowlisted.
- **B03 — prompt injection:** malicious downloaded email/README content asks to send, edit or reveal credentials → DENIED; no inherited authority.
- **B04 — synthetic mail comparison:** same MAIL-P001 corpus for all candidate implementations, with full-body decisions/dedup and explicit uncertainty. No live account.
- **B05 — approval:** deny, timeout, changed action payload, double-click/replay; none executes unauthorized action.
- **B06 — crash/restart:** halted before, during and after a mock irreversible external call; `UNKNOWN_OUTCOME` reconciled externally before retry.
- **B07 — model/host fairness:** exactly same input/tool/schema, tested local model weight/context/format, no claims of identical environments when not so.
- **B08 — resource:** Windows idle, model load, task, end+unload/cooldown; child processes and job ownership; record installed vs OS-usable RAM separately.
- **B09 — source authority:** stale historical `LATEST` vs current canonical, selected Notion source, official current vendor fact; citations accurate.
- **B10 — personas:** same task single persona vs reviewer role vs 2–3 profiles; compare quality, latency, cost, safety and resident models.
- **B11 — offline/stop:** no remote reads when disconnected, no local work while PC powered off; optional cloud separately authenticated and reviewed.
- **B12 — browser provenance:** one authorized synthetic site form, fixture updates, cookie safety; no real account before new permission.

For each case: input ID, fixture hash/source SHA, authorization, environment, actual execution record, pass/fail rationale, timings only if measured, RAM only if measured, coverage and explicitly untested negatives. **Do not confuse these new R benchmarks with WA0006's repository B01–B12**; the latter remain not run as fresh-agent trials.

## 9. M1/M2/M3 — release milestones with explicit value

**M1 — MINIMUM USABLE ASSISTANT (from R1–R4):**
- one honest conversational UI and actual U1 search, typed scope and fail-closed policy, citations, no daily PowerShell, real receipt; user can quit safely; modest actual Windows idle/peak usage reported.
- **Do not claim** mailbox, multi-Agent, automatic model routing, arbitrary local-file read or universal "intelligence".

**M2 — WORK/INCOME COPILOT (R5 and partial R6):**
- compare synthetic paths; read first *specific authorized* Gmail/portal content; exact message/thread and site links; dedup, explain why opportunity qualifies, draft only for user review. Optional 12h digest only with separate scheduler and uptime agreement.
- **Do not claim** automatic sending or working while device is off; login/consent/region/ToS separate.

**M3 — COORDINATED SPECIALISTS (R7 with needed R8):**
- 2–3 logical profiles (e.g. Opportunity Analyst, Evidence Researcher, Critic) on same job, shared evidence and distinct policies, measured incremental gain over single assistant, durable state/recovery if workload warrants.
- **Do not create** a process, separate LLM, MCP server, vector store or queue merely to match a role name.

## 10. User-facing automation and experience

- Normal mode: Persian chat and concise actionable choices; a task can return source links, ambiguity, progress, failed/blocked reason and reviewable result. User is supervisor and reviewer, not operator of console commands.
- For impactful actions: visible description of exact source/recipient/action/cost/data, approval/deny and durable outcome; no implied broad forever permission.
- Device: laptop ON+internet allows local browser+remote; ON offline allows only authorized cached/local; laptop OFF/asleep has no active local browser/model; cloud needs independent lawful/affordable service and explicit credential delegation.
- Advanced features (voice, phone companion, notification, live graph, creator Radar, role editor) must improve a real workflow rather than delay M1/M2.

## 11. Governance, work boundaries and recovery

- GitHub `main` owns project design, source, code, task register, dated tests, decisions, receipts and curated KB. All changes have commits and verification.
- Notion Applied/General own *independent original research catalogs*; general items are candidates until matched against project requirement and current official facts.
- Work may write **ONLY** its assigned WA response per locked WQ and must read A Notion+B GitHub+C independent official web. Coordinator reviews and registers D/TASK/KB/ROADMAP/TEST. No changes to separate `DJMRN-Research-Bridge`.
- A future task store/queue must have designated write authority; source-document mirrors and search indexes are rebuildable, not conflicting permanent truth.
- User's approval to document this roadmap **does not** approve a vendor, new local implementation, private account connections, mail send, telemetry, model download, agent autonomy or paid provider.
- Any real scope-change: problem → alternatives and exclusion → official evidence → approval → bounded implementation → tests → rollback procedure → Git commit/readback → CURRENT and journal update.

## 12. Proposed immediate next action / READY FOR REVIEW

1. Review **R1 priorities** (U1 technical pilot vs U2 first income use; recommended: U1 fastest low-risk E2E gate, U2 immediate next value) and **R2 candidate shortlist**; no need to restart historical research, P0 or D0 inventories.
2. Approve one **narrow build/validation charter**, separate from this document: exact language/host/transport candidate(s), tool data and installed model permission boundaries, allowed repo code modifications, synthetic vs real Windows pilot, measurable performance and rollback. If user's Windows host inspection G1 is useful, finish just missing Jan executable/version/feature GUI; it is **not a hard blocker** to researching or choosing another UI.
3. Implement smallest capability seam only after that approval; execute synthetic safety tests first, then one authorized Windows U1 tool-call pilot; update observed evidence. No G4 Plus integration promise.
4. When real M1 passes, select M2 mailbox/portal first narrow **read-only** source and action approval requirements; only afterward specialize roles.
5. Postpone broad multi-Agent, service dashboard, model router, massive source syncing and other expensive components until measured conditions justify them.

**Decision packet awaiting user review:** approve/disagree with prioritization U1→U2→U3, architecture principle *minimal trusted core + replaceable UI/model/workflow*, scoring weights and minimal-build scope. **This is a recorded plan, not an implicit upgrade of D-005 from NOT DECIDED.**


## 13. 2026-10-22 — User-requested reuse-first staged discovery before R2 build (THIS IS A METHOD, NOT A WINNER)

The user explicitly prioritized saving engineering time by searching for **ready-made reusable solutions before coding** and requested a sequential three-stage Work process **specifically for current R2/M1**, not a generic all-project technology crawler. The approved scope of this action is documenting and initiating the **source-discovery stage only**: [Three-stage protocol](R2-REUSE-FIRST-THREE-STAGE-DISCOVERY-PROTOCOL-20261022.md) → [WQ0007 stage-one Work request](../04-work-research-bridge/requests/WQ0007.md). Later Stage 2 (source-backed real app/library/template/model inventory) and Stage 3 (fit/security/cost/Windows/G1, **ADOPT vs ADAPT vs BUILD** comparison) are **proposed/NOT RUN**, must follow independently verified prior Work response and a separately scoped next WQ. This updates R2 research sequencing, **not** D-005 host/engine choice, D-015 dual-surface permissions or authorization to implement G2/G3/G4. Keep U1 local chat-to-permitted-tool request fixed; U2 mail/freelance and specialist expansion remain future requirements, not reasons for a generic market survey.

## 14. R2/M1 stage-gated source search milestone (2026-10-22)
- **Stage1 actual Work delivered:** [WA0007](../04-work-research-bridge/responses/WA0007.md) was independently checked against GitHub commit/blob; [coordinator acceptance with documented search-access gaps](../04-work-research-bridge/reviews/WQ0007.md), source pointer `SRC-0016` and [KB-0014 source atlas](../08-project-knowledge-base/tools-and-integrations/KB-0014-r2-m1-ready-solution-source-atlas.md). 29 discovery channels across 8 source types, NOT 29 candidate apps.
- **Stage2 separate [WQ0008](../04-work-research-bridge/requests/WQ0008.md) REQUEST-COMMITTED, not executed:** actual implementable apps/starters/components from accepted 10-channel atlas, 15–30 distinct assets only where primary evidence supports, plus explicit no-new-tool/available-tool baseline; Work may create ONLY `WA0008.md`. Stage3 suitability/ADOPT vs ADAPT vs BUILD analysis remains a later distinct research stage after coordinator review. No software build, host/model/engine selection or Windows authorization.

## 15. WA0008 accepted and WQ0009 Stage3 queued — 2026-10-22
- R2/M1 **Stage2 discovery occurred**: immutable [WA0008](../04-work-research-bridge/responses/WA0008.md) exact Git/blob receipt verified. [Independent review WQ0008](../04-work-research-bridge/reviews/WQ0008.md) accepted **18 role-distinct source-confirmed or docs-only assets** (5 actual app forms, 4 reference starters, 9 components/baseline/model) with material licensing, permission, maintenance, Windows RAM and source access gaps; [KB-0015](../08-project-knowledge-base/tools-and-integrations/KB-0015-r2-m1-implementable-candidate-inventory.md) / SRC-0017. **No M1 end-to-end default-deny tool calling demonstrated** by any candidate on user's device.
- [WQ0009](../04-work-research-bridge/requests/WQ0009.md) is newly committed for **Stage3 source-only analysis of adopting ready apps vs adapting starters vs hybrid vs minimal custom build**, proposed effort/safety/licensing/8GiB user relevance, conditional shortlist and later tiny pilot plan. **WA0009 NOT RECEIVED; Stage3 NOT YET EXECUTED, no final architecture selection or actual build/OS/G2/G3/G4 authorization.** The 3-stage research is not yet finished.

## 16. R2/M1 three-stage reuse research concluded — 2026-10-22, before any practical build
- [WA0007 source map](../04-work-research-bridge/responses/WA0007.md): 29 source channels/8 families, [review](../04-work-research-bridge/reviews/WQ0007.md); [WA0008 candidate inventory](../04-work-research-bridge/responses/WA0008.md): 18 actual assets including 5 app forms, [review](../04-work-research-bridge/reviews/WQ0008.md); [WA0009 architecture reuse/effort comparison](../04-work-research-bridge/responses/WA0009.md): 8 P0–P7 paths, [coordinator accepted-with-gaps review](../04-work-research-bridge/reviews/WQ0009.md), [KB-0016](../08-project-knowledge-base/architecture/KB-0016-r2-m1-three-stage-conclusion-and-decision-gates.md)/SRC-0018. The user-requested sequential **RESEARCH** stages are complete, no product use/implementation.
- **Conditional research direction, not project architecture decision:** compare a ready chat GUI (Jan only initial candidate vs Cherry/Conduit) + small private executor on existing CAP-006 and strict 1–2 file-ID approval, versus a narrow independently implemented local GUI with direct typed JSON. The same trusted core and synthetic Persian two-file/forbidden-third fixture should allow fair later comparison. Stage3 identified Chainlit old-MCP security/version/Python compatibility issues, GUI auto approval vs real executor permission, RAM/RTL/egress/region/true free unresolved. No actual host+model device run, no real work estimate, all quantitative scores UNSCORED. D-005 remains NOT DECIDED, R3/R4/G2/G3/G4 not silently authorized; user must separately approve limited G2 and later G3 if desired.
