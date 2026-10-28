import argparse
import json
from pathlib import Path
import sys

# Under Python -I, explicitly trust only this script's own application directory.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from quote import quote
from screen import screen

def evaluate(item, policy):
    pricing = quote(item)
    candidate = dict(item)
    candidate.pop("net_effective_hourly_rate", None)
    if pricing["result"] == "CALCULATED":
        candidate["net_effective_hourly_rate"] = pricing["net_effective_hourly_rate"]
    screening = screen(candidate, policy)
    if pricing["result"] != "CALCULATED" and screening["decision"] != "REJECT":
        screening = {"decision": "HOLD_FOR_REVIEW", "reasons": screening["reasons"] + ["PRICING_" + pricing["reason"]]}
    return {"pricing": pricing, "screening": screening, "outbound_actions": 0}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--policy", required=True)
    a = p.parse_args()
    item = json.loads(Path(a.input).read_text(encoding="utf-8-sig"))
    policy = json.loads(Path(a.policy).read_text(encoding="utf-8-sig"))
    if policy.get("schema_version") != "djmrn.oh.policy.v1":
        raise ValueError("Unsupported policy version")
    print(json.dumps(evaluate(item, policy), ensure_ascii=False, indent=2))
