"""Read-only integrity verification. Run with python -B verify_bundle.py."""
import hashlib
import json
from pathlib import Path
import sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
expected=manifest['files']
actual={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
        for p in root.rglob('*') if p.is_file() and p.name!='manifest.json'}
missing=sorted(set(expected)-set(actual))
extra=sorted(set(actual)-set(expected))
changed=sorted(p for p in set(expected)&set(actual) if expected[p]!=actual[p])
print(json.dumps(dict(status='PASS' if not(missing or extra or changed) else 'FAIL',
                     verified_files=len(expected),missing=missing,extra=extra,changed=changed),indent=2))
sys.exit(bool(missing or extra or changed))
