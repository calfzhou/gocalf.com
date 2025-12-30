'use strict';

const intra_links = require('./intra_links');
const markdown_it = require('./markdown_it');
const md_path_to_permalink = require('./md_path_to_permalink');

hexo.extend.filter.register('before_post_render', md_path_to_permalink.preProcess, 20);
hexo.extend.filter.register('before_post_render', md_path_to_permalink.convertLinks, 21);

hexo.extend.filter.register('before_post_render', intra_links.preProcess, 30);
hexo.extend.filter.register('before_post_render', intra_links.processSite, 31);
hexo.extend.filter.register('before_post_render', intra_links.postProcess, 32);

hexo.extend.filter.register('markdown-it:renderer', markdown_it.customize, 10);
