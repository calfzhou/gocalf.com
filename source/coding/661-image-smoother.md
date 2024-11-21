---
title: 661. Image Smoother
notebook: coding
tags:
- easy
date: 2024-11-18 17:05:10
updated: 2024-11-18 17:05:10
---
## Problem

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

{% invert %}
{% image 661-image-smoother/problem.png %}
{% endinvert %}

Given an `m x n` integer matrix `img` representing the grayscale of an image, return _the image after applying the smoother on each cell of it_.

<https://leetcode.cn/problems/image-smoother/>

**Example 1:**

{% invert %}
{% image 661-image-smoother/case1.png %}
{% endinvert %}

> Input: `img = [[1,1,1],[1,0,1],[1,1,1]]`
> Output: `[[0,0,0],[0,0,0],[0,0,0]]`
> Explanation:
> For the points (0,0), (0,2), (2,0), (2,2): `floor(3/4) = floor(0.75) = 0`
> For the points (0,1), (1,0), (1,2), (2,1): `floor(5/6) = floor(0.83333333) = 0`
> For the point (1,1): `floor(8/9) = floor(0.88888889) = 0`

**Example 2:**

{% invert %}
{% image 661-image-smoother/case2.png %}
{% endinvert %}

> Input: `img = [[100,200,100],[200,50,200],[100,200,100]]`
> Output: `[[137,141,137],[141,138,141],[137,141,137]]`
> Explanation:
> For the points (0,0), (0,2), (2,0), (2,2): `floor((100+200+200+50)/4) = floor(137.5) = 137`
> For the points (0,1), (1,0), (1,2), (2,1): `floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141`
> For the point (1,1): `floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138`

**Constraints:**

- `m == img.length`
- `n == img[i].length`
- `1 <= m, n <= 200`
- `0 <= img[i][j] <= 255`

## Test Cases

{% asset_code coding/661-image-smoother/solution_test.py %}

## Thoughts

遍历所有格子计算即可。

可以的优化点（减少一些重复计算），先不考虑边界，设当前在计算某行第 j 列的格子，可以记录 `s_l`、`s_m` 和 `s_r` 分别表示 `j-1`、`j` 和 `j+1` 三列中，上中下三个格子的和。那么下一步处理 `j+1` 列时，只需要丢弃 `s_l`，算出 `j+2` 列的三数之和，跟 `s_m` 和 `s_r` 相加再求均值即可。

不过没有太大必要，还是会有很多边界条件的判定一直跟着。如果真要减少不必要的边界判定，可以对边界单独处理，然后中间的区域就完全不用判断是否越界。

## Code

{% asset_code coding/661-image-smoother/solution.py %}
