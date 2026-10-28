"""OH-06 read-only inventory and conservative title triage."""
import argparse, json, sqlite3
from contextlib import closing
from pathlib import Path

def classify(title):
    t=title.casefold()
    relevant=("video edit","video produc","motion graphic","multimedia","music video","video creator","content creat","automation","workflow automation","windows support","desktop support","technical support","social media video")
    unrelated=("weblogic","oracle financials","devops","kafka","electronic warfare","rubrik","mfa engineer","assembly technician","gdpr","data protection","network engineer","observability engineer","project controller","swift developer","finops","cost optimisation","aws","java/react","marketo","security clearance","sc cleared")
    if any(s in t for s in relevant):return "PRIORITY_REVIEW"
    if any(s in t for s in unrelated):return "LIKELY_UNRELATED"
    return "NEEDS_DETAILS"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--database",required=True)
    args=ap.parse_args()
    dbpath=Path(args.database).resolve(strict=True)
    with closing(sqlite3.connect("file:"+dbpath.as_posix()+"?mode=ro",uri=True)) as db:
        db.execute("PRAGMA query_only=ON")
        ver=db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
        if not ver or ver[0]!="djmrn.oh.local.v1":raise RuntimeError("UNEXPECTED_SCHEMA")
        rows=db.execute("SELECT id,source_site,external_id,title,canonical_url,status FROM opportunities ORDER BY id").fetchall()
    from collections import Counter
    counts=Counter()
    print("OH_06_READ_ONLY_REPORT=PASS")
    print("TOTAL_RECORDS="+str(len(rows)))
    for oid,site,eid,title,url,status in rows:
        cat=classify(title)
        counts[cat]+=1
        print(json.dumps({"id":oid,"category":cat,"title":title,"status":status,"url":url},ensure_ascii=False))
    for cat in ("PRIORITY_REVIEW","NEEDS_DETAILS","LIKELY_UNRELATED"):
        print(cat+"="+str(counts[cat]))
    print("DATABASE_WRITES=0; OUTBOUND_ACTIONS=0")

if __name__=="__main__":main()
