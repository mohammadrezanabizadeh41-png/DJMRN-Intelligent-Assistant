# Research Exchange Ledger — واحد، immutable IDs
| ID | Request | Response | Coordinator review | State | Next |
|---|---|---|---|---|---|
| T0001 | [request ready](requests/T0001.md) | **NONE** | **NONE** | READY / NOT DISPATCHED / Work access unverified | user copies short instruction to Work |
| WQ0001 ↔ WA0001 | NONE (not allocated) | NONE | NONE | NOT STARTED | only after user approves topic and/or successful T0001 |

**قانون تغییر:** بعد از هر create/fetch با شواهد commit SHA و URL، وضعیت مربوط را update و READ BACK کنید؛ log «تحویل شد» فقط با فایل واقعی Work معتبر است. اگر Work یک پاسخ partial/failed ایجاد کرد، گزارش را overwrite نکنید؛ gap را ثبت و با amendment/new request پیگیری کنید.

**واژه‌نامه:** DRAFT (not on GitHub), REQUEST-COMMITTED, DISPATCHED, RESPONSE-COMMITTED, VERIFIED-RECEIPT, REVIEWED, ACCEPTED-PARTIAL, ACCEPTED, BLOCKED, SUPERSEDED. هر update با زمان و evidence.
