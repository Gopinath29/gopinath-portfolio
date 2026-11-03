/* Astrofy static adaptation. Accessible progressive enhancements only. */
(() => {
  'use strict';
  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  const preference = matchMedia('(prefers-color-scheme: dark)');
  try {
    const saved = localStorage.getItem('gg-theme');
    if (saved === 'light' || saved === 'dark') root.dataset.theme = saved;
  } catch { /* System preference remains available without storage. */ }
  const currentTheme = () => root.dataset.theme || (preference.matches ? 'dark' : 'light');
  const updateTheme = () => {
    const dark = currentTheme() === 'dark';
    if (themeButton) {
      themeButton.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
      themeButton.setAttribute('aria-pressed', String(dark));
    }
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', dark ? '#17201d' : '#f8f7f3');
  };
  if (themeButton) {
    themeButton.hidden = false;
    themeButton.addEventListener('click', () => {
      root.dataset.theme = currentTheme() === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('gg-theme', root.dataset.theme); } catch { /* Keep the visit preference. */ }
      updateTheme();
    });
  }
  preference.addEventListener('change', updateTheme);
  updateTheme();
  // The final value is source text. Enhance only the flows figure when styled,
  // visible and motion is welcome; keep its accessible name stable throughout.
  const flowCount = document.querySelector('[data-target]');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const counterStyled = () => flowCount && getComputedStyle(flowCount).getPropertyValue('--flow-counter-motion').trim() === 'enabled';
  if (flowCount && counterStyled() && !reducedMotion.matches && 'IntersectionObserver' in window) {
    const target = Number(flowCount.dataset.target);
    const observer = new IntersectionObserver(entries => {
      if (!entries.some(entry => entry.isIntersecting)) return;
      observer.disconnect();
      const start = performance.now();
      const tick = now => {
        const progress = reducedMotion.matches || !counterStyled() ? 1 : Math.min((now - start) / 850, 1);
        flowCount.textContent = String(Math.round(target * (1 - (1 - progress) ** 3)));
        if (progress < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }, { threshold: 0.5 });
    observer.observe(flowCount);
  }
  const copyButton = document.querySelector('.copy-email');
  if (copyButton && navigator.clipboard?.writeText) {
    copyButton.hidden = false;
    copyButton.addEventListener('click', async () => {
      const status = document.querySelector('.copy-status');
      try {
        await navigator.clipboard.writeText('itiangopi@gmail.com');
        copyButton.textContent = 'Copied!';
        if (status) status.textContent = 'Email address copied to clipboard.';
        setTimeout(() => { copyButton.textContent = 'Copy email'; }, 2200);
      } catch {
        if (status) status.textContent = 'Copy unavailable. Select the email address or use the email link.';
        copyButton.textContent = 'Select email to copy';
      }
    });
  }
  const navigation = [...document.querySelectorAll('.architect-panel nav a')];
  const sections = navigation.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
  const updateNavigation = () => {
    const headerHeight = document.querySelector('.site-header')?.getBoundingClientRect().height || 96;
    let active;
    sections.forEach(section => { if (section.getBoundingClientRect().top <= headerHeight + 90) active = section.id; });
    if (innerHeight + scrollY >= document.documentElement.scrollHeight - 8) active = 'contact';
    navigation.forEach(link => {
      if (link.hash === `#${active}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };
  let scheduled = false;
  addEventListener('scroll', () => {
    if (!scheduled) {
      scheduled = true;
      requestAnimationFrame(() => { updateNavigation(); scheduled = false; });
    }
  }, { passive: true });
  addEventListener('resize', updateNavigation);
  updateNavigation();
})();
