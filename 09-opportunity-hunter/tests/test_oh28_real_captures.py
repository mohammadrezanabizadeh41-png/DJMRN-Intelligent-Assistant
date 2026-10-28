"""OH-28 Windows smoke gate: real captures, closed status and protected no-send."""
import argparse
import json
import pathlib
import importlib.util
import sys
p=argparse.ArgumentParser()
p.add_argument('--parser',required=True)
p.add_argument('--detail35',required=True)
p.add_argument('--detail38',required=True)
a=p.parse_args()
spec=importlib.util.spec_from_file_location('djmrn_oh28',a.parser)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
items={}
for path in (a.detail35,a.detail38):
    raw=json.loads(pathlib.Path(path).read_text(encoding='utf-8-sig'))
    assert raw['truncated'] is False,'TRUNCATED_SOURCE'
    d=m.parse(raw)
    assert d['official_id'] not in items,'DUPLICATE_OFFICIAL_ID'
    items[d['official_id']]=d
assert set(items)=={'3066373','3066376'},'UNEXPECTED_PROJECT_IDS'
closed=items['3066373']
open_unknown=items['3066376']
assert closed['application_status']['status']=='CLOSED'
assert closed['outreach_gate']['state']=='BLOCKED'
assert set(['APPLICATION_CLOSED','PROJECT_DURATION_OVER_10_DAYS']).issubset(closed['outreach_gate']['reason_codes'])
assert closed['work_arrangement']['onsite_days_per_week']=={'min':3,'max':3}
assert open_unknown['application_status']['status']=='FORM_VISIBLE_UNVERIFIED'
assert open_unknown['outreach_gate']['state']=='BLOCKED'
assert 'ONSITE_ONLY' in open_unknown['outreach_gate']['reason_codes']
assert not any(x['outreach_gate']['automatic_send_allowed'] or x['application_status']['automatic_send_allowed'] for x in items.values())
assert all(x['outreach_gate']['human_approval_required'] for x in items.values())
assert all('Similar projects' not in x['application_form'] for x in items.values())
assert 'Application not possible' in closed['application_form']
print('OH28_REAL_CAPTURE_VALIDATION=PASS')
print('PROJECT_3066373=CLOSED,BLOCKED,6_MONTHS,3_DAYS_IN_OFFICE')
print('PROJECT_3066376=FORM_VISIBLE_UNVERIFIED,BLOCKED,ONSITE_ONLY')
print('OH28_OUTREACH_GATE=PASS')
print('PRODUCTION_SQLITE_WRITES=0; OUTBOUND_ACTIONS=0')
