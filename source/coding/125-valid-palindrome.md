---
title: 125. Valid Palindrome
notebook: coding
tags:
- easy
date: 2024-11-26 11:10:30
updated: 2024-11-26 11:10:30
---
## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` _if it is a **palindrome**, or_ `false` _otherwise_.

<https://leetcode.com/problems/valid-palindrome/>

**Example 1:**

> Input: `s = "A man, a plan, a canal: Panama"`
> Output: `true`
> Explanation: `"amanaplanacanalpanama"` is a palindrome.

**Example 2:**

> Input: `s = "race a car"`
> Output: `false`
> Explanation: `"raceacar"` is not a palindrome.

**Example 3:**

> Input: `s = " "`
> Output: `true`
> Explanation: s is an empty string `""` after removing non-alphanumeric characters.
> Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:**

- `1 <= s.length <= 2 * 10⁵`
- `s` consists only of printable ASCII characters.

## Test Cases

``` python
class Solution:
    def isPalindrome(self, s: str) -> bool:
```

{% asset_code coding/125-valid-palindrome/solution_test.py %}

## Thoughts

从两头向中间扫描，跳过非字母数字。

## Code

{% asset_code coding/125-valid-palindrome/solution.py %}
