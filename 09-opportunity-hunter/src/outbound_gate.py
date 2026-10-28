"""OH-11 read-only outbound eligibility gate; no sending or DB mutation."""
import argparse,json,sqlite3
from contextlib import closing
from datetime import datetime,timezone,timedelta
from pathlib import Path

def parse_time(value):
    if not value:return None
    t=datetime.fromisoformat(value.replace("Z","+00:00"))
    if t.tzinfo is None:raise ValueError("TIMEZONE_REQUIRED")
    return t.astimezone(timezone.utc)

def assess(policy,site,account,project_id,approved,usage,now=None):
    now=now or datetime.now(timezone.utc)
    global_policy=policy["global"]
    rule=policy["sites"].get(site)
    reasons=[]
    if not rule:reasons.append("SITE_POLICY_UNKNOWN")
    if not approved:reasons.append("PROJECT_MESSAGE_APPROVAL_MISSING")
    if rule:
        if not rule.get("send_enabled",False):reasons.append("SEND_DISABLED")
        if rule.get("automation_permission")!="VERIFIED_ALLOWED":reasons.append("AUTOMATION_PERMISSION_UNVERIFIED")
        if rule.get("account_remaining_quota") is None:reasons.append("QUOTA_UNKNOWN")
        elif rule["account_remaining_quota"]<=0:reasons.append("QUOTA_EXHAUSTED")
        cap=rule.get("monthly_application_limit")
        if cap is not None and usage.get("site_month_count",0)>=cap:reasons.append("MONTHLY_LIMIT_REACHED")
        daily=rule.get("max_daily_applications")
        if daily is not None and usage.get("site_day_count",0)>=daily:reasons.append("DAILY_LIMIT_REACHED")
    last=parse_time(usage.get("global_last_send_or_unknown_utc"))
    if last and now-last<timedelta(seconds=global_policy["minimum_spacing_seconds"]):reasons.append("GLOBAL_COOLDOWN_ACTIVE")
    if usage.get("already_sent_or_unknown_for_project"):reasons.append("DUPLICATE_OR_UNCERTAIN_SEND")
    if usage.get("account_warning"):reasons.append("ACCOUNT_WARNING")
    return {"site":site,"account":account,"project_id":project_id,"decision":"HOLD" if reasons else "ELIGIBLE_FOR_SEPARATE_SEND_REVIEW","reasons":reasons,"minimum_spacing_seconds":global_policy["minimum_spacing_seconds"],"actual_sends":0,"database_writes":0}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--policy",required=True)
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    policy=json.loads(Path(a.policy).read_text(encoding="utf-8-sig"))
    assert policy["global"]["minimum_spacing_seconds"]==300
    assert policy["global"]["scope"]=="all_sites_all_accounts"
    if not a.self_test:raise SystemExit("SELF_TEST_REQUIRED")
    cases=[
        ("freelancermap",True,{"site_month_count":0,"site_day_count":0},["SEND_DISABLED","AUTOMATION_PERMISSION_UNVERIFIED","QUOTA_UNKNOWN"]),
        ("freelancermap",True,{"site_month_count":10},["MONTHLY_LIMIT_REACHED"]),
        ("another-site",True,{},["SITE_POLICY_UNKNOWN"]),
        ("freelancermap",False,{"global_last_send_or_unknown_utc":datetime.now(timezone.utc).isoformat()},["GLOBAL_COOLDOWN_ACTIVE","PROJECT_MESSAGE_APPROVAL_MISSING"]),
    ]
    for site,approved,usage,expected in cases:
        result=assess(policy,site,"test-account","test-project",approved,usage)
        if any(reason not in result["reasons"] for reason in expected):raise AssertionError(result)
        print(json.dumps(result,ensure_ascii=False))
    print("OH_11_GATE_SELF_TEST=PASS; CASES=4; GLOBAL_COOLDOWN_SECONDS=300; FREELANCEMAP_MONTHLY_LIMIT=10; SENDS=0; DB_WRITES=0")
if __name__=="__main__":main()
