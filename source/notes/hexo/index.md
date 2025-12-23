---
title: Hexo 相关问题
notebook: notes
tags:
  - it/web
date: 2024-04-21 14:42:16
updated: 2025-07-02 23:04:33
---
## Hexo

[Hexo - A fast, simple & powerful blog framework](https://hexo.io/)

{% badge_github hexojs hexo release:true %}

> Hexo is a fast, simple and powerful blog framework. You write posts in Markdown (or other markup languages) and Hexo generates static files with a beautiful theme in seconds.

## Themes

### Stellar

[Stellar：开始您全新的博客之旅 - XAOXUU](https://xaoxuu.com/wiki/stellar/)

{% badge_github xaoxuu hexo-theme-stellar release:true %}

> Stellar 是一个内置文档系统的简约商务风 Hexo 主题，支持丰富的标签和动态数据组件，帮助您简单从容地应对各种表达需求，十分推荐内容创作者使用 Stellar 开始您全新的博客之旅。

## Issues / Notices

### 关于 Notes

Hexo 还是以（博客）文章（posts）为核心的，虽然 Stellar 独创了文档（wiki）系统，也可以基于其实现笔记（notes）的功能，但还是有很多地方对非文章（posts）不是那么友好。

- （博客）文章（posts）：一般是持续增加新页面，以时间排序。虽然也可以再更新，但一般后续更新只是小修小补。这个天生带着很强的创建时间属性。
- 专栏（posts + topic）：本质还是文章（强调时间顺序性），但增强了同专栏下文章的前后关联关系。
- 文档（wiki）：更像是项目级别的 wiki，强调目录树（手动指定顺序、分组）。
- 笔记（notes）：虽然目前是基于 wiki 实现，但还是有极大区别的，应该更像以前的 MediaWiki，或者常见的桌面或在线笔记软件那样。文章之间的引用关系会更丰富，不像文章那样强调创建时间，而且内容一般是持续不断更新的。

### License in Wiki

[Stellar：如何使用文档系统 # 显示许可协议 - XAOXUU](https://xaoxuu.com/wiki/stellar/wiki-settings/#%E6%98%BE%E7%A4%BA%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE) 中提到可以给 wiki 开启 license 显示，或者指定协议内容。但实际没有显示出来。

- 2024-05-08: 提了 [PR](https://github.com/xaoxuu/hexo-theme-stellar/pull/460) 进行修复。
- 2024-06-17: Stellar 1.29.0 版本中修复了。

### 引用图片等 assets

[Asset Folders | Hexo](https://hexo.io/zh-cn/docs/asset-folders) 中提到可以开启 `post_asset_folder` 以便让每篇文章的资源文件存放在其旁边的同名目录中，但这个对非文章（posts）类型的页面不起作用，包括 Stellar 中的 wiki。

理想状态：不管是文章（posts）还是普通页面（pages），都可以优雅地引用与其相伴的资源文件，对于图片资源，最好还能直接在 Visual Studio Code 的 Markdown 预览中也能显示出来。

调整 hexo 配置 `_config.yml`:

引用图片可以有几种语法：

- Markdown 语法 `![alt](assets/src)`
- Hexo 提供的 `asset_img` 标签插件 `{% asset_img slug [title] %}`
- Stellar 主题提供的 [`image` 标签插件](https://xaoxuu.com/wiki/stellar/tag-plugins/express/#image-%E5%9B%BE%E7%89%87%E6%A0%87%E7%AD%BE) `{% image src [description] %}`

``` yaml
post_asset_folder: true # https://hexo.io/docs/asset-folders#Post-Asset-Folder
marked: # https://github.com/hexojs/hexo-renderer-marked
  prependRoot: true
  postAsset: true
```

Visual Studio Code 中安装扩展 [Hexo Utils - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=fantasy.vscode-hexo-utils)。

> 不确定是因为 7.2 的一些改动，还是因为换了 renderer，下面两个表的效果发生了变化。
> 目前是 2024-07-11 基于 Hexo 7.3 验证的结果。

文章和笔记（或其他页面）的差异，应该是因为路由路径不同：

- 文章 post-slug.md ⇒ `/path/to/post-slug/index.html`
- 笔记 note-slug.md ⇒ `/path/to/note-slug.html`

#### 文章（Post）中引用图片

Syntax | Slug / Src | Hexo | VS Code
--|--|--|--
Markdown | `filename` | {% mark ✓ color:green %} | {% mark ✗ color:red %}
Markdown | `post-slug/filename` | {% mark ✗ color:red %} | {% mark ✓ color:green %}
`asset_img` | `filename` | {% mark ✗ color:red %} | {% mark ✓ color:green %}
`asset_img` | `post-slug/filename` | {% mark ✗ color:red %} | {% mark ✓ color:green %}
`image` | `filename` | {% mark ✓ color:green %} | {% mark ✗ color:red %}
`image` | `post-slug/filename` | {% mark ✗ color:red %} | {% mark ✗ color:red %}

#### 笔记（Note）中引用图片

> TODO: 关于 assets 目录的变化。

Syntax | Slug / Src | Hexo | VS Code | Demo
--|--|--|--|--
Markdown | `note-slug/filename` | {% mark ✓ color:green %} | {% mark ✓ color:green %} | ![demo](assets/hexo/demo.png)
Markdown | `notes/note-slug/filename` | {% mark ✗ color:red %} | {% mark ✗ color:red %} | ![demo](assets/notes/hexo/demo.png)
Markdown | `../notes/note-slug/filename` | {% mark ✓ color:green %} ~~`/../` 没影响~~ | {% mark ✓ color:green %} | ![demo](../notes/assets/hexo/demo.png)
`asset_img` | `filename` | {% mark ✗ color:red %} 连 `<img>` 都没有 | {% mark ✓ color:green %} | {% asset_img assets/demo.png %}
`asset_img` | `note-slug/filename` | {% mark ✗ color:red %} 连 `<img>` 都没有 | {% mark ✓ color:green %} | {% asset_img assets/hexo/demo.png %}
`asset_img` | `notes/note-slug/filename` | {% mark ✗ color:red %} 连 `<img>` 都没有 | {% mark ✗ color:red %} | {% asset_img notes/assets/hexo/demo.png %}
`asset_img` | `../notes/note-slug/filename` | {% mark ✗ color:red %} 连 `<img>` 都没有 | {% mark ✓ color:green %} | {% asset_img ../notes/assets/hexo/demo.png %}
`image` | `note-slug/filename` | {% mark ✓ color:green %} | {% mark ✗ color:red %} | {% image assets/hexo/demo.png %}
`image` | `../notes/note-slug/filename` | {% mark ✓ color:green %} | {% mark ✗ color:red %} | {% image ../notes/assets/hexo/demo.png %}

> 其他页面可能类似，待确认。

### Mermaid

当 Mermaid 图比较宽的时候，在手机上展示不全，且无法缩放、滑动。比如 [这里](../pgp/index.md#架构)。

- 2024-06-17: Stellar 1.29.0 版本中修复了。

### 明暗主题色

目前可以通过配置文件指定 `prefers_theme` 是自动、亮色、还是暗色。还需要能够通过页面上的按钮手动切换的功能。

- 2024-04-28: 提了 [PR](https://github.com/xaoxuu/hexo-theme-stellar/pull/449) 以支持运行时切换明暗。
- 2024-06-17: Stellar 1.29.0 版本中修复了。

### Minify

JS、CSS 文件可以用 [uiolee/hexo-esbuild: Minify JavaScripts, CSS files via esbuild](https://github.com/uiolee/hexo-esbuild)。

HTML 文件可以用 [uiolee/hexo-htmlnano: Minify HTML files with htmlnano](https://github.com/uiolee/hexo-htmlnano)。

还有一个同时支持 HTML、CSS、JS、Font、Image，[Lete114/hexo-minify: Hexo-minify is a Hexo compression plug-in that compresses HTML, CSS, JS, Font and Image(jpg,png,gif,webp,svg)](https://github.com/Lete114/hexo-minify)。但是太庞大了，一下子多引入小五百个 npm 包，累觉不爱。

### diagrams.net / draw.io

在文章内插入 diagrams.net / draw.io 图。

[Diagrams.net | Kutt Katrea's plugins for Hexo](https://kuttkatrea.github.io/hexo-plugins/diagrams-net/)

``` bash
pnpm add hexo-diagrams-net
```

``` markdown
{% diagramsnet assets/hexo/flowchart.drawio %}
```

{% invert %}
{% diagramsnet assets/hexo/flowchart.drawio %}
{% endinvert %}

- 如何适配明暗主题？
  - 参考 <https://github.com/jgraph/drawio-integration/blob/master/inline.js>
    - 效果 <http://jgraph.github.io/drawio-integration/inline.html>
  - 用自定义的 [`invert` 标签](/blog/2024/05/21/illustration-fit-color-scheme/#当前的方案)

## Stellar 主题增加 Notebook（笔记本）支持

### 概念和预期效果

- Notebooks: 指笔记本的列表。默认可以支持任意多个笔记本。
- Notebook: 笔记本。
- Note: （一篇）笔记，对应于 Hexo 中的一个 page，具体来说是一个在 front-matter 中指定了归属的 notebook 的 page。一篇笔记只能归属于一个笔记本。
- Tag: 笔记标签。在一个笔记本内，所有的笔记可以通过 tag 来组织。一篇笔记可以对应任意多个 tag（也可以没有）。tag 支持层级结果，通过 `/` 分割，如 `it/web` 表示在 `it` 标签下有个 `web` 子标签。

整体类似于 [Bear](https://bear.app/) 中的结构。Bear 中的数据相当于一个笔记本，笔记、tag 都是对应的。因为本身就是以网站形式呈现，暂时也就不支持归档、回收站等功能。

会有以下一些路由：

- /notebooks: 笔记本列表页。具体的地址可以通过配置修改。leftbar 中可以放所有笔记本中最近更新的内容。主体部分是笔记本列表，类似 wiki 列表。
- /notebooks/xxx: ID 为 xxx 的笔记本的页面。具体地址可以通过该笔记本的配置文件修改。leftbar 可以放该笔记本的标签树、最近更新的内容（需要么？）。主体部分是笔记列表，类似博客列表页。无限加载最好，但可能不适合于静态站点，那就分页或者想博客的归档页那样列出所有。
- /notebooks/xxx/tags/ttt: xxx 笔记本的 ttt 标签页面。跟笔记本页面类似，但标签树会高亮当前标签，最近更新（需要么？）和笔记列表都限定在该标签内。
  - 父标签包含所有子标签里的笔记。比如一篇笔记的标签是 `t1/t2/t3`，那么在 `t1` 和 `t1/t2` 中都可以看到该笔记。
- /notebooks/xxx/yyy: xxx 笔记本的 yyy 笔记页面。主体部分是该笔记本身。

笔记本页或笔记本标签页，笔记的排序，至少支持按更新时间倒序排列。可以考虑允许配置按照更新时间、创建时间、标题的正序或倒序排列。可以支持笔记置顶，置顶的笔记始终排在最前面。

### 代码结构和处理流程

`scripts/generators` 目录中增加 `notebooks.js` 以定义 notebooks 相关的路由，如 `/notebooks`、`/notebooks/xxx`、`/notebooks/xxx/tags/ttt` 等。

需要在这之前，对 notebooks 相关信息做预处理，在 `scripts/events/lib` 中增加 `notebooks.js`，并在 `scripts/events/index.js` 中引用（添加到 `generateBefore` 事件上）。这个文件要遍历 pages，把 notebooks 信息整理出来，并计算出每个 notebooks 中标签树的信息（标签本身、标签的层级关系、标签和页面的关联关系等）。

页面主体部分的渲染，在 `layout` 目录中增加 `notebooks.ejs` 渲染笔记本列表页，增加 `notes.ejs` 渲染笔记列表页（笔记本页和选中的标签页）。

笔记的渲染跟普通 page 类似，在内容底部增加该笔记的 tags 列表（增加 `layout/_partial/main/notebook/note_tags.ejs` 文件）。点击某个标签可以跳转到对应的标签页（归属于该标签的笔记列表页）。

侧边栏最近更新能支持限定在所有笔记本（在笔记本列表页）或当前笔记本 ~~或当前标签（待定）~~。

搜索框能支持限定在 ~~所有笔记本、~~ 当前笔记本 ~~、或当前标签~~。

标签树组件，在 `layout/_partial/widgets` 中增加 `tagtree.ejs` 用来渲染标签树，还需要修改 `layout/_partial/sidebar` 中相应文件来应用在配置文件中定义的不同 layout 下的 sidebar 配置。

- 2024-05-13: 提了 [PR](https://github.com/xaoxuu/hexo-theme-stellar/pull/464)，基本完成初版笔记系统。
- 2024-06-17: Stellar 1.29.0 版本中包含笔记系统。
