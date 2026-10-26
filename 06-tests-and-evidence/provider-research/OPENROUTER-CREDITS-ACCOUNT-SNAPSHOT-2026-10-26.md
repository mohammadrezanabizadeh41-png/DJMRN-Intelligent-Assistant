# OpenRouter Credits account snapshot — 2026-10-26
Source: user screenshot, Account → Credits.

## Verified visible facts
- Total Available: **$0.00** (Pay-as-you-go balance).
- Recent Transactions: **No results**, **0 transactions**.
- Buy Credits / Add Credits offered, but no purchase made.
- Auto Top-Up section displays **Add a Payment Method**; no evidence that auto-top-up is enabled or payment method attached.
- Crypto toggle under Buy Credits is off; this is not relevant to free-only API use.
- Do not store account email or other PII in repository.

## Interpretation
- No purchased credit balance is visible; `$100` shown on a separate Default API key is a key limit, NOT funded credit.
- Free model catalog screenshots show 29 model entries marked `(free)` with $0 token prices, but user-specific free request access and quota remain **UNTESTED**.
- Dedicated `DJMRN-OmniRoute` API key has lifetime credit limit $0.000; unclear whether this blocks free calls.

## Pending
- Check official current free-tier API request limits and data/privacy conditions.
- Test one `:free` API call with the dedicated key without exposing it.
- Retrieve exact model IDs and availability; integrate into OmniRoute only after testing.
- No paid service or top-up authorized.
