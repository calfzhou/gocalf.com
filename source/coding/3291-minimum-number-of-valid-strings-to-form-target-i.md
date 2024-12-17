---
title: 3291. Minimum Number of Valid Strings to Form Target I
notebook: coding
tags:
- medium
- hard
- todo
katex: true
date: 2024-12-17 16:11:08
updated: 2024-12-17 16:11:08
---
## Problem

You are given an array of strings `words` and a string `target`.

A string `x` is called **valid** if `x` is a prefix of **any** string in `words`.

> A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.

Return the **minimum** number of **valid** strings that can be _concatenated_ to form `target`. If it is **not** possible to form `target`, return `-1`.

<https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/>

**Example 1:**

> Input: `words = ["abc","aaaaa","bcdef"], target = "aabcdabc"`
> Output: `3`
> Explanation:
> The target string can be formed by concatenating:
>
> - Prefix of length 2 of `words[1]`, i.e. `"aa"`.
> - Prefix of length 3 of `words[2]`, i.e. `"bcd"`.
> - Prefix of length 3 of `words[0]`, i.e. `"abc"`.

**Example 2:**

> Input: `words = ["abababab","ab"], target = "ababaababa"`
> Output: `2`
> Explanation:
> The target string can be formed by concatenating:
>
> - Prefix of length 5 of `words[0]`, i.e. `"ababa"`.
> - Prefix of length 5 of `words[0]`, i.e. `"ababa"`.

**Example 3:**

> Input: `words = ["abcdef"], target = "xyz"`
> Output: `-1`

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 5 * 10³`
- The input is generated such that `sum(words[i].length) <= 10⁵`.
- `words[i]` consists only of lowercase English letters.
- `1 <= target.length <= 5 * 10³`
- `target` consists only of lowercase English letters.

## Test Cases

``` python
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
```

{% asset_code coding/3291-minimum-number-of-valid-strings-to-form-target-i/solution_test.py %}

## Thoughts

直观的想法是看以位置 i 开头的子字符串 `target[i:]`，从位置 i 开始最长能够在 `words` 中匹配到的长度（记为 `plenᵢ`），可以取任意 `1 ≤ p ≤ plenᵢ` 将 `target[i:]` 分为两段，即 `target[i:i+p]` 和 `target[i+p:]`，前半段是一个 `words` 的前缀，递归处理后半段子问题即可。

记 `dp(i)` 表示可以拼接出 `target[i:]` 的最小 valid 字符串个数，那么有：

$$
dp(i)=1+\min_{1\le p\le plen_i}dp(i+p)
$$

考虑到边界和递推，如果 `dp(i)` 是 0，直接记为 -1。另外记初值 `dp(n) = 0`。

最后的结果取 `dp(0)`。

用 `words` 构建前缀树（参见 [208. Implement Trie (Prefix Tree)](208-implement-trie-prefix-tree)、[139. Word Break](139-word-break#Improve)），定义一个 `match` 方法在前缀树中找到能匹配指定字符串的最长前缀，其长度即为 `plenᵢ`。

时间复杂度 `O(k m + n²)`，其中 k 是 `words` 中单词的平均长度，m 是 `words` 的长度，n 是 `target` 的长度。空间复杂度 `O(k m + n)`。

比较慢。

## Code

{% asset_code coding/3291-minimum-number-of-valid-strings-to-form-target-i/solution.py %}

## Faster - AC 自动机

TODO
