---
title: 2429. Minimize XOR
notebook: coding
tags:
- medium
date: 2025-01-15 11:02:53
updated: 2025-01-15 11:02:53
---
## Problem

Given two positive integers `num1` and `num2`, find the positive integer `x` such that:

- `x` has the same number of set bits as `num2`, and
- The value `x XOR num1` is **minimal**.

Note that `XOR` is the bitwise XOR operation.

Return _the integer_ `x`. The test cases are generated such that `x` is **uniquely determined**.

The number of **set bits** of an integer is the number of `1`'s in its binary representation.

<https://leetcode.com/problems/minimize-xor/>

**Example 1:**

> Input: `num1 = 3, num2 = 5`
> Output: `3`
> Explanation:
> The binary representations of num1 and num2 are `0011` and `0101`, respectively.
> The integer 3 has the same number of set bits as num2, and the value `3 XOR 3 = 0` is minimal.

**Example 2:**

> Input: `num1 = 1, num2 = 12`
> Output: `3`
> Explanation:
> The binary representations of num1 and num2 are `0001` and `1100`, respectively.
> The integer 3 has the same number of set bits as num2, and the value `3 XOR 1 = 2` is minimal.

**Constraints:**

- `1 <= num1, num2 <= 10⁹`

## Test Cases

``` python
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
```

{% asset_code coding/assets/2429-minimize-xor/solution_test.py %}

## Thoughts

先统计 num1 和 num2 各自二进制表示中的 1 的个数（可以用 [191. Number of 1 Bits](../191-number-of-1-bits/index.md) 里提到的各种方法，或者直接用语言自带的方法如 Python 中 [`int.bit_count`](https://docs.python.org/3.10/library/stdtypes.html#int.bit_count)）。

如果它俩的二进制表示中 1 的个数一致，那么 num1 就是所求结果，它与自己的 XOR 结果为 0，是最小的。

如果 num1 的 1 的个数少一些，就需要把一些二进制位的 1 改成 0，为了让 XOR 的结果最小，显然应该先改低位的 1。

如果 num1 的 1 的个数多一些，就需要把一些二进制为的 0 改成 1，同理可知为了让 XOR 的结果最小，应该先改低位的 0。

时间复杂度 `O(log num1 + log num2)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/2429-minimize-xor/solution.py %}
