/* global hexo */
'use strict';

const path = require('path');
const root = path.join('..', 'plugins', 'filters');

const markdown_it = require(path.join(root, 'markdown_it'));
hexo.extend.filter.register('markdown-it:renderer', markdown_it.customize, 10);

const md_path_to_permalink = require(path.join(root, 'md_path_to_permalink'));
hexo.extend.filter.register('before_post_render', md_path_to_permalink.preProcess, 40);
hexo.extend.filter.register('before_post_render', md_path_to_permalink.convertLinks, 41);

const intra_links = require(path.join(root, 'intra_links'));
hexo.extend.filter.register('before_post_render', intra_links.preProcess, 45);
hexo.extend.filter.register('before_post_render', intra_links.processSite, 46);
hexo.extend.filter.register('before_post_render', intra_links.postProcess, 47);
