---
title: 3233. Find the Count of Numbers Which Are Not Special
notebook: coding
tags:
- medium
katex: true
date: 2024-11-22 14:43:51
updated: 2024-11-22 14:43:51
---
## Problem

You are given 2 **positive** integers `l` and `r`. For any number `x`, all positive divisors of `x` _except_ `x` are called the **proper divisors** of `x`.

A number is called **special** if it has exactly 2 **proper divisors**. For example:

- The number 4 is _special_ because it has proper divisors 1 and 2.
- The number 6 is _not special_ because it has proper divisors 1, 2, and 3.

Return the count of numbers in the range `[l, r]` that are **not** **special**.

<https://leetcode.cn/problems/find-the-count-of-numbers-which-are-not-special/>

**Example 1:**

> Input: `l = 5, r = 7`
> Output: `3`
> Explanation:
> There are no special numbers in the range `[5, 7]`.

**Example 2:**

> Input: `l = 4, r = 16`
> Output: `11`
> Explanation:
> The special numbers in the range `[4, 16]` are 4 and 9.

**Constraints:**

- `1 <= l <= r <= 10⁹`

## Test Cases

``` python
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
```

{% asset_code coding/3233-find-the-count-of-numbers-which-are-not-special/solution_test.py %}

## Thoughts

「特殊数」就是质数的平方。相当于先求出 `[l', r']` 内质数的个数，其中 $l'=\lceil\sqrt l\rceil$、$r'=\lfloor\sqrt r\rfloor$。

判断自然数 n 是不是质数，需看所有的 `2 <= i <= √n`，n 能否被 i 整除，时间复杂度 `O(√n)`。

如果已经有了所有小于等于 `√n` 的质数集合，可以遍历已知的质数，看能否被 n 整除，时间复杂度约为 $O(\sqrt n/\ln\sqrt n)$。

> 根据 [质数定理](https://en.wikipedia.org/wiki/Prime_number_theorem) 可知，n 以内的质数个数为 $\pi(n)≈n/\ln n$。

判断连续多个自然数是否是质数，可以考虑把已知的质数保存起来。

判断 `[l', r']` 内质数的个数，如果不缓存已知的质数表，需要时间大约是 $\sum_{i=l'}^{r'}\sqrt i$。如果要用质数表，需要从 1 开始构建，需要的时间大约是 $\sum_{i=1}^{r'}(\sqrt i/\ln\sqrt i)$。

粗估下来，对于限定的 `1 <= l <= r <= 10⁹` 范围，当 `r' > l' + 10` 时，从 1 开始构建质数表就更划算。

## Code

{% asset_code coding/3233-find-the-count-of-numbers-which-are-not-special/solution.py %}

在 LeetCode 上提交的话，一个可选的作 bú 弊 shì 方案是把质数表缓存到 `Solution.nonSpecialCount` 之外，甚至直接提前先算好整个质数表（上限取 $\lfloor\sqrt{1e9}\rfloor=31622$ 即可），并进一步计算出所有的 $\pi(n)$（小于 n 的质数个数），在 `Solution.nonSpecialCount` 里用常数时间计算 $\pi(r'+1)-\pi(l')$ 即可。

{% asset_code coding/3233-find-the-count-of-numbers-which-are-not-special/solution2.py %}
