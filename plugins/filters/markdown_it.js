'use strict';

const { alert } = require('@mdit/plugin-alert');
const { figure } = require('@mdit/plugin-figure');
const { obsidianImageSize } = require('@mdit/plugin-img-size');
// const { snippet } = require('@mdit/plugin-snippet');

module.exports.customize = parser => {
  parser
    .use(alert)
    .use(figure)
    .use(obsidianImageSize);

  // parser.use(snippet, {
  //   // `postPath` is provided by hexo-renderer-markdown-it
  //   // See: https://github.com/hexojs/hexo-renderer-markdown-it/blob/master/lib/renderer.js
  //   currentPath: (env) => env.postPath,
  // });
};
