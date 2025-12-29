---
title: 767. Reorganize String
notebook: coding
tags:
- medium
katex: true
date: 2025-01-01 22:39:40
updated: 2025-01-01 22:39:40
---
## Problem

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return _any possible rearrangement of_ `s` _or return_ `""` _if not possible_.

<https://leetcode.com/problems/reorganize-string/>

**Example 1:**

> Input: `s = "aab"`
> Output: `"aba"`

**Example 2:**

> Input: `s = "aaab"`
> Output: `""`

**Constraints:**

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Test Cases

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
```

{% asset_code coding/767-reorganize-string/solution_test.py %}

## Thoughts

判定是否可行很简单，显然如果有一个字符的出现次数大于 $\lceil n/2\rceil$ 就不可行，否则可行。

开始以为重新排列 s 的逻辑类似于 [2182. Construct String With Repeat Limit](../2182-construct-string-with-repeat-limit/index.md)，相当于 `repeatLimit = 1`，且不限定字符的顺序。但是因为要求是用掉所有的字符（当可行的时候），重建的逻辑就还是会有些不同。[Problem 2182](../2182-construct-string-with-repeat-limit/index.md) 中因为要让结果字符串按字典序最大，每次都先取最大的字符，却并不保证所有字符都能用上。

本题需要把所有的字符都用上，可以考虑建一个词频的最大堆（词频相同时按字符的字典序），每次从堆中取出词频最大的两个字符，添加到结果字符串末尾。把两个字符以及剩余的词频（如果还大于零）放回到堆中。因为词频相同的字符会按字典序排序，本次取出的第二个字符一定不会跟下一次取出的第一个字符相同，不会产生连续重复字符。

最后如果堆里只剩下一个字符（显然剩余的词频只能是 1），将其加到结果字符串的末尾即可。

时间复杂度 `O(n log C)`，空间复杂度 `O(C)`，其中 C 是 s 中各不相同的字符总数，题目中 `C ≤ 26` 可以认为是常数。

## Code

{% asset_code coding/767-reorganize-string/solution.py %}
