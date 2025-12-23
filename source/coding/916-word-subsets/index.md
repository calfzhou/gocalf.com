---
title: 916. Word Subsets
notebook: coding
tags:
- medium
date: 2025-01-10 09:52:50
updated: 2025-01-10 09:52:50
---
## Problem

You are given two string arrays `words1` and `words2`.

A string `b` is a **subset** of string `a` if every letter in `b` occurs in `a` including multiplicity.

- For example, `"wrr"` is a subset of `"warrior"` but is not a subset of `"world"`.

A string `a` from `words1` is **universal** if for every string `b` in `words2`, `b` is a subset of `a`.

Return an array of all the **universal** strings in `words1`. You may return the answer in **any order**.

<https://leetcode.com/problems/word-subsets/>

**Example 1:**

> Input: `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]`
> Output: `["facebook","google","leetcode"]`

**Example 2:**

> Input: `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]`
> Output: `["apple","google","leetcode"]`

**Constraints:**

- `1 <= words1.length, words2.length <= 10⁴`
- `1 <= words1[i].length, words2[i].length <= 10`
- `words1[i]` and `words2[i]` consist only of lowercase English letters.
- All the strings of `words1` are **unique**.

## Test Cases

``` python
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
```

{% asset_code coding/916-word-subsets/solution_test.py %}

## Thoughts

因为 universal word 能够包含 words2 中的所有单词，可以先汇总 words2 所有单词的信息。

对于 words2 中的每个单词，统计其中每个字符的出现次数。然后把每个单词的字符次数合并，对于任何一个字符，取最大的出现次数（相当于 Python [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) 的 `union` 操作（`operator |`）。

然后遍历 words1 的每一个单词，看是否包含汇总之后的所有字符的次数。

时间复杂度 `O(m + n)`，额外的空间复杂度 `O(1)`。

## Code

{% asset_code coding/916-word-subsets/solution.py %}

用 [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) 会慢一些：

{% asset_code coding/916-word-subsets/solution2.py %}
