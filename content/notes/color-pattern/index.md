---
title: 配色
tags:
- it/ui
date: "2024-12-15T10:08:14+08:00"
lastmod: "2026-10-24T19:03:48+08:00"
params:
  pinned: true
  ai_label: polished
---
## Tailwind Color Palette

[Customizing Colors - Tailwind CSS](https://tailwindcss.com/docs/customizing-colors)

各个颜色的居中（500）色值：

| Color Name | 颜色名 | RGB (hex)                                    |
|------------|--------|----------------------------------------------|
| Slate      | 石板灰 | $\textcolor{64748b}{\blacksquare}$ `#64748b` |
| Gray       | 灰色   | $\textcolor{6b7280}{\blacksquare}$ `#6b7280` |
| Zinc       | 锌色   | $\textcolor{71717a}{\blacksquare}$ `#71717a` |
| Neutral    | 中性色 | $\textcolor{737373}{\blacksquare}$ `#737373` |
| Stone      | 石色   | $\textcolor{a8a29e}{\blacksquare}$ `#a8a29e` |
| Red        | 红色   | $\textcolor{ef4444}{\blacksquare}$ `#ef4444` |
| Orange     | 橙色   | $\textcolor{f97316}{\blacksquare}$ `#f97316` |
| Amber      | 琥珀色 | $\textcolor{f59e0b}{\blacksquare}$ `#f59e0b` |
| Yellow     | 黄色   | $\textcolor{eab308}{\blacksquare}$ `#eab308` |
| Lime       | 酸橙色 | $\textcolor{84cc16}{\blacksquare}$ `#84cc16` |
| Green      | 绿色   | $\textcolor{22c55e}{\blacksquare}$ `#22c55e` |
| Emerald    | 翡翠色 | $\textcolor{10b981}{\blacksquare}$ `#10b981` |
| Teal       | 青绿色 | $\textcolor{14b8a6}{\blacksquare}$ `#14b8a6` |
| Cyan       | 青色   | $\textcolor{06b6d4}{\blacksquare}$ `#06b6d4` |
| Sky        | 天蓝色 | $\textcolor{0ea5e9}{\blacksquare}$ `#0ea5e9` |
| Blue       | 蓝色   | $\textcolor{3b82f6}{\blacksquare}$ `#3b82f6` |
| Indigo     | 靛蓝色 | $\textcolor{6366f1}{\blacksquare}$ `#6366f1` |
| Violet     | 紫罗兰 | $\textcolor{8b5cf6}{\blacksquare}$ `#8b5cf6` |
| Purple     | 紫色   | $\textcolor{a855f7}{\blacksquare}$ `#a855f7` |
| Fuchsia    | 紫红色 | $\textcolor{d946ef}{\blacksquare}$ `#d946ef` |
| Pink       | 粉色   | $\textcolor{ec4899}{\blacksquare}$ `#ec4899` |
| Rose       | 玫瑰色 | $\textcolor{f43f5e}{\blacksquare}$ `#f43f5e` |

## Sidera

Source: [Sidera](https://github.com/calfzhou/hugo-theme-sidera), `assets/css/sidera.css`.

Eight chromatic families—red, orange, yellow, green, cyan, blue, purple and pink—plus a separately tuned neutral family.

### Design coordinates

OKLCH separates perceptual lightness **L**, chroma **C** and hue **H**. Lightness is
written on a 0–1 scale here; hue is in degrees.

| Family  | Hue                 |
| ------- | ------------------- |
| Red     | 25                  |
| Orange  | 55                  |
| Yellow  | 95                  |
| Green   | 145                 |
| Cyan    | 205                 |
| Blue    | 255                 |
| Purple  | 300                 |
| Pink    | 345                 |
| Neutral | Independently tuned |

| Role      | Light L / C  | Dark L / C    |
| --------- | ------------ | ------------- |
| Text      | 0.44 / 0.12  | 0.82 / 0.12   |
| Accent    | 0.58 / 0.143 | 0.67 / 0.143  |
| Surface   | 0.96 / 0.018 | 0.26 / 0.028  |
| Highlight | 0.90 / 0.078 | 0.34 / 0.0585 |

Border: 30% accent + 70% surface, mixed in sRGB

### Light palette

#### Quiet boxes

| Family  | Demo                                                               | Text      | Border    | Surface   |
| ------- | ------------------------------------------------------------------ | --------- | --------- | --------- |
| Red     | $$\fcolorbox{ebbebd}{feedec}{\textcolor{89312e}{$\blacksquare$}}$$ | `#89312e` | `#ebbebd` | `#feedec` |
| Orange  | $$\fcolorbox{e8c3a2}{fcefe7}{\textcolor{7e3f00}{$\blacksquare$}}$$ | `#7e3f00` | `#e8c3a2` | `#fcefe7` |
| Yellow  | $$\fcolorbox{d7cea0}{f5f2e5}{\textcolor{625100}{$\blacksquare$}}$$ | `#625100` | `#d7cea0` | `#f5f2e5` |
| Green   | $$\fcolorbox{b5d6b8}{ebf5eb}{\textcolor{1a6323}{$\blacksquare$}}$$ | `#1a6323` | `#b5d6b8` | `#ebf5eb` |
| Cyan    | $$\fcolorbox{a0d6db}{e5f6f8}{\textcolor{005e66}{$\blacksquare$}}$$ | `#005e66` | `#a0d6db` | `#e5f6f8` |
| Blue    | $$\fcolorbox{b5cfef}{eaf3fe}{\textcolor{1b5292}{$\blacksquare$}}$$ | `#1b5292` | `#b5cfef` | `#eaf3fe` |
| Purple  | $$\fcolorbox{d3c5eb}{f3effc}{\textcolor{5d408a}{$\blacksquare$}}$$ | `#5d408a` | `#d3c5eb` | `#f3effc` |
| Pink    | $$\fcolorbox{e6bfd5}{fbedf4}{\textcolor{7e3261}{$\blacksquare$}}$$ | `#7e3261` | `#e6bfd5` | `#fbedf4` |
| Neutral | $$\fcolorbox{cbcfd4}{f1f3f5}{\textcolor{4b535c}{$\blacksquare$}}$$ | `#4b535c` | `#cbcfd4` | `#f1f3f5` |

#### Highlight boxes

| Family  | Demo                                                               | Text      | Accent    | Highlight |
| ------- | ------------------------------------------------------------------ | --------- | --------- | --------- |
| Red     | $$\fcolorbox{c0524e}{ffd1cd}{\textcolor{89312e}{$\blacksquare$}}$$ | `#89312e` | `#c0524e` | `#ffd1cd` |
| Orange  | $$\fcolorbox{b95e01}{ffd4b8}{\textcolor{7e3f00}{$\blacksquare$}}$$ | `#7e3f00` | `#b95e01` | `#ffd4b8` |
| Yellow  | $$\fcolorbox{917900}{eedea4}{\textcolor{625100}{$\blacksquare$}}$$ | `#625100` | `#917900` | `#eedea4` |
| Green   | $$\fcolorbox{388f40}{beecbf}{\textcolor{1a6323}{$\blacksquare$}}$$ | `#1a6323` | `#388f40` | `#beecbf` |
| Cyan    | $$\fcolorbox{008b96}{9fedf7}{\textcolor{005e66}{$\blacksquare$}}$$ | `#005e66` | `#008b96` | `#9fedf7` |
| Blue    | $$\fcolorbox{387bcc}{c9e0ff}{\textcolor{1b5292}{$\blacksquare$}}$$ | `#1b5292` | `#387bcc` | `#c9e0ff` |
| Purple  | $$\fcolorbox{8963c2}{e3d6ff}{\textcolor{5d408a}{$\blacksquare$}}$$ | `#5d408a` | `#8963c2` | `#e3d6ff` |
| Pink    | $$\fcolorbox{b4538d}{ffcde8}{\textcolor{7e3261}{$\blacksquare$}}$$ | `#7e3261` | `#b4538d` | `#ffcde8` |
| Neutral | $$\fcolorbox{727c87}{dfe4ea}{\textcolor{4b535c}{$\blacksquare$}}$$ | `#4b535c` | `#727c87` | `#dfe4ea` |

### Dark palette

#### Quiet boxes

| Family  | Demo                                                               | Text      | Border    | Surface   |
| ------- | ------------------------------------------------------------------ | --------- | --------- | --------- |
| Red     | $$\fcolorbox{643734}{301f1d}{\textcolor{ffaba3}{$\blacksquare$}}$$ | `#ffaba3` | `#643734` | `#301f1d` |
| Orange  | $$\fcolorbox{613b1f}{2f2017}{\textcolor{ffaf78}{$\blacksquare$}}$$ | `#ffaf78` | `#613b1f` | `#2f2017` |
| Yellow  | $$\fcolorbox{51450e}{282414}{\textcolor{dcc463}{$\blacksquare$}}$$ | `#dcc463` | `#51450e` | `#282414` |
| Green   | $$\fcolorbox{2d502f}{1b281c}{\textcolor{91d993}{$\blacksquare$}}$$ | `#91d993` | `#2d502f` | `#1b281c` |
| Cyan    | $$\fcolorbox{0d4f54}{12282a}{\textcolor{4ddae9}{$\blacksquare$}}$$ | `#4ddae9` | `#0d4f54` | `#12282a` |
| Blue    | $$\fcolorbox{2c476a}{1b2532}{\textcolor{9cc7ff}{$\blacksquare$}}$$ | `#9cc7ff` | `#2c476a` | `#1b2532` |
| Purple  | $$\fcolorbox{4c3d65}{262130}{\textcolor{cfb5ff}{$\blacksquare$}}$$ | `#cfb5ff` | `#4c3d65` | `#262130` |
| Pink    | $$\fcolorbox{5f374e}{2e1f27}{\textcolor{fba4d6}{$\blacksquare$}}$$ | `#fba4d6` | `#5f374e` | `#2e1f27` |
| Neutral | $$\fcolorbox{485057}{252b31}{\textcolor{ccd1d7}{$\blacksquare$}}$$ | `#ccd1d7` | `#485057` | `#252b31` |

#### Highlight boxes

| Family  | Demo                                                               | Text      | Accent    | Highlight |
| ------- | ------------------------------------------------------------------ | --------- | --------- | --------- |
| Red     | $$\fcolorbox{df6e68}{522c28}{\textcolor{ffaba3}{$\blacksquare$}}$$ | `#ffaba3` | `#df6e68` | `#522c28` |
| Orange  | $$\fcolorbox{d77a31}{4f3018}{\textcolor{ffaf78}{$\blacksquare$}}$$ | `#ffaf78` | `#d77a31` | `#4f3018` |
| Yellow  | $$\fcolorbox{b09300}{41380e}{\textcolor{dcc463}{$\blacksquare$}}$$ | `#dcc463` | `#b09300` | `#41380e` |
| Green   | $$\fcolorbox{56ac5b}{244024}{\textcolor{91d993}{$\blacksquare$}}$$ | `#91d993` | `#56ac5b` | `#244024` |
| Cyan    | $$\fcolorbox{00a9b6}{004146}{\textcolor{4ddae9}{$\blacksquare$}}$$ | `#4ddae9` | `#00a9b6` | `#004146` |
| Blue    | $$\fcolorbox{5397eb}{233956}{\textcolor{9cc7ff}{$\blacksquare$}}$$ | `#9cc7ff` | `#5397eb` | `#233956` |
| Purple  | $$\fcolorbox{a47ee0}{3c3152}{\textcolor{cfb5ff}{$\blacksquare$}}$$ | `#cfb5ff` | `#a47ee0` | `#3c3152` |
| Pink    | $$\fcolorbox{d16eaa}{4e2b3f}{\textcolor{fba4d6}{$\blacksquare$}}$$ | `#fba4d6` | `#d16eaa` | `#4e2b3f` |
| Neutral | $$\fcolorbox{9aa5b1}{3a444f}{\textcolor{ccd1d7}{$\blacksquare$}}$$ | `#ccd1d7` | `#9aa5b1` | `#3a444f` |

### Draw.io Starter

{{< diagramsnet src="sidera-palette.drawio" >}}
