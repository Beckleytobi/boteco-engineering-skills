"""Read-only structural checks; never claims diagram semantics or rendering passed."""
import hashlib
import json
import sys
from pathlib import Path

def validate(record, directory):
 errors=[]
 if not isinstance(record,dict): return ['Record must be an object']
 for key in ('diagram_id','version','purpose','owner_skill','design_level','baseline','source','source_hash','nodes','edges','validation','approval','freshness'):
  if key not in record: errors.append('Missing '+key)
 if errors: return errors
 for key in ('baseline','approval','validation'):
  if not isinstance(record[key],dict): errors.append(key+' must be an object')
 for key in ('nodes','edges'):
  if not isinstance(record[key],list) or any(not isinstance(x,dict) for x in record[key]): errors.append(key+' must contain objects')
 if errors:return errors
 if not isinstance(record['diagram_id'],str) or not record['diagram_id'].strip():return ['Diagram ID must be a nonempty string']
 if not isinstance(record['source'],str) or not record['source'].strip():return ['Source must be a nonempty path string']
 outputs=record.get('rendered_outputs',[])
 if not isinstance(outputs,list):return ['rendered_outputs must be a list']
 for output in outputs:
  if not isinstance(output,dict) or not isinstance(output.get('path'),str) or not output['path'].strip():return ['Rendered output must contain a nonempty path string']
 for node in record['nodes']:
  if not isinstance(node.get('id'),str) or not node['id'].strip():return ['Node ID must be a nonempty string']
 for edge in record['edges']:
  if any(not isinstance(edge.get(k),str) or not edge[k].strip() for k in ('id','from','to')):return ['Edge ID and endpoints must be nonempty strings']
 for key in ('id','version','hash'):
  if not record['baseline'].get(key):errors.append('Baseline '+key+' missing')
 root=Path(directory).resolve()
 source=(root/record['source']).resolve()
 if not source.is_relative_to(root): return ['Source escapes artifact directory']
 if not source.is_file(): return ['Source missing']
 digest=hashlib.sha256(source.read_bytes()).hexdigest()
 if digest!=record['source_hash']: errors.append('Source hash mismatch')
 ids=set()
 for node in record['nodes']:
  if node.get('id') in ids: errors.append('Duplicate node ID')
  ids.add(node.get('id'))
  if not node.get('id') or not node.get('state'): errors.append('Node identity/state missing')
  if not node.get('source_refs'): errors.append('Node provenance missing')
  if node.get('state')=='VERIFIED' and not node.get('evidence_ids'): errors.append('Verified node lacks evidence')
 edge_ids=set()
 for edge in record['edges']:
  if edge.get('id') in edge_ids:errors.append('Duplicate edge ID')
  edge_ids.add(edge.get('id'))
  if not edge.get('id') or not edge.get('state') or not edge.get('source_refs'): errors.append('Edge identity/state/provenance missing')
  if edge.get('from') not in ids or edge.get('to') not in ids: errors.append('Dangling edge')
  if edge.get('state')=='VERIFIED' and not edge.get('evidence_ids'): errors.append('Verified edge lacks evidence')
 if record['approval'].get('state')=='APPROVED':
  if not record['approval'].get('evidence_reference'): errors.append('Approval evidence missing')
  if record['approval'].get('source_hash')!=digest: errors.append('Approval hash mismatch')
  if record['freshness']!='CURRENT': errors.append('Approval is not current')
  if record['approval'].get('baseline')!=record['baseline']:errors.append('Approval baseline mismatch')
 for name in ('metadata','traceability','syntax','rendering','visual_inspection','specification_consistency'):
  check=record['validation'].get(name,{})
  if not isinstance(check,dict):errors.append('Invalid validation object: '+name);continue
  if check.get('status') not in ('PASS','FAIL','NOT RUN'): errors.append('Invalid validation state: '+name)
  if check.get('status')=='PASS' and not check.get('evidence'): errors.append('Missing validation evidence: '+name)
 for output in record.get('rendered_outputs',[]):
  path=(root/output['path']).resolve()
  if not path.is_relative_to(root) or not path.is_file():errors.append('Rendered output missing or outside artifact directory');continue
  if output.get('source_hash')!=digest:errors.append('Rendered source hash mismatch')
  if output.get('hash')!=hashlib.sha256(path.read_bytes()).hexdigest():errors.append('Rendered output hash mismatch')
 return errors

if __name__=='__main__':
 try:
  p=Path(sys.argv[1]); errors=validate(json.loads(p.read_text(encoding='utf-8')),p.parent)
 except (OSError,ValueError,TypeError) as exc:
  errors=['Invalid record: '+str(exc)]
 print('\n'.join(errors) if errors else 'PASS: structural consistency only')
 sys.exit(bool(errors))
