---
title: Understanding Hexo
notebook: notes
tags:
  - it/web
date: 2026-01-01 01:19:45
updated: 2026-01-02 00:34:29
---
## Hexo

[Hexo - A fast, simple & powerful blog framework](https://hexo.io/)

[hexojs/hexo: A fast, simple & powerful blog framework, powered by Node.js.](https://github.com/hexojs/hexo)

## Hexo API

### Tag (Plugin)

[Tag | Hexo](https://hexo.io/api/tag)

> A tag allows users to quickly and easily insert snippets into their posts.

#### 访问 Hexo 实例

如果定义和注册放在一起，可以：

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

### Filters

[Filter | Hexo](https://hexo.io/api/filter)

> A filter is used to modify some specified data. Hexo passes data to filters in sequence and the filters then modify the data one after the other. This concept was borrowed from [WordPress](http://codex.wordpress.org/Plugin_API#Filters).

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

1. Initialization
    - `"Validating config"`
    - `after_init` filter
    - `ready` event
2. `"Start processing"`
3. Content (Posts and Pages) Rendering
    - `post_permalink` filter (per `_posts` `.md` and asset file❔)
    - `generateBefore` event
    - `post_permalink` filter (per `_posts` `.md` file)
    - `before_post_render` filter (per `.md` file)
    - `markdown-it:renderer` filter (per `.md` file)
    - Tag plugins (`markdown-it:renderer` filter might be called if tag plugin calls renderer)
    - `after_post_render` filter (per `.md` file)
4. ❔
    - `"hexo-esbuild: processed ..."` (per `.css` file) 
    - `after_post_render` filter (per `.md` file)
5. Generation
    - `before_generate` filter
    - `post_permalink` filter (per `_posts` `.md` file)
    - registered generators
    - `post_permalink` filter (per `_posts` asset file❔)
    - `template_locals` filter (called repeatedly)
    - `generateAfter` event
    - `after_generate` filter
6. ❔
    - `"Files loaded in nn.nn s"`
7. HTML Rendering
    - `markdown-it:renderer` filter (called repeatedly, for 正文之外的部分，如 side bar, footer)
8. HTML Generation
    - Together:
        - `Generated: ...` (outputting files)
        - `"hexo-esbuild: processed ..."` (per `.js`, `.styl` file) 
    - `"n files generated in nn.nn s"`
9. Exit
    - `before_exit` filter
    - `exit` event

### "hexo server"

The server starting:

1. Initialization
    - Same with `hexo generate`
2. `server_middleware` filter
3. `"Start processing"`
4. Content (Posts and Pages) Rendering
    - Same with `hexo generate`
5. ❔
    - Same with `hexo generate`
6. From where:
    - `"正在获取图片长宽比。首次可能耗时较久，请耐心等待..."`
    - `"[image-ratios.json] 生成完成"`
7. Generation
    - Same with `hexo generate`
8. Server Started
    - `"Hexo is running at http://localhost:4000/ . Press Ctrl+C to stop."`
    - `before_exit` filter
    - `exit` event
9. `generateBefore` event
10. Generation Again
    - Same with above

When browsing a page:

1. HTML Rendering
    - `markdown-it:renderer` filter (called repeatedly, for 正文之外的部分如 side bar, footer)
2. Assets Generation
    - `"hexo-esbuild: processed ..."` (per `.js`, `.styl` file) 


When a post or page modified:

1. Content (Posts and Pages) Rendering
    - `post_permalink` filter (for the modified file, if in `_posts`)
    - `generateBefore` event
    - `post_permalink` filter (for the modified file, if in `_posts`)
    - `before_post_render` filter (for the modified file)
    - `markdown-it:renderer` filter (for the modified file)
    - Tag plugins (`markdown-it:renderer` filter might be called if tag plugin calls renderer)
    - `after_post_render` filter (for the modified file)
2. Generation
    - `before_generate` filter
    - `post_permalink` filter (per `_posts` `.md` file)
    - registered generators
    - `post_permalink` filter (per `_posts` asset file❔)
    - `template_locals` filter (called repeatedly)
    - `generateAfter` event
    - `after_generate` filter

Stopping the server:

1. Exit
    - `"Have a nice day"` or `"Bye!"` or similar message, twice
    - `before_exit` filter
    - `exit` event

### "hexo clean"

```log
> hexo clean

INFO  Validating config
INFO  [Demo] Filter for after_init called
INFO  [Demo] Event ready emitted
INFO  [Demo] Filter for after_clean called
INFO  Deleted database.
INFO  Deleted public folder.
INFO  [Demo] Filter for before_exit called
INFO  [Demo] Event exit emitted
```
