---
title: Understanding Hexo
notebook: notes
tags:
  - it/web
date: 2026-01-01 01:19:45
updated: 2026-01-02 19:37:01
---
## Hexo

[Hexo - A fast, simple & powerful blog framework](https://hexo.io/)

[hexojs/hexo: A fast, simple & powerful blog framework, powered by Node.js.](https://github.com/hexojs/hexo)

### How Hexo Load Plugins

[hexo/lib/hexo/load\_plugins.ts at master · hexojs/hexo](https://github.com/hexojs/hexo/blob/master/lib/hexo/load_plugins.ts)

Load Modules: `package.json` 中 `hexo-` 开头和 `hexo-theme-` 开头的。

Load Scripts: `${theme_dir}/scripts` 和 `/scripts` 目录下所有的文件。这些文件都可以直接访问全局变量 `hexo`。

## Hexo API

### Tag (Plugin)

[Tag | Hexo](https://hexo.io/api/tag)

> A tag allows users to quickly and easily insert snippets into their posts.

#### Inline Tag vs. Block Tag

注册：

```js
// inline tag
hexo.extend.tag.register(
  'foo',
  args => { ... }
);

// block tag with `end`
hexo.extend.tag.register(
  'bar',
  (args, content) => { ... },
  { ends: true } // or simply `true`
);
```

在 `.md` 中使用：

```markdown
<!-- inline tag, no `end` -->
{% foo arg1 arg2 %}

<!-- block tag, need `end` -->
{% bar arg1 arg2 %}
markdown content
{% endbar %}
```

#### Async Tag

如果 Tag 的处理逻辑中有 async 函数调用，可以将其注册为 async Tag:

```js
hexo.extend.tag.register(
  'foo',
  args => { ... },
  { async: true }
);
```

#### 处理参数 `args`

比如 foo Tag 支持这样的语法（有必填参数，可选参数，可选的命名参数）：

```markdown
{% foo param1 [param2] [opt1:val1] [opt2:val2] %}
```

通过 `hexo.args.map()` 将传入的 `args` 转成参数信息对象：

```js
hexo => args => {
  args = hexo.args.map(args, ['opt1', 'opt2'], ['key1', 'key2']);
  let { key1, key2 = 'param2', opt1 = 'val1', opt2 = 'val2' } = args;
};
```

#### 访问 Hexo 实例

如果是 `scripts` 目录里的文件，就可以直接访问全局变量 `hexo`：

```js
hexo.extend.tag.register('foo', args => {
  // `hexo` is accessible
});
```

如果分开，则：

```js lib/foo.js
module.exports = hexo => args => {
  // `hexo` is accessible
};
```

```js index.js
hexo.extend.tag.register('foo', require("./lib/foo")(hexo));
```

#### 访问当前 Article (Post/Page) 信息

`this` 即为当前文件的信息，如：

```js
module.exports = hexo => function (args) {
  const {
    source, // file path (relative to `source/`)
    title, // article title
    _content, // original content
    content // HTML-rendered content
  } = this;
};
```

> [!caution]
> 这里 `function (args) { ... }` 不能写成 `args => { ... }`，因为 arrow functions ignore `this`.

### Filters

[Filter | Hexo](https://hexo.io/api/filter)

> A filter is used to modify some specified data. Hexo passes data to filters in sequence and the filters then modify the data one after the other. This concept was borrowed from [WordPress](http://codex.wordpress.org/Plugin_API#Filters).

Hexo 内置的 filter type，filter 被调用时，`this` 就是 Hexo 实例（不要用 arrow functions）。

#### Type `markdown-it:renderer`

Provided by `hexo-renderer-markdown-it`.

[hexojs/hexo-renderer-markdown-it: Markdown-it is a Markdown parser, done right. A faster and CommonMark compliant alternative for Hexo.](https://github.com/hexojs/hexo-renderer-markdown-it)

> This plugin overrides some default behaviors of how markdown-it plugin renders the markdown into html, to integrate with the Hexo ecosystem. It is possible to override this plugin too, without resorting to forking the whole thing.

自定义 filter 的调用逻辑为：

```js
this.hexo.execFilterSync('markdown-it:renderer', this.parser, { context: this });
```

其中 `this` 为 `class Renderer` 的实例，`this.hexo` 即为 Hexo 实例，`this.parser` 是 `class MarkdownIt` 的实例。

自定义 filter 的例子：

```js lib/foo.js
module.exports = function (parser) {
  const { hexo } = this;
  // parser === this.parser
};
```

### Events

[Events | Hexo](https://hexo.io/api/events)

> Hexo inherits from [EventEmitter](https://nodejs.org/dist/latest/docs/api/events.html). Use the `on` method to listen for events emitted by Hexo, and use the `emit` method to emit events. For more information, refer to the Node.js API documentation.

## Hexo Processing Flow

use `pnpm hexo generate --debug` to output debug level logs.

Add demo filters:

```js
const filterTypes = [
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

filterTypes.forEach(filterType => {
  hexo.extend.filter.register(filterType, function(data, options = {}) {
    let source = data?.source;
    if (!source) {
      if (filterType === 'post_permalink') {
        source = data;
      }
    }

    hexo.log.info(`[Demo] Filter for ${filterType} called: ${source}`);
    return data;
  }, 20);
});
```

Add demo event handlers:

```js
const events = [
  'deployBefore',
  'deployAfter',
  'exit',
  'generateBefore',
  'generateAfter',
  'new',
  'processBefore',
  'processAfter',
  'ready'
];

events.forEach(event => {
  hexo.on(event, function() {
    hexo.log.info(`[Demo] Event ${event} emitted`);
  });
});
```

Add demo tag plugin:

```js
const foobar = ctx => function (args) {
  const { source } = this;
  ctx.log.info(`[Demo] Foobar tag with args "${args}" called in source file: ${source}`);
  return '<div class="foobar-tag">Foobar tag called with args: ' + args.join(' ') + '</div>';
};

hexo.extend.tag.register('foobar', foobar(hexo));
```

### "hexo generate"

1. Database
    - `[D] "Writing database to .../db.json"`
2. Initialization
    - `[D] "Hexo version: 8.1.1"`
    - `[D] "Workding directory: ..."`
    - `[D] "Config loaded: .../_config.yml"`
    - `"Validating config"`
    - `[D] "Second Theme Config loaded: .../_config.stellar.yml"`
    - `[D] "Plugin loaded: ..."` (per `hexo-*` and `@*/hexo-*` dependency)
    - `[D] "Script loaded: ..."` (per `scripts/**/*.js`)
    - `[D] "Script loaded: ..."` (per `{theme}/scripts/**/*.js`)
    - `after_init` filter
    - `ready` event
3. Process Source Files (`hexo.source` and `hexo.theme`) (see [Box | Hexo](https://hexo.io/api/box))
    - `"Start processing"`
    - `[D] "Processed: ..."`
        - `post_permalink` filter (per `_posts` `.md` and asset file)
4. Content (Posts and Pages) Rendering
    - `generateBefore` event
    - `[D] "Rendering file: ...` (per `.css`, `.js`, and `.json` file)
    - `post_permalink` filter (per `_posts` `.md` file)
    - `before_post_render` filter (per `.md` file)
    - `[D] "Rendering post: ..."` (per `.md` file)
    - `markdown-it:renderer` filter (per `.md` file)
    - Tag plugins (`markdown-it:renderer` filter might be called if tag plugin calls renderer)
    - Together:
        - `after_post_render` filter (per `.md` file)
        - `"hexo-esbuild: processed ..."` (per `.css` file) 
5. Content Generation
    - `before_generate` filter
    - registered generators
        - `post_permalink` filter (per `_posts` `.md` file, when `"Generator: post"`)
    - `post_permalink` filter (per `_posts` asset file❔)
    - `template_locals` filter (called repeatedly)
    - `generateAfter` event
    - `after_generate` filter
6. ❔
    - `"Files loaded in d.dd s"`
7. HTML Rendering
    - `[D] "Rendering HTML xxx: ....html`
        - `markdown-it:renderer` filter (called repeatedly, for 正文之外的部分，如 side bar, footer)
8. HTML Generation
    - Together:
        - `Generated: ...` (outputting files)
        - `"hexo-esbuild: processed ..."` (per `.js`, `.styl` file) 
    - `"n files generated in d.dd s"`
9. Database
    - `[D] "Database saved"`
10. Exit
    - `before_exit` filter
    - `exit` event

### "hexo server"

The server starting:

1. Database
    - Same with `hexo generate`
2. Initialization
    - Same with `hexo generate`
3. `server_middleware` filter
4. Process Source Files (`hexo.source` and `hexo.theme`) (see [Box | Hexo](https://hexo.io/api/box))
    - Same with `hexo generate`
5. Content (Posts and Pages) Rendering
    - Same with `hexo generate`
6. From where:
    - `"正在获取图片长宽比。首次可能耗时较久，请耐心等待..."`
    - `"[image-ratios.json] 生成完成"`
7. Content Generation
    - Same with `hexo generate`
8. Server Started
    - `"Hexo is running at http://localhost:4000/ . Press Ctrl+C to stop."`
    - `[D] "Database saved"`
    - `before_exit` filter
    - `exit` event
9. Generation Again
    - `generateBefore` event
    - Same with about "Content Generation"

When browsing a page:

1. HTML Rendering
    - Same with `hexo generate`
2. HTML Accessing
    - `"GET /... 200 d.ddd ms - - "`
        - `"hexo-esbuild: processed ..."` (per `.js`, `.styl` file) 

When a post or page modified:

1. Process Source Files
    - `[D] "Processed: ..."` (for the modified file)
        - `post_permalink` filter (for the modified file, if in `_posts`)
2. Content (Posts and Pages) Rendering
    - Same with `hexo generate`, but only for the modified file
3. Content Generation
    - Same with `hexo generate`

Stopping the server:

1. Goodbye
    - `"Have a nice day"` or `"Bye!"` or similar message, twice
2. Exit
    - Same with `hexo generate`

### "hexo clean"

1. Initialization
    - Same with `hexo generate`
2. Clean
    - `"Deleted database."`
    - `"Deleted public folder."`
3. Exit
    - Same with `hexo generate`
