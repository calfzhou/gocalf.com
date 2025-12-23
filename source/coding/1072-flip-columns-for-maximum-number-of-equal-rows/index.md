---
title: 1072. Flip Columns For Maximum Number of Equal Rows
notebook: coding
tags:
- medium
date: 2025-01-01 19:15:29
updated: 2025-01-01 19:15:29
---
## Problem

You are given an `m x n` binary matrix `matrix`.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from `0` to `1` or vice versa).

Return _the maximum number of rows that have all values equal after some number of flips_.

<https://todo>

**Example 1:**

> Input: `matrix = [[0,1],[1,1]]`
> Output: `1`
> Explanation: After flipping no values, 1 row has all values equal.

**Example 2:**

> Input: `matrix = [[0,1],[1,0]]`
> Output: `2`
> Explanation: After flipping values in the first column, both rows have equal values.

**Example 3:**

> Input: `matrix = [[0,0,0],[0,0,1],[1,1,0]]`
> Output: `2`
> Explanation: After flipping values in the first two columns, the last two rows have equal values.

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is either `0` or `1`.

## Test Cases

``` python
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
```

{% asset_code coding/1072-flip-columns-for-maximum-number-of-equal-rows/solution_test.py %}

## Thoughts

如果某一行经过若干列的翻转可以变成全零（或全一），那么初始时跟它完全相同的行也会变成全零（或全一），而跟它完全相反（零一互补）的行会变成全一（或全零）。

把 matrix 中完全相同或互补的行归为一堆，最终看最大的一堆有多少行即可。

为了方便地处理互补的行，可以把所有行的第一个数字都翻转成一样的，比如都是 1。如果一行的第一个数字原本就是 1 则不用动，如果是 0 则把每个数字都翻转。

时间复杂度 `O(m * n)`，空间复杂度最坏情况也是 `O(m * n)`。

## Code

{% asset_code coding/1072-flip-columns-for-maximum-number-of-equal-rows/solution.py %}
