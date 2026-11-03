/* Progressive enhancement: content and navigation work without JavaScript. */
(() => {
  'use strict';
  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  const colourPreference = window.matchMedia('(prefers-color-scheme: dark)');
  try {
    const saved = localStorage.getItem('gg-theme');
    if (saved === 'light' || saved === 'dark') root.dataset.theme = saved;
  } catch { /* Storage may be unavailable. */ }
  const currentTheme = () => root.dataset.theme || (colourPreference.matches ? 'dark' : 'light');
  const updateTheme = () => {
    const dark = currentTheme() === 'dark';
    if (themeButton) {
      themeButton.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
      themeButton.setAttribute('aria-pressed', String(dark));
    }
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', dark ? '#101923' : '#f8faf9');
  };
  if (themeButton) {
    themeButton.hidden = false;
    themeButton.addEventListener('click', () => {
      root.dataset.theme = currentTheme() === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('gg-theme', root.dataset.theme); } catch { /* Use the current visit. */ }
      updateTheme();
    });
  }
  colourPreference.addEventListener('change', updateTheme);
  updateTheme();
  const copyButton = document.querySelector('.copy-email');
  if (copyButton && navigator.clipboard?.writeText) {
    copyButton.hidden = false;
    copyButton.addEventListener('click', async () => {
      const status = document.querySelector('.copy-status');
      try {
        await navigator.clipboard.writeText('itiangopi@gmail.com');
        copyButton.textContent = 'Copied!';
        if (status) status.textContent = 'Email address copied to clipboard.';
        window.setTimeout(() => { copyButton.textContent = 'Copy email'; }, 2200);
      } catch {
        if (status) status.textContent = 'Copy unavailable. Select the email address or use the email link.';
        copyButton.textContent = 'Select email to copy';
      }
    });
  }
  if (!('IntersectionObserver' in window)) return;
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.04 });
  if (!motion.matches) {
    document.querySelectorAll('.reveal').forEach(element => revealObserver.observe(element));
    root.classList.add('reveal-enabled');
  }
  motion.addEventListener('change', event => {
    if (event.matches) { root.classList.remove('reveal-enabled'); revealObserver.disconnect(); }
  });
  const format = new Intl.NumberFormat('en-IE');
  const counterObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      counterObserver.unobserve(entry.target);
      const counter = entry.target;
      const target = Number(counter.dataset.count);
      if (motion.matches) return;
      // Preserve authoritative accessible values while animating visual numbers.
      const accessible = document.createElement('span');
      accessible.className = 'sr-only'; accessible.textContent = format.format(target);
      const visual = document.createElement('span'); visual.setAttribute('aria-hidden', 'true');
      // CSS renders the animation; without it, only the source value is visible.
      visual.className = 'counter-visual';
      counter.replaceChildren(accessible, visual);
      const start = performance.now();
      const tick = now => {
        const progress = motion.matches ? 1 : Math.min((now - start) / 950, 1);
        visual.dataset.value = format.format(Math.round(target * (1 - Math.pow(1 - progress, 3))));
        if (progress < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.8 });
  document.querySelectorAll('[data-count]').forEach(counter => counterObserver.observe(counter));
  const navigation = [...document.querySelectorAll('.site-header nav a')];
  const sections = navigation.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
  const updateNavigation = () => {
    const headerHeight = document.querySelector('.site-header')?.getBoundingClientRect().height || 90;
    let active;
    sections.forEach(section => {
      if (section.getBoundingClientRect().top <= headerHeight + 90) active = section.id;
    });
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 8) active = 'contact';
    navigation.forEach(link => {
      if (link.hash === `#${active}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };
  let scheduled = false;
  window.addEventListener('scroll', () => {
    if (!scheduled) {
      scheduled = true;
      requestAnimationFrame(() => { updateNavigation(); scheduled = false; });
    }
  }, { passive: true });
  window.addEventListener('resize', updateNavigation);
  updateNavigation();
})();
