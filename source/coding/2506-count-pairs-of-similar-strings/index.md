---
title: 2506. Count Pairs Of Similar Strings
notebook: coding
tags:
- easy
date: 2025-02-22 09:31:29
updated: 2025-02-22 09:31:29
---
## Problem

You are given a **0-indexed** string array `words`.

Two strings are **similar** if they consist of the same characters.

- For example, `"abca"` and `"cba"` are similar since both consist of characters `'a'`, `'b'`, and `'c'`.
- However, `"abacba"` and `"bcfd"` are not similar since they do not consist of the same characters.

Return _the number of pairs_ `(i, j)` _such that_ `0 <= i < j <= word.length - 1` _and the two strings_ `words[i]` _and_ `words[j]` _are similar_.

<https://leetcode.cn/problems/count-pairs-of-similar-strings/>

**Example 1:**

> Input: `words = ["aba","aabb","abcd","bac","aabc"]`
> Output: `2`
> Explanation: There are 2 pairs that satisfy the conditions:
>
> - `i = 0` and `j = 1` : both `words[0]` and `words[1]` only consist of characters `'a'` and `'b'`.
> - `i = 3` and `j = 4` : both `words[3]` and `words[4]` only consist of characters `'a'`, `'b'`, and `'c'`.

**Example 2:**

> Input: `words = ["aabb","ab","ba"]`
> Output: `3`
> Explanation: There are 3 pairs that satisfy the conditions:
>
> - `i = 0` and `j = 1` : both `words[0]` and `words[1]` only consist of characters `'a'` and `'b'`.
> - `i = 0` and `j = 2` : both `words[0]` and `words[2]` only consist of characters `'a'` and `'b'`.
> - `i = 1` and `j = 2` : both `words[1]` and `words[2]` only consist of characters `'a'` and `'b'`.

**Example 3:**

> Input: `words = ["nba","cba","dba"]`
> Output: `0`
> Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consist of only lowercase English letters.

## Test Cases

```python
class Solution:
    def similarPairs(self, words: List[str]) -> int:
```

{% asset_code coding/2506-count-pairs-of-similar-strings/solution_test.py %}

## Thoughts

对 words 中的单词按照每个单词的构成字符分组，具有相同构成字符的单词放到同一组。设这一组有 m 个单词，那么这一组单词对结果的贡献值为 `m * (m - 1) / 2`。

分组的时候用字典，value 只需要记录该组内单词的个数，key 可以有多种选择，比如通过 hash set 得到单词中各不相同的所有字符，然后排序，用元组或者拼成字符串；Python 中还可以直接用 [frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset)。字典的 key 必需用不可变的值（immutable）。

时间复杂度 `O(n * W)`，空间复杂度 `O(n)`，其中 W 是单词的长度。

## Code

{% asset_code coding/2506-count-pairs-of-similar-strings/solution.py %}
