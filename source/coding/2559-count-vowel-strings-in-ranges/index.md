---
title: 2559. Count Vowel Strings in Ranges
notebook: coding
tags:
- medium
date: 2025-01-02 10:12:27
updated: 2025-01-02 10:12:27
---
## Problem

You are given a **0-indexed** array of strings `words` and a 2D array of integers `queries`.

Each query `queries[i] = [lᵢ, rᵢ]` asks us to find the number of strings present in the range `lᵢ` to `rᵢ` (both **inclusive**) of `words` that start and end with a vowel.

Return _an array_ `ans` _of size_ `queries.length`_, where_ `ans[i]` _is the answer to the_ `i`ᵗʰ _query_.

**Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

<https://leetcode.com/problems/count-vowel-strings-in-ranges/>

**Example 1:**

> Input: `words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]`
> Output: `[2,3,0]`
> Explanation: The strings starting and ending with a vowel are `"aba"`, `"ece"`, `"aa"` and `"e"`.
> The answer to the query `[0,2]` is 2 (strings `"aba"` and `"ece"`).
> to query `[1,4]` is 3 (strings `"ece"`, `"aa"`, `"e"`).
> to query `[1,1]` is 0.
> We return `[2,3,0]`.

**Example 2:**

> Input: `words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]`
> Output: `[3,2,1]`
> Explanation: Every string satisfies the conditions, so we return `[3,2,1]`.

**Constraints:**

- `1 <= words.length <= 10⁵`
- `1 <= words[i].length <= 40`
- `words[i]` consists only of lowercase English letters.
- `sum(words[i].length) <= 3 * 10⁵`
- `1 <= queries.length <= 10⁵`
- `0 <= lᵢ <= rᵢ < words.length`

## Test Cases

``` python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
```

{% asset_code coding/assets/2559-count-vowel-strings-in-ranges/solution_test.py %}

## Thoughts

先扫描一次 words，定义 `dp(i)`（`0 ≤ i < n`）表示 `words[:i+1]` 中，首尾字母是元音的单词个数。显然如果 `words[i]` 首尾字母是元音，则 `dp(i) = dp(i - 1) + 1`，否则 `dp(i) = dp(i - 1)`。初值 `dp(0)` 根据 `words[0]` 首尾字母是否是元音来确定。

这样对于任何一个 `query = (l, r)`，看 words 在区间 `[l, r]` 内首尾字母是元音的单词个数，根据上边定义的 dp 易知结果为 `dp(r) - dp(l - 1)`（如果 `l = 0` 则为 `dp(r)`）。

时间复杂度 `O(n + m)`，空间复杂度 `O(n)`，其中 n、m 分别是 words 和 queries 的长度。

实践中可以给 dp 数组最左边增加一个 0，简化边界处理。

## Code

{% asset_code coding/assets/2559-count-vowel-strings-in-ranges/solution.py %}
