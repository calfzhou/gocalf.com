---
title: 3239. Minimum Number of Flips to Make Binary Grid Palindromic I
notebook: coding
tags:
- medium
date: 2024-11-15 10:46:43
updated: 2024-11-15 10:46:43
---
## Problem

You are given an `m x n` binary matrix `grid`.

A row or column is considered **palindromic** if its values read the same forward and backward.

You can **flip** any number of cells in `grid` from `0` to `1`, or from `1` to `0`.

Return the **minimum** number of cells that need to be flipped to make **either** all rows **palindromic** or all columns **palindromic**.

<https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/>

**Example 1:**

> Input: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
> Output: `2`
> Explanation:
> {% invert %}
{% image 3239-minimum-number-of-flips-to-make-binary-grid-palindromic-i/case1.png %}
{% endinvert %}
> Flipping the highlighted cells makes all the rows palindromic.

**Example 2:**

> Input: `grid = [[0,1],[0,1],[0,0]]`
> Output: `1`
> Explanation:
> {% invert %}
{% image 3239-minimum-number-of-flips-to-make-binary-grid-palindromic-i/case2.png %}
{% endinvert %}
> Flipping the highlighted cell makes all the columns palindromic.

**Example 3:**

> Input: `grid = [[1],[0]]`
> Output: `0`
> Explanation:
> All rows are already palindromic.

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m * n <= 2 * 10^5`
- `0 <= grid[i][j] <= 1`

## Test Cases

``` python
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
```

{% asset_code coding/3239-minimum-number-of-flips-to-make-binary-grid-palindromic-i/solution_test.py %}

## Thoughts

对于一行，从两头往中间逐个比对，不一致的格子对数，就是需要翻转的数量（一对两个格子中翻转任意一个）。

行与行彼此独立，各行需要翻转的数量累加起来就是最终所有行都是回文所需的翻转总数。

同理求出所有列所需要的翻转总数。二者取最小。

时间复杂度 `O(m * n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/3239-minimum-number-of-flips-to-make-binary-grid-palindromic-i/solution.py %}
