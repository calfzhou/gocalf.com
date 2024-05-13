---
title: 魔方手记
notebook: notes
tags:
  - game/puzzle
date: 2024-04-25 22:36:21
updated: 2024-04-25 22:36:21
animcube3: true
---
## 三阶 - 简易层先法

### 说明

魔方公式中的符号说明参见：

- [三阶魔方公式图解--魔方乐园](http://www.mf100.org/base/about.php)
- [WCA Regulations - Article 12: Notation | World Cube Association](https://www.worldcubeassociation.org/regulations/#article-12-notation)

以下配图与公式，基于的配色约定为：

- 上黄－下白
- 前蓝－后绿
- 左橙－右红

{% image rubik-cube/cube-color.png 图片来自魔方乐园 mf100.org %}

简易层先法的复原步骤为：

{% image rubik-cube/simple-steps.png 图片来自魔方乐园 mf100.org bg:#ffffff fancybox:true %}

- 面位：只有一面颜色与中心块颜色相同， 其他面颜色不相同；
- 到位：位置正确，但任一面的颜色和所在面的中心块颜色都不相同；
- 归位：每面块的颜色均和所在面的中心块的颜色同色，它是魔方块还原后的状态。

这组公式经过一定的分类整理，记忆量极小（代价是复原较慢，大体需要 1 分钟才能完成整个复原）。每一个阶段，最少记住一个公式就可以应对所有情况。

另外，公式不是照着字面去背，而是照着公式去拧，多拧几次，形成肌肉记忆就记住了。默写公式大概率写不出来，但魔方在手就能复原。

### 一图流

{% image rubik-cube/img_3842.png 三阶魔方简易层先法一图流 width:320px download:true fancybox:true %}

### 中棱归位

#### ① 向后归位

{% grid c:5 %}
<!-- cell -->
![3-1](../notes/rubik-cube/simple-3-1.png)
{% endgrid %}

`(R U R U) R (U' R' U' R')`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:zzzzygzzzWWWWWWWWWzzbzbbzzbZZGZGGZZGzzzzozoooZZRRRRZZR
  move:"RURU.R.U'R'U'R'"
%}
{% endfolding %}

#### ② 向前归位

{% grid c:5 %}
<!-- cell -->
![3-2](../notes/rubik-cube/simple-3-2.png)
{% endgrid %}

`(R' U' R' U') R' (U R U R)`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:zzzzybzzzWWWWWWWWWzzbzbbzzbZZGZGGZZGzzzzozoooZZRRRRZZR
  move:"R'U'R'U'.R'.URUR"
%}
{% endfolding %}

### 顶棱面位

#### ① ┓ 形

{% grid c:5 %}
<!-- cell -->
![4-1](../notes/rubik-cube/simple-4-1.png)
{% endgrid %}

`B' (U' R' U R) B`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:zyzyyyzyzWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"B'.U'R'UR.B"
  initrevmove:#
%}
{% endfolding %}

#### ② ┅ 形

{% grid c:5 %}
<!-- cell -->
![4-2](../notes/rubik-cube/simple-4-2.png)
{% endgrid %}

`B' (R' U' R U) B` 或 `① ①`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:zyzyyyzyzWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"B'.R'U'RU.B;{① ①}{<①> ①}B'U'R'URB.{① <①>}B'U'R'URB"
  initrevmove:#
%}
{% endfolding %}

#### ③ · 形

{% grid c:5 %}
<!-- cell -->
![4-3](../notes/rubik-cube/simple-4-3.png)
{% endgrid %}

`① U ②`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:zyzyyyzyzWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"{① U ②}{<①> U ②}B'U'R'URB.{① <U> ②}U.{① U <②>}B'R'U'RUB"
  initrevmove:#
%}
{% endfolding %}

### 顶角面位

#### ① 缺三逆向

{% grid c:5 %}
<!-- cell -->
![5-1](../notes/rubik-cube/simple-5-1.png)
{% endgrid %}

`(R U2' R') (U' R U' R')`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"RU2'R'.U'RU'R'"
  initrevmove:#
%}
{% endfolding %}

#### ② 缺三顺向

{% grid c:5 %}
<!-- cell -->
![5-2](../notes/rubik-cube/simple-5-2.png)
{% endgrid %}

`U (R' U2 R) (U R' U R)` 或 `① U2 ①`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"U.R'U2R.UR'UR;{① U2 ①}{<①> U2 ①}RU2'R'U'RU'R'.{① <U2> ①}U2.{① U2 <①>}RU2'R'U'RU'R'"
  initrevmove:#
%}
{% endfolding %}

#### ③ 缺二

{% grid c:5 %}
<!-- cell -->
![5-3a](../notes/rubik-cube/simple-5-3a.png)
<!-- cell -->
![5-3b](../notes/rubik-cube/simple-5-3b.png)
<!-- cell -->
![5-3c](../notes/rubik-cube/simple-5-3c.png)
{% endgrid %}

`① {∅ | U' | U} ②`

{% folding 动画演示 %}
{% grid %}
<!-- cell -->
{% animcube width:100% config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"{① ②}{<①> ②}RU2'R'U'RU'R'.{① <②>}UR'U2RUR'UR"
  initrevmove:#
%}
<!-- cell -->
{% animcube width:100% config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"{① U' ②}{<①> U' ②}RU2'R'U'RU'R'.{① <U'> ②}U'.{① U' <②>}UR'U2RUR'UR"
  initrevmove:#
%}
<!-- cell -->
{% animcube width:100% config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"{① U ②}{<①> U ②}RU2'R'U'RU'R'.{① <U> ②}U.{① U <②>}UR'U2RUR'UR"
  initrevmove:#
%}
{% endgrid %}
{% endfolding %}

#### ④ 缺四

{% grid c:5 %}
<!-- cell -->
![5-4a](../notes/rubik-cube/simple-5-4a.png)
<!-- cell -->
![5-4b](../notes/rubik-cube/simple-5-4b.png)
{% endgrid %}

`① {∅ | U'} ①`

{% folding 动画演示 %}
{% grid %}
<!-- cell -->
{% animcube width:100% config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"{① ①}{<①> ①}RU2'R'U'RU'R'.{① <①>}RU2'R'U'RU'R'"
  initrevmove:#
%}
<!-- cell -->
{% animcube width:100% config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWzbbzbbzbbZGGZGGZGGzzzooooooZRRZRRZRR
  move:"{① U' ①}{<①> U' ①}RU2'R'U'RU'R'.{① <U'> ①}U'.{① U' <①>}RU2'R'U'RU'R'"
  initrevmove:#
%}
{% endgrid %}
{% endfolding %}

### 顶角归位

#### ① 同色

{% grid c:5 %}
<!-- cell -->
![6-1](../notes/rubik-cube/simple-6-1.png)
{% endgrid %}

`(R B' R F2) (R' B R F2) R2`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWbbbzbbbbbGGGZGGGGGozoooooooRRRZRRRRR
  move:"RB'RF2.R'BRF2.R2"
  initrevmove:#
%}
{% endfolding %}

#### ② 异色

{% grid c:5 %}
<!-- cell -->
![6-2](../notes/rubik-cube/simple-6-2.png)
{% endgrid %}

`① U' ①`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  facelets:yyyyyyyyyWWWWWWWWWbbbzbbbbbGGGZGGGGGozoooooooRRRZRRRRR
  move:"{① U' ①}{<①> U' ①}RB'RF2R'BRF2R2.{① <U'> ①}U'.{① U' <①>}RB'RF2R'BRF2R2"
  initrevmove:#
%}
{% endfolding %}

### 顶棱归位

#### ① 逆时针归位

{% grid c:5 %}
<!-- cell -->
![7-1](../notes/rubik-cube/simple-7-1.png)
{% endgrid %}

`(R U' R) (U R U R) (U' R' U' R2')`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  move:"RU'R.URUR.U'R'U'R2'"
  initrevmove:#
%}
{% endfolding %}

#### ② 顺时针归位

{% grid c:5 %}
<!-- cell -->
![7-2](../notes/rubik-cube/simple-7-2.png)
{% endgrid %}

`(R2 U R U) (R' U' R' U') (R' U R')` 或 `① ①`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  move:"R2URU.R'U'R'U'.R'UR';{① ①}{<①> ①}RU'RURURU'R'U'R2'.{① <①>}RU'RURURU'R'U'R2'"
  initrevmove:#
%}
{% endfolding %}

#### ③ 交叉归位

{% grid c:5 %}
<!-- cell -->
![7-3](../notes/rubik-cube/simple-7-3.png)
{% endgrid %}

`① U ①`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  move:"{① U ①}{<①> U ①}RU'RURURU'R'U'R2'.{① <U> ①}U.{① U <①>}RU'RURURU'R'U'R2'"
  initrevmove:#
%}
{% endfolding %}

#### ④ 平行归位

{% grid c:5 %}
<!-- cell -->
![7-4](../notes/rubik-cube/simple-7-4.png)
{% endgrid %}

`① U’ ①`

{% folding 动画演示 %}
{% animcube config:rubik-cube/cube.conf
  move:"{① U' ①}{<①> U' ①}RU'RURURU'R'U'R2'.{① <U'> ①}U'.{① U' <①>}RU'RURURU'R'U'R2'"
  initrevmove:#
%}
{% endfolding %}
