import json
import sys
from pathlib import Path
from validate_visual_record import validate
from validate_visual_coverage import validate_coverage

def validate_pack(root):
 root=Path(root);records=sorted((root/'diagram-records').glob('*.json'))
 if not records:
  exemption=root/'visual-not-applicable.json'
  if exemption.is_file():
   try:
    decision=json.loads(exemption.read_text(encoding='utf-8'))
    if isinstance(decision,dict) and all(isinstance(decision.get(k),str) and decision[k].strip() for k in ('reason','scope','evidence')):return validate_coverage(root,[])
   except (ValueError,OSError):pass
  return ['Visual completion unverified: no diagram records or justified non-applicability record']
 errors=[];ids=set();loaded=[]
 for path in records:
  try:
   record=json.loads(path.read_text(encoding='utf-8'));loaded.append(record)
   structural_errors=validate(record,root)
   if structural_errors:
    errors.extend(f'{path.name}: {e}' for e in structural_errors)
    continue
   if record.get('diagram_id') in ids:errors.append('Duplicate diagram ID')
   ids.add(record.get('diagram_id'))
   for name,check in record.get('validation',{}).items():
    if not isinstance(check,dict) or check.get('status')!='PASS': errors.append(f'{path.name}: completion check {name} is not PASS')
   if not record.get('rendered_outputs'):errors.append(f'{path.name}: rendered outputs absent')
  except (OSError,ValueError,TypeError,KeyError) as e:errors.append(f'{path.name}: invalid record: {e}')
 errors.extend(validate_coverage(root,loaded))
 return errors

if __name__=='__main__':
 errors=validate_pack(sys.argv[1]);print('\n'.join(errors) if errors else 'PASS: visual record structures');sys.exit(bool(errors))
