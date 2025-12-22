'use strict';

// Override hexo-theme-stellar pretty_urls helper to use default URL formatting.
// See: https://github.com/xaoxuu/hexo-theme-stellar/commit/fd21ccd89c50a3bdb96b0e1b50b342089519f493
hexo.extend.helper.register('pretty_url', path => {
  return this.url_for(path);
});
