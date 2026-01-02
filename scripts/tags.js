/* global hexo */
'use strict';

const path = require('path');
const root = path.join('..', 'plugins', 'tags');

hexo.extend.tag.register('animcube', require(path.join(root, 'animate_cube'))(hexo));
hexo.extend.tag.register('badge_github', require(path.join(root, 'badge_github'))(hexo));
hexo.extend.tag.register('invert', require(path.join(root, 'invert'))(hexo), true);
hexo.extend.tag.register('snippet', require(path.join(root, 'snippet'))(hexo), { async: true });
