"""OH-03 offline net effective hourly rate calculator; amounts in one currency."""
import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

def decimal_value(value, field, positive=False):
    if value is None or isinstance(value, bool):
        raise ValueError(field + "_MISSING_OR_INVALID")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError(field + "_MISSING_OR_INVALID")
    if not result.is_finite() or result < 0 or (positive and result == 0):
        raise ValueError(field + "_MISSING_OR_INVALID")
    return result

def quote(item):
    currency = item.get("currency")
    if currency not in ("USD", "TOMAN"):
        return {"result": "HOLD_FOR_REVIEW", "reason": "UNSUPPORTED_OR_MISSING_CURRENCY"}
    try:
        gross = decimal_value(item.get("gross_amount"), "gross_amount")
        fee_percent = decimal_value(item.get("platform_fee_percent"), "platform_fee_percent")
        fixed = decimal_value(item.get("fixed_fees"), "fixed_fees")
        costs = decimal_value(item.get("other_costs"), "other_costs")
        hours = decimal_value(item.get("effective_hours"), "effective_hours", positive=True)
        if fee_percent > 100:
            raise ValueError("FEE_PERCENT_ABOVE_100")
    except ValueError as exc:
        return {"result": "HOLD_FOR_REVIEW", "reason": str(exc)}
    net = gross - gross * fee_percent / Decimal(100) - fixed - costs
    rate = net / hours
    return {"result": "CALCULATED", "currency": currency,
            "net_amount": str(net.quantize(Decimal("0.01"))),
            "net_effective_hourly_rate": str(rate.quantize(Decimal("0.01"))),
            "effective_hours": str(hours), "outbound_actions": 0}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    args = p.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8-sig"))
    print(json.dumps(quote(data), ensure_ascii=False, indent=2))
