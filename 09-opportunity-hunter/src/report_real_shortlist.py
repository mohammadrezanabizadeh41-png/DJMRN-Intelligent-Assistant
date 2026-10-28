"""OH-17: real SQLite read-only shortlist, conservative evidence handling."""
import argparse,json,sqlite3,sys
from pathlib import Path
from collections import Counter
from contextlib import closing
sys.path.insert(0,str(Path(__file__).resolve().parent))
from report_title_triage import classify

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True)
    a=p.parse_args()
    dbpath=Path(a.database).resolve(strict=True)
    with closing(sqlite3.connect("file:"+dbpath.as_posix()+"?mode=ro",uri=True)) as db:
        db.execute("PRAGMA query_only=ON")
        if db.execute("PRAGMA quick_check").fetchone()[0]!="ok":raise RuntimeError("DB_INTEGRITY")
        rows=db.execute("""SELECT o.id,o.title,o.canonical_url,o.status,d.structured_json
          FROM opportunities o LEFT JOIN opportunity_details d ON d.opportunity_id=o.id
          WHERE o.source_site='freelancermap' ORDER BY o.id""").fetchall()
    counts=Counter()
    for oid,title,url,status,raw in rows:
        title_class=classify(title)
        reasons=[]
        detail=json.loads(raw) if raw else None
        if detail:
            months=detail.get("duration_months")
            if isinstance(months,(int,float)) and months>=1:reasons.append("DURATION_MONTHS_OVER_10_DAYS")
            modes=detail.get("work_mode_header") or []
            if "On-site" in modes:reasons.append("ON_SITE_LISTING")
            if "WORK_MODE_CONFLICT" in (detail.get("warnings") or []):reasons.append("WORK_MODE_CONFLICT")
        if reasons:
            decision="NOT_SUITABLE_OR_CONFLICT"
        elif title_class=="LIKELY_UNRELATED":
            decision="LOW_PRIORITY_TITLE_ONLY"
        else:
            decision="NEEDS_DETAILS"
        counts[decision]+=1
        print(json.dumps({"id":oid,"title":title,"url":url,"status":status,
          "has_detail":bool(detail),"title_triage":title_class,
          "decision":decision,"reasons":reasons,
          "application_recommended":False},ensure_ascii=False))
    print("OH_17_REAL_READ_ONLY_REPORT=PASS")
    print("TOTAL="+str(len(rows))+"; DETAIL_ROWS="+str(sum(bool(r[4]) for r in rows)))
    for k in ("NOT_SUITABLE_OR_CONFLICT","LOW_PRIORITY_TITLE_ONLY","NEEDS_DETAILS"):
        print(k+"="+str(counts[k]))
    print("APPLICATION_RECOMMENDATIONS=0; PRODUCTION_WRITES=0; OUTBOUND_ACTIONS=0")
if __name__=="__main__":main()
