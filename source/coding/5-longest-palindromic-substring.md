---
title: 5. Longest Palindromic Substring
notebook: coding
tags:
- medium
date: 2024-11-10 03:29:56
updated: 2024-11-10 03:37:00
---
## Problem

<https://leetcode.com/problems/longest-palindromic-substring/description/>

Given a string `s`, return _the longest palindromic substring_ in `s`.

> A string is **palindromic** if it reads the same forward and backward.
> A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

> Input: `s = "babad"`
> Output: `"bab"`
> Explanation: `"aba"` is also a valid answer.

Example 2:

> Input: s = `"cbbd"`
> Output: `"bb"`

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Test Cases

[solution_test.py](5-longest-palindromic-substring/solution_test.py)

## Thoughts

Palindromic string（回文）一定是按中间位置对称的。注意奇数长度和偶数长度的区别。

从左到右遍历每个字符，对于当前字符，检查以其为中心能够构成的最长的 palindromic（注意奇偶问题）。

- 奇数长度的：以其为正中心。
- 偶数长度的：以其及其右边相邻字符为中心。

时间复杂度比 `O(n)` 略高，但一般情况不会太高。

遍历时候大部分字符无法形成长于 1 的回文，判定所需的时间为常数。

假设这个字符串由 k 个长度为 m 的非平凡回文构成，`k * m = n`，那么大约需要做 k 次 `O(m)` 的判定，总计约 `O(k * m) = O(n)`。

连续的相同字符越多，时间复杂度越高。最差情况，字符串的 n 个字符全都一样，那么对于第 i 个字符，需要的时间大致为 `O(max(k, n-k))`，总共大约为 `O(n^2)`。

所以最坏情况时间复杂度为 `O(n^2)`，但一般情况下，时间负载度基本是 `O(n)`。

## Code

[solution.py](5-longest-palindromic-substring/solution.py)

## Extra

有个严格 `O(n)` 时间复杂度（`O(n)` 空间复杂度）的算法，叫 [Manacher's algorithm](https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm)。

比较复杂，先不看了。
