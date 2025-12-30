---
title: 3297. Count Substrings That Can Be Rearranged to Contain a String I
notebook: coding
tags:
- medium
date: 2025-01-09 10:18:28
updated: 2025-01-09 10:18:28
---
## Problem

You are given two strings `word1` and `word2`.

A string `x` is called **valid** if `x` can be rearranged to have `word2` as a prefix.

> A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.

Return the total number of **valid** substrings of `word1`.

> A **substring** is a contiguous **non-empty** sequence of characters within a string.

<https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/>

**Example 1:**

> Input: `word1 = "bcca", word2 = "abc"`
> Output: `1`
> Explanation:
> The only valid substring is `"bcca"` which can be rearranged to `"abcc"` having `"abc"` as a prefix.

**Example 2:**

> Input: `word1 = "abcabc", word2 = "abc"`
> Output: `10`
> Explanation:
> All the substrings except substrings of size 1 and size 2 are valid.

**Example 3:**

> Input: `word1 = "abcabc", word2 = "aaabc"`
> Output: `0`

**Constraints:**

- `1 <= word1.length <= 10⁵`
- `1 <= word2.length <= 10⁵`
- `word1` and `word2` consist only of lowercase English letters.

## Test Cases

```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

跟 [76. Minimum Window Substring](../76-minimum-window-substring/index.md) 基本是同一个问题。本题的 valid substring 就相当于 [problem 76](../76-minimum-window-substring/index.md) 中的 window substring，只不过本题不是要找最短的 valid substring，而是要统计所有 valid substring 的数量。

显然包含最短 valid substring 的所有 substrings，都是 valid（要避免重复）。那么直接搬 [76. Minimum Window Substring](../76-minimum-window-substring/index.md) 的代码过来，先去掉记录最短 valid substring 的逻辑。

在窗口移动过程中，如果当前窗口 `[i, j)` 对应的 substring `word1[i:j]` 是 valid，显然对于任意的 k（`j ≤ k ≤ n`），`word1[i:k]` 都 valid，总数为 `n - j - 1`（n 是 word1 的长度）。因为这些 substring 都是以位置 i 为起点，在此之前和之后都不会再遇到这些 substring，不会重复计数。

时间复杂度 `O(n + m)`（n 和 m 分别是 word1 和 word2 的长度），空间复杂度 `O(k) ≈ O(1)`（k 是 word2 中不同字符的个数）。

## Code

{% asset_code solution.py %}
