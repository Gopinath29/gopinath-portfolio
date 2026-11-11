"""Regression probes for required privacy, content and interaction-markup failures. Every temporary fixture is removed."""
from pathlib import Path
import subprocess
import sys
import os
import tempfile
import zlib
ROOT=Path(__file__).resolve().parents[1]
def verify(env=None):
    return subprocess.run([sys.executable,str(ROOT/'scripts/verify.py')],capture_output=True,text=True,env=env)

def fixture_pdf(text):
    """Build a compressed, extractable PDF without a fixture or extra dependency."""
    escaped=text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    stream=zlib.compress(f'BT /F1 12 Tf 40 750 Td ({escaped}) Tj ET'.encode('ascii'))
    objects=[
        b'<< /Type /Catalog /Pages 2 0 R >>',
        b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
        f'<< /Length {len(stream)} /Filter /FlateDecode >>\nstream\n'.encode()+stream+b'\nendstream',
    ]
    data=b'%PDF-1.4\n'
    offsets=[0]
    for number,obj in enumerate(objects,1):
        offsets.append(len(data))
        data+=f'{number} 0 obj\n'.encode()+obj+b'\nendobj\n'
    start=len(data)
    data+=f'xref\n0 {len(offsets)}\n0000000000 65535 f \n'.encode()
    data+=b''.join(f'{offset:010d} 00000 n \n'.encode() for offset in offsets[1:])
    data+=f'trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n'.encode()
    return data
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
# Runtime-only probes exercise compressed PDF text, nested/case-insensitive paths,
# the QA-directory phone guard, extraction failures and a missing dependency.
phone=''.join(str(digit) for digit in (2,0,2,5,5,5,0,1,2,3))
pdf_probes=[
    (ROOT/'assets/privacy-probe.pdf',fixture_pdf('Public recruiter CV'),None),
    (ROOT/'assets/resume/privacy-probe.PDF',fixture_pdf(bytes((67,67,80,67)).decode().lower()),'private client name found'),
    (ROOT/'assets/privacy-probe.pdf',fixture_pdf(phone),'phone-like number found'),
    (ROOT/'qa-artifacts/privacy-probe.pdf',fixture_pdf('(' + phone[:3] + ') ' + phone[3:6] + '-' + phone[6:]),'phone-like number found'),
    (ROOT/'assets/privacy-probe.pdf',b'%PDF-invalid','PDF text extraction failed'),
]
for path,data,expected in pdf_probes:
    assert not path.exists(),'PDF probe path already exists'
    try:
        path.write_bytes(data)
        result=verify()
        if expected:
            assert result.returncode!=0 and expected in result.stderr,result.stderr
        else:
            assert result.returncode==0,result.stderr
        checks+=1
    finally:
        path.unlink()
with tempfile.TemporaryDirectory(prefix='portfolio-verifier-') as empty_path:
    result=verify(env={**os.environ,'PATH':empty_path})
    assert result.returncode!=0 and 'requires pdftotext' in result.stderr,result.stderr
    checks+=1
for name, old, new, expected in (
    ('404.html', '</main>', '<a href="https://example.com/">External</a></main>', 'external link needs target=_blank and rel=noopener noreferrer'),
    ('404.html', '</main>', '<a href="mailto:itiangopi@gmail.com">Email</a></main>', 'external link needs target=_blank and rel=noopener noreferrer'),
    ('index.html', 'rel="noopener noreferrer"', 'rel="noopener"', 'external link needs target=_blank and rel=noopener noreferrer'),
    ('index.html', '(opens in new tab)', '(external)', 'external link needs accessible opens in new tab hint'),
    ('index.html', 'href="#main"', 'href="#main" target="_blank"', 'navigation and CV links must stay same-tab'),
    ('index.html', 'download="Gopinath_Gurusamy_Resume.pdf"', 'target="_blank" download="Gopinath_Gurusamy_Resume.pdf"', 'navigation and CV links must stay same-tab'),
    ('404.html', 'href="./"', 'href="./" target="_blank"', 'navigation and CV links must stay same-tab'),
    ('index.html', 'back to top">GG</a>', 'back to top">G</a>', 'expected accessible GG wordmark'),
    ('404.html', 'GG, Gopinath Gurusamy, home', 'Gopinath Gurusamy, home', 'expected accessible GG wordmark'),
    ('index.html', '<details class="career-record">', '<details class="career-record" open>', 'career records closed by default'),
    ('index.html', 'Case summaries that include custom fields', 'Case summaries', 'missing AI & Copilot fact'),
    ('index.html', '<p class="micro">Workflow automation</p>', '<p class="micro">100+ flows</p>', 'Power Automate card must not repeat'),
    ('index.html', 'Architecture that holds up.', 'Design authority.', 'redundant hero tagline remains'),
    ('index.html', 'Kongu Engineering College', 'College', 'About must contain education/languages'),
    ('index.html', '<div class="copilot-config"><ul>', '<div class="copilot-config"><a href="https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/33c24ca4ad0be38e" target="_blank" rel="noopener">AB-620</a><ul>', 'AI & Copilot must not repeat credential verify links'),
    ('index.html', 'href="#case-assistant">Explore the Case Assistant solution', 'href="#work">Explore the Case Assistant solution', 'AI & Copilot must link to Case Assistant work'),
    ('index.html', '<p class="chapter-description">Configured Dynamics', '<p class="chapter-description">Find case documents. Configured Dynamics', 'AI & Copilot must not repeat Work topics'),
    ('index.html', '<h1 id="hero-title">', '<h1 id="hero-title">' + 'extra ' * 100, 'total word count must be'),
    ('index.html', 'Help case officers at a regulatory body', 'extra ' * 40 + 'Help case officers at a regulatory body', 'Work must be about 350 words'),
    ('index.html', 'class="atmosphere"', 'class="missing-scene"', 'missing decorative background layer'),
    ('assets/css/styles.css', '.atmosphere{display:none!important}', '.atmosphere{display:block!important}', 'Background must be fully disabled'),
    ('index.html', 'styles.css?v=17', 'styles.css?v=11', 'expected v=17 cache-busting'),
    ('assets/js/main.js', 'i < 104', 'i < 28', 'Dark scenery must create 80–120 stars'),
    ('assets/css/styles.css', 'z-index:0;pointer-events:none', 'z-index:-1;pointer-events:none', 'Background must paint above the page wash'),
    ('assets/css/styles.css', 'animation:shoot 12s', 'animation:shoot 27s', 'Dark shooting trails must retain'),
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
print(f'PASS: {checks} verifier regression assertions; text/PDF privacy, PDF extraction/dependency, external links, accessible hints, same-tab navigation/CV, V5 content, GG headers, closed career records, background, reduced-motion and cache guards reject broken fixtures; source restored.')
