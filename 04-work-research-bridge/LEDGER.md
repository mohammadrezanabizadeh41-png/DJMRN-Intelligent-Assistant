# Research Exchange Ledger — واحد، immutable IDs
| ID | Request | Response | Coordinator review | State | Next |
|---|---|---|---|---|---|
| T0001 | [request](requests/T0001.md) | [response](responses/T0001.md) | [verified review](reviews/T0001.md) | **PASS / COORDINATOR READBACK VERIFIED 2026-10-20** | Define precise WQ0001 topic before research |
| WQ0001 ↔ WA0001 | [request](requests/WQ0001.md) | [WA0001](responses/WA0001.md) | [coordinator review](reviews/WQ0001.md) | **RESPONSE VERIFIED / REVIEWED / ACCEPTED-PARTIAL (SHA receipt errors) 2026-10-20** | D-009 proposed; awaiting user decision; no build |

| WQ0002 ↔ WA0002 | [WQ0002](requests/WQ0002.md) | [WA0002](responses/WA0002.md), [Work commit e567aaa](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/e567aaa845d101257b42101ceb923d7d90a21ce0), blob `614b5dd440cd824eaee042c2dbdeda4708403c78` | [Independent coordinator review](reviews/WQ0002.md), commit `3a4eef07b8cde86ae0e15dec8ab28816535b115f` | **RESPONSE VERIFIED / REVIEWED / ACCEPTED FOR DECISION SUPPORT — 2026-10-21; NO BUILD APPROVED** | Work transport correct, exact repo/main, commit changed only WA0002. Notion+official-source research receipts and code spotchecked. Next: user chooses real need **A documents / C two-source evidence / B CSV**, then authorize minimum scope of possible pilot. CAP-006 VERIFIED-REAL BOUNDED only; no install/Account/Windows execution. |

**قانون تغییر:** بعد از هر create/fetch با شواهد commit SHA و URL، وضعیت مربوط را update و READ BACK کنید؛ log «تحویل شد» فقط با فایل واقعی Work معتبر است. اگر Work یک پاسخ partial/failed ایجاد کرد، گزارش را overwrite نکنید؛ gap را ثبت و با amendment/new request پیگیری کنید.

**واژه‌نامه:** DRAFT (not on GitHub), REQUEST-COMMITTED, DISPATCHED, RESPONSE-COMMITTED, VERIFIED-RECEIPT, REVIEWED, ACCEPTED-PARTIAL, ACCEPTED, BLOCKED, SUPERSEDED. هر update با زمان و evidence.
