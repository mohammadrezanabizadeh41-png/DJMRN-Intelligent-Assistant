"""DJMRN OH-02 deterministic, read-only opportunity screening."""
import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

def screen(item, policy):
    reasons = []
    hold = []
    site = str(item.get("site", "")).lower()
    config = policy.get("sites", {}).get(site)
    if config is None or site == "iranian_template":
        return {"decision": "HOLD_FOR_REVIEW", "reasons": ["UNKNOWN_OR_TEMPLATE_SITE"]}
    market = policy["markets"][config["market"]]
    kind = item.get("kind")
    if kind not in ("project", "employment"):
        return {"decision": "HOLD_FOR_REVIEW", "reasons": ["UNKNOWN_OPPORTUNITY_KIND"]}
    if item.get("explicit_incompatible") is True or item.get("unpaid") is True:
        reasons.append("EXPLICIT_INCOMPATIBILITY_OR_UNPAID")
    if kind == "employment":
        if config["employment_allowed"] is False:
            reasons.append("EMPLOYMENT_NOT_ALLOWED_ON_SITE")
        elif config["employment_allowed"] is None:
            hold.append("EMPLOYMENT_POLICY_UNDEFINED")
        hold.append("EMPLOYMENT_REQUIRES_HUMAN_REVIEW")
    else:
        for field, limit in (("estimated_hours", policy["global_project_limits"]["max_hours"]),
                             ("calendar_days", policy["global_project_limits"]["max_calendar_days"])):
            value = item.get(field)
            try:
                n = Decimal(str(value))
                if not n.is_finite() or n <= 0:
                    hold.append("INVALID_" + field.upper())
                elif n > limit:
                    reasons.append(field.upper() + "_EXCEEDS_LIMIT")
            except (InvalidOperation, TypeError):
                hold.append("MISSING_OR_INVALID_" + field.upper())
        floor = market.get("project_hourly_floor")
        rate = item.get("net_effective_hourly_rate")
        if floor is None:
            hold.append("MARKET_HOURLY_FLOOR_UNDEFINED")
        else:
            try:
                n = Decimal(str(rate))
                if not n.is_finite() or n < 0:
                    hold.append("INVALID_NET_RATE")
                elif n < Decimal(str(floor)):
                    reasons.append("NET_RATE_BELOW_FLOOR")
            except (InvalidOperation, TypeError):
                hold.append("NET_RATE_UNAVAILABLE")
    if reasons:
        return {"decision": "REJECT", "reasons": reasons + hold}
    if hold:
        return {"decision": "HOLD_FOR_REVIEW", "reasons": hold}
    return {"decision": "ACCEPT_FOR_REVIEW", "reasons": ["PASSED_DETERMINISTIC_GATES"]}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
    if policy.get("schema_version") != "djmrn.oh.policy.v1":
        raise ValueError("Unsupported policy version")
    item = json.loads(Path(args.input).read_text(encoding="utf-8"))
    print(json.dumps(screen(item, policy), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
