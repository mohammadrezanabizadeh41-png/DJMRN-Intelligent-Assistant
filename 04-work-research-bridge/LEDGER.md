# Research Exchange Ledger — واحد، immutable IDs
| ID | Request | Response | Coordinator review | State | Next |
|---|---|---|---|---|---|
| T0001 | [request](requests/T0001.md) | [response](responses/T0001.md) | [verified review](reviews/T0001.md) | **PASS / COORDINATOR READBACK VERIFIED 2026-10-20** | Define precise WQ0001 topic before research |
| WQ0001 ↔ WA0001 | [request](requests/WQ0001.md) | [WA0001](responses/WA0001.md) | [coordinator review](reviews/WQ0001.md) | **RESPONSE VERIFIED / REVIEWED / ACCEPTED-PARTIAL (SHA receipt errors) 2026-10-20** | D-009 proposed; awaiting user decision; no build |

| WQ0002 ↔ WA0002 | [WQ0002 committed](requests/WQ0002.md) | **NOT RECEIVED** — [expected path](responses/WA0002.md) | NOT REVIEWED | **REQUEST-COMMITTED / AWAITING USER DISPATCH TO WORK — 2026-10-21** | User dispatches exact WQ0002 and Work reads Applied Notion + independent sources; only Work creates WA0002 and reports commit+readback; coordinator audits actual WA before decisions. WQ commit `ba8763e02ff11bf4a49b2a88f809670d84f9d944`; request blob `bb108c752a9f8c51cf63df9c98a5546ff0d08ebd` |

**قانون تغییر:** بعد از هر create/fetch با شواهد commit SHA و URL، وضعیت مربوط را update و READ BACK کنید؛ log «تحویل شد» فقط با فایل واقعی Work معتبر است. اگر Work یک پاسخ partial/failed ایجاد کرد، گزارش را overwrite نکنید؛ gap را ثبت و با amendment/new request پیگیری کنید.

**واژه‌نامه:** DRAFT (not on GitHub), REQUEST-COMMITTED, DISPATCHED, RESPONSE-COMMITTED, VERIFIED-RECEIPT, REVIEWED, ACCEPTED-PARTIAL, ACCEPTED, BLOCKED, SUPERSEDED. هر update با زمان و evidence.
