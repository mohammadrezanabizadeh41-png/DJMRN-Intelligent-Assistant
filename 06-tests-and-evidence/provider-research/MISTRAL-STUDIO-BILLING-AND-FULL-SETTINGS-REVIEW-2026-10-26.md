# Mistral Studio — billing snapshot and full settings audit queue
Date: 2026-10-26
Source: user screenshots of Mistral Studio Home, account menu, and Billing.

## Verified account state
- Signed in to Mistral Studio with Default Workspace visible.
- Billing: Credits **€0.00**.
- Payment methods: **No payment method added yet**.
- Auto Recharge: **Disabled**; requires payment method to enable.
- Billing information has Add action; Redeem a code exists.
- No evidence of a purchase or activated paid tier.
- API key creation entry visible on Home/API Keys menu, but key creation not yet confirmed.
- Actual API free plan, quotas, eligible models and exact limits: **UNKNOWN**.

## User instruction — full settings recheck later
Revisit **all** settings and account/workspace controls after initial onboarding, including:
- Organization, Workspace, Profile, Admin settings, Billing, Security and account controls.
- API Keys, active models, usage and rate limits.
- Agents, Audio, Batches, Document AI/OCR, Workflows, Secrets Manager.
- Connectors, Libraries, Files, Prompts, Skills and other available menu items.
- Document settings as observed vs settings changed; do not assume access or free status from menu visibility.
- Check free-tier terms, data retention, provider limits, whether a one-time purchase increases free quotas (do not assume OpenRouter policy applies).

## Governance
- No payment method, paid upgrade, auto recharge, or secret publication without user approval.
- Do not store account identifiers or API key secrets in repository.
- Next immediate step: inspect API Keys and active plan/limits, then model inventory; later comprehensive settings audit.
