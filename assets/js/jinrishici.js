// Site-owned SDK bridge. Keep provider text out of HTML parsing and article indexes.
(() => {
  const host = document.querySelector('[data-gocalf-poem]');
  if (!host || host.dataset.initialized) return;
  host.dataset.initialized = 'true';
  host.dataset.state = 'loading';
  const sentence = host.querySelector('[data-poem-text]');
  let settled = false;
  const unavailable = () => {
    if (settled) return;
    settled = true;
    clearTimeout(timer);
    host.dataset.state = 'unavailable'; // Leave the empty widget hidden.
  };
  const timer = setTimeout(unavailable, 12000);
  const load = () => {
    if (settled) return;
    try {
      if (typeof window.jinrishici?.load !== 'function') return unavailable();
      window.jinrishici.load(result => {
        if (settled) return;
        const text = result?.data?.content;
        if (result?.status !== 'success' || typeof text !== 'string' || !text.trim()) return unavailable();
        settled = true;
        clearTimeout(timer);
        sentence.textContent = text;
        host.hidden = false;
        host.dataset.state = 'ready';
      }, unavailable);
    } catch { unavailable(); }
  };
  if (typeof window.jinrishici?.load === 'function') return load();
  const sdk = document.createElement('script');
  sdk.src = 'https://sdk.jinrishici.com/v2/browser/jinrishici.js';
  sdk.async = true;
  sdk.referrerPolicy = 'no-referrer';
  sdk.addEventListener('load', load, {once: true});
  sdk.addEventListener('error', unavailable, {once: true});
  document.head.append(sdk);
})();
