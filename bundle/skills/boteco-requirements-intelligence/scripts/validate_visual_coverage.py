"""Check declared visual coverage, not whether the author's applicability judgment is true."""
import json
from pathlib import Path

CATALOGUE={
 'boteco-requirements-intelligence': {'business_process','requirements_traceability'},
 'builders-system-design': {'architecture','cross_system_flow'},
 'builders-software-design': {'sequence','state_and_exceptions'},
 'boteco-change-impact-regression-guard': {'blast_radius','protected_behaviours'},
 'production-readiness': {'deployment_and_recovery'},
}
CONSUMERS={'software-design-principles','testing-verification','ci-cd-delivery-governance'}

def text(x): return isinstance(x,str) and bool(x.strip())

def validate_coverage(root, records):
    path=Path(root)/'visual-coverage.json'
    if not path.is_file(): return ['Visual coverage register missing: visual-coverage.json']
    try:
        data=json.loads(path.read_text(encoding='utf-8'))
        if not isinstance(data,dict): return ['Visual coverage must be an object']
        owner=data.get('owner_skill')
        if not isinstance(owner,str) or owner not in set(CATALOGUE)|CONSUMERS:
            return ['Unknown visual coverage owner_skill']
        views=data.get('views')
        if not isinstance(views,list) or any(not isinstance(v,dict) for v in views):
            return ['Visual coverage views must be objects']
        errors=[]; seen=set(); used=set()
        available={r['diagram_id'] for r in records if isinstance(r,dict) and text(r.get('diagram_id'))}
        for view in views:
            name=view.get('view')
            if not text(name) or name in seen: errors.append('Missing or duplicate visual view');continue
            seen.add(name)
            state=view.get('status')
            if state=='PROVIDED':
                links=view.get('diagram_ids')
                if not isinstance(links,list) or not links or any(not text(x) for x in links):
                    errors.append(name+': diagram_ids required');continue
                used.update(links)
                if not set(links)<=available: errors.append(name+': missing diagram record')
            elif state=='NOT APPLICABLE':
                for key in ('reason','scope','evidence'):
                    if not text(view.get(key)): errors.append(name+': omission requires '+key)
            elif state=='REQUIRED BUT INCOMPLETE':
                errors.append(name+': required view incomplete; '+str(view.get('reason','reason missing')))
            else: errors.append(name+': invalid coverage status')
        for name in sorted(CATALOGUE.get(owner,set())-seen): errors.append('Coverage decision missing for '+name)
        if available-used: errors.append('Diagram records absent from coverage register: '+', '.join(sorted(available-used)))
        if owner in CONSUMERS and not views and not text(data.get('none_reason')):
            errors.append('Consumer with no required views must record none_reason')
        return errors
    except (OSError,ValueError,TypeError) as exc:
        return ['Invalid visual coverage: '+str(exc)]
