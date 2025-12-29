---
title: 3138. Minimum Length of Anagram Concatenation
notebook: coding
tags:
- medium
date: 2024-12-20 10:38:00
updated: 2024-12-20 10:38:00
---
## Problem

You are given a string `s`, which is known to be a concatenation of **anagrams** of some string `t`.

Return the **minimum** possible length of the string `t`.

An **anagram** is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

<https://leetcode.cn/problems/minimum-length-of-anagram-concatenation/>

**Example 1:**

> Input: `s = "abba"`
> Output: `2`
> Explanation:
> One possible string t could be `"ba"`.

**Example 2:**

> Input: `s = "cdef"`
> Output: `4`
> Explanation:
> One possible string t could be `"cdef"`, notice that t can be equal to s.

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s` consist only of lowercase English letters.

## Test Cases

```python
class Solution:
    def minAnagramLength(self, s: str) -> int:
```

{% asset_code coding/3138-minimum-length-of-anagram-concatenation/solution_test.py %}

## Thoughts

任取从左端开始长度为 i 的子字符串 `s[:i]`，判断它是不是一个可行的 t。

首先 s 的长度 n 必须能被 i 整除。s 中的每一个字符，都必须在 `s[:i]` 中出现，且它在 s 中的词频能被在 `s[:i]` 中的词频整除。

接下来看剩余的子字符串 `s[i:]` 是不是由若干个 `s[:i]` 的 anagrams（同位字符串）连接而成。分别检查 `s[i:2i]`、`s[2i:3i]`、……，对于某一个片段，统计其中各字符的词频，如果跟 `s[:i]` 中各字符的词频完全一致，就是 `s[:i]` 的 anagram。如果所有片段都是 anagrams，则 `s[:i]` 是可行的 t。

为了找到最短的 t，从 `i = 1` 开始遍历，最大只需要到 `n // 2` 即可。如果到 `n // 2` 都不行，返回 n。

最坏时间复杂度 `O(n²)`，空间复杂度 `O(1)`（或者 `O(k)`，k ui s 中各不相同的字符个数）。

## Code

{% asset_code coding/3138-minimum-length-of-anagram-concatenation/solution.py %}
