# KB-0012 — Browser-first email, Gmail and freelance-account copilot: alternative product routes

**2026-10-21 | CURATED / SELECTIVE PRIMARY VERIFICATION / ACCEPTED-PARTIAL / NOT SELECTED**
Raw original [WA0005](../../04-work-research-bridge/responses/WA0005.md), Work commit `69b60c557501b7c909353cd3201d092311bfc35a`, Git blob `c3ec981d2fb79e8999b8829b6e8ad84c78054868`; [independent review with Gmail erratum](../../04-work-research-bridge/reviews/WQ0005.md); SOURCE-REGISTER `SRC-0014`. Scope USER goal, not a chosen software installation.
Keywords: Gmail, Email Triage, Octopus Mail, OpenSidekick, WebBrain, Automa, browser RPA, cloud browser, OAuth, 12-hour digest, Persian triage, freelance opportunities, API cost, Windows RAM, مرورگرمحور, پیگیری ایمیل.

## User value and separable layers
First useful assistant = full Gmail body/thread and selected associated opportunity/site details → source-cited Persian triage/report → contextual follow-up and drafts, with external actions approval-gated. User prefers browser-first if less costly/complex, but avoids premature rejection of reliably read-only APIs.

**Transport:** current connected Gmail viewer, regular Gmail browser/manual tab, scoped third-party browser extension/DOM reader, Gmail REST readonly, OAuth IMAP, ready SaaS connector. A no-code/browser-facing UI can still use Google's API in background.
**Execution/UX:** simple deterministic local rules + chat; Email Triage ready local browser UI; Octopus Mail IMAP desktop client; Automa/Playwright for one authorized website; optional OpenSidekick/WebBrain agent only when justified; source citation/state/reporting separate.
**Uptime:** Laptop ON+internet=local browser works; ON without internet=only pre-saved data; OFF/asleep=external independently online hosted worker/browser is necessary, not a browser tab left open on laptop.

## Candidate families and independent checked facts
| Example | Original source | Conditional role | Blocking uncertainty |
|---|---|---|---|
| Email Triage | https://github.com/seb-krols/email_triage | No-account deterministic **demo** and local UI, approval workflow; compare before building everything | Live OAuth write-capable; full threads/attachments, Persian, incremental RAM unknown |
| Octopus Mail | https://github.com/CFGPeter/octopus-mail | Local-first IMAP/SMTP, separate account-level agent rights; home server option | Unsigned/early client; provider scopes, full workflow and production/security not proven |
| OpenSidekick/WebBrain | https://github.com/esterhuizen/opensidekick ; https://github.com/webbrain-one/webbrain | Chat-in-browser side panel, site read/actions and model integration | Broad debugger/host access and unknown Persian/RAM, secret/session risks |
| Automa or Playwright | https://github.com/AutomaApp/automa ; https://playwright.dev/docs/auth | Deterministic repeatable read of a **site explicitly permitted by its operator** | Site ToS, login, dynamic HTML, approval, selector drift, cookie custody |
| Cloudflare Browser Run/Browserbase | https://developers.cloudflare.com/browser-run/limits/ ; https://www.browserbase.com/pricing | Short separately hosted jobs with published free allowances | Cloudflare Free 10 minutes/day; Browserbase Free 1 browser hour; **no verified full free private 12h service**, region/privacy/session/scheduler/model unknown |
| Gmail REST readonly | https://developers.google.com/workspace/gmail/api/reference/quota ; https://developers.google.com/workspace/gmail/api/auth/scopes | Source-stable complete message/thread IDs with incremental history | Restricted OAuth, developer project/region, token scope/storage; user access NOT checked |
| Workflow sources | https://www.activepieces.com/pieces/gmail ; https://n8n.io/workflows/ | Reuse structure/draft/approval logic without mandatory server install | Template is not proof of secure live approval or free AI; licence/credit/RAM gates |

Other **Work-only provisional identities**, not independently audited as runnable: miel, EmailSignal, WebOperator, MILA, Nanobrowser, Multi-Inbox, Puppetflow, Workflow Use, KIMI++, Gecko Agent, Open Assistant and additional unqualified leads in report's matrix. Browserbase/Automa/Playwright are not necessarily new General tech identities; do not assign new TECH IDs based on this project research.

## Mandatory official Gmail quota correction (2026-10-21)
**WA0005 §7.2 method costs 60/120 for messages.get/threads.get are contradicted by** https://developers.google.com/workspace/gmail/api/reference/quota **current 20/40**. Same sample => `2*(30*20+2+5)=1,214 units/day` (two runs/day, 30 new messages/run, one history+list per run), initial 1000 messages + two lists `20,010`, 30 extra complete thread gets per run `2,400`. Quota threshold 80 million units/day no additional charge is not developer eligibility, guaranteed zero provider billing under all future rules or approval to activate. Gmail readonly is Restricted. Report remains immutable; cite [review](../../04-work-research-bridge/reviews/WQ0005.md) for corrected calculations.

## Next gate
Recommend comparing **identical synthetic corpus** of 20–30 example mails/threads + mock job dashboards: existing supervised chat (no extra host), Email Triage demo, a lightweight deterministic page/mail parser or Automa/Playwright fixture. Compare full-body coverage, historical thread link, recipient and attachments, Persian decision relevance, duplicate alerts, budgets/payment eligibility/unknown flags, changed site description, non-send approval, RAM measured only with separate Windows consent, true recurring cost. No source/extension/model or technical stack selected.
Then separately authorize (a) one narrow real Gmail read-only route, (b) one lawful site read-only account, (c) draft/send and (d) laptop-OFF service after entitlement and security proof. G1 Jan remains PARTIAL; previously tested CAP-006 searches files only.

Related: [KB-0007](KB-0007-ready-made-workflow-products.md), [KB-0011](KB-0011-cross-forge-radar-source-map.md), [REQ-012](../../02-project-management/CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md), [TASK-0017](../../02-project-management/TASK-REGISTER.md), [Notion Applied Mission](https://app.notion.com/p/3fdc8c6846908167a77feab9564dc66d).
