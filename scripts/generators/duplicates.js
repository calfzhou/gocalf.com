'use strict';

// Inspired by https://github.com/hexojs/hexo-generator-alias, but will duplicate the content instead of redirecting.
hexo.extend.generator.register('duplicates', function (locals) {
  const routes = [];

  const { config } = hexo;
  const duplicatesConfig = config.duplicates;
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
});
