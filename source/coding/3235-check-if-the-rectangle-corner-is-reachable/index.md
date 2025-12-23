---
title: 3235. Check if the Rectangle Corner Is Reachable
notebook: coding
tags:
- hard
- difficult
date: 2024-11-09 20:20:29
updated: 2024-11-09 20:20:29
---

## Problem

You are given two positive integers `xCorner` and `yCorner`, and a 2D array `circles`, where `circles[i] = [xᵢ, yᵢ, rᵢ]` denotes a circle with center at `(xᵢ, yᵢ)` and radius `rᵢ`.

There is a rectangle in the coordinate plane with its bottom left corner at the origin and top right corner at the coordinate `(xCorner, yCorner)`. You need to check whether there is a path from the bottom left corner to the top right corner such that the **entire path** lies inside the rectangle, **does not** touch or lie inside **any** circle, and touches the rectangle **only** at the two corners.

Return `true` if such a path exists, and `false` otherwise.

<https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/>

**Example 1:**

> Input: `xCorner = 3, yCorner = 4, circles = [[2,1,1]]`
> Output: true
> Explanation:
> {% invert %}
![case1](assets/3235-check-if-the-rectangle-corner-is-reachable/case1.png)
{% endinvert %}
> The curve shows a possible path between `(0, 0)` and `(3, 4)`.

**Example 2:**

> Input: `xCorner = 3, yCorner = 3, circles = [[1,1,2]]`
> Output: false
> Explanation:
> {% invert %}
![case2](assets/3235-check-if-the-rectangle-corner-is-reachable/case2.png)
{% endinvert %}
> No path exists from `(0, 0)` to `(3, 3)`.

**Example 3:**

> Input: `xCorner = 3, yCorner = 3, circles = [[2,1,1],[1,2,1]]`
> Output: false
> Explanation:
> {% invert %}
![case3](assets/3235-check-if-the-rectangle-corner-is-reachable/case3.png)
{% endinvert %}
> No path exists from `(0, 0)` to `(3, 3)`.

**Example 4:**

> Input: `xCorner = 4, yCorner = 4, circles = [[5,5,1]]`
> Output: true
> Explanation:
> {% invert %}
![case4](assets/3235-check-if-the-rectangle-corner-is-reachable/case4.png)
{% endinvert %}

**Constraints:**

- `3 <= xCorner, yCorner <= 10⁹`
- `1 <= circles.length <= 1000`
- `circles[i].length == 3`
- `1 <= xᵢ, yᵢ, rᵢ <= 10⁹`

## Test Cases

``` python
class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
```

{% asset_code coding/3235-check-if-the-rectangle-corner-is-reachable/solution_test.py %}

## Thoughts

### 直观想法

先看单个圆，看圆和矩形的哪些边相交/相切，如果相交/相切的边的集合如下，则没有通路：

- 上 & 下
- 左 & 右
- 左 & 下
- 右 & 上

判断圆是否和某个边相交/相切：

> 圆与线段相交/相切 iff
>
> - 圆心到任一端点距离 ≤ 半径
> - 或
> - 圆心到线的距离 ≤ 半径 && 两个端点在垂线两边（利用水平垂直特点可以简化计算）

再看多个圆，把相交/相切的圆归为一堆，他们相交/相切的边取并集，最终并集结果如果符合上边四种情况，则没
有通路。

判断两个圆是否相交/相切：

> 两个圆相交/相切 iff 圆心距离 ≤ 圆心半径和

需要注意，如果一个圆完全在矩形之外，应该直接丢弃。
否则可能会出现一个圆压住上边界，一个圆压住右边界，然后矩形外有一堆圆把前两个圆连接起来。但并不影响通路。
如：`3, 3, [[1,2,1], [1,4,1], [2,5,1], [4,5,1], [5,4,1], [5,2,1], [4,2,1]]`。

判断圆在矩形外：

> 圆在矩形外 iff 圆与四边都不相交/相切 && 圆不在矩形内

所有圆/连成一片的圆都判定完，没有出现不通的情况，最后结果就是有通路。

记录已经处理过的圆组成的相连的团簇，对于每个圆，跟所有已有的团簇的圆判定是否相连（注意可能会同时跟多
个团簇相连，导致团簇合并）。

复杂度 `O(n²)`，n 是 圆的个数。

降低复杂度关键：如何快速计算出所有的团簇，裁剪掉不必要的比较，比如用四叉树。

问题：两个圆心在外边的圆相交，但各自跟上和右边相交，但并不影响通路，如 `3, 3, [[2,10,7], [10,2,7]]`。

取相交/相切圆的圆心连线中的等比点（该点到两个圆心的距离与两个半径同比），如果该点在矩形外就不连成团簇。

设两个圆分别是 `(x1, y1, r1)`、`(x2, y2, r2)`，连线上等比点的位置是 `(x, y)`，则

`x = x1 + (x2 - x1) * r1 / (r1 + r2)`，y 类似（要避免浮点运算）。

判定 `(x, y)` 是否在矩形内。

### 最难点

> 取相交/相切圆的圆心连线中的等比点（该点到两个圆心的距离与两个半径同比），如果该点在矩形外就不连成团簇。

这是个平面几何数学知识点。

## Code

{% asset_code coding/3235-check-if-the-rectangle-corner-is-reachable/solution.py %}

Test cases for solution inner methods:

{% asset_code coding/3235-check-if-the-rectangle-corner-is-reachable/solution_inner_test.py %}
