---
title: 3405. Count the Number of Arrays with K Matching Adjacent Elements
notebook: coding
tags:
- hard
katex: true
date: 2025-01-03 19:16:49
updated: 2025-01-03 19:16:49
---
## Problem

You are given three integers `n`, `m`, `k`. A **good array** `arr` of size `n` is defined as follows:

- Each element in `arr` is in the **inclusive** range `[1, m]`.
- _Exactly_ `k` indices `i` (where `1 <= i < n`) satisfy the condition `arr[i - 1] == arr[i]`.

Return the number of **good arrays** that can be formed.

Since the answer may be very large, return it **modulo** `10⁹ + 7`.

<https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/>

**Example 1:**

> Input: `n = 3, m = 2, k = 1`
> Output: `4`
> Explanation:
>
> - There are 4 good arrays. They are `[1, 1, 2]`, `[1, 2, 2]`, `[2, 1, 1]` and `[2, 2, 1]`.
> - Hence, the answer is 4.

**Example 2:**

> Input: `n = 4, m = 2, k = 2`
> Output: `6`
> Explanation:
>
> - The good arrays are `[1, 1, 1, 2]`, `[1, 1, 2, 2]`, `[1, 2, 2, 2]`, `[2, 1, 1, 1]`, `[2, 2, 1, 1]` and `[2, 2, 2, 1]`.
> - Hence, the answer is 6.

**Example 3:**

> Input: `n = 5, m = 2, k = 0`
> Output: `2`
> Explanation:
>
> - The good arrays are `[1, 2, 1, 2, 1]` and `[2, 1, 2, 1, 2]`. Hence, the answer is 2.

**Constraints:**

- `1 <= n <= 10⁵`
- `1 <= m <= 10⁵`
- `0 <= k <= n - 1`

## Test Cases

```python
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
```

{% snippet solution_test.py %}

## Thoughts

全都是数论知识。

首先 n 个位置中，有且只有 k 个位置的数跟其左边的数相等，显然除了 `i = 0` 之外其他的都可以，相当于从 `n - 1` 个位置中任选 k 个，一共有 $C(n-1, k) = \binom{n-1}{k}$ 个选择。

把选中的 k 个位置先拿掉，剩下 `n - k` 个，这些位置填入的数字都不能与其左边的数字相等。第一个位置有 m 个选择，之后的每个位置都有 `m - 1` 个选择，一共有 `m * (m - 1) ** (n - k - 1)` 个选择。

上边两个事件相互独立，所以乘积就是总的选择数，即可以构造出的 good array 总数：

$$
m \times (m-1)^{n-k-1} \times \binom{n-1}{k}
$$

其中 $(m-1)^{n-k-1}$ 可以用 [3266. Final Array State After K Multiplication Operations II](../3266-final-array-state-after-k-multiplication-operations-ii/index.md) 中提到的二分法幂运算。

组合数 $\binom{n-1}{k}$ 就有点儿棘手，因为 $\binom{n-1}{k} = \frac{(n-1)!}{k!\times (n-1-k)!}$，但是模运算不支持除法。

这里需要用到模逆元（[Modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)）。如果要计算 `(x / a) % p`，可以先求 a 对于 p 的模逆元 b（`(a * b) % p = 1`），再计算 `(x * b) % p` 即可。

求 a 对于 p（本题中 `p = 10⁹ + 7` 是个质数）的模逆元，可以用费马小定理（[Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)），易知 `a ** (p - 2) % MOD` 是 a 的逆元（因为 $a\times a^{p-2} = a^{p-1}\equiv 1\pmod{p}$）。

可以事先把最大值（10⁵）以内所有数的阶乘，以及每个阶乘的模逆元都计算好存下来，用的时候直接查表即可。

求模逆元的时间复杂度是 `O(log p)`。

对于连续自然数的阶乘，并不用每个结果都求模逆元，可以对最后一个结果求模逆元，然后倒着推算回去，因为：

$$
inv(i!)\equiv inv(\frac{(i+1)!}{i+1})\equiv inv((i+1)!)\times(i+1)\pmod{p}
$$

不考虑提前缓存所有的阶乘与阶乘的模逆元，时间复杂度为 `O(n)`（幂运算是 `O(log n)`，阶乘是 `O(n)`，阶乘的模逆元是 `O(log (10⁹ + 7))` 可以认为是常数。

## Code

{% snippet solution.py %}
