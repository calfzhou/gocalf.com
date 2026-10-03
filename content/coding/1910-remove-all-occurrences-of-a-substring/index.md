---
title: 1910. Remove All Occurrences of a Substring
notebook: coding
tags:
- medium
date: 2025-02-11 09:30:46
updated: 2025-02-11 09:30:46
---
## Problem

Given two strings `s` and `part`, perform the following operation on `s` until **all** occurrences of the substring `part` are removed:

- Find the **leftmost** occurrence of the substring `part` and **remove** it from `s`.

Return `s` _after removing all occurrences of_ `part`.

A **substring** is a contiguous sequence of characters in a string.

<https://leetcode.com/problems/remove-all-occurrences-of-a-substring/>

**Example 1:**

> Input: `s = "daabcbaabcbc", part = "abc"`
> Output: `"dab"`
> Explanation: The following operations are done:
>
> - `s = "da`{% u abc %}`baabcbc"`, remove `"abc"` starting at index 2, so `s = "dabaabcbc"`.
> - `s = "daba`{% u abc %}`bc"`, remove `"abc"` starting at index 4, so `s = "dababc"`.
> - `s = "dab`{% u abc %}`"`, remove `"abc"` starting at index 3, so `s = "dab"`.
>
> Now s has no occurrences of `"abc".`

**Example 2:**

> Input: `s = "axxxxyyyyb", part = "xy"`
> Output: `"ab"`
> Explanation: The following operations are done:
>
> - `s = "axxx`{% u xy %}`yyyb"`, remove `"xy"` starting at index 4 so `s = "axxxyyyb"`.
> - `s = "axx`{% u xy %}`yyb"`, remove `"xy"` starting at index 3 so `s = "axxyyb"`.
> - `s = "ax`{% u xy %}`yb"`, remove `"xy"` starting at index 2 so `s = "axyb"`.
> - `s = "a`{% u xy %}`b"`, remove `"xy"` starting at index 1 so `s = "ab"`.
>
> Now s has no occurrences of `"xy"`.

**Constraints:**

- `1 <= s.length <= 1000`
- `1 <= part.length <= 1000`
- `s`​​​​​​ and `part` consists of lowercase English letters.

## Test Cases

```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
```

{% snippet solution_test.py %}

## Thoughts

可以看作是 [3174. Clear Digits](../3174-clear-digits/index.md) 的进阶版，待匹配的 pattern 从两个字符（一个字母+一个数字）变成任意长度的字符串。

处理方法也类似，用一个栈记录结果字符串的字符。遍历 s，对于每个字符，先入栈，然后对比栈顶 m 个字符是否与 part 一致（设 part 的长度为 m），一致就把这些字符都弹出。

时间复杂度 `O(n * m)`，空间复杂度 `O(n)`。

## Code

{% snippet solution.py %}
