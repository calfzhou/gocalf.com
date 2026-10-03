---
title: 50. Pow(x, n)
notebook: coding
tags:
- medium
date: 2024-12-20 19:31:16
updated: 2024-12-20 19:31:16
---
## Problem

Implement [pow(x, n)](http://www.cplusplus.com/reference/valarray/pow/), which calculates `x` raised to the power `n` (i.e., `xⁿ`).

<https://leetcode.com/problems/powx-n/>

**Example 1:**

> Input: `x = 2.00000, n = 10`
> Output: `1024.00000`

**Example 2:**

> Input: `x = 2.10000, n = 3`
> Output: `9.26100`

**Example 3:**

> Input: `x = 2.00000, n = -2`
> Output: `0.25000`
> Explanation: `2⁻² = 1/2² = 1/4 = 0.25`

**Constraints:**

- `-100.0 < x < 100.0`
- `-2³¹ <= n <= 2³¹-1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.
- `-10⁴ <= xⁿ <= 10⁴`

## Test Cases

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
```

{% snippet solution_test.py %}

## Thoughts

在 [3266. Final Array State After K Multiplication Operations II](../3266-final-array-state-after-k-multiplication-operations-ii/index.md) 中已经实现了两种二分法幂运算的逻辑，直接套用其中一种即可。

如果 n 是负数，则令 `x = 1 / x`，然后计算 `x⁻ⁿ` 即可。

## Code

{% snippet solution.py %}
