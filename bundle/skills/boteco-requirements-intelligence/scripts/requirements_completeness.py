"""Structural completeness only; evidence and product decisions require review."""
STATES = {'VALIDATED', 'VALIDATED WITH OPEN ITEMS', 'NEEDS DECISION', 'BLOCKED'}

def text(value):
    return isinstance(value, str) and bool(value.strip())

def ids(value, label, allow_empty=False):
    if not isinstance(value, list) or (not value and not allow_empty) or any(not text(x) for x in value) or len(set(value)) != len(value):
        raise ValueError(label + ' must be a list of unique nonblank strings')
    return set(value)

def validate_completeness(data):
    if data.get('validation_state') not in STATES:
        raise ValueError('validation_state must use the documented requirements verdicts')
    reqs=data.get('requirements'); criteria=data.get('acceptance_criteria')
    if not isinstance(reqs,list) or not isinstance(criteria,list):
        raise ValueError('requirements and acceptance_criteria must be lists')
    if any(not isinstance(x,dict) for x in reqs+criteria):
        raise ValueError('requirements and criteria must contain objects')
    rids=ids([x.get('id') for x in reqs], 'requirement IDs')
    aids=ids([x.get('id') for x in criteria], 'criterion IDs')
    forward=set(); reverse=set()
    for r in reqs:
        ids(r.get('sources'),r['id']+' sources')
        links=ids(r.get('acceptance_criterion_ids'),r['id']+' acceptance_criterion_ids')
        if not links <= aids: raise ValueError('Unknown acceptance criterion')
        forward.update((r['id'],a) for a in links)
    for a in criteria:
        links=ids(a.get('requirement_ids'),a['id']+' requirement_ids')
        if not links <= rids: raise ValueError('Unknown requirement')
        reverse.update((r,a['id']) for r in links)
    if forward != reverse:
        raise ValueError('Requirement and acceptance-criterion links must be reciprocal')
    seen=set()
    for key in ('business_rules','assumptions','open_decisions'):
        reg=data.get(key)
        if not isinstance(reg,dict) or not isinstance(reg.get('items'),list):
            raise ValueError(key+' register requires an items list')
        if not reg['items'] and not text(reg.get('none_reason')):
            raise ValueError(key+' requires explicit none_reason when empty')
        for item in reg['items']:
            if not isinstance(item,dict) or not text(item.get('id')) or item['id'] in seen:
                raise ValueError(key+' requires unique record IDs')
            seen.add(item['id'])
            links=ids(item.get('requirement_ids'),key+' requirement_ids')
            if not links <= rids: raise ValueError(key+' references unknown requirements')
            for field in ('owner','validation_method','disposition'):
                if not text(item.get(field)): raise ValueError(key+' requires '+field)
            if key=='business_rules':
                if item.get('status') not in ('PROPOSED','CONFIRMED','REJECTED'):
                    raise ValueError('business_rules status invalid')
                # The linked requirement is the canonical rule; no duplicate wording is required.
            else:
                if not text(item.get('statement')) or not isinstance(item.get('material'),bool):
                    raise ValueError(key+' requires statement and boolean material')
                allowed={'OPEN','VALIDATED','REJECTED'} if key=='assumptions' else {'OPEN','RESOLVED','DEFERRED'}
                if item.get('status') not in allowed: raise ValueError(key+' status invalid')
                if item['status'] in ('VALIDATED','RESOLVED') and not text(item.get('evidence_reference')):
                    raise ValueError(key+' resolved records require evidence_reference')
