"""Regression probes for required privacy failures. Every temporary fixture is removed."""
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
def verify():
    return subprocess.run([sys.executable,str(ROOT/'scripts/verify.py')],capture_output=True,text=True)
assert verify().returncode==0,'Baseline verifier failed'
checks=1
probes=[(ROOT/'qa-artifacts/privacy-probe.txt',bytes((67,67,80,67)).decode().lower())]
for value in ((83,101,108,108,101,114,74,111,121),(83,116,111,99,107,32,68,101,115,107),(71,83,84,32,70,105,108,105,110,103)):
    probes.append((ROOT/'assets/privacy-probe.txt',bytes(value).decode().swapcase()))
for path,value in probes:
    assert not path.exists(),'Probe path already exists'
    try:
        path.write_text(value)
        result=verify()
        assert result.returncode!=0,'Verifier accepted forbidden content'
        assert ('private client name found' in result.stderr or 'unsupported personal project found' in result.stderr),result.stderr
        checks+=1
    finally:
        path.unlink()
assert verify().returncode==0,'Cleanup verifier failed'
checks+=1
for name, old, new, expected in (
    ('index.html', 'class="atmosphere"', 'class="missing-scene"', 'missing decorative background layer'),
    ('assets/css/styles.css', '.atmosphere{display:none!important}', '.atmosphere{display:block!important}', 'Background must be fully disabled'),
    ('index.html', 'styles.css?v=12', 'styles.css?v=11', 'expected v=12 cache-busting'),
):
    path=ROOT/name
    original=path.read_text()
    assert old in original, 'Regression target missing'
    try:
        path.write_text(original.replace(old,new))
        result=verify()
        assert result.returncode!=0 and expected in result.stderr,result.stderr
        checks+=1
    finally:
        path.write_text(original)
assert verify().returncode==0,'Final cleanup verifier failed'
print(f'PASS: {checks} verifier regression assertions; privacy, background, reduced-motion and cache guards reject broken fixtures; source restored.')
