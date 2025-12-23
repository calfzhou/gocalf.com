---
title: 200. Number of Islands
notebook: coding
tags:
- medium
date: 2024-11-21 10:40:59
updated: 2024-11-21 10:40:59
---
## Problem

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

<https://leetcode.com/problems/number-of-islands/>

**Example 1:**

> Input:
>
> ``` c++
> grid = [
>   ["1","1","1","1","0"],
>   ["1","1","0","1","0"],
>   ["1","1","0","0","0"],
>   ["0","0","0","0","0"]
> ]
> ```
>
> Output: `1`

**Example 2:**

> Input:
>
> ``` c++
> grid = [
>   ["1","1","0","0","0"],
>   ["1","1","0","0","0"],
>   ["0","0","1","0","0"],
>   ["0","0","0","1","1"]
> ]
> ```
>
> Output: `3`

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Test Cases

``` python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
```

{% asset_code coding/200-number-of-islands/solution_test.py %}

## Thoughts

计算机图形学中的漫填充算法。

如果当前位置是陆地，把它改成水，然后看上下左右四个位置，如果有陆地就放到栈里。每次对出栈的位置做相同的处理。这样把整个岛屿都改成水了。

扫描整个区域，每发现一块陆地就用漫填充算法把相连的陆地都换成水，记录次数。

## Code

{% asset_code coding/200-number-of-islands/solution.py %}
