"""Validate pack identity and declared links; never authenticates approval authority."""
import hashlib
import json
from pathlib import Path

def text(v): return isinstance(v,str) and bool(v.strip())
def require(ok,message):
    if not ok: raise ValueError(message)
def load(root,path):
    require(text(path),'Local artifact path required')
    p=(root/path).resolve()
    require(p.is_relative_to(root) and p.is_file(),'Artifact missing or outside pack')
    return json.loads(p.read_text(encoding='utf-8'))
def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def identity(b): return {k:b[k] for k in ('baseline_id','version','content_hash')}
def approval(a,b):
    require(isinstance(a,dict) and a.get('state')=='APPROVED','Approved governing baseline required for READY')
    require(a.get('baseline_id')==b['baseline_id'] and a.get('baseline_version')==b['version'] and a.get('content_hash')==b['content_hash'],'Baseline approval identity mismatch')
    for k in ('approver','decided_at','evidence_reference'): require(text(a.get(k)),'Baseline approval requires '+k)

def validate_handoff(root,level):
    root=Path(root).resolve()
    try:
        h=load(root,'design-handoff.json')
        require(isinstance(h,dict),'Design handoff must be an object')
        for k in ('artifact_id','artifact_version'): require(text(h.get(k)),'Design handoff requires '+k)
        require(h.get('design_level')==level,'Design level mismatch')
        require(h.get('lifecycle') in ('DRAFT','READY'),'Design lifecycle must be DRAFT or READY')
        ready=h['lifecycle']=='READY'
        require(h.get('freshness') in ('CURRENT','STALE','INVALIDATED'),'Invalid design freshness')
        if ready: require(h['freshness']=='CURRENT','READY design cannot be stale or invalidated')
        b=load(root,h.get('baseline_path'))
        require(isinstance(b,dict),'Baseline must be an object')
        require(h.get('baseline')==identity(b),'Design baseline identity mismatch')
        require(b['content_hash']==digest({k:v for k,v in b.items() if k not in {'content_hash','approval','downstream_artifacts'}}),'Baseline content hash mismatch')
        if ready: approval(b.get('approval'),b)
        else: require(text(h.get('limitations')),'DRAFT requires explicit limitations')
        rr=b.get('requirements'); aa=b.get('acceptance_criteria')
        require(isinstance(rr,list) and isinstance(aa,list) and all(isinstance(x,dict) for x in rr+aa),'Baseline requirements and criteria malformed')
        rids={r['id'] for r in rr}; aids={a['id'] for a in aa}
        trace=h.get('traceability')
        require(isinstance(trace,list) and bool(trace),'Design traceability is required')
        seen=set()
        for t in trace:
            require(isinstance(t,dict) and text(t.get('decision_id')),'Decision identity required')
            require(t['decision_id'] not in seen,'Duplicate design decision');seen.add(t['decision_id'])
            for key,known in [('requirement_ids',rids),('acceptance_criterion_ids',aids)]:
                v=t.get(key)
                require(isinstance(v,list) and bool(v) and all(text(x) for x in v) and set(v)<=known,'Unknown or missing '+key)
            for aid in t['acceptance_criterion_ids']:
                ac=next(x for x in aa if x['id']==aid)
                require(bool(set(ac['requirement_ids']) & set(t['requirement_ids'])),'Design criterion unrelated to declared requirements')
        if level=='LLD':
            dep=h.get('hld')
            require(isinstance(dep,dict),'LLD must declare HLD dependency')
            if dep.get('state')=='NOT APPLICABLE':
                for key in ('reason','scope','evidence'):require(text(dep.get(key)),'HLD omission requires '+key)
                require(dep.get('introduces_system_boundary') is False,'New system boundaries require HLD review')
            else:
                require(dep.get('state')=='REFERENCED','Invalid HLD dependency state')
                payload=load(root,dep.get('path'))
                require(isinstance(payload,dict),'HLD payload must be an object')
                require(dep.get('content_hash')==digest(payload),'HLD content hash mismatch')
                require(dep.get('artifact_id')==payload.get('artifact_id') and dep.get('artifact_version')==payload.get('artifact_version') and text(dep.get('artifact_id')) and text(dep.get('artifact_version')),'HLD identity mismatch')
                require(payload.get('design_level')=='HLD','Referenced artifact is not HLD')
                if ready:
                    require(dep.get('freshness')=='CURRENT','HLD dependency not current')
                    governing=payload.get('baseline')
                    require(isinstance(governing,dict),'HLD baseline identity missing')
                    if governing!=identity(b):
                        review=dep.get('equivalence_review')
                        require(isinstance(review,dict) and review.get('decision')=='EQUIVALENT','Older HLD baseline requires evidence-backed equivalence review')
                        require(governing.get('baseline_id')==b['baseline_id'] and review.get('from_baseline')==governing and review.get('to_baseline')==identity(b),'HLD equivalence baseline mismatch')
                        used=dep.get('requirements_used'); reviewed=review.get('requirements_reviewed')
                        require(isinstance(used,list) and bool(used) and all(text(x) for x in used) and set(used)<=rids,'HLD declared dependencies required')
                        require(isinstance(reviewed,list) and all(text(x) for x in reviewed) and set(reviewed)==set(used),'HLD equivalence must cover all declared dependencies')
                        for key in ('reviewer','reviewed_at','evidence_reference','rationale'): require(text(review.get(key)),'HLD equivalence requires '+key)
                    a=dep.get('approval')
                    require(isinstance(a,dict) and a.get('state')=='APPROVED','HLD approval required')
                    require(a.get('content_hash')==dep['content_hash'] and a.get('artifact_id')==dep['artifact_id'] and a.get('artifact_version')==dep['artifact_version'] and a.get('baseline')==governing,'HLD approval binding mismatch')
                    for key in ('authority','decided_at','evidence_reference'): require(text(a.get(key)),'HLD approval requires '+key)
        return []
    except (OSError,ValueError,TypeError,KeyError) as exc:
        return ['Design handoff invalid: '+str(exc)]
