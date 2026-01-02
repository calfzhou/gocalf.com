/* global hexo */
'use strict';

const path = require('path');
const root = path.join('..', 'plugins', 'generators');

hexo.extend.generator.register('sitemap', require(path.join(root, 'duplicates')));
