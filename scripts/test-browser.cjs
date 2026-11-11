/* Local QA only. Requires Playwright and axe installed outside this checkout. */
const {chromium,webkit}=require('playwright');
const engine=process.env.PW_ENGINE==='webkit'?webkit:chromium;
const {default:AxeBuilder}=require('@axe-core/playwright');
const {writeFileSync,readFileSync}=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const dest=path.resolve(__dirname,'../qa-artifacts'),url='http://127.0.0.1:8093/';
const results={engine:'headless Playwright '+engine.name(),samples:[],motion:[],interactions:[],accessibility:[],errors:[]};
let checks=0,browser;
function check(ok,label){assert.ok(ok,label);checks++;}
const blocked=[[67,67,80,67],[83,101,108,108,101,114,74,111,121],[83,116,111,99,107,32,68,101,115,107],[71,83,84,32,70,105,108,105,110,103]].map(a=>String.fromCharCode(...a));
function privacy(t){check(!blocked.some(s=>t.toLowerCase().includes(s.toLowerCase())),'private text absent');check(!/(?:\+?\d[ ()-]*){10,15}/.test(t),'phone absent');}
async function ready(p){await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);}
async function linkTargets(p) {
 const external=p.locator('a[href^="https:"],a[href^="http:"],a[href^="mailto:"]');
 for(const link of await external.all()) {
  check(await link.getAttribute('target')==='_blank','external link opens new tab');
  check(await link.evaluate(e=>['noopener','noreferrer'].every(v=>e.relList.contains(v))),'external link isolates opener and referrer');
  check((await link.ariaSnapshot()).includes('opens in new tab'),'external link accessible new tab hint');
 }
 check(await p.locator('a[href^="#"],a[href^="./"],.cv-link').evaluateAll(es=>es.every(e=>e.target!=='_blank')),'navigation, skip, wordmark, back-to-top and CV stay same-tab');
}
async function wordmark(p,home=true){
 await linkTargets(p);
 const label='GG, Gopinath Gurusamy, '+(home?'back to top':'home');
 const mark=p.locator('.wordmark');
 check(await mark.innerText()==='GG','visible wordmark is exactly GG');
 check(await p.getByRole('link',{name:label,exact:true}).count()===1,'wordmark accessible name includes GG, full name and destination');
 check(await mark.getAttribute('href')===(home?'#top':'./'),'wordmark target preserved');
 const style=await mark.evaluate(async e=>{
  const s=getComputedStyle(e),photo=getComputedStyle(e,'::before');
  const source=photo.backgroundImage.match(/url\(["']?(.*?)["']?\)/)?.[1];
  const img=new Image();img.src=source||'';let loaded=false;try{await img.decode();loaded=img.naturalWidth>0;}catch{}
  const range=document.createRange();range.selectNodeContents(e);const text=range.getBoundingClientRect();
  return {font:s.fontFamily,weight:s.fontWeight,color:s.color,ink:getComputedStyle(document.body).color,photo:photo.backgroundImage,width:parseFloat(photo.width),height:parseFloat(photo.height),content:photo.content,display:photo.display,loaded,visible:text.width>0&&text.height>0};
 });
 check(style.visible&&style.font.includes('Sora')&&style.weight==='700','GG visible in bold Sora');
 check(style.color===style.ink,'both Gs use masthead ink');
 check(style.photo.includes('headshot.jpg')&&style.loaded&&style.width>0&&style.height>0&&style.content!=='none'&&style.display!=='none','wordmark photo loaded with visible box');
 results.headers??=[];results.headers.push({page:home?'home':'404',width:p.viewportSize().width,label,...style});
}
async function career(p){
 const records=p.locator('details.career-record'),codec=p.locator('#career-codec details'),summary=codec.locator('summary');
 check(await records.count()===5&&await records.evaluateAll(ds=>ds.every(d=>!d.open)),'all five career records initially closed');
 await summary.click();check(await codec.evaluate(e=>e.open),'Codec summary click opens');
 await summary.click();check(!await codec.evaluate(e=>e.open),'Codec summary click closes');
 await summary.focus();
 for(const key of ['Enter','Space']){
  await p.keyboard.press(key);check(await codec.evaluate(e=>e.open),'Codec '+key+' opens');
  await p.keyboard.press(key);check(!await codec.evaluate(e=>e.open),'Codec '+key+' closes');
 }
 await p.getByRole('link',{name:'Codec Ireland career record ↗'}).first().click();
 check(await codec.evaluate(e=>e.open),'related Codec link opens closed record');
 await summary.click();
 await p.evaluate(()=>{history.replaceState(null,'',location.pathname);window.scrollTo(0,0);});
}
async function measure(p){return p.evaluate(()=>{
 const q=s=>document.querySelector(s),all=s=>[...document.querySelectorAll(s)],st=getComputedStyle(document.documentElement);
 const rgb=s=>(s.match(/[\d.]+/g)||[]).map(Number),hex=s=>{s=s.trim();return [1,3,5].map(i=>parseInt(s.slice(i,i+2),16))};
 const mix=(a,b)=>a.slice(0,3).map((c,i)=>c*(a[3]??1)+b[i]*(1-(a[3]??1)));
 const lum=v=>v.map(c=>{c/=255;return c<=.04045?c/12.92:((c+.055)/1.055)**2.4}).reduce((n,c,i)=>n+c*[.2126,.7152,.0722][i],0);
 const ratio=(a,b)=>(Math.max(lum(a),lum(b))+.05)/(Math.min(lum(a),lum(b))+.05);
 const dark=document.documentElement.dataset.theme==='dark';
 const bases=['--bg','--hero-bg'].map(n=>hex(st.getPropertyValue(n)));
 // Assume a full white scenery pixel behind content: brighter than either star or trail.
 // Opaque text islands reset to the page wash; denser glass composites over white.
 const glow=rgb(st.getPropertyValue('--glow'));let extreme=bases[1];extreme=mix(glow,mix(glow,extreme));
 const skyExtreme=extreme;extreme=dark?[255,255,255]:mix([255,255,255,.75],extreme);
 bases.push(extreme);
 const failures=[];let tested=0,minRatio=99;const categories={};
 function backgrounds(el){const chain=[];let a=el;while(a&&a!==document.body){chain.unshift(a);a=a.parentElement;}return bases.map(base=>{let b=base;for(const p of chain){const ps=getComputedStyle(p);const c=rgb(ps.backgroundColor);if(c.length>=3)b=mix(c,b);if(dark&&ps.backgroundImage.includes('radial-gradient'))b=skyExtreme;if(p.matches('.solid-link'))b=mix([255,255,255,.12],b);}return b;});}
 for(const el of all('body *')){
  const own=[...el.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim();
  if(!own||!el.getClientRects().length||['SCRIPT','STYLE'].includes(el.tagName)||getComputedStyle(el).visibility==='hidden'||el.closest('.atmosphere')||el.classList.contains('sr-only'))continue;
  const cs=getComputedStyle(el),fg=rgb(cs.color);if(fg.length<3)continue;
  const r=Math.min(...backgrounds(el).map(b=>ratio(mix(fg,b),b)));
  const large=parseFloat(cs.fontSize)>=24||(parseFloat(cs.fontSize)>=18.66&&parseFloat(cs.fontWeight)>=700);
  const cat=el.closest('button,.solid-link')?'buttons':el.closest('a')?'links':cs.color===getComputedStyle(q('.hero-role')||document.body).color?'muted':'body';categories[cat]=Math.min(categories[cat]??99,r);
  tested++;minRatio=Math.min(minRatio,r);if(r+.005<(large?3:4.5))failures.push({tag:el.tagName,text:own.slice(0,65),ratio:+r.toFixed(2),size:cs.fontSize,color:cs.color});
 }
 const uis=[];for(const selector of ['.solid-link','.theme-toggle','.copy-email','.terminal-form button']){
  const el=q(selector);if(!el||!el.getClientRects().length)continue;
  const color=selector==='.solid-link'?rgb(getComputedStyle(el).backgroundColor):selector==='.terminal-form button'?rgb(getComputedStyle(el).backgroundColor):rgb(st.getPropertyValue('--accent-ink').trim().startsWith('#')?'rgb('+hex(st.getPropertyValue('--accent-ink')).join(',')+')':getComputedStyle(el).borderColor);
  const bgs=backgrounds(el.parentElement);const r=Math.min(...bgs.map(b=>ratio(color,b)));uis.push({selector,ratio:+r.toFixed(2)});
 }
 const rects={};for(const s of ['.hero','.hero-story','.hero-proof','.portrait-border','.headshot','#about','#work','#copilot','#contact']){const e=q(s);if(e){const r=e.getBoundingClientRect();rects[s]=[r.x,r.y,r.width,r.height];}}
 const img=q('.headshot');let portrait=null;if(img){const b=img.getBoundingClientRect(),f=img.parentElement.getBoundingClientRect();portrait={loaded:img.naturalWidth>0,inside:b.left>=f.left&&b.right<=f.right&&b.top>=f.top&&b.bottom<=f.bottom,objectPosition:getComputedStyle(img).objectPosition};}
 return {width:innerWidth,height:innerHeight,theme:document.documentElement.dataset.theme,overflow:document.documentElement.scrollWidth>innerWidth,accent:st.getPropertyValue('--accent').trim(),accentInk:st.getPropertyValue('--accent-ink').trim(),background:st.getPropertyValue('--bg').trim(),state:q('.atmosphere').dataset.state,scene:q('.atmosphere').dataset.scene,activeScene:all('.sky-light,.sky-dark').filter(e=>getComputedStyle(e).display!=='none').map(e=>e.className),animations:document.getAnimations().map(a=>({name:a.animationName,state:a.playState})),contrast:{tested,minRatio:+minRatio.toFixed(2),categories:Object.fromEntries(Object.entries(categories).map(([k,v])=>[k,+v.toFixed(2)])),ui:uis,failures},fonts:['Sora','Plus Jakarta Sans','JetBrains Mono'].map(f=>document.fonts.check('16px "'+f+'"')),portrait,rects,flow:q('[data-count="100"]')?.parentElement.textContent};
 });}
async function commands(p,theme,reduced=false){
 const input=p.locator('#terminal-command'),out=p.locator('.terminal-output');
 const expected={help:/pac certs[\s\S]*pac contact[\s\S]*pac projects[\s\S]*pac copilot[\s\S]*clear/,'pac certs':/PL-600[\s\S]*AB-100[\s\S]*AB-620/,'pac contact':/^Email: itiangopi@gmail.com\nLinkedIn: https:\/\/www.linkedin.com\/in\/gopinath-gurusamy\s*$/,'pac projects':/^Case Assistant[\s\S]*Irish national healthcare organisation[\s\S]*AI & Copilot/,'pac copilot':/Client: a regulatory body[\s\S]*Find and summarise a case[\s\S]*Find case documents[\s\S]*Suggest next steps[\s\S]*Create a case[\s\S]*AB-100 · AB-620[\s\S]*Credentials \(#certifications\)/};
 for(const [cmd,re] of Object.entries(expected)){await input.fill(cmd);await input.press('Enter');const t=await out.locator('p').last().textContent();check(re.test(t),cmd+' output');if(cmd==='pac contact') {
  const answer=out.locator('p').last();
  check(await answer.locator('a').count()===2,'contact has two real links');
  for(const href of ['https://www.linkedin.com/in/gopinath-gurusamy','mailto:itiangopi@gmail.com']) {
   const link=answer.locator(`a[href="${href}"]`);
   check(await link.getAttribute('target')==='_blank','terminal contact opens new tab');
   check(await link.evaluate(e=>['noopener','noreferrer'].every(v=>e.relList.contains(v))),'terminal contact safe rel');
   check((await link.ariaSnapshot()).includes('opens in new tab'),'terminal accessible new tab hint');
  }
 }privacy(t);check(await input.evaluate(e=>document.activeElement===e),cmd+' focus');results.interactions.push({width:p.viewportSize().width,theme,reduced,command:cmd,output:t.trim()});}
 await input.fill('clear');await input.press('Enter');check(await out.locator('*').count()===0,'clear');
 await input.fill('<img src=x onerror=alert(1)>');await input.press('Enter');check(await out.locator('img').count()===0,'safe terminal text');await input.fill('https://example.com/ <a href=javascript:alert(1)>test</a>');await input.press('Enter');check(await out.locator('p').last().locator('a').count()===0,'typed URLs never linkified');check(await out.locator('.command-echo').last().locator('*').count()===0,'typed HTML stays text');await input.fill('clear');await input.press('Enter');
}
async function stars(p,width,theme){
 const sharp=require('sharp');
 const field=await p.evaluate(()=>({count:document.querySelectorAll('.star').length,sizes:[...new Set([...document.querySelectorAll('.star')].map(e=>e.style.getPropertyValue('--star-size')))],rect:document.querySelector('.atmosphere').getBoundingClientRect().toJSON(),pointer:getComputedStyle(document.querySelector('.atmosphere')).pointerEvents}));
 check(field.count>=80&&field.count<=120,'80–120 stars exist');check(field.sizes.length>=3,'mixed star sizes');check(field.rect.width===width&&field.rect.height===p.viewportSize().height,'atmosphere fills viewport');check(field.pointer==='none','scenery never intercepts clicks');
 await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).forEach(a=>a.pause()));await p.waitForTimeout(50);
 const positions=await p.locator('.star').evaluateAll(es=>es.map((e,index)=>{const b=e.getBoundingClientRect();return {index,x:b.x+b.width/2,y:b.y+b.height/2,width:b.width,opacity:+getComputedStyle(e).opacity}}));
 check(positions.filter(s=>s.opacity>0&&s.x>=0&&s.x<width&&s.y>=0&&s.y<p.viewportSize().height).length>=80,'computed visible stars in viewport');
 const before=await sharp(await p.screenshot()).removeAlpha().raw().toBuffer({resolveWithObject:true});
 const hide=await p.addStyleTag({content:'.star-field{visibility:hidden!important}'});const after=await sharp(await p.screenshot()).removeAlpha().raw().toBuffer({resolveWithObject:true});await hide.evaluate(e=>e.remove());
 function deltaAt(x,y,radius,b,a){let peak=0,count=0;for(let j=Math.max(0,Math.floor(y-radius));j<=Math.min(b.info.height-1,Math.ceil(y+radius));j++)for(let i=Math.max(0,Math.floor(x-radius));i<=Math.min(b.info.width-1,Math.ceil(x+radius));i++){const n=(j*b.info.width+i)*3;const d=Math.max(...[0,1,2].map(k=>b.data[n+k]-a.data[n+k]));peak=Math.max(peak,d);if(d>=24)count++;}return {peak,count};}
 const visible=positions.map(s=>({...s,...deltaAt(s.x,s.y,4,before,after)})).filter(s=>s.peak>=24&&s.count>=1);
 check(visible.length>=(width===390?6:15),'pixel proof: stars render above wash and are not fully covered');check(visible.some(s=>s.width>=3&&s.peak>=60),'larger bright stars are obvious pixels');
 await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).forEach(a=>a.play()));
 const opacityA=await p.locator('.star').evaluateAll(es=>es.map(e=>+getComputedStyle(e).opacity));await p.waitForTimeout(650);const opacityB=await p.locator('.star').evaluateAll(es=>es.map(e=>+getComputedStyle(e).opacity));
 check(opacityA.some((v,i)=>Math.abs(v-opacityB[i])>.1),'twinkle visibly changes opacity with real elapsed time');
 const trailSamples=[];let pixelTrail=null;
 for(let i=0;i<34;i++){
  const sample=await p.locator('.shooting-star').evaluateAll(es=>es.map(e=>{const b=e.getBoundingClientRect(),a=e.getAnimations()[0];return {x:b.x,y:b.y,width:b.width,height:b.height,opacity:+getComputedStyle(e).opacity,time:a.currentTime,duration:a.effect.getTiming().duration,delay:a.effect.getTiming().delay}}));
  trailSamples.push(sample);
  if(!pixelTrail){const active=sample.find(s=>s.opacity>.5&&s.x+s.width>0&&s.x<width&&s.y>64&&s.y<p.viewportSize().height);if(active){
   await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).forEach(a=>a.pause()));await p.waitForTimeout(40);
   const on=await sharp(await p.screenshot()).removeAlpha().raw().toBuffer({resolveWithObject:true});const style=await p.addStyleTag({content:'.shooting-star{visibility:hidden!important}'});const off=await sharp(await p.screenshot()).removeAlpha().raw().toBuffer({resolveWithObject:true});await style.evaluate(e=>e.remove());
   let changed=0,bright=0;for(let n=0;n<on.data.length;n+=3){const d=Math.max(...[0,1,2].map(k=>on.data[n+k]-off.data[n+k]));if(d>=24)changed++;if(d>=80)bright++;}
   await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).forEach(a=>a.play()));if(bright>=5&&changed>=30)pixelTrail={changedPixels:changed,brightPixels:bright};
  }}
  await p.waitForTimeout(200);
 }
 check(!!pixelTrail,'shooting trail has bright visible pixels during a normal seven-second window');
 check(trailSamples.some((s,i)=>i&&s.some((a,j)=>a.opacity>.4&&trailSamples[i-1][j].opacity>.4&&Math.abs(a.x-trailSamples[i-1][j].x)>15)),'shooting star travels with actual time');
 const periods=trailSamples[0];check(periods.every(s=>s.duration===12000)&&Math.abs(periods[0].delay-periods[1].delay)===6000,'one trail starts every six seconds');
 await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).forEach(a=>a.pause()));
 const rect=await p.evaluate(()=>{scrollTo({top:document.querySelector('#work').offsetTop,behavior:'instant'});return document.querySelector('.atmosphere').getBoundingClientRect().toJSON()});check(rect.top===0&&rect.height===p.viewportSize().height,'scene remains viewport-fixed beyond hero');
 const workOn=await sharp(await p.screenshot()).removeAlpha().raw().toBuffer({resolveWithObject:true});const hideWork=await p.addStyleTag({content:'.star-field{visibility:hidden!important}'});const workOff=await sharp(await p.screenshot()).removeAlpha().raw().toBuffer({resolveWithObject:true});await hideWork.evaluate(e=>e.remove());
 const pixelStarsBeyondHero=positions.filter(s=>deltaAt(s.x,s.y,4,workOn,workOff).peak>=24).length;check(pixelStarsBeyondHero>=6,'pixel proof: stars remain visible after scrolling beyond hero');
 if(width===1440||width===390)await p.screenshot({path:path.join(dest,`v5-stars-${engine.name()}-${width}-work-dark.png`)});
 await p.evaluate(()=>scrollTo({top:0,behavior:'instant'}));
 // Capture an actual keyframe halfway across the open sky, with stars retained.
 await p.evaluate(()=>{const es=document.querySelector('.atmosphere').getAnimations({subtree:true});es.forEach(a=>a.pause());document.querySelector('.shooting-one').getAnimations()[0].currentTime=150;});await p.waitForTimeout(50);
 await p.screenshot({path:path.join(dest,`v5-${engine===webkit?'webkit-':''}${width}-dark.png`),animations:'allow'});
 await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).forEach(a=>a.play()));
 results.starVisibility??=[];results.starVisibility.push({width,theme,stars:field.count,inViewport:positions.length,pixelVisibleStars:visible.length,peakStarDifference:Math.max(...visible.map(v=>v.peak)),twinkleObserved:true,trail:pixelTrail,trailPeriodMs:6000,fixedBeyondHero:true,pixelStarsBeyondHero,trailSamples});
}

async function rockets(p){
 check(await p.locator('.sky-light .sky-rocket').count()===2,'two light rockets');
 check(await p.locator('.sky-plane').count()===0,'planes removed');
 check(await p.locator('.sky-light .cloud').count()===3,'three clouds retained');
 const sample=()=>p.locator('.sky-rocket').evaluateAll(es=>es.map(e=>{
  const style=getComputedStyle(e),r=e.getBoundingClientRect();
  return {x:r.x,opacity:+style.opacity,flight:e.getAnimations()[0]?.animationName,puffs:[...e.querySelectorAll('.smoke-puff')].map(p=>({transform:getComputedStyle(p).transform,opacity:getComputedStyle(p).opacity,animation:p.getAnimations()[0]?.animationName})),flame:{opacity:getComputedStyle(e.querySelector('.rocket-flame')).opacity,animation:e.querySelector('.rocket-flame').getAnimations()[0]?.animationName},nose:e.querySelector('.rocket-nose').getBoundingClientRect().x,nozzle:e.querySelector('.rocket-nozzle').getBoundingClientRect().x};
 }));
 const before=await sample();await p.waitForTimeout(350);const after=await sample();
 check(after.every(r=>r.flight==='rocket-flight'&&r.opacity>0&&r.opacity<=.3&&r.nose>r.nozzle),'subtle rockets point along flight');
 check(after.every((r,i)=>r.x>before[i].x),'both rockets fly with elapsed time');
 check(after.every(r=>r.puffs.length===5&&r.puffs.every(s=>s.animation==='smoke-drift')&&r.flame.animation==='flame-flicker'),'each rocket animates five puffs and a flame');
 check(after.every((r,i)=>r.puffs.every((s,j)=>s.transform!==before[i].puffs[j].transform&&s.opacity!==before[i].puffs[j].opacity)),'both smoke trails drift and fade with elapsed time');
 check(after.every((r,i)=>r.flame.opacity!==before[i].flame.opacity),'both nozzle flames flicker with elapsed time');
 results.rockets??=[];results.rockets.push({page:new URL(p.url()).pathname,width:p.viewportSize().width,before,after});
}

async function launch(){browser=await engine.launch({headless:true,...(engine===chromium?{args:['--single-process','--no-zygote']}:{})});results.browserVersion=browser.version();return browser;}
async function close(){await browser.close();browser=null;}
(async()=>{
 for(const [width,height] of [[1440,900],[1280,900],[768,1024],[390,844]])for(const theme of ['light','dark']){
  await launch();const context=await browser.newContext({viewport:{width,height},deviceScaleFactor:1,colorScheme:theme});const p=await context.newPage();
  p.on('pageerror',e=>results.errors.push(e.message));p.on('requestfailed',r=>results.errors.push({url:r.url(),error:r.failure()?.errorText}));
  await p.addInitScript(()=>{window.motionShifts=[];if(PerformanceObserver.supportedEntryTypes.includes('layout-shift'))new PerformanceObserver(list=>{for(const e of list.getEntries())if(!e.hadRecentInput)window.motionShifts.push(e.value)}).observe({type:'layout-shift',buffered:true});});
  await p.goto(url,{waitUntil:'networkidle'});await ready(p);
  await wordmark(p);
  const s=await measure(p);results.samples.push(s);if(theme==='dark')await stars(p,width,theme);
  check(s.theme===theme,'theme follows system');check(s.scene===theme,'background follows theme');check(s.state==='running','motion enabled');check(s.activeScene.length===1&&s.activeScene[0]==='sky-'+theme,'one visible scene');check(!s.overflow,`${width} ${theme} overflow`);check(s.fonts.every(Boolean),'fonts loaded');check(s.portrait.loaded&&s.portrait.inside&&s.portrait.objectPosition==='50% 0%','portrait fits and preserves top');check(s.flow==='100+','final metric');check(s.contrast.failures.length===0,'all text AA '+JSON.stringify(s.contrast.failures));check(s.contrast.ui.every(u=>u.ratio>=3),'UI contrast');
  check(theme==='dark'?s.animations.some(a=>a.name==='twinkle')&&s.animations.some(a=>a.name==='shoot'):s.animations.some(a=>a.name==='cloud-drift')&&['rocket-flight','smoke-drift','flame-flicker'].every(name=>s.animations.some(a=>a.name===name)),'correct active animations');
  check(s.animations.every(a=>theme==='light'?!['twinkle','shoot'].includes(a.name):!['cloud-drift','rocket-flight','smoke-drift','flame-flicker'].includes(a.name)),'inactive scene has no rendered animations');
  if(theme==='light')await rockets(p);
  if(theme==='light')await p.screenshot({path:path.join(dest,`v5-${engine===webkit?'webkit-':''}${width}-${theme}.png`),animations:'allow'});if(width===1440&&theme==='light')await p.screenshot({path:path.join(dest,`v5-${engine===webkit?'webkit-':''}1440-full-light.png`),fullPage:true});
  const initial=await p.evaluate(()=>({shifts:window.motionShifts.length,sum:window.motionShifts.reduce((a,b)=>a+b,0)}));await p.waitForTimeout(250);
  await p.emulateMedia({reducedMotion:'reduce'});await p.waitForFunction(()=>document.querySelector('.atmosphere').dataset.state==='disabled');const reduced=await measure(p);let maxDelta=0;for(const key in s.rects)for(let i=0;i<4;i++)maxDelta=Math.max(maxDelta,Math.abs(s.rects[key][i]-reduced.rects[key][i]));
  check(maxDelta<.01,'motion does not shift layout');check(reduced.state==='disabled','reduced state');check(reduced.animations.every(a=>a.state!=='running'),'no animations in reduced mode');check(await p.locator('.atmosphere').evaluate(e=>getComputedStyle(e).display)==='none','no scenery under reduce');check(reduced.flow==='100+','reduced metric');
  await p.emulateMedia({reducedMotion:'no-preference'});await p.waitForTimeout(60);check((await measure(p)).state==='running','motion resumes after preference changes');
  await p.evaluate(()=>{Object.defineProperty(document,'hidden',{configurable:true,get:()=>true});document.dispatchEvent(new Event('visibilitychange'));});
  check(await p.locator('.atmosphere').getAttribute('data-state')==='paused','hidden state');
  await p.waitForTimeout(60);const before=await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).map(a=>({time:a.currentTime,state:a.playState})));await p.waitForTimeout(180);const after=await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).map(a=>({time:a.currentTime,state:a.playState})));
  check(before.length>0&&after.every(a=>a.state==='paused'),'hidden CSS loops paused');check(after.every((a,i)=>Math.abs(a.time-before[i].time)<.01),'hidden timeline stops');
  await p.evaluate(()=>{delete document.hidden;document.dispatchEvent(new Event('visibilitychange'));});await p.waitForTimeout(100);const resumed=await p.evaluate(()=>document.querySelector('.atmosphere').getAnimations({subtree:true}).map(a=>({time:a.currentTime,state:a.playState})));
  check(resumed.every((a,i)=>a.state==='running'&&a.time>after[i].time),'visible timelines resume');results.motion.push({width,theme,maxLayoutDelta:maxDelta,initialCLS:initial.sum,pausedAnimations:after.length,hiddenTimelinesStopped:true,resumed:true});
  await career(p);
  // Full retained disclosures and targeted contrast remain usable with motion.
  await p.locator('details').evaluateAll(ds=>ds.forEach(d=>d.open=true));const expanded=await measure(p);check(!expanded.overflow,'expanded overflow');check(expanded.contrast.failures.length===0,'expanded text AA '+JSON.stringify(expanded.contrast.failures));
  const axe=await new AxeBuilder({page:p}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();results.accessibility.push({width,theme,violations:axe.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))})),incomplete:axe.incomplete.map(v=>({id:v.id,nodes:v.nodes.length}))});check(axe.violations.length===0,'axe violations '+JSON.stringify(results.accessibility.at(-1).violations));
  await p.locator('details').evaluateAll(ds=>ds.forEach(d=>d.open=false));
  if(width===1440||width===390)await commands(p,theme);
  const next=theme==='light'?'dark':'light';await p.locator('.theme-toggle').focus();await p.keyboard.press('Enter');await p.waitForTimeout(300);const switched=await measure(p);check(switched.scene===next&&switched.activeScene.length===1&&switched.activeScene[0]==='sky-'+next,'toggle removes old scene');check(switched.accent===(next==='dark'?'#80ded5':'#075d73'),'accent toggles');await p.reload({waitUntil:'networkidle'});check(await p.locator('html').getAttribute('data-theme')===next,'theme persists after reload');check(await p.locator('.atmosphere').getAttribute('data-scene')===next,'scene persists after reload');await p.emulateMedia({colorScheme:theme});check(await p.locator('html').getAttribute('data-theme')===next,'saved theme overrides system');
  if(width===1440&&theme==='light'&&engine===chromium){
   await p.getByRole('link',{name:'Codec Ireland career record ↗'}).first().click();check(await p.locator('#career-codec details').evaluate(e=>e.open),'related career opens');await context.grantPermissions(['clipboard-read','clipboard-write']);await p.locator('.copy-email').click();await p.getByText('Email copied.',{exact:true}).waitFor();check(await p.evaluate(()=>navigator.clipboard.readText())==='itiangopi@gmail.com','copy email');
   const [download]=await Promise.all([p.waitForEvent('download'),p.getByRole('link',{name:'Download CV'}).click()]);check(download.suggestedFilename()==='Gopinath_Gurusamy_Resume.pdf','download filename');await download.saveAs('/private/tmp/portfolio-v5-resume.pdf');check(readFileSync('/private/tmp/portfolio-v5-resume.pdf').subarray(0,5).toString()==='%PDF-','valid downloaded PDF');
  }
  console.log(JSON.stringify({width,theme,status:'PASS',minContrast:s.contrast.minRatio,layoutDelta:maxDelta}));await close();
 }
 for(const theme of ['light','dark']){
  await launch();const p=await browser.newPage({viewport:{width:390,height:844},deviceScaleFactor:1,colorScheme:theme,reducedMotion:'reduce'});await p.goto(url,{waitUntil:'networkidle'});await ready(p);const s=await measure(p);check(s.state==='disabled'&&s.animations.length===0,'reduced motion on initial load');check(s.flow==='100+','reduced initial metric');await commands(p,theme,true);await p.locator('.theme-toggle').click();check(await p.locator('.atmosphere').getAttribute('data-state')==='disabled','toggle keeps reduce disabled');await close();
 }
 await launch();const p=await browser.newPage({viewport:{width:1440,height:900},colorScheme:'light'});await p.goto(url,{waitUntil:'networkidle'});await p.emulateMedia({colorScheme:'dark'});await p.waitForFunction(()=>document.documentElement.dataset.theme==='dark');check(await p.locator('.atmosphere').getAttribute('data-scene')==='dark','unsaved system dark scene');await p.emulateMedia({colorScheme:'light'});await p.waitForFunction(()=>document.documentElement.dataset.theme==='light');check(await p.locator('.atmosphere').getAttribute('data-scene')==='light','unsaved system light scene');
 for(const width of [320,360,650,960,1000,1100,1200])for(const theme of ['light','dark']){await p.setViewportSize({width,height:900});await p.emulateMedia({colorScheme:theme});await p.waitForFunction(t=>document.documentElement.dataset.theme===t,theme);check(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`extra ${width} ${theme} overflow`);}
 for(const width of [1440,390]){await p.setViewportSize({width,height:900});await p.goto(url+'#career-codec',{waitUntil:'networkidle'});check(await p.locator('#career-codec details').evaluate(e=>e.open),'initial Codec hash opens record');await p.evaluate(()=>{location.hash='career-bank';});await p.waitForFunction(()=>document.querySelector('#career-bank details').open);check(await p.locator('#career-bank details').evaluate(e=>e.open),'hashchange opens career record');}
 for(const theme of ['light','dark']){await p.emulateMedia({colorScheme:theme});for(const width of [1440,390]){await p.setViewportSize({width,height:900});await p.goto(url+'404.html',{waitUntil:'networkidle'});await ready(p);await wordmark(p,false);const s=await measure(p);check(!s.overflow,'404 overflow');check(s.scene===theme,'404 scene');if(theme==='light')await rockets(p);check(s.contrast.failures.length===0,'404 contrast');await p.getByRole('link',{name:/Back to portfolio/}).click();check(await p.locator('#hero-title').count()===1,'404 return');}}
 await close();check(results.errors.length===0,'no page/request errors');results.status='PASS';results.checks=checks;writeFileSync(path.join(dest,`v5-stars-${engine.name()}-results.json`),JSON.stringify(results,(_k,v)=>typeof v==='number'?Math.round(v*100)/100:v,2));console.log(JSON.stringify({status:results.status,checks,samples:results.samples.length,motion:results.motion,errors:results.errors},null,2));
})().catch(async e=>{results.status=engine===webkit&&!results.browserVersion?'BLOCKED':'FAIL';results.failure=e.message;results.checks=checks;writeFileSync(path.join(dest,`v5-stars-${engine.name()}-results.json`),JSON.stringify(results,(_k,v)=>typeof v==='number'?Math.round(v*100)/100:v,2));console.error(e);if(browser)await close();process.exitCode=1;});
