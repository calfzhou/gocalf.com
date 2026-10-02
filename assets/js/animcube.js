// GoCalf-owned adapter. Original libraries are trusted local source assets; author
// data selects no executable names/code, eval APIs or external configuration URLs.
(() => {
  const constructors = {2: window.AnimCube2, 3: window.AnimCube3, 4: window.AnimCube4,
    5: window.AnimCube5, 6: window.AnimCube6, 7: window.AnimCube7};
  const allowed = new Set(['config', 'facelets', 'markers', 'move', 'initmove',
    'initrevmove', 'movetext', 'position', 'repeat']);
  const figures = [...document.querySelectorAll('.gocalf-cube')];
  function initialize(figure) {
    const view = figure.querySelector('.cube-view');
    // Do not instantiate a zero-width canvas inside a closed native disclosure.
    if (figure.dataset.cubeInitialized || figure.closest('details:not([open])') || !view.getClientRects().length || view.clientWidth === 0) return;
    figure.dataset.cubeInitialized = 'true';
    try {
      const options = JSON.parse(figure.dataset.cubeOptions);
      if (!options || Array.isArray(options) || typeof options !== 'object') throw new Error('Invalid cube data');
      const parts = [['id', view.id]];
      for (const [key, value] of Object.entries(options)) {
        if (!allowed.has(key) || typeof value !== 'string' || /[\x00-\x1f\x7f]/.test(value)) throw new Error('Invalid cube parameter');
        if (key === 'config' && !/^[A-Za-z0-9_-]+\.conf$/.test(value)) throw new Error('Invalid cube config');
        parts.push([key, value]);
      }
      const create = constructors[figure.dataset.cubeSize];
      if (typeof create !== 'function') throw new Error('Missing local cube library');
      // Encode values separately: algorithms/markers stay data after the library's
      // decodeURIComponent. Never interpolate them into JavaScript source.
      create(parts.map(([k, v]) => k + '=' + encodeURIComponent(v)).join('&'));
    } catch (error) {
      figure.dataset.cubeInitialized = 'failed';
      figure.querySelector('.cube-error').hidden = false;
      console.warn('GoCalf cube could not initialize', error);
    }
  }
  // Native libraries own their canvas/mouse/animation lifecycle. Defer closed-fold
  // initialization until visible; no clones or reinitialization on repeated toggles.
  figures.forEach(initialize);
  for (const details of document.querySelectorAll('details')) {
    details.addEventListener('toggle', () => {
      if (!details.open) return;
      details.querySelectorAll('.gocalf-cube').forEach(initialize);
      // The preserved library owns window resize. Do not synthesize resize while
      // another cube is still loading its asynchronous config (graphics not ready).
    });
  }
})();
