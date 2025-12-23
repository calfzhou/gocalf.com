---
title: 680. Valid Palindrome II
notebook: coding
tags:
- easy
date: 2025-02-03 11:01:26
updated: 2025-02-03 11:01:26
---
## Problem

Given a string `s`, return `true` _if the_ `s` _can be palindrome after deleting **at most one** character from it_.

<https://leetcode.cn/problems/valid-palindrome-ii/>

**Example 1:**

> Input: `s = "aba"`
> Output: `true`

**Example 2:**

> Input: `s = "abca"`
> Output: `true`
> Explanation: You could delete the character `'c'`.

**Example 3:**

> Input: `s = "abc"`
> Output: `false`

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters.

## Test Cases

``` python
class Solution:
    def validPalindrome(self, s: str) -> bool:
```

{% asset_code coding/assets/680-valid-palindrome-ii/solution_test.py %}

## Thoughts

[125. Valid Palindrome](../125-valid-palindrome/index.md) 的进阶版，这次允许删除最多一个字符（同时去掉了大小写转换和特殊字符的处理）。

依然从两头向中间扫描。当扫描过程中遇到 `s[i] ≠ s[j]` 的情况，要么删除位置 i 的字符，要么删除位置 j 的字符。即检查 `s[i+1...j]` 或 `s[i...j+1]` 是否是回文，如果都不是，则结果为 false。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/680-valid-palindrome-ii/solution.py %}
