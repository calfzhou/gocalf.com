---
title: 1408. String Matching in an Array
notebook: coding
tags:
- easy
date: 2025-01-07 09:47:38
updated: 2025-01-07 09:47:38
---
## Problem

Given an array of string `words`, return _all strings in_ `words` _that is a **substring** of another word_. You can return the answer in **any order**.

A **substring** is a contiguous sequence of characters within a string.

<https://leetcode.com/problems/string-matching-in-an-array/>

**Example 1:**

> Input: `words = ["mass","as","hero","superhero"]`
> Output: `["as","hero"]`
> Explanation: `"as"` is substring of `"mass"` and `"hero"` is substring of `"superhero"`.
> `["hero","as"]` is also a valid answer.

**Example 2:**

> Input: `words = ["leetcode","et","code"]`
> Output: `["et","code"]`
> Explanation: `"et"`, `"code"` are substring of `"leetcode"`.

**Example 3:**

> Input: `words = ["blue","green","bu"]`
> Output: `[]`
> Explanation: No string of words is substring of another string.

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 30`
- `words[i]` contains only lowercase English letters.
- All the strings of `words` are **unique**.

## Test Cases

```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
```

{% asset_code solution_test.py %}

## Thoughts

先对 words 按单词长度排序，可以减少后续的循环次数，并能很好地避免重复输出。

用两重循环比较任意两个字符串，看较长的是否包含较短的。

时间复杂度 `O(n²)`，额外的空间复杂度 `O(1)`。

## Code

{% asset_code solution.py %}
