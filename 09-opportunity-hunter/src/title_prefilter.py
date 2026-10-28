"""OH-21 conservative title-only triage of real opportunities; no database writes."""
import argparse,json,re,sqlite3
from pathlib import Path
from contextlib import closing
from collections import Counter

STRONG=("video edit","video produc","motion graphic","music video","multimedia","video creator","workflow automation","desktop support","windows support")
POSSIBLE=("content design","content creat","intune","endpoint management","modern workplace","2nd line support","technical support","python","power apps","ai platform")
OTHER=("apigee","devops","kubernetes","weblogic","oracle financials","salesforce","java","rubrik","network engineer","supply chain","payments consultant","architect","swift developer","aws","mfa engineer","assembly technician")
def classify(title,has_detail):
    t=title.casefold()
    flags=[]
    if re.search(r"\b(?:6|12)\s*[- ]?months?\b",t):flags.append("LONG_TERM_IN_TITLE")
    if re.search(r"\b(?:on[- ]?site|hybrid|\d+\s*days?\s*on\s*site)\b",t):flags.append("LOCATION_RESTRICTION_IN_TITLE")
    if re.search(r"\b(?:sc cleared|sc clearance|active sc|sc clearable|security clearance)\b",t):flags.append("SECURITY_CLEARANCE_IN_TITLE")
    if re.search(r"\\(sc\\)",t) and "SECURITY_CLEARANCE_IN_TITLE" not in flags:flags.append("POSSIBLE_SC_CLEARANCE_ABBREVIATION")
    if "inside ir35" in t:flags.append("INSIDE_IR35")
    if any(x in t for x in STRONG):fit="STRONG_TITLE_MATCH"
    elif any(x in t for x in POSSIBLE):fit="POSSIBLE_TITLE_MATCH"
    elif any(x in t for x in OTHER):fit="LOW_TITLE_MATCH"
    else:fit="UNKNOWN_TITLE_MATCH"
    if "LONG_TERM_IN_TITLE" in flags or "LOCATION_RESTRICTION_IN_TITLE" in flags:
        queue="DEFER_CONSTRAINTS"
    elif fit=="STRONG_TITLE_MATCH":queue="DETAIL_PRIORITY"
    elif fit=="POSSIBLE_TITLE_MATCH":queue="DETAIL_REVIEW"
    else:queue="LOW_PRIORITY"
    if ("SECURITY_CLEARANCE_IN_TITLE" in flags or "POSSIBLE_SC_CLEARANCE_ABBREVIATION" in flags) and queue=="DETAIL_REVIEW":queue="DETAIL_REVIEW_WITH_CLEARANCE_CHECK"
    if has_detail:queue="DETAIL_ALREADY_CAPTURED"
    return {"fit":fit,"flags":flags,"queue":queue}
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True)
    a=p.parse_args()
    uri="file:"+Path(a.database).resolve(strict=True).as_posix()+"?mode=ro"
    with closing(sqlite3.connect(uri,uri=True)) as db:
        db.execute("PRAGMA query_only=ON")
        if db.execute("PRAGMA quick_check").fetchone()[0]!="ok":raise RuntimeError("DB_INTEGRITY")
        rows=db.execute("SELECT o.id,o.title,o.canonical_url,d.opportunity_id FROM opportunities o LEFT JOIN opportunity_details d ON o.id=d.opportunity_id WHERE o.source_site='freelancermap' ORDER BY o.id").fetchall()
    counts=Counter()
    for oid,title,url,detail_id in rows:
        result=classify(title,detail_id is not None)
        counts[result["queue"]]+=1
        print(json.dumps({"id":oid,"title":title,"url":url,**result},ensure_ascii=False))
    print("OH_21_TITLE_PREFILTER=PASS; TOTAL="+str(len(rows)))
    for k in ("DETAIL_PRIORITY","DETAIL_REVIEW","DETAIL_REVIEW_WITH_CLEARANCE_CHECK","DEFER_CONSTRAINTS","DETAIL_ALREADY_CAPTURED","LOW_PRIORITY"):
        print(k+"="+str(counts[k]))
    print("DB_WRITES=0; OUTBOUND_ACTIONS=0; APPLICATIONS_USED=0")
if __name__=="__main__":main()
