# Research Exchange Ledger — واحد، immutable IDs
| ID | Request | Response | Coordinator review | State | Next |
|---|---|---|---|---|---|
| T0001 | [request](requests/T0001.md) | [response](responses/T0001.md) | [verified review](reviews/T0001.md) | **PASS / COORDINATOR READBACK VERIFIED 2026-10-20** | Define precise WQ0001 topic before research |
| WQ0001 ↔ WA0001 | NONE (not allocated) | NONE | NONE | NOT STARTED | after T0001 success; only after use-case/gap review |

**قانون تغییر:** بعد از هر create/fetch با شواهد commit SHA و URL، وضعیت مربوط را update و READ BACK کنید؛ log «تحویل شد» فقط با فایل واقعی Work معتبر است. اگر Work یک پاسخ partial/failed ایجاد کرد، گزارش را overwrite نکنید؛ gap را ثبت و با amendment/new request پیگیری کنید.

**واژه‌نامه:** DRAFT (not on GitHub), REQUEST-COMMITTED, DISPATCHED, RESPONSE-COMMITTED, VERIFIED-RECEIPT, REVIEWED, ACCEPTED-PARTIAL, ACCEPTED, BLOCKED, SUPERSEDED. هر update با زمان و evidence.
