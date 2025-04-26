---
title: 字体 font-family 选择
notebook: notes
tags:
  - calf
  - it/font
date: 2024-04-17 22:25:24
updated: 2025-04-26 12:04:00
---
## 网页文本字体的选择

一般在显示器上，使用无衬线体（sans-serif）会比较舒服，衬线体（serif）看着会比较累，或者说比较正式，也更适合印刷制品。

网页中选定字体，如果不同时提供字体文件，就还得考虑浏览器端系统是否有相应的字体。尤其对于中文，不同的操作系统会有不同的默认字体，甚至同一字体在不同操作系统中的渲染效果也会有所差异。

比较优雅的处理方式是把英文字体排在前边，可以让英文和数字更好看一些，避免选择的中文字体中英文部分不是特别漂亮。然后列出中文字体，最好兼顾到不同的操作系统。最后可以列上字体族（如无衬线体）作为兜底。

目前倾向的排列为：

> 注：参考 [如何优雅的选择字体(font-family) - 前端学习 - SegmentFault 思否](https://segmentfault.com/a/1190000006110417)。

1. 英文字体在前
   1. "Helvetica Neue"
   2. Helvetica
   3. Tahoma
   4. Arial
2. 中文
   1. 微软雅黑 "Microsoft YaHei" - Windows
   2. 苹方 "PingFang SC" - Mac
   3. 冬青黑体 "Hiragino Sans GB" - Mac
   4. 黑体-简 "Heiti SC" - Mac
   5. 文泉驿微米黑 "WenQuanYi Micro Hei" - Linux
3. 向下兼容
   1. 华文西黑 - Mac
   2. 黑体 - Windows
4. 字体族
   1. 无衬线体 sans-serif

本站把 ["LXGW WenKai" / 霞鹜(Wù)文楷](https://github.com/lxgw/LxgwWenKai) 排在最前边，甚至 inline code 也使用该字体。

## 网页中等宽字体的选择

展示代码片段的时候，用等宽字体看起来更符合习惯。一般代码中中文不多，可以不考虑中文部分。

目前倾向的排列为：

1. Monaco
2. Menlo
3. Consolas
4. "Courier New"
5. monospace

本站把 ["Source Code Pro"](https://github.com/adobe-fonts/source-code-pro) 排在最前边；把 ["LXGW WenKai Mono" / 霞鹜文楷](https://github.com/lxgw/LxgwWenKai) 排在最后边用于渲染中文。

## Visual Studio Code 里中英文对不齐的问题

一般如果假设中文字符宽度是 1 的话，大部分等宽英文字体的宽度并不是 0.5，而是大多介于 0.55 到 0.65 之间，以 0.6 居多。

很多编辑器可以做到中英文对齐（即一个中文字符的宽度刚好等于两个英文字符的宽度），是在将字体渲染到屏幕前做了一些微调，如将英文字符压缩到 0.5 宽度，或者给中文字符左右各加 0.1 的空白。

VS Code 无法实现这点，因为它是基于 Electron 也就是浏览器的 HTML DOM 做的字符渲染，很难做到这种调整。（VS Code 自带的 terminal 里中英文是能对齐的，那就是个 canvas，完全是画出来的。）

所以需要在 VS Code 中使用宽度刚好是 0.5 的英文等宽字体，但可能会看起来觉得英文字符很瘦，需要适应。

> 其他基于 HTML DOM 渲染字符的软件，包括浏览器，也都有同样的问题。

试试看是否能对齐：

``` text
liLI10Oo
你好中文
```

## 编程用的等宽字体的选择

VS Code `editor.fontFamily` setting: `'Ubuntu Mono', 'Source Code Pro', Consolas, 'Courier New', monospace, 'LXGW WenKai Mono'`.

### Ubuntu Mono

[Ubuntu Mono - Google Fonts](https://fonts.google.com/specimen/Ubuntu+Mono)

[fonts/UbuntuMono at master · powerline/fonts](https://github.com/powerline/fonts/tree/master/UbuntuMono)

- {% mark ✓ color:green %} 中英文比例严格，能对齐。
- {% mark ✓ color:green %} 英文长宽比很协调，不会显得很瘦。
- {% mark ✓ color:green %} 字符 `liLI10O` 区分明显，适合编程。

VS Code 最适宜的字体。

### LXGW WenKai Mono

[LXGW WenKai / 霞鹜(Wù)文楷](https://github.com/lxgw/LxgwWenKai)

霞鹜文楷中的等宽字体，中英文可以对齐的，但是可能看习惯了 Ubuntu Mono，觉得 LXGW WenKai Mono 的英文字符过细。

VS Code 中文部分最适宜的字体。

### Source Code Pro

[GitHub - adobe-fonts/source-code-pro: Monospaced font family for user interface and coding environments](https://github.com/adobe-fonts/source-code-pro)

Font Family: `Source Code Pro` or `Source Code Variable`

- {% mark ✗ color:red %} 不支持中文，中文字符的宽度不等于两个英文字符

非 HTML DOM 渲染的软件（如 iTerm2 等）最适宜的字体。

### Inconsolata

[Inconsolata - Google Fonts](https://fonts.google.com/specimen/Inconsolata)

这个是宽度为 0.5 的等宽字体，同时比较漂亮，不会显得英文字符特别瘦。

### Source Han Mono

[GitHub - adobe-fonts/source-han-mono: Source Han Mono | 思源等宽 | 思源等寬 | 思源等寬 香港 | 源ノ等幅 | 본모노](https://github.com/adobe-fonts/source-han-mono)

- {% mark ✗ color:red %} 中文字符的宽度不等于两个英文字符

### Noto Sans Mono

我们进入谷歌字体的官方 GitHub 仓库 <https://github.com/googlefonts/noto-cjk> ，点击右边的 Releases，找到带「Monospace」和「简体中文」字样的链接（13_NotoSansMonoCJKsc），下载，解压，里面有常规和加粗两个版本，分别对它们点击右键，再点击安装，即可安装完成。

重启编辑器，就可以从字体设置中选择，或者在 VS Code 的字体设置中手动输入 `'Noto Sans Mono CJK SC', monospace` 来使用了。

### M+

中文字符宽度等于两个英文字符的字体

[M+ FONTS | ENGLISH](http://mplus-fonts.osdn.jp/about-en.html)

[M+ 1m Font Free by M+ Fonts » Font Squirrel](https://www.fontsquirrel.com/fonts/m-1m)

Font Family: `M+ 1m`

- {% mark ✗ color:red %} 英文字符太瘦了

## 本站字体选择

在 `_config.stellar.yml` 中配置字体。

``` yaml
inject:
  head:
    - <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@callmebill/lxgw-wenkai-web@latest/style.css">
    - <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/source-code-pro@2.38.0/source-code-pro.min.css">

style:
  font-family:
    logo: '"LXGW WenKai", "Helvetica Neue", Helvetica, "Lucida Grande", Lucida, Tahoma, Arial, "Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", STXiHei, SimHei, sans-serif'
    body: '"LXGW WenKai", "Helvetica Neue", Helvetica, "Lucida Grande", Lucida, Tahoma, Arial, "Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", STXiHei, SimHei, sans-serif'
    code: '"LXGW WenKai", "Source Code Pro", Monaco, Menlo, Consolas, "Courier New", monospace'
    codeblock: '"Source Code Pro", Monaco, Menlo, Consolas, "Courier New", monospace, "LXGW WenKai Mono"'
```
