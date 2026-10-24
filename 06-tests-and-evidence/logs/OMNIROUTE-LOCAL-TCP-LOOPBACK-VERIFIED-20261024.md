# DJMRN — OmniRoute localhost-only TCP listener verified from user's Windows

**Date:** 2026-10-24 (user local time); **evidence level:** USER_WINDOWS_POWERSHELL_READ_ONLY_OUTPUT. **Applies only to the Windows 11 device and the moment of this test.**

## Actual Windows output
```powershell
PS C:\WINDOWS\system32> Get-NetTCPConnection -State Listen -LocalPort 20128 | Select-Object LocalAddress,LocalPort,OwningProcess

LocalAddress LocalPort OwningProcess
------------ --------- -------------
127.0.0.1        20128          6556
```

**Verdict:** `LOCAL_TCP_LISTEN_LOOPBACK_IPV4_PASS`. Windows reported one listener on port 20128 bound to IPv4 `127.0.0.1` owned by PID `6556`, with **no all-interface `0.0.0.0` or IPv6 `::` listener in this query result**. This is strong evidence that the currently running gateway API port was not directly listening on the machine's LAN interface at test time. **It does not prove any remote proxy, port-forwarding, future relaunch mode, process provenance, or API authorization.** The PID is transient, not a persistent project identity.

### Reconciliation with prior screenshots
- Endpoints UI advertised `http://localhost:20128/v1`, status Running, and an additional private LAN URL. The LAN URL's display is not evidence of LAN reachability; the actual Windows TCP bind test is more authoritative for this instant.
- Dashboard Require login ON and UI says `Password updated successfully`; IP Access Control Disabled. Since localhost-only TCP listener verified, do NOT enable whitelist/IP ACL preemptively or change Windows Defender/firewall. Continue Desktop-first.
- No providers, account secrets, paid/Free providers, tunnels or models have been activated by this observation. Previous screenshot showed **0 core chat/media models** (Web Search 28 catalog entries unvalidated).

### Remaining API auth gate
**Official vendor documentation:** https://omniroute.hagicode.com/en-US/security/inference-auth-posture/ confirms `GET /v1/models` is governed by dashboard auth rather than the distinct `REQUIRE_API_KEY` switch for inference routes. Thus a `401` on `/v1/models` **cannot establish** that `POST /v1/chat/completions` or `POST /v1/responses` requires an API key.

A subsequent **bounded, deliberately fake-model no-auth test** may be proposed using only `http://127.0.0.1:20128`, a nonexistent model ID, no credentials and a bounded timeout; test interpretation: `401` supports API auth enforcement, a routing/model-not-found error instead of 401 suggests anonymous inference requests reach the router. **This test is NOT_RUN, not permission for real inference**. Validate request intercept order and ensure no real models/providers are present before such a probe; do not use GET /v1/models as substitute. Alternatively, read an explicit authenticated status control without ever revealing environment secrets.

### Next and stop
- **NETWORK GATE:** Pass at observed instant (TCP loopback-only).
- **API AUTH:** NOT_VERIFIED.
- **MODEL/PROVIDER AND FREE-ONLY COST GUARDS:** NOT_RUN/UNKNOWN.
- **D-005:** OPEN; **G3B/M1:** CLOSED.
- No application config, secret, firewall, account, schema or paid use changed by the command.
