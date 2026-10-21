# MAIL-P001 — actual observed evidence / reproducibility

**2026-10-21 | Environment:** temporary isolated model container, Linux, Python 3.13.5, no external network calls, no GUI/browser, no user's Windows access.

## Exact steps performed

1. WQ0005/WA0005 research context and coordinator's KB-0012 independently available from previously GitHub-verified conversation; no new real account actions.
2. Constructed completely fabricated English/Persian `synthetic_inbox.json`: 20 email records + 6 portal records, all links under `https://fixture.example/`. Four repeated `offer_id` values cross-source; two portal-only entries.
3. Implemented pure-standard-library `mail_triage_v0.py` with minimal deterministic classification, sparse price extraction, origin ID grouping and a Persian Markdown report. It has no request/login/send code.
4. Executed `python -m unittest -v test_mail_triage_v0.py`: **7 tests, PASS**, in 0.003 seconds shown in execution transcript (timing is container-only and not a Windows benchmark).
5. Executed `python mail_triage_v0.py > ACTUAL_SYNTHETIC_REPORT.md`; output counts below; content is preserved, not reconstructed from a proposed run.
6. Checked `analyze` counts and no-send/no-real-account flags. These flags describe application design; **not** a penetration/security audit.

## Observed result

`input_count=26; source_counts={email:20, portal:6}; unique_offers=22; categories={OPPORTUNITY_REVIEW:8, FOLLOW_UP:4, OTHER:4, BLOCKED_OR_VERIFY:4, NEEDS_REVIEW:2}`.

## Seven test cases

- ۲۶ برچسب مرجع سازگار با قواعد fixture؛ نتیجه مبتنی بر دادهٔ طراحی‌شده توسط نویسنده است، نه دقت واقعی.
- علامت‌گذاری دستور غیرقابل اعتمادِ داخل متن؛ بدون هیچ تابع ارسال.
- ادغام ۴ تکرار ایمیل/پورتال و اولویت‌دادن به شرح کامل‌تر ساختگی پورتال.
- استخراج مبلغ از متن بدنه نه عنوان (چهار مورد بررسی‌شده).
- رد URL غیرساختگی برای جلوگیری از اشتباه در دادهٔ آزمایش.
- رد شناسهٔ رکورد تکراری.
- ایجاد گزارش فارسی ساختگی، کنترل عدم اتصال/ارسال.

## Methodological gaps

- A ChatGPT/Gmail supervised: **NOT RUN ON SAME CORPUS**.
- B Email Triage demo: **NOT INSTALLED / NOT RUN**.
- C deterministic stdlib: **TESTED-SYNTHETIC**, not Windows verified or production.
- No real email, OAuth, IMAP, browser, portal account, CAPTCHA, SMS OTP or external network touched.
- No claim of API costs measured, functional thread completeness, real phishing detection, Persian model accuracy, model selection, live eligibility, user-laptop RAM or mail send safety.

## Artifact hashes and Git receipt

See `FILE-SHA256.json` for SHA256 digests (self-generated after artifacts are stable). **A GitHub commit is a separate event requiring successful GitHub connection and explicit readback.** If connector unavailable, mark `NOT COMMITTED` and avoid claiming persistence.
