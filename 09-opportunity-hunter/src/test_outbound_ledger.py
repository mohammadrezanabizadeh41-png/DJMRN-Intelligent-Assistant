"""OH-12 isolated outbound usage ledger tests; never opens production DB or sends."""
import sqlite3,tempfile
from contextlib import closing
from datetime import datetime,timezone,timedelta

SCHEMA="""CREATE TABLE outbound_attempts (
 id INTEGER PRIMARY KEY, site TEXT NOT NULL, account TEXT NOT NULL,
 project_key TEXT NOT NULL, state TEXT NOT NULL
 CHECK(state IN ('RESERVED','SENT','UNKNOWN_SEND','FAILED_CONFIRMED')),
 created_utc TEXT NOT NULL, updated_utc TEXT NOT NULL,
 UNIQUE(site,account,project_key))"""

def usage(db,site,account,now):
    month=now.strftime("%Y-%m")
    day=now.date().isoformat()
    active=("RESERVED","SENT","UNKNOWN_SEND")
    rows=db.execute("SELECT site,account,project_key,state,updated_utc FROM outbound_attempts").fetchall()
    counted=[r for r in rows if r[3] in active]
    site_rows=[r for r in counted if r[0]==site and r[1]==account]
    times=[]
    for r in counted:
        t=datetime.fromisoformat(r[4].replace("Z","+00:00"))
        if t.tzinfo is None:raise ValueError("NAIVE_TIMESTAMP")
        times.append(t.astimezone(timezone.utc))
    return {"site_month_count":sum(1 for r in site_rows if r[4][:7]==month),
      "site_day_count":sum(1 for r in site_rows if r[4][:10]==day),
      "global_last_send_or_unknown_utc":max(times).isoformat() if times else None}

def main():
    now=datetime(2026,10,28,16,30,tzinfo=timezone.utc)
    with tempfile.TemporaryDirectory(prefix="djmrn-oh12-") as td:
        with closing(sqlite3.connect(td+"/test.sqlite3")) as db:
            db.execute(SCHEMA)
            def add(site,account,key,state,minutes):
                t=(now-timedelta(minutes=minutes)).isoformat()
                db.execute("INSERT INTO outbound_attempts(site,account,project_key,state,created_utc,updated_utc) VALUES(?,?,?,?,?,?)",(site,account,key,state,t,t))
            for i in range(8):add("freelancermap","basic","project-"+str(i),"SENT",120+i)
            add("freelancermap","basic","pending","RESERVED",15)
            add("freelancermap","basic","uncertain","UNKNOWN_SEND",10)
            add("other","basic","cross-site","SENT",2)
            add("freelancermap","basic","confirmed-failed","FAILED_CONFIRMED",1)
            db.commit()
            u=usage(db,"freelancermap","basic",now)
            assert u["site_month_count"]==10,u
            assert u["site_day_count"]==10,u
            assert datetime.fromisoformat(u["global_last_send_or_unknown_utc"])==now-timedelta(minutes=2),u
            try:
                add("freelancermap","basic","pending","SENT",0)
                raise AssertionError("DUPLICATE_ALLOWED")
            except sqlite3.IntegrityError:db.rollback()
            assert db.execute("SELECT COUNT(*) FROM outbound_attempts").fetchone()[0]==12
            print("OH_12_LEDGER_TEST=PASS")
            print("MONTHLY_COUNT=10; DAILY_COUNT=10; GLOBAL_LAST_EVENT_FROM_OTHER_SITE=YES")
            print("RESERVED_AND_UNKNOWN_COUNTED=YES; CONFIRMED_FAILURE_EXCLUDED=YES")
            print("DUPLICATE_PREVENTED=YES; TEMP_DATABASE_ONLY=YES; PRODUCTION_WRITES=0; SENDS=0")
if __name__=="__main__":main()
