'use strict'

const intra_links = require('./intra_links')

hexo.extend.filter.register('before_post_render', intra_links.preProcess, 10)
hexo.extend.filter.register('before_post_render', intra_links.processSite, 20)
hexo.extend.filter.register('before_post_render', intra_links.postProcess, 30)
