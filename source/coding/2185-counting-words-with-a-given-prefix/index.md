---
title: 2185. Counting Words With a Given Prefix
notebook: coding
tags:
- easy
date: 2025-01-09 10:31:41
updated: 2025-01-09 10:31:41
---
## Problem

You are given an array of strings `words` and a string `pref`.

Return _the number of strings in_ `words` _that contain_ `pref` _as a **prefix**_.

A **prefix** of a string `s` is any leading contiguous substring of `s`.

<https://leetcode.com/problems/counting-words-with-a-given-prefix/>

**Example 1:**

> Input: `words = ["pay","attention","practice","attend"], pref = "at"`
> Output: `2`
> Explanation: The 2 strings that contain `"at"` as a prefix are: `"attention"` and `"attend"`.

**Example 2:**

> Input: `words = ["leetcode","win","loops","success"], pref = "code"`
> Output: `0`
> Explanation: There are no strings that contain `"code"` as a prefix.

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length, pref.length <= 100`
- `words[i]` and `pref` consist of lowercase English letters.

## Test Cases

```python
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

## Code

{% asset_code solution.py %}
