'use strict';

hexo.extend.tag.register('badge_github', require('./badge_github')(hexo));
hexo.extend.tag.register('animcube', require('./animate_cube')(hexo));
hexo.extend.tag.register('invert', require('./invert')(hexo), true);
hexo.extend.tag.register('asset_code', require('./asset_code')(hexo), { async: true });
