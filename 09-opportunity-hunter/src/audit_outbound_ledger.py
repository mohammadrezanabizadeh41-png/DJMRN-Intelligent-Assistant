"""OH-14 read-only operational ledger audit and fail-closed policy evaluation."""
import argparse,json,sqlite3,sys
from contextlib import closing
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from outbound_gate import assess

ACTIVE={"RESERVED","SENT","UNKNOWN_SEND"}
def iso(v):
    d=datetime.fromisoformat(v.replace("Z","+00:00"))
    if d.tzinfo is None:raise ValueError("NAIVE_LEDGER_TIMESTAMP")
    return d.astimezone(timezone.utc)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True)
    p.add_argument("--policy",required=True)
    p.add_argument("--site",default="freelancermap")
    p.add_argument("--account",default="basic")
    p.add_argument("--project-id",default="OH14-READ-ONLY-CHECK")
    a=p.parse_args()
    policy=json.loads(Path(a.policy).read_text(encoding="utf-8-sig"))
    now=datetime.now(timezone.utc)
    uri="file:"+Path(a.database).resolve(strict=True).as_posix()+"?mode=ro"
    with closing(sqlite3.connect(uri,uri=True)) as db:
        if db.execute("PRAGMA quick_check").fetchone()[0]!="ok":raise RuntimeError("DB_INTEGRITY")
        columns=[r[1] for r in db.execute("PRAGMA table_info(outbound_attempts)")]
        if columns!=["id","site","account","project_key","state","created_utc","updated_utc"]:raise RuntimeError("LEDGER_SCHEMA")
        rows=db.execute("SELECT site,account,project_key,state,created_utc,updated_utc FROM outbound_attempts").fetchall()
        if any(r[3] not in ACTIVE|{"FAILED_CONFIRMED"} for r in rows):raise RuntimeError("UNKNOWN_STATE")
        active=[r for r in rows if r[3] in ACTIVE]
        site_rows=[r for r in active if r[0]==a.site and r[1]==a.account]
        month=now.strftime("%Y-%m")
        day=now.date().isoformat()
        usage={"site_month_count":sum(1 for r in site_rows if iso(r[4]).strftime("%Y-%m")==month),
               "site_day_count":sum(1 for r in site_rows if iso(r[4]).date().isoformat()==day),
               "already_sent_or_unknown_for_project":any(r[0]==a.site and r[1]==a.account and r[2]==a.project_id and r[3] in ACTIVE for r in rows)}
        # RESERVED blocks quota but is not evidence of an actual send. Only SENT and UNKNOWN_SEND affect cooldown.
        send_times=[iso(r[5]) for r in rows if r[3] in {"SENT","UNKNOWN_SEND"}]
        if send_times:usage["global_last_send_or_unknown_utc"]=max(send_times).isoformat()
        decision=assess(policy,a.site,a.account,a.project_id,False,usage,now)
        print("OH_14_READ_ONLY_AUDIT=PASS")
        print("LEDGER_ROWS="+str(len(rows))+"; LOCAL_MONTH_COUNT="+str(usage["site_month_count"])+"; LOCAL_DAY_COUNT="+str(usage["site_day_count"]))
        print("ACCOUNT_QUOTA_FROM_SITE=UNVERIFIED; LOCAL_LEDGER_NOT_AUTHORITATIVE_FOR_SITE_BALANCE=YES")
        print("DECISION="+decision["decision"]+"; REASONS="+",".join(decision["reasons"]))
        if decision["decision"]!="HOLD":raise RuntimeError("FAIL_CLOSED_CHECK")
        print("PRODUCTION_WRITES=0; OUTBOUND_ACTIONS=0")
if __name__=="__main__":main()
