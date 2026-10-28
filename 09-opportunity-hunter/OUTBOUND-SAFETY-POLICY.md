# OH-10 / outbound contact safety policy (2026-10-28)

Status: DESIGN ONLY. No automated sending enabled. Approval of a draft is not authorization for unrestricted recurring sends.

## Confirmed freelancermap limits
Official pricing and help pages confirm Basic: 10 applications per month; Premium: unlimited applications. Basic also has a separate limit of replying to up to 3 paid-client contact requests. Sources:
https://www.freelancermap.com/pricing/freelancer
https://www.freelancermap.com/help.html
Terms forbid spam and excessive infrastructure load: https://www.freelancermap.com/term-and-conditions.html

## Per-site policy record
For each site/account store: plan, verified source URL and checked date, monthly application quota, quota reset policy (unknown until verified), separate messaging limits, eligibility restrictions, automation permission, user-approved send mode, cooldown, daily ceiling, and suspension/error state. Unknown quota/permissions => HOLD, not assumed unlimited.

## Outbound gating
Default mode DRAFT_ONLY; each application must be individually reviewed and approved by user; one approval authorizes only one target and one exact message. Sending implementation remains DISABLED until platform permission and safe method are verified. Five minutes is a *minimum spacing preference*, not proof of platform permission or ban avoidance; never use timed bulk sends to evade anti-spam. Do not send identical generic proposals. Do not retry automatically on uncertain send status, CAPTCHA, 429, warning, or account restrictions. Record SENT only on verified success; otherwise UNKNOWN_SEND requiring manual reconciliation. Idempotency key: site/account/project/action. Count pending/reserved/confirmed sends against a conservative local budget; reconcile with platform's displayed remaining quota. Stop at the stricter limit. Never exceed plan limits; do not infer quota reset as calendar month.

## Next steps
Finish OH-10 detail-store migration separately from outbound actions. Build site policy config and read-only eligibility report before any send adapter.
