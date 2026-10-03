---
title: 3258. Count Substrings That Satisfy K-Constraint I
notebook: coding
tags:
- easy
date: 2024-11-12 15:01:35
updated: 2024-11-12 15:01:35
katex: true
---
## Problem

You are given a **binary** string `s` and an integer `k`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

- The number of `0`'s in the string is at most `k`.
- The number of `1`'s in the string is at most `k`.

Return an integer denoting the number of substrings of `s` that satisfy the **k-constraint**.

> A substring is a contiguous non-empty sequence of characters within a string.

<https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/>

**Example 1:**

> Input: `s = "10101", k = 1`
> Output: `12`
> Explanation:
> Every substring of s except the substrings `"1010"`, `"10101"`, and `"0101"` satisfies the k-constraint.

**Example 2:**

> Input: `s = "1010101", k = 2`
> Output: `25`
> Explanation:
> Every substring of `s` except the substrings with a length greater than 5 satisfies the k-constraint.

**Example 3:**

> Input: `s = "11111", k = 1`
> Output: `15`
> Explanation:
> All substrings of `s` satisfy the k-constraint.

**Constraints:**

- `1 <= s.length <= 50`
- `1 <= k <= s.length`
- `s[i]` is either `'0'` or `'1'`.

## Test Cases

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
```

{% snippet solution_test.py %}

## Thoughts

设 `s` 长度为 `n`。

$\forall 1\le i\le n$，计算以 i 开头的符合 k-constraint 的子串个数。

如果存在 j，$i<j\le n$，$s_{i,j}$ 不符合 k-constraint 但 $s_{i,j-1}$ 符合，显然以 i 开头的共有 j - i 个子串（$s_{i,i},s_{i,i+1},s_{i,i+2},\dots,s_{i,j-1}$）符合 k-constraint。

如果 $s_{i,n}$ 符合，那么以 i 开头子串数为 n - i + 1。

用双指针 i 和 j，从 i = j = 1 开始向右扫描字符串。如果 $s_{i,j}$ 符合，则右移 j，否则总数增加 j - i，再向右移动 i。

关键是按这个方式移动，任何时候如果 $s_{i,j}$ 不符合，一定有 $s_{i,j-1}$ 符合。

当 j 超过字符串右端（即 j = n + 1）时，$s_{i,n}$ 及其所有 substring 都符合，令 m = j - i，共 m * (m + 1) / 2 个。

移动过程中动态更新当前子串中 `0` 和 `1` 的个数，用常数时间进更新和判定，总计时间复杂度为 `O(n)`，空间复杂度 `O(1)`。

## Code

{% snippet solution.py %}
