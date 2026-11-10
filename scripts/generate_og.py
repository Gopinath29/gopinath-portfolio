"""Original social image: uv run --with pillow scripts/generate_og.py."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / 'assets/fonts'
image = Image.new('RGB', (1200, 630))
draw = ImageDraw.Draw(image)
for y in range(630):
    t=y/630
    draw.line((0,y,1200,y), fill=tuple(round(a+(b-a)*t) for a,b in zip((168,223,246),(126,200,255))))
def write(x,y,text,size,font='sora.ttf',colour='#0d2b4a'):
    face=ImageFont.truetype(str(FONTS/font),size)
    face.set_variation_by_axes([600 if font == 'sora.ttf' else 500 if font == 'jetbrains-mono.ttf' else 400])
    draw.text((x,y),text,font=face,fill=colour)
write(60,40,'GOPINATH GURUSAMY // SOLUTION ARCHITECT',14,'jetbrains-mono.ttf','#08418a')
write(55,105,'Architecture that',58)
write(55,179,'holds up.',68,colour='#08418a')
write(60,302,'Dynamics 365 CE & Power Platform',23,'plus-jakarta-sans.ttf')
write(60,345,'Technical Lead · Copilot Studio & AI Agents',18,'plus-jakarta-sans.ttf')
draw.rounded_rectangle((55,440,785,575),radius=18,fill='#d5edff')
write(78,460,'FEATURED WORK // COPILOT STUDIO',12,'jetbrains-mono.ttf','#08418a')
write(78,491,'Case Assistant',29)
write(78,538,'Agent for Dynamics 365 Customer Service',15,'plus-jakarta-sans.ttf')
draw.rounded_rectangle((845,100,1140,410),radius=32,fill='#d5edff')
p=ImageOps.fit(Image.open(ROOT/'assets/img/headshot.jpg').convert('RGB'),(271,286),Image.Resampling.LANCZOS,centering=(.5,.35))
mask=Image.new('L',p.size,0);ImageDraw.Draw(mask).rounded_rectangle((0,0,270,285),radius=24,fill=255)
image.paste(p,(857,112),mask)
write(850,445,'Design authority.',19)
write(850,476,'Hands-on delivery.',19,colour='#08418a')
image.save(ROOT/'assets/img/og-image.png')
# Editable original SVG companion uses the same OFL font families.
(ROOT/'assets/img/og-image.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><defs><linearGradient id="sky" x2="0" y2="1"><stop stop-color="#a8dff6"/><stop offset="1" stop-color="#7ec8ff"/></linearGradient><clipPath id="portrait"><rect x="857" y="112" width="271" height="286" rx="24"/></clipPath></defs><rect width="1200" height="630" fill="url(#sky)"/><g fill="#0d2b4a" font-family="Sora,system-ui,sans-serif"><text x="55" y="163" font-size="58">Architecture that</text><text x="55" y="247" font-size="68" fill="#08418a">holds up.</text><text x="850" y="466" font-size="19">Design authority.</text><text x="850" y="497" font-size="19" fill="#08418a">Hands-on delivery.</text></g><g fill="#0d2b4a" font-family="Plus Jakarta Sans,system-ui,sans-serif"><text x="60" y="328" font-size="23">Dynamics 365 CE &amp; Power Platform</text><text x="60" y="366" font-size="18">Technical Lead · Copilot Studio &amp; AI Agents</text></g><rect x="55" y="440" width="730" height="135" rx="18" fill="#d5edff"/><text x="78" y="477" font-family="JetBrains Mono,monospace" font-size="12" fill="#08418a">FEATURED WORK // COPILOT STUDIO</text><text x="78" y="524" font-family="Sora,sans-serif" font-size="29" fill="#0d2b4a">Case Assistant</text><text x="78" y="555" font-family="Plus Jakarta Sans,sans-serif" font-size="15" fill="#0d2b4a">Agent for Dynamics 365 Customer Service</text><text x="60" y="57" font-family="JetBrains Mono,monospace" font-size="14" fill="#08418a">GOPINATH GURUSAMY // SOLUTION ARCHITECT</text><rect x="845" y="100" width="295" height="310" rx="32" fill="#d5edff"/><image href="headshot.jpg" x="857" y="112" width="271" height="286" preserveAspectRatio="xMidYMid slice" clip-path="url(#portrait)"/></svg>''')
print('Generated original 1200 × 630 light-theme social image.')

# Refresh the legacy favicon to the same blue/navy system.
icon=Image.new('RGBA',(64,64),(0,0,0,0));ink=ImageDraw.Draw(icon)
ink.rounded_rectangle((0,0,63,63),radius=18,fill='#0b2a4a')
face=ImageFont.truetype(str(FONTS/'sora.ttf'),25);face.set_variation_by_axes([600])
ink.text((8,17),'GG.',font=face,fill='#a8dff6')
icon.save(ROOT/'favicon.ico',sizes=[(16,16),(32,32),(64,64)])
(ROOT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="18" fill="#0b2a4a"/><text x="32" y="42" text-anchor="middle" font-family="Sora,system-ui,sans-serif" font-weight="600" font-size="25" letter-spacing="-1" fill="#a8dff6">GG.</text></svg>')
