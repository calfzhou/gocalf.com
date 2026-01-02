---
title: 1092. Shortest Common Supersequence
notebook: coding
tags:
- hard
date: 2025-02-28 15:31:26
updated: 2025-02-28 15:31:26
---
## Problem

Given two strings `str1` and `str2`, return _the shortest string that has both_ `str1` _and_ `str2` _as **subsequences**_. If there are multiple valid strings, return **any** of them.

A string `s` is a **subsequence** of string `t` if deleting some number of characters from `t` (possibly `0`) results in the string `s`.

<https://leetcode.com/problems/shortest-common-supersequence/>

**Example 1:**

> Input: `str1 = "abac", str2 = "cab"`
> Output: `"cabac"`
> Explanation:
> `str1 = "abac"` is a subsequence of "`cabac"` because we can delete the first `"c"`.
> `str2 = "cab"` is a subsequence of `"cabac"` because we can delete the last `"ac"`.
> The answer provided is the shortest such string that satisfies these properties.

**Example 2:**

> Input: `str1 = "aaaaaaaa", str2 = "aaaaaaaa"`
> Output: `"aaaaaaaa"`

**Constraints:**

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of lowercase English letters.

## Test Cases

```python
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
```

{% snippet solution_test.py %}

## Thoughts

跟 [1143. Longest Common Subsequence](../1143-longest-common-subsequence/index.md) 本质上是同一个问题。想要公共超序列最短，就是要让公共子序列最长。设 str1 和 str2 的长度分别为 m 和 n，如果最长的公共子序列长度为 k，那么最短的公共超序列长度即为 `k + (m - k) + (n - k) = m + n - k`。

先照搬 [1143. Longest Common Subsequence](../1143-longest-common-subsequence/index.md) 的代码，在最后会得到完整的 `lcs(i, j)` 表格。从 `lcs(m, n)` 开始就可以找出构造 LCS 的方式，而在 LCS 中把那些不相等的字符加上，就能得到最短公共超序列（SCS）。

对于 `(i, j)`，如果 `lcs(i, j) == lcs(i-1, j)` 则说明 `str1[i-1]` 不属于 LCS，将其添加到 SCS，并继续看 `(i-1, j)`；否则如果 `lcs(i, j) == lcs(i, j-1)` 则说明 `str2[j-1]` 不属于 LCS，将其添加到 SCS，并继续看 `(i, j-1)`；否则（必然有 `lcs(i, j) == lcs(i-1, j-1) + 1`）说明 `str1[i-1] == str2[j-1]` 属于 LCS，将其加入 LCS 和 SCS，并继续看 `(i-1, j-1)`。

以 `str1 = "abac"`、`str2 = "cab"` 为例，根据 `lcs(i, j)` 表格求出 LCS 和 SCS 的过程如下图示：

::: invert-when-dark
{% diagramsnet lcs_scs.drawio %}
:::

按上边提到的规则，找到从 `(m, n)` 到 `(0, 0)` 的路径。对于除了终点的任何一个格子，向上走的取所在行对应的字符（取自 str1），向左走的取所在列对应的字符（取自 str2），斜向左上走的说明所在行和列的字符相同。

空间复杂度 `O(m * n)`，时间复杂度 `O(m * n)`。

## Code

{% snippet solution.py %}
