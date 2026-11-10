/* Original progressive enhancements; all public facts remain in HTML. */
(() => {
  'use strict';
  const root = document.documentElement;
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  let chosenTheme;
  try { chosenTheme = localStorage.getItem('portfolio-theme'); } catch { /* Storage is optional. */ }
  if (chosenTheme !== 'light' && chosenTheme !== 'dark') chosenTheme = undefined;
  const toggle = document.querySelector('.theme-toggle');
  function applyTheme(theme) {
    root.dataset.theme = theme;
    const themeColour = document.querySelector('meta[name="theme-color"]');
    if (themeColour) themeColour.content = theme === 'dark' ? '#081631' : '#7ec8ff';
    if (toggle) {
      toggle.setAttribute('aria-pressed', String(theme === 'dark'));
      toggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`);
      toggle.textContent = '☀ ☾';
    }
  }
  applyTheme(chosenTheme === 'light' || chosenTheme === 'dark' ? chosenTheme : systemTheme.matches ? 'dark' : 'light');
  if (toggle) {
    toggle.hidden = false;
    toggle.addEventListener('click', () => {
      chosenTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      applyTheme(chosenTheme);
      try { localStorage.setItem('portfolio-theme', chosenTheme); } catch { /* Preference still works for this visit. */ }
    });
  }
  systemTheme.addEventListener('change', event => { if (!chosenTheme) applyTheme(event.matches ? 'dark' : 'light'); });
  const copy = document.querySelector('.copy-email');
  if (copy && navigator.clipboard && window.isSecureContext) {
    copy.hidden = false;
    copy.addEventListener('click', async () => {
      const status = document.querySelector('.copy-status');
      try { await navigator.clipboard.writeText('itiangopi@gmail.com'); status.textContent = 'Email copied.'; }
      catch { status.textContent = 'Select the email address to copy it.'; }
    });
  }
  // Values stay final: no distracting or misleading intermediate counts.
  const navLinks = [...document.querySelectorAll('.desktop-nav a')];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) {
        navLinks.forEach(link => {
          if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      }
    }, { rootMargin: '-10% 0px -55% 0px' });
    navLinks.forEach(link => { const section = document.querySelector(link.hash); if (section) observer.observe(section); });
  }
  // Related links also open their target record when it is a disclosure.
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', () => {
      const target = document.getElementById(link.hash.slice(1));
      const record = target?.querySelector('details.career-record');
      if (record) record.open = true;
    });
  });
  function openLinkedRecord() {
    const target = document.getElementById(location.hash.slice(1));
    const record = target?.querySelector('details.career-record');
    if (record) record.open = true;
  }
  window.addEventListener('hashchange', openLinkedRecord);
  openLinkedRecord();
  const terminal = document.querySelector('[data-terminal]');
  if (!terminal) return;
  const output = terminal.querySelector('.terminal-output');
  const input = terminal.querySelector('input');
  const form = terminal.querySelector('form');
  const certifications = [...document.querySelectorAll('.credential-register li')].map(item => {
    return `${item.querySelector('.register-code').textContent} — ${item.querySelector('h3').textContent}`;
  });
  const projects = [...document.querySelectorAll('#work > .solution-card h3')].map(item => item.textContent);
  const commands = {
    'help': 'Available commands:\nhelp — show commands\npac certs — Microsoft certifications\npac contact — email and LinkedIn\npac projects — selected work; see #work\npac copilot — AI & Copilot; see #copilot\nclear — clear terminal',
    'pac certs': certifications.join('\n') + '\nAlso: MB2-707 · MB2-715 · MB2-716 · MB2-718 · ICAgile Fundamentals',
    'pac contact': 'Email: itiangopi@gmail.com\nLinkedIn: https://www.linkedin.com/in/gopinath-gurusamy',
    'pac projects': projects.join('\n') + '\nAI & Copilot: #copilot (pac copilot)',
    'pac copilot': 'AI & Copilot — #copilot\nCase Assistant: Copilot Studio agent for Dynamics 365 Customer Service\nClient: a regulatory body\nFind and summarise a case\nFind case documents\nSuggest next steps\nCreate a case\nD365 Copilot: case summaries including custom fields; draft email replies; knowledge-grounded answers with citations; similar-case matching.\nAB-100 · AB-620 — verify links in AI & Copilot.'
  };
  form.addEventListener('submit', event => {
    event.preventDefault();
    const typed = input.value.trim();
    const command = typed.toLowerCase().replace(/\s+/g, ' ');
    if (!command) { input.focus(); return; }
    if (command === 'clear') output.replaceChildren();
    else {
      const echo = document.createElement('p');
      echo.className = 'command-echo';
      echo.textContent = `› ${typed} `;
      const answer = document.createElement('p');
      answer.textContent = (commands[command] || 'Command not recognised. Type help for available commands.') + ' ';
      output.append(echo, answer);
      // Keep long sessions manageable without ever interpreting input as HTML.
      while (output.children.length > 60) output.firstElementChild.remove();
      output.scrollTop = output.scrollHeight;
    }
    input.value = '';
    input.focus();
  });
})();
