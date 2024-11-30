---
title: 51. N-Queens
notebook: coding
tags:
- hard
date: 2024-12-01 01:45:08
updated: 2024-12-01 01:45:08
---
## Problem

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

<https://leetcode.cn/problems/n-queens/>

**Example 1:**

{% invert %}
{% image 51-n-queens/case1.png %}
{% endinvert %}

> Input: `n = 4`
> Output: `[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]`
> Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

**Example 2:**

> Input: `n = 1`
> Output: `[["Q"]]`

**Constraints:**

- `1 <= n <= 9`

## Test Cases

``` python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
```

{% asset_code coding/51-n-queens/solution_test.py %}

## Thoughts

任何两个皇后不能在同一行或同一列或同一斜线上。

经典的回溯算法问题。

按行来摆放皇后，每行只放一个，直接保证任何两个皇后不在同一行。

已经放过的皇后的列也不再放，确保任何两个皇后不在同一列。

斜线上任意两个位置的坐标特点是，要么行列下标之和相等，要么行列下标之差相等。设两个皇后的位置分别在 `(i₁, j₁)` 和 `(i₂, j₂)`。她俩在同一斜线，当且仅当，`i₁ + j₁ = i₂ + j₂` 或 `i₁ - j₁ = i₂ - j₂`，亦即 `|i₁ - i₂| = |j₁ - j₂|`。

对每一行，遍历此行皇后可行的置放位置。

可以直接递归。或者改写成循环。

## Code

> 都不是很快啊，可能细节上还可以优化。

### Recursively

{% asset_code coding/51-n-queens/solution.py %}

### Iteratively

{% asset_code coding/51-n-queens/solution2.py %}
