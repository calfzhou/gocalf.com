---
title: 52. N-Queens II
notebook: coding
tags:
- hard
date: 2024-12-02 10:46:48
updated: 2024-12-02 10:46:48
---
## Problem

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _the number of distinct solutions to the **n-queens puzzle**_.

<https://leetcode.cn/problems/n-queens-ii/description/>

**Example 1:**

![case1](../51-n-queens/case1.png){.invert-when-dark}

> Input: n = 4
> Output: 2
> Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

**Example 2:**

> Input: n = 1
> Output: 1

**Constraints:**

- `1 <= n <= 9`

## Test Cases

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

跟 [51. N-Queens](../51-n-queens/index.md) 差不多，只是不用输出皇后的摆放结果，直接记录方案数量即可。

## Code

### Recursively

{% asset_code solution.py %}

### Iteratively

{% asset_code solution2.py %}

递归版本可以去掉记录每行的皇后摆放的位置，因为每一层递归的局部变量里已经记录了该信息。而非递归版还是需要的。
