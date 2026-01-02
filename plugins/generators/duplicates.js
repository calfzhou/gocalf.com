'use strict';

// Inspired by https://github.com/hexojs/hexo-generator-alias, but will duplicate the content instead of redirecting.
module.exports = function (locals) {
  const routes = [];
  const hexo = this;

  const duplicatesConfig = hexo.config.duplicates;
  if (typeof duplicatesConfig === 'object') {
    Object.entries(duplicatesConfig).forEach(([dst, src]) => {
      // console.log('duplicates from', src, 'to', dst);
      routes.push({
        path: dst,
        data: function () {
          return hexo.route.get(src);
        },
      });
    });
  }

  return routes;
};
