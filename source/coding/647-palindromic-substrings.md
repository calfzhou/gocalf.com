---
title: 647. Palindromic Substrings
notebook: coding
tags:
- medium
date: 2024-11-10 17:25:53
updated: 2024-11-10 17:25:53
---
## Problem

Given a string `s`, return _the number of **palindromic substrings** in it_.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

<https://leetcode.com/problems/palindromic-substrings/description/>

**Example 1:**

> Input: `s = "abc"`
> Output: 3
> Explanation: Three palindromic strings: "a", "b", "c".

**Example 2:**

> Input: `s = "aaa"`
> Output: 6
> Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Test Cases

{% asset_code coding/647-palindromic-substrings/solution_test.py %}

## Thoughts

这个跟 [5. Longest Palindromic Substring](/coding/5-longest-palindromic-substring) 的处理逻辑几乎一致。

区别就是那个问题只记录最长的回文长度，而这个问题需要记录见到的所有回文的数量。

同样是从左到右遍历每个字符，对于当前字符，检查以其为中心能够构成的 palindromic 数量。

计数的时候注意，一个回文去掉首尾字符后的子回文也算一个。

## Code

{% asset_code coding/647-palindromic-substrings/solution.py %}
