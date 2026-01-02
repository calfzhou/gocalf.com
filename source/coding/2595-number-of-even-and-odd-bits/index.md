---
title: 2595. Number of Even and Odd Bits
notebook: coding
tags:
- easy
date: 2025-02-20 09:43:50
updated: 2025-02-20 09:43:50
---
## Problem

You are given a **positive** integer `n`.

Let `even` denote the number of even indices in the binary representation of `n` with value 1.

Let `odd` denote the number of odd indices in the binary representation of `n` with value 1.

Note that bits are indexed from **right to left** in the binary representation of a number.

Return the array `[even, odd]`.

<https://leetcode.cn/problems/number-of-even-and-odd-bits/>

**Example 1:**

> Input: `n = 50`
> Output: `[1,2]`
> Explanation:
> The binary representation of 50 is `110010`.
> It contains 1 on indices 1, 4, and 5.

**Example 2:**

> Input: `n = 2`
> Output: `[0,1]`
> Explanation:
> The binary representation of 2 is `10`.
> It contains 1 only on index 1.

**Constraints:**

- `1 <= n <= 1000`

## Test Cases

```python
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
```

{% snippet solution_test.py %}

## Thoughts

直接遍历 n 的每个二进制位。时间复杂度 `O(log n)`，空间复杂度 `O(1)`。

## Code

{% snippet solution.py %}
