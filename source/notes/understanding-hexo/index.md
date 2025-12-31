---
title: Understanding Hexo
notebook: notes
tags:
  - it/web
date: 2026-01-01 01:19:45
updated: 2026-01-01 01:19:45
---
## Hexo

[Hexo - A fast, simple & powerful blog framework](https://hexo.io/)

[hexojs/hexo: A fast, simple & powerful blog framework, powered by Node.js.](https://github.com/hexojs/hexo)

## Filters

[Filter | Hexo](https://hexo.io/api/filter)

Use demo filters to check evaluating order:

```js
const demoFilters = [
  'before_post_render',
  'after_post_render',
  'before_exit',
  'before_generate',
  'after_generate',
  'template_locals',
  'after_init',
  'new_post_path',
  'post_permalink',
  'after_render',
  'after_clean',
  'server_middleware',
  'markdown-it:renderer'
];

demoFilters.forEach(filter => {
  hexo.extend.filter.register(filter, function(data, options = {}) {
    let source = data?.source;
    if (!source) {
      if (filter === 'post_permalink') {
        source = data;
      }
    }

    console.log(`[Demo] Filter for ${filter} called: ${source}`);
    return data;
  }, 20);
});
```

### Processing Flow of `hexo generate`

1. Initialization
    - `Validating config`
    - `after_init` filter
    - `Start processing`
2. Article (Posts and Pages) Rendering
    - `post_permalink` filter (called repeatedly, for `_posts`)
    - `before_post_render` filter (called repeatedly)
    - `markdown-it:renderer` filter (called repeatedly, for `.md` files)
    - Tag plugins (`markdown-it:renderer` filter might be called if tag plugin calls renderer)
    - `after_post_render` filter (called repeatedly)
3. Generation
    - `before_generate` filter
    - `post_permalink` filter (called repeatedly again, for `_posts`)
    - `template_locals` filter (called repeatedly)
    - `after_generate` filter
4. Files Loaded❔
    - `Files loaded`
5. HTML Rendering
    - `markdown-it:renderer` filter (called repeatedly, for 正文之外的部分如 side bar, footer)
6. HTML Generation
    - `Generated: ...` (outputting files)
    - `hexo-esbuild: processed ...` (js and css files minify) 
7. Exit
    - `before_exit` filter

### Processing Flow of `hexo server`

The server starting:

1. Initialization
    - `Validating config`
    - `after_init` filter
    - 🆕 `server_middleware` filter
    - `Start processing`
2. Article (Posts and Pages) Rendering
    - `post_permalink` filter (called repeatedly, for `_posts`)
    - `before_post_render` filter (called repeatedly)
    - `markdown-it:renderer` filter (called repeatedly, for `.md` files)
    - Tag plugins (`markdown-it:renderer` filter might be called if tag plugin calls renderer)
    - `after_post_render` filter (called repeatedly)
3. Generation
    - `before_generate` filter
    - `post_permalink` filter (called repeatedly again, for `_posts`)
    - `template_locals` filter (called repeatedly)
    - `after_generate` filter
4. Server Started
    - `Hexo is running at http://localhost:4000/ . Press Ctrl+C to stop.`
    - `before_exit` filter
5. Generation Again
    - `before_generate` filter
    - `post_permalink` filter (called repeatedly again, for `_posts`)
    - `template_locals` filter (called repeatedly)
    - `after_generate` filter

When browsing a page:

1. HTML Rendering
    - `markdown-it:renderer` filter (called repeatedly, for 正文之外的部分如 side bar, footer)
2. Assets Generation
    - `hexo-esbuild: processed ...` (js and css files minify) 

When a post or page modified:

1. Article (Posts and Pages) Rendering
    - `before_post_render` filter (for the modified file)
    - `markdown-it:renderer` filter (for the modified file)
    - Tag plugins (`markdown-it:renderer` filter might be called if tag plugin calls renderer)
    - `after_post_render` filter (for the modified file)
2. Generation
    - `before_generate` filter
    - `post_permalink` filter (called repeatedly again, for `_posts`)
    - `template_locals` filter (called repeatedly)
    - `after_generate` filter

Stopping the server:

1. Exit
    - `Have a nice day`
    - `before_exit` filter

### Processing Flow of `hexo clean`

```log
> hexo clean

INFO  Validating config
[Demo] Filter for after_init called
[Demo] Filter for after_clean called
INFO  Deleted database.
INFO  Deleted public folder.
[Demo] Filter for before_exit called
```
