#!/usr/bin/env python3
"""Design-only, offline structural contract check. This is NOT runtime/authorization certification."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))

schema=load('schemas/hub-record.schema.json')
Draft202012Validator.check_schema(schema)
examples=load('examples/valid-records.json')
validator=Draft202012Validator(schema,format_checker=FormatChecker())
for name,example in examples.items():
 assert example['kind']==name
 validator.validate(example)
 print('PASS valid',name)

# Deliberate failures prove denied/corrupt payload cannot sneak past structural checks.
negatives={
 'no_contract_version':{k:v for k,v in examples['TASK_SUBMISSION'].items() if k!='contract_version'},
 'unauthorized_unknown_field':{**examples['TASK_SUBMISSION'],'permission':'ALL'},
 'invalid_state':{**examples['TASK_RECORD'],'status':'EVERYTHING_APPROVED'},
 'bad_digest':{**examples['APPROVAL_RECORD'],'payload_sha256':'not-a-digest'},
 'worker_wrong_kind':{**examples['WORKER_RESULT'],'kind':'SOMETHING_ELSE'},
 'wrong_locale':{**examples['TASK_SUBMISSION'],'locale':'en-US'}
}
for label,bad in negatives.items():
 errors=list(validator.iter_errors(bad))
 assert errors,label
 print('PASS rejected',label,errors[0].message[:140])

spec=load('openapi/hub.openapi.json')
assert spec['openapi'].startswith('3.1')
assert spec.get('security')==[{'sessionAuth':[]}]
expected={'/v1/tasks','/v1/tasks/{task_id}','/v1/dispatches','/v1/worker-results','/v1/capabilities','/v1/approvals/{approval_id}/decision','/v1/tasks/{task_id}/events'}
assert expected==set(spec['paths'])
for path,obj in spec['paths'].items():
 for method,detail in obj.items():
  if method=='parameters':continue
  assert method in ('post','get')
  assert detail['operationId']
  assert '403' in detail['responses']
  if method=='post':
   ref=detail['requestBody']['content']['application/json']['schema']['$ref']
   file,*frag=ref.split('#')
   assert (ROOT/'openapi'/file).resolve().is_file()
   if frag:
    d=load((ROOT/'openapi'/file).resolve().relative_to(ROOT)); cur=d
    for el in frag[0].lstrip('/').split('/'): cur=cur[el]
    assert isinstance(cur,dict)
 print('PASS API',path)

manifest=load('manifest.v1.json')
assert manifest['status']=='DESIGN_COMPLETE_PENDING_APPROVAL_NO_DEPLOYMENT'
assert manifest['authority']['task_ledger']=='djmrn_hub'
print('PASS manifest reviewed, version',manifest['version'])
print('STRUCTURAL TESTS PASSED; NO RUNTIME, A2A TCK, MCP INTEROP, AUTH, CRASH OR WINDOWS TEST PERFORMED')