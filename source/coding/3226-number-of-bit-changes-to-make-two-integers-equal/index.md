---
title: 3226. Number of Bit Changes to Make Two Integers Equal
notebook: coding
tags:
- easy
date: 2024-11-26 23:29:31
updated: 2024-11-26 23:29:31
katex: true
---
## Problem

You are given two positive integers `n` and `k`.

You can choose **any** bit in the **binary representation** of `n` that is equal to 1 and change it to 0.

Return the _number of changes_ needed to make `n` equal to `k`. If it is impossible, return -1.

<https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/>

**Example 1:**

> Input: `n = 13, k = 4`
> Output: `2`
> Explanation:
> Initially, the binary representations of `n` and `k` are `n = 1101₂` and `k = 0100₂`.
> We can change the first and fourth bits of `n`. The resulting integer is `n = 0100₂ = k`.

**Example 2:**

> Input: `n = 21, k = 21`
> Output: `0`
> Explanation:
> `n` and `k` are already equal, so no changes are needed.

**Example 3:**

> Input: `n = 14, k = 13`
> Output: `-1`
> Explanation:
> It is not possible to make `n` equal to `k`.

**Constraints:**

- `1 <= n, k <= 10⁶`

## Test Cases

``` python
class Solution:
    def minChanges(self, n: int, k: int) -> int:
```

{% asset_code coding/3226-number-of-bit-changes-to-make-two-integers-equal/solution_test.py %}

## Thoughts

先看单个二进制位。当 `n = 1, k = 0`（$\iff(n\oplus k)\land=1$）时需要修改一次，当 `n = 0, k = 1`（$\iff(n\oplus k)\land k=1$）时无法成功，其他情况不用修改。

$$
\begin{array}{cc:cc}
  n & k & (n\oplus k)\land n & (n\oplus k)\land k \\
  \hline
  0 & 0 & 0 & 0 \\
  0 & 1 & 0 & \boxed{1} \\
  1 & 0 & \boxed{1} & 0 \\
  1 & 1 & 0 & 0
\end{array}
$$

扩展到多个二进制位也是一样的。

所以只要 $(n\oplus k)\land k$ 不为零，就无法成功。否则计算 $(n\oplus k)\land n$ 中 `1` 的个数，就是需要修改的次数。

计算某个二进制数中 `1` 的个数，可以按照 [191. Number of 1 Bits](../191-number-of-1-bits/index.md) 中的方法计算。

对于无法成功的情况，只需要 `O(1)` 时间。对于能成功的情况，设修改次数为 c，则时间复杂度为 `O(c)`。

## Code

{% asset_code coding/3226-number-of-bit-changes-to-make-two-integers-equal/solution.py %}
