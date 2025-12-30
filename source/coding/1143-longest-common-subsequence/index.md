---
title: 1143. Longest Common Subsequence
notebook: coding
tags:
- medium
date: 2024-11-23 21:33:04
updated: 2024-11-23 21:33:04
---
## Problem

Given two strings `text1` and `text2`, return _the length of their longest **common subsequence**._ If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

<https://leetcode.com/problems/longest-common-subsequence/>

**Example 1:**

> Input: `text1 = "abcde", text2 = "ace"`
> Output: `3`
> Explanation: The longest common subsequence is `"ace"` and its length is 3.

**Example 2:**

> Input: `text1 = "abc", text2 = "abc"`
> Output: `3`
> Explanation: The longest common subsequence is `"abc"` and its length is 3.

**Example 3:**

> Input: `text1 = "abc", text2 = "def"`
> Output: `0`
> Explanation: There is no such common subsequence, so the result is 0.

**Constraints:**

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

## Test Cases

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

经典的动态规划算法问题。

考虑 `text1` 前 i 个字符、与 `text2` 前 j 个字符的字问题，记二者的最长公共子序列长度为 `lcs(i, j)`。

如果 `text1` 的第 i 个字符和 `text2` 的第 j 个字符相同，那么这一对字符可以加入已有的最长公共子序列，即 `lcs(i, j) = 1 + lcs(i-1, j-1)`。

否则公共子序列不会加长，`lcs(i, j)` 只能取所有子问题中的最大值，即在 `lcs(i-1, j-1)`、`lcs(i, j-1)` 和 `lcs(i-1, j)` 中取最大。但显然 `lcs(i-1, j-1)` 不可能比后两个大，所以只需要从后两个值中取最大。

初始值，对于任意的 i、j，有 `lcs(i, 0) = lcs(0, j) = 0`。

最终结果为 `lcs(m, n)`，其中 m 和 n 分别是 `text1` 和 `text2` 的长度。

空间复杂度 `O(m * n)`，时间复杂度 `O(m * n)`。

## Code

{% asset_code solution.py %}
