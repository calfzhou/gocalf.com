---
title: 242. Valid Anagram
notebook: coding
tags:
- easy
date: 2024-11-25 13:42:37
updated: 2024-11-25 13:42:37
---
## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

> An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

<https://leetcode.com/problems/valid-anagram/>

**Example 1:**

> Input: `s = "anagram", t = "nagaram"`
> Output: `true`

**Example 2:**

> Input: `s = "rat", t = "car"`
> Output: `false`

**Constraints:**

- `1 <= s.length, t.length <= 5 * 10⁴`
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Test Cases

``` python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
```

{% asset_code coding/assets/242-valid-anagram/solution_test.py %}

## Thoughts

题目限定了只有小写英文字母，可以用大小为 26 的数组记录每个字母出现的次数。

如果可以包含任意 Unicode 字符，那么用哈希表记录每个字符的次数。

## Code

{% asset_code coding/assets/242-valid-anagram/solution.py %}
