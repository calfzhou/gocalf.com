---
title: 3291. Minimum Number of Valid Strings to Form Target I
notebook: coding
tags:
- medium
- hard
katex: true
date: 2024-12-17 16:11:08
updated: 2024-12-18 16:23:05
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

在 [3213. Construct String with Minimum Cost](3213-construct-string-with-minimum-cost) 中实现了 AC 自动机，利用 AC 自动机，可以用平均 `O(km + n)` 时间找出 target 中所有能匹配到的单词。

但这里只是需要有前缀，可以不是完全匹配，需要稍微修改一下 [problem 3213](3213-construct-string-with-minimum-cost) 中 AC 自动机的 match 方法。match 方法在匹配路径的终点返回构造时记录的所有单词，从而得到所有匹配到的单词。实际上即使没到终点，路径上的任何一个位置，都是一个前缀。所以把路径上的位置都输出即可。新的方法命名为 prefix。

仿照 [problem 3213](3213-construct-string-with-minimum-cost) 中正向的动态规划 `dp'`，重新定义本题的 dp：`dp(i)` 表示可以拼接出子字符串 `target[:i]` 的最小前缀个数，定义 `dp(0) = 0`，其他值均初始化为 ∞，最终所求结果为 `dp(n)`。

令 i 从 0 递增到 `n - 1`。对于当前的 i，如果 `dp(i) = ∞`，说明 `target[:i]` 无法由前缀拼接而成，跳过。否则看从位置 i 开始可以匹配到哪些前缀，比如 `target[i:j]` 是一个前缀，那么 `dp(j) = min{dp(j), dp(i) + 1}`。

注意到对于 `0 ≤ i < k < j < n`，如果 `target[i:k]` 和 `target[i:j]` 都是前缀，那么即使 `target[k:j]` 是前缀也不需要考虑，因为把 `target[k:j]` 与左边的 `target[i:k]` 拼成一个新的前缀，所用的前缀数量更少。而上边基于 AC 自动机 match 方法改造出来的前缀搜索方法 prefix，刚好不会输出 `target[k:j]`（这么巧吗？）。

时间复杂度 `O(km + n)`，空间复杂度 `O(km + n)`。

{% asset_code coding/3291-minimum-number-of-valid-strings-to-form-target-i/solution_ac.py %}

附：针对 AC 自动机的构建和多模式前缀搜索的 test cases：

{% asset_code coding/3291-minimum-number-of-valid-strings-to-form-target-i/solution_ac_test.py %}
