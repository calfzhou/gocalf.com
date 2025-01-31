---
title: 827. Making A Large Island
notebook: coding
tags:
- hard
date: 2025-01-31 22:46:37
updated: 2025-01-31 22:46:37
---
## Problem

You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to be `1`.

Return _the size of the largest **island** in_ `grid` _after applying this operation_.

An **island** is a 4-directionally connected group of `1`s.

<https://leetcode.com/problems/making-a-large-island/>

**Example 1:**

> Input: `grid = [[1,0],[0,1]]`
> Output: `3`
> Explanation: Change one 0 to 1 and connect two 1s, then we get an island with `area = 3`.

**Example 2:**

> Input: `grid = [[1,1],[1,0]]`
> Output: `4`
> Explanation: Change the 0 to 1 and make the island bigger, only one island with `area = 4`.

**Example 3:**

> Input: `grid = [[1,1],[1,1]]`
> Output: `4`
> Explanation: Can't change any 0 to 1, only one island with `area = 4`.

**Constraints:**

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 500`
- `grid[i][j]` is either `0` or `1`.

## Test Cases

``` python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
```

{% asset_code coding/827-making-a-large-island/solution_test.py %}

## Thoughts

跟 [200. Number of Islands](200-number-of-islands) 和 [2658. Maximum Number of Fish in a Grid](2658-maximum-number-of-fish-in-a-grid) 类似。

先用跟 [200. Number of Islands](200-number-of-islands) 一样的漫填充算法对 grid 做一遍处理，找到所有的 island 并计算每个 island 的面积。因为 grid 中的 0 表示水，1 表示陆地，所以从 2 开始对 island 编号（即发现的第一个 island 的编号为 2）。填充 island 的时候，直接用其编号写到 grid 的对应位置。用额外的数组或字典记录每个 island 的面积。

然后再遍历一遍 grid，检查每一个水（值为 0）的 cell，看其上下左右四个 cell 分别属于哪个 island（或者是水），把各不相同的 island 的面积相加，再加上 1（当前 cell），得到对当前 cell 执行「填海」操作后能连成一体的新的 island 的大小。

始终记录见到的最大的 island（原本的 island 或者「填海」连起来的新 island）的面积即可。

时间复杂度 `O(n²)`，空间复杂度 `O(n²)`（grid 可以 in-place 修改，但还需要记录每个 island 的面积）。

## Code

{% asset_code coding/827-making-a-large-island/solution.py %}
