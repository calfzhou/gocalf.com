---
title: 424. Longest Repeating Character Replacement
notebook: coding
tags:
- medium
date: 2024-11-16 20:04:14
updated: 2024-11-16 20:04:14
---
## Problem

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return _the length of the longest substring containing the same letter you can get after performing the above operations_.

<https://leetcode.com/problems/longest-repeating-character-replacement/>

**Example 1:**

> Input: `s = "ABAB", k = 2`
> Output: `4`
> Explanation: Replace the two `'A'`s with two `'B'`s or vice versa.

**Example 2:**

> Input: `s = "AABABBA", k = 1`
> Output: `4`
> Explanation: Replace the one `'A'` in the middle with `'B'` and form `"AABBBBA"`.
> The substring `"BBBB"` has the longest repeating letters, which is 4.
> There may exists other ways to achieve this answer too.

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Test Cases

``` python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
```

{% asset_code coding/assets/424-longest-repeating-character-replacement/solution_test.py %}

## Thoughts

先考虑某一个字母，比如 'A'。最多把 k 个其他字母改成 'A'，看能得到的最长的连续 'A' 有多长。

设当前的子串 `s[i:j]` 是连续的 'A'，且其中有 `r` 个 'A' 是从其他字母换过来的（`0 <= i < j <= n`，`0 <= r <= k`）。

如果 `s[j]` 是 'A'，或者还有替换次数尚未用完，则可以右移 `j`（并更新 `k` 的使用次数）。

否则根据 `s[i]` 释放 `k` 的使用次数，并向右移动 `i`。

设各不相同的字母总数是 `C`，那么时间复杂度是 `O(C * n)`，空间复杂度是 `O(C)`。

PS：之前用这种滑窗法的时候，写循环的时候总是被边界条件搞得头疼。主要是在想思路的时候，往往会让区间的一头直接移动到最远，然后再移动另一头。但如果按这个方式写代码，就会引入嵌套的循环，增加更多的边界条件判定，代码看着也复杂。实际上代码里应该就一个循环，每次循环只移动一步。比如即使区间的右边界可以连续移动五步，也不要在主循环体内直接让它移动五步，而是要正常地循环五次，每次都移动一步。

## Code

{% asset_code coding/assets/424-longest-repeating-character-replacement/solution.py %}

> 似乎不是很快，先这样吧。
