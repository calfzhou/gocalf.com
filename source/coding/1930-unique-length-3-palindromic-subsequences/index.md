---
title: 1930. Unique Length-3 Palindromic Subsequences
notebook: coding
tags:
- medium
date: 2025-01-04 10:40:47
updated: 2025-01-04 10:40:47
---
## Problem

Given a string `s`, return _the number of **unique palindromes of length three** that are a **subsequence** of_ `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

<https://leetcode.com/problems/unique-length-3-palindromic-subsequences/>

**Example 1:**

> Input: `s = "aabca"`
> Output: `3`
> Explanation: The 3 palindromic subsequences of length 3 are:
>
> - `"aba"` (subsequence of `"aabca"`)
> - `"aaa"` (subsequence of `"aabca"`)
> - `"aca"` (subsequence of `"aabca"`)

**Example 2:**

> Input: `s = "adc"`
> Output: `0`
> Explanation: There are no palindromic subsequences of length 3 in `"adc"`.

**Example 3:**

> Input: `s = "bbcbaba"`
> Output: `4`
> Explanation: The 4 palindromic subsequences of length 3 are:
>
> - `"bbb"` (subsequence of `"bbcbaba"`)
> - `"bcb"` (subsequence of `"bbcbaba"`)
> - `"bab"` (subsequence of `"bbcbaba"`)
> - `"aba"` (subsequence of `"bbcbaba"`)

**Constraints:**

- `3 <= s.length <= 10⁵`
- `s` consists of only lowercase English letters.

## Test Cases

``` python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
```

{% asset_code coding/assets/1930-unique-length-3-palindromic-subsequences/solution_test.py %}

## Thoughts

相当于 [730. Count Different Palindromic Subsequences](730-count-different-palindromic-subsequences) 的极简版。

先确定首尾字符，必须是相同的字符，然后看它们之间一共有多少个各不相同的字符。

先遍历一遍数组，记录 s 中一共有哪些字符，同时记录每个字符最左和最右的所在位置。

不妨设字符 c 在 s 中最左和最右的下标分别为 l 和 r，只要看 `s[l+1:r]` 包含多少个各不相同的字符（可以有 c），每一个都可以跟一对 c 组成一个长度为 3 的回文。累加每个字符能构成的回文数量即可。

时间复杂度 `O(C * n)`，空间复杂度 `O(C)`，其中 C 是 s 中各不相同的字符数，不超过 26，可以认为是常数。

想到另外一个办法是像 [2559. Count Vowel Strings in Ranges](2559-count-vowel-strings-in-ranges) 一样，事先记录每个字符在子字符串 `s[:i+1]` 中的个数，这样对于指定的 l 和 r，可以用常数时间判断 `s[l+1:r]` 中是否包含某个字符。不过前期的准备工作同样需要 `O(C * n)` 时间，平均系数还更大一些，而且还要用 `O(C * n)` 空间，没什么必要了。

## Code

{% asset_code coding/assets/1930-unique-length-3-palindromic-subsequences/solution.py %}
