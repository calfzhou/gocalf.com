---
title: 3. Longest Substring Without Repeating Characters
notebook: coding
tags:
- medium
date: 2024-11-10 01:06:36
updated: 2024-11-10 01:06:36
---
## Problem

Given a string `s`, find the length of the **longest substring** without repeating characters.

> A **substring** is a contiguous **non-empty** sequence of characters within a string.

<https://leetcode.com/problems/longest-substring-without-repeating-characters/>

**Example 1:**

> Input: `s = "abcabcbb"`
> Output: `3`
> Explanation: The answer is "abc", with the length of 3.

**Example 2:**

> Input: `s = "bbbbb"`
> Output: `1`
> Explanation: The answer is "b", with the length of 1.

**Example 3:**

> Input: `s = "pwwkew"`
> Output: `3`
> Explanation: The answer is "wke", with the length of 3.
> Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**

- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols and spaces.

## Test Cases

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

从第一个字符开始，这时候 substring 长度为 1。

设当前的 substring 范围是 `[i, j]`。把范围向右扩大到 `[i, j+1]`，要检查是否包含 repeating chars 并做出调整。

从 i 到 j 逐个与 j+1 位置的字符比较，假设 `s[k] == s[j+1]`，则把范围缩小为 `[k+1, j+1]`。

用一个变量记录见到过的最长的 substring 长度。

假设所求的 longest substring 长度为 m，时间复杂度为 `O(m*n)`，空间复杂度 `O(1)`。

## Code

{% asset_code solution.py %}

## 快一些

如果用哈希表动态地记录当前 substring 中的字符（key 是字符，value 是位置下标），则时间复杂度为 `O(n)`（基本上每个字符都会入栈一次，出栈一次），空间复杂度为 `O(m)`。

{% asset_code solution2.py %}
