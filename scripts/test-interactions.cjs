/* Development-only interaction checks. Requires jsdom; production has no dependencies. */
const { JSDOM } = require('jsdom');
const { readFileSync } = require('node:fs');
const { resolve } = require('node:path');
const assert = require('node:assert/strict');
const root = resolve(__dirname, '..');
const html = readFileSync(resolve(root, 'index.html'), 'utf8');
const code = readFileSync(resolve(root, 'assets/js/main.js'), 'utf8');
let checks = 0;
function check(fn) { fn(); checks++; }
function page({stored, dark = false, storageFailure = false, clipboardFailure = false, reduced = false} = {}) {
  const dom = new JSDOM(html, { url: 'http://127.0.0.1:8093/', runScripts: 'outside-only' });
  const w = dom.window;
  const listeners = {};
  w.matchMedia = query => ({matches: query.includes('reduced-motion') ? reduced : dark, addEventListener: (type, fn) => { listeners[query] = fn; }});
  if (stored) w.localStorage.setItem('portfolio-theme', stored);
  if (storageFailure) Object.defineProperty(w, 'localStorage', {get(){throw Error('Unavailable');}});
  Object.defineProperty(w, 'isSecureContext', {value:true});
  let copied;
  Object.defineProperty(w.navigator, 'clipboard', {value:{writeText: async value => {if(clipboardFailure)throw Error('Denied');copied=value;}}});
  w.eval(code);
  return {w,doc:w.document,listeners,getCopied:()=>copied,close:()=>w.close()};
}
(async () => {
  for (const reduced of [false, true]) {
    const p = page({reduced}); const {w,doc}=p;
    const input=doc.querySelector('#terminal-command'),form=doc.querySelector('.terminal-form'),out=doc.querySelector('.terminal-output');
    function run(command){input.value=command;form.dispatchEvent(new w.Event('submit',{bubbles:true,cancelable:true}));return out.lastElementChild?.textContent.trimEnd();}
    check(()=>assert.match(run('help'), /pac certs[\s\S]*pac contact[\s\S]*pac projects[\s\S]*clear/));
    check(()=>assert.ok(out.textContent.includes('explore. › help ')));
    check(()=>assert.match(run('pac certs'), /PL-600[\s\S]*AB-100[\s\S]*AB-620[\s\S]*MCSE[\s\S]*MCSA/));
    const contact=run('pac contact');
    check(()=>assert.equal(contact,'Email: itiangopi@gmail.com\nLinkedIn: https://www.linkedin.com/in/gopinath-gurusamy'));
    const projects=run('pac projects').split('\n');
    check(()=>assert.equal(projects[0],'Case Assistant'));
    check(()=>assert.equal(projects.length,6));
    check(()=>assert.match(run('pac copilot'), /AI & Copilot[\s\S]*Find and summarise a case[\s\S]*AB-100 · AB-620/));
    check(()=>assert.match(run('  PAC   CONTACT '), /itiangopi@gmail.com/));
    check(()=>assert.equal(doc.activeElement,input));
    check(()=>assert.equal(input.value,''));
    check(()=>assert.match(run('<img src=x onerror=alert(1)>'),/not recognised/));
    check(()=>assert.equal(out.querySelectorAll('img').length,0));
    run('clear');check(()=>assert.equal(out.children.length,0));
    run('   ');check(()=>assert.equal(out.children.length,0));
    for(let i=0;i<40;i++)run('help');check(()=>assert.equal(out.children.length,60));
    check(()=>assert.equal(doc.querySelector('[data-count="100"]').parentElement.textContent,'100+'));
    const toggle=doc.querySelector('.theme-toggle');toggle.click();
    check(()=>assert.equal(doc.documentElement.dataset.theme,'dark'));
    check(()=>assert.equal(w.localStorage.getItem('portfolio-theme'),'dark'));
    check(()=>assert.equal(toggle.getAttribute('aria-pressed'),'true'));
    check(()=>assert.equal(toggle.getAttribute('aria-label'),'Switch to light theme'));
    toggle.click();check(()=>assert.equal(doc.documentElement.dataset.theme,'light'));
    doc.querySelector('#career-bank details').open=false;
    doc.querySelector('a[href="#career-bank"]').click();check(()=>assert.equal(doc.querySelector('#career-bank details').open,true));
    doc.querySelector('.copy-email').click();await new Promise(resolve=>setImmediate(resolve));
    check(()=>assert.equal(p.getCopied(),'itiangopi@gmail.com'));
    check(()=>assert.equal(doc.querySelector('.copy-status').textContent,'Email copied.'));
    p.close();
  }
  for(const options of [{stored:'dark'}, {dark:true}, {stored:'invalid',dark:true}]){
    const p=page(options);check(()=>assert.equal(p.doc.documentElement.dataset.theme,'dark'));p.close();
  }
  const saved=page({stored:'light',dark:true});check(()=>assert.equal(saved.doc.documentElement.dataset.theme,'light'));saved.close();
  const denied=page({storageFailure:true});denied.doc.querySelector('.theme-toggle').click();check(()=>assert.equal(denied.doc.documentElement.dataset.theme,'dark'));denied.close();
  const system=page();system.listeners['(prefers-color-scheme: dark)']({matches:true});check(()=>assert.equal(system.doc.documentElement.dataset.theme,'dark'));system.close();
  const clipboard=page({clipboardFailure:true});clipboard.doc.querySelector('.copy-email').click();await new Promise(resolve=>setImmediate(resolve));check(()=>assert.match(clipboard.doc.querySelector('.copy-status').textContent,/Select the email/));clipboard.close();
  console.log(`PASS: ${checks} interaction assertions (DOM simulation; browser layout tested separately).`);
})().catch(error=>{console.error(error);process.exitCode=1;});
