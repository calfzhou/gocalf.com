---
title: 1260. Shift 2D Grid
notebook: coding
tags:
- easy
date: 2025-01-03 11:05:26
updated: 2025-01-03 11:05:26
---
## Problem

Given a 2D `grid` of size `m x n` and an integer `k`. You need to shift the `grid` `k` times.

In one shift operation:

- Element at `grid[i][j]` moves to `grid[i][j + 1]`.
- Element at `grid[i][n - 1]` moves to `grid[i + 1][0]`.
- Element at `grid[m - 1][n - 1]` moves to `grid[0][0]`.

Return the _2D grid_ after applying shift operation `k` times.

<https://leetcode.com/problems/shift-2d-grid/>

**Example 1:**

![case1|400](case1.png "case1"){.invert-when-dark}

> Input: `grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
> Output: `[[9,1,2],[3,4,5],[6,7,8]]`

**Example 2:**

![case2|400](case2.png "case2"){.invert-when-dark}

> Input: `grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4`
> Output: `[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]`

**Example 3:**

> Input: `grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9`
> Output: `[[1,2,3],[4,5,6],[7,8,9]]`

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 50`
- `1 <= n <= 50`
- `-1000 <= grid[i][j] <= 1000`
- `0 <= k <= 100`

## Test Cases

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
```

{% snippet solution_test.py %}

## Thoughts

In-place 轮换比较麻烦，一般的实现方式也是需要用 `O(m * n)` 的辅助空间。直接生成新的二维数组写入轮换后的结果即可。

## Code

{% snippet solution.py %}
