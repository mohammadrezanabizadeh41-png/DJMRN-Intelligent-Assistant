"""OH-16 conservative, offline shortlist for scarce application quota. No outbound."""
import argparse,json
from pathlib import Path

def assess(p):
    reasons=[]
    if p.get("employment") is True:reasons.append("EMPLOYMENT_NOT_PROJECT")
    if p.get("duration_days") is not None and p["duration_days"]>10:reasons.append("DURATION_OVER_10_DAYS")
    if p.get("estimated_hours") is not None and p["estimated_hours"]>100:reasons.append("HOURS_OVER_100")
    if p.get("requires_unavailable_work_authorization") is True:reasons.append("WORK_AUTHORIZATION")
    if p.get("on_site_required") is True:reasons.append("ON_SITE_REQUIRED")
    if reasons:return {"decision":"NOT_SUITABLE","reasons":reasons,"may_use_application_quota":False}
    missing=[]
    if p.get("duration_days") is None:missing.append("DURATION_UNKNOWN")
    if p.get("estimated_hours") is None:missing.append("HOURS_UNKNOWN")
    if p.get("net_usd_per_hour") is None:missing.append("BUDGET_UNKNOWN")
    if p.get("remote_eligible") is not True:missing.append("REMOTE_ELIGIBILITY_UNVERIFIED")
    if p.get("requirements_match") is not True:missing.append("SKILLS_MATCH_UNVERIFIED")
    if missing:return {"decision":"NEEDS_DETAILS","reasons":missing,"may_use_application_quota":False}
    if p["net_usd_per_hour"]<5:return {"decision":"NOT_SUITABLE","reasons":["RATE_BELOW_MINIMUM"],"may_use_application_quota":False}
    return {"decision":"READY_FOR_HUMAN_REVIEW","reasons":[],"may_use_application_quota":False}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--profile",required=True)
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    cfg=json.loads(Path(args.profile).read_text(encoding="utf-8-sig"))
    assert cfg["site"]=="freelancermap"
    assert cfg["outbound"]["site_monthly_limit"]==10
    assert cfg["outbound"]["global_spacing_seconds"]==300
    assert cfg["outbound"]["send_enabled"] is False
    if not args.self_test:raise SystemExit("SELF_TEST_REQUIRED")
    cases=[
        ({"duration_days":180,"on_site_required":True},"NOT_SUITABLE"),
        ({"duration_days":180,"requires_unavailable_work_authorization":True},"NOT_SUITABLE"),
        ({"title":"Video editing"},"NEEDS_DETAILS"),
        ({"duration_days":5,"estimated_hours":30,"net_usd_per_hour":8,"remote_eligible":True,"requirements_match":True},"READY_FOR_HUMAN_REVIEW"),
        ({"duration_days":5,"estimated_hours":30,"net_usd_per_hour":3,"remote_eligible":True,"requirements_match":True},"NOT_SUITABLE")
    ]
    for item,expected in cases:
        result=assess(item)
        assert result["decision"]==expected,(item,result)
        assert result["may_use_application_quota"] is False
        print(json.dumps(result,ensure_ascii=False))
    print("OH_16_SHORTLIST_SELF_TEST=PASS; CASES=5; APPLICATIONS_USED=0; DB_WRITES=0; OUTBOUND_ACTIONS=0")
if __name__=="__main__":main()
