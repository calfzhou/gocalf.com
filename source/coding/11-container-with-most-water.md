---
title: 11. Container With Most Water
notebook: coding
tags:
- medium
date: 2024-11-11 02:38:27
updated: 2024-11-11 11:44:19
katex: true
---
## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Notice** that you may not slant the container.

<https://leetcode.com/problems/container-with-most-water/>

**Example 1:**

{% invert %}
{% image 11-container-with-most-water/case1.png %}
{% endinvert %}

> Input: `height = [1,8,6,2,5,4,8,3,7]`
> Output: `49`
> Explanation: The above vertical lines are represented by array `[1,8,6,2,5,4,8,3,7]`. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**

> Input: `height = [1,1]`
> Output: `1`

**Constraints:**

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Test Case

{% asset_code coding/11-container-with-most-water/solution_test.py %}

## Thoughts

对于 $\forall 1 \le i < j \le n$，第 i、j 两个竖线围起来的面积为 $area_{i,j}=(j-i)\times\min\{h_i,h_j\}$。

直接遍历所有的 i、j，找到最大值即可，时间复杂度 `O(n^2)`，空间复杂度 `O(1)`。

显然太慢了，需要降低时间复杂度。

实际上以任意两个竖线围成一个容器，该容器的高度一定跟两个竖线中较矮的那个一致，称这条竖线为该容器的等高边，称该容器为这条竖线的等高容器。

竖线 i 左侧存在等高容器，当且仅当 $\exists 1\le j<i, h_j\ge h_i$，面积为 $(i-j)\times h_i$。

竖线 i 右侧存在等高容器，当且仅当 $\exists i<k\le n, h_k\ge h_i$，面积为 $(k-i)\times h_i$。

计算所有竖线的最大等高容器（有可能没有）的面积，其中最大的那个就是题目要求的最大容器的面积。

时间复杂度还是 `O(n^2)`。

以左侧最大等高容器为例，怎么更快的遍历完所有竖线呢？

从第一条竖线开始往右遍历，当前为竖线 i。这时候再从第一条竖线开始往右，遇到高度大于等于 `h_i` 的线时停止。可以记录前 i - 1 条竖线的最大高度，如果小于 `h_i` 则直接跳过。

这种裁剪的效果聊胜于无，还是要看怎么更快地确定符合 $h_j\ge h_i$ 的最小的 j。

刚才是要从 1 一直递增遍历到 j。其中有一些是不必要的比较，比如那些比自身左侧竖线矮的线，就不需要比较了。

可以记录下从左到右见到的每一个历史新高，形成一个有序数组，再用二分法在它们中寻找 j。

如果当前竖线是 i，那么这个辅助数组的元素是 $\{j|\forall 1\le p<j<i,h_p<h_j\}$。

时间复杂度小于 `O(n log n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/11-container-with-most-water/solution.py %}

## Improve

先看最两边的竖线 i = 1、j = n 围起来的容器 $C_{i,j}$，是所有可能容器中最宽的，其高度为 $h_{i,j}=min\{h_i,h_j\}$。

其他容器的宽度一定比这个窄，只有当高度更高时，才有可能比 $C_{i,j}$ 面积大。

假设 $h_i\le h_j$，看 i 右边的竖线，如果 $h_{i+1}\le h_i$，那么 $C_{i+1,j}$ 的面积只会更小。

从 i + 1 开始向依次右找，如果能找到一个 k（i < k < j），$h_k > h_i$，用竖线 k 和 j 围起来的容器 $C_{k,j}$ 高度更高，面积有可能更大一些。

用同样的方法在竖线 k、j 之间继续一个一个找到高度更高的容器，直到两个竖线重合。

在找到过的所有容器（从最宽最矮，到最窄最高）中，面积最大的那个就是题目所求的容器。

整体只需要对所有竖线从两头往中间遍历一次，时间复杂度 `O(n)`，空间复杂度 `O(1)`。

代码有两版实现，其中 `maxArea` 的逻辑复杂一些，但计算量小很多（仅在需要时计算容器面积），速度更快。`maxArea_simple` 逻辑更直接，但会计算每一个遇到的容器面积，速度略慢。

{% asset_code coding/11-container-with-most-water/solution2.py %}
