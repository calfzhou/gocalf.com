---
title: 1374. Generate a String With Characters That Have Odd Counts
notebook: coding
tags:
- easy
date: 2025-01-03 10:37:05
updated: 2025-01-03 10:37:05
---
## Problem

Given an integer `n`, _return a string with `n` characters such that each character in such string occurs **an odd number of times**_.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return **any** of them.

<https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/>

**Example 1:**

> Input: `n = 4`
> Output: `"pppz"`
> Explanation: `"pppz"` is a valid string since the character `'p'` occurs three times and the character `'z'` occurs once. Note that there are many other valid strings such as `"ohhh"` and `"love"`.

**Example 2:**

> Input: `n = 2`
> Output: `"xy"`
> Explanation: `"xy"` is a valid string since the characters `'x'` and `'y'` occur once. Note that there are many other valid strings such as `"ag"` and `"ur"`.

**Example 3:**

> Input: `n = 7`
> Output: `"holasss"`

**Constraints:**

- `1 <= n <= 500`

## Test Cases

```python
class Solution:
    def generateTheString(self, n: int) -> str:
```

{% asset_code coding/1347-generate-a-string-with-characters-that-have-odd-counts/solution_test.py %}

## Thoughts

如果 n 是奇数，直接用 n 个任意字母（如 `'a'`）拼成字符串。否则可以用 `n - 1` 个任意字母（如 `'a'`）再加任意另外一个字母（如 `'b'`）即可。

## Code

{% asset_code coding/1347-generate-a-string-with-characters-that-have-odd-counts/solution.py %}
