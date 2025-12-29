---
title: 插图适配明暗配色
date: 2024-05-21 14:48:24
updated: 2025-12-27 11:20:00
---
## 背景

有时候想要展示一些插图（尤其数理类的），这种图往往制作的时候会是白底（或透明底）黑字，在亮色主题下就还好，但在暗色主题下就很违和。可能会是在整体暗色页面中突兀出一块大面积白色的，可能会是因为透明而导致黑色文字在暗色背景下辨识度很低。

比如在暗色主题下出现下面这样一张图：

![A light image](/notes/rubik-cube/high-center-formula.png)

即便在亮色主题下，页面背景色往往不是纯白的，也会出现一块明显与背景色不一致的区域，不比暗色主题下好太多。

另外字体的变化也会对沉浸阅读有一定的影响。

## 理想

理想的方式是用 SVG 做为图片格式（本身制作插图的时候一般也是用矢量图），背景直接透明，前景色用 [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/color)，也就是当前主题下的文字颜色。图中彩色的部分，使用主题中定义的颜色变量。图中的文字（用 `text` 而非 `path` 的），直接沿用页面的字体设置。

但可能把 SVG 直接嵌入在 HTML 代码中的时候，这些是能够实现的，比如本站中很多 icon 都用 `currentColor` 来按需调整颜色。但如果用 `<img>` 标签引入时，页面的设置就无法传递给 SVG 了。

## 折中

一个折中的方式是用 CSS 的 [filter](https://developer.mozilla.org/en-US/docs/Web/CSS/filter) 来调整颜色。也就是很多人都提到的 `invert` 大法：

``` css
filter: invert(1) hue-rotate(180deg);
```

然而不理想之处就是虽然用 `hue-rotate` 把色相改回来，但很多时候效果并不太好。大部分彩色颜色都会变得有些奇怪，还有很多就几乎变成了黑色。看到有很多人在问怎么能在翻转（主要针对黑白色）的同时尽量保持其他彩色颜色，但还没看到有效的解决办法。

改变不了别人，就改变自己吧。在选择颜色的时候，尽量选那些反转之后不会太离谱的。以 [Tailwind CSS](https://tailwindcss.com/) 默认调色板为例，看一下不同颜色翻转前后的对比，尽量不要选那些太亮的彩色颜色。

{% folding Color Palette 翻转前后对比 %}
{% grid c:2 %}
<!-- cell -->
![原始色彩](colors.png) {.no-caption}
<!-- cell -->
![翻转的色彩](colors.png){.invert-when-dark .invert-when-light} {.no-caption}
{% endgrid %}
{% endfolding %}

比如选用 500 值的各个颜色，详见 [配色 - Tailwind Color Palette](../../notes/color-pattern/index.md#Tailwind-Color-Palette)

## 当前的方案

目前通过一些操作来提高这种类型插图的展示体验。

首选 SVG 或者 透明背景的 PNG。

图片中的字体跟站点字体一致。因为站点本身提供了自己要用的字体，基本上不会因为字体缺失而产生较大的偏差。

图中的当黑色用的颜色，使用 `#333333`，即本站在亮色主题时的文字颜色。背景色直接用透明。如果需要白色，用 `#f9fafb`（本站亮色主题的背景色）或 `#e3e1de`（本站暗色主题背景色的补色）。

如果需要用彩色，尽量用 Tailwind CSS 默认调色板中居中的那些颜色（尤其避免低于 200）。不要随便选择调色板之外的颜色，翻车概率高。

如果用 SVG，注意图中设置的 `width` 和 `height` 值，可以调整成需要的值，或者直接删掉，在 `image` 标签中指定。

最后在图片的明暗风格跟页面的明暗主题不一致时，对图片应用 filter 进行颜色翻转。

参见 [图片适配明暗配色](../../notes/hexo/index.md#图片适配明暗配色)。

本文开头提到的图片，按照这个逻辑处理完，看到的效果是：

![适配后的效果](/notes/rubik-cube/high-center-formula.ink.svg){.invert-when-dark}
