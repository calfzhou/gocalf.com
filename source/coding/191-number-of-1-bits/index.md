---
title: 191. Number of 1 Bits
notebook: coding
tags:
- easy
date: 2024-11-19 16:52:28
updated: 2024-11-19 16:52:28
---
## Problem

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).

> A **set bit** refers to a bit in the binary representation of a number that has a value of `1`.

<https://leetcode.com/problems/number-of-1-bits/>

**Example 1:**

> Input: `n = 11`
> Output: `3`
> Explanation:
> The input binary string `1011` has a total of three set bits.

**Example 2:**

> Input: `n = 128`
> Output: `1`
> Explanation:
> The input binary string `10000000` has a total of one set bit.

**Example 3:**

> Input: `n = 2147483645`
> Output: `30`
> Explanation:
> The input binary string `1111111111111111111111111111101` has a total of thirty set bits.

**Constraints:**

- `1 <= n <= 2³¹ - 1`

**Follow up:** If this function is called many times, how would you optimize it?

## Test Cases

{% asset_code coding/assets/191-number-of-1-bits/solution_test.py %}

## Thoughts

判断最低位是否是 `1`，然后右移一位，直到数字变为 0。

## Code

``` python
class Solution:
    def hammingWeight(self, n: int) -> int:
```

{% asset_code coding/assets/191-number-of-1-bits/solution.py %}

## Faster

考虑更「二进制」的计算方法。

对于一个 4 bits 二进制数，一共 16 个不同的数字，每个数字中 `1` 的个数可以先算好，保存在数组中，数组下标就是数字本身。

对于一个 32 bits 二进制数，可以分成 8 段，每段是一个 4 bit 二进制数，直接查表得到这一段内 `1` 的个数，8 段的结果累加即可。

{% asset_code coding/assets/191-number-of-1-bits/solution2.py %}

## Another Way

回到开始的循环移位法，循环次数跟 n 的位数一致。看有没有可能没循环一次都去掉一个 `1`。

对于奇数 n，最低位是 1，那么 `n - 1` 的最低位变成 `0`，而所有的高位都不变。二者取 bit-and，结果会少一个 `1`。

对于偶数 n（大于 0），最低位是 0，那么 `n - 1` 会把最低的连续的 `0` 都变成 `1`，而原来最后一个 `1` 变成 `0`（如 `0b1011100 - 1 = 0b1011011`），再和 n 取 bit-and，原来最后一个 `1` 以及所有的低位都会变成 `0`（如 `0b1011100 & 0b1011011 = 0b1011000`）。

这样每次都让 n 和 `n - 1` 取 bit-and，每次会去掉最后一个 `1`，直到得到 0。

循环的次数跟 n 中 `1` 的个数一致。

{% asset_code coding/assets/191-number-of-1-bits/solution3.py %}
