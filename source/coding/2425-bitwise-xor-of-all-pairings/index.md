---
title: 2425. Bitwise XOR of All Pairings
notebook: coding
tags:
- medium
katex: true
date: 2025-01-16 16:26:37
updated: 2025-01-16 16:26:37
---
## Problem

You are given two **0-indexed** arrays, `nums1` and `nums2`, consisting of non-negative integers. There exists another array, `nums3`, which contains the bitwise XOR of **all pairings** of integers between `nums1` and `nums2` (every integer in `nums1` is paired with every integer in `nums2` **exactly once**).

Return _the **bitwise XOR** of all integers in_ `nums3`.

<https://leetcode.com/problems/bitwise-xor-of-all-pairings/>

**Example 1:**

> Input: `nums1 = [2,1,3], nums2 = [10,2,5,0]`
> Output: `13`
> Explanation:
> A possible nums3 array is `[8,0,7,2,11,3,4,1,9,1,6,3]`.
> The bitwise XOR of all these numbers is 13, so we return 13.

**Example 2:**

> Input: `nums1 = [1,2], nums2 = [3,4]`
> Output: `0`
> Explanation:
> All possible pairs of bitwise XORs are `nums1[0] ^ nums2[0]`, `nums1[0] ^ nums2[1]`, `nums1[1] ^ nums2[0]`,
> and `nums1[1] ^ nums2[1]`.
> Thus, one possible nums3 array is `[2,5,1,6]`.
> `2 ^ 5 ^ 1 ^ 6 = 0`, so we return 0.

**Constraints:**

- `1 <= nums1.length, nums2.length <= 10⁵`
- `0 <= nums1[i], nums2[j] <= 10⁹`

## Test Cases

``` python
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
```

{% asset_code coding/assets/2425-bitwise-xor-of-all-pairings/solution_test.py %}

## Thoughts

首先对于一个非负整数 x，偶数个 x 的 `XOR` 的结果为 0，奇数个 x 的 `XOR` 的结果为 x。

不妨设 nums1 的长度为 m，其元素分别为 $a_1,a_2,\dots,a_m$。nums2 的长度为 n，元素为 $b_1,b_2,\dots,b_n$。

那么所求的结果为：

$$
\begin{array}{rl}
  & (a_1\oplus b_1)\oplus(a_1\oplus b_2)\oplus\dots\oplus(a_1\oplus b_n) \\
  \oplus & (a_2\oplus b_1)\oplus(a_2\oplus b_2)\oplus\dots\oplus(a_2\oplus b_n) \\
  \oplus & \dots \\
  \oplus & (a_m\oplus b_1)\oplus(a_m\oplus b_2)\oplus\dots\oplus(a_m\oplus b_n) \\
  \\
  = & (\underbrace{a_1\oplus a_1\oplus\dots\oplus a_1}_{n}) \\
  \oplus & (\underbrace{a_2\oplus a_2\oplus\dots\oplus a_2}_{n}) \\
  \oplus & \dots \\
  \oplus & (\underbrace{a_m\oplus a_m\oplus\dots\oplus a_m}_{n}) \\
  \oplus & (\underbrace{b_1\oplus b_1\oplus\dots\oplus b_1}_{m}) \\
  \oplus & (\underbrace{b_2\oplus b_2\oplus\dots\oplus b_2}_{m}) \\
  \oplus & \dots \\
  \oplus & (\underbrace{b_n\oplus b_n\oplus\dots\oplus b_n}_{m}) \\
  \\
  = & \begin{cases}
    0 & \text{if }n\equiv 0\pmod{2} \\
    a_1\oplus a_2\oplus\dots\oplus a_m & \text{otherwise}
  \end{cases} \\
  \oplus & \begin{cases}
    0 & \text{if }m\equiv 0\pmod{2} \\
    b_1\oplus b_2\oplus\dots\oplus b_n & \text{otherwise}
  \end{cases}
\end{array}
$$

所以如果 n 是偶数就取 0，否则取 nums1 中每个数字 `XOR` 的结果；如果 m 是偶数就取 0，否则取 nums2 中每个数字 `XOR` 的结果；这两个中间结果取 `XOR` 即可。

时间复杂度 `O(m + n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/2425-bitwise-xor-of-all-pairings/solution.py %}
