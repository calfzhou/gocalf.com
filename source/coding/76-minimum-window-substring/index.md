---
title: 76. Minimum Window Substring
notebook: coding
tags:
- hard
date: 2024-11-21 16:39:53
updated: 2024-11-21 16:39:53
---
## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return _the **minimum window substring** of_ `s` _such that every character in_ `t` _(**including duplicates**) is included in the window_. If there is no such substring, return _the empty string_ `""`.

> A **substring** is a contiguous **non-empty** sequence of characters within a string.

The testcases will be generated such that the answer is **unique**.

<https://leetcode.com/problems/minimum-window-substring/>

**Example 1:**

> Input: `s = "ADOBECODEBANC", t = "ABC"`
> Output: `"BANC"`
> Explanation: The minimum window substring `"BANC"` includes 'A', 'B', and 'C' from string t.

**Example 2:**

> Input: `s = "a", t = "a"`
> Output: `"a"`
> Explanation: The entire string s is the minimum window.

**Example 3:**

> Input: `s = "a", t = "aa"`
> Output: `""`
> Explanation: Both 'a's from t must be included in the window.
> Since the largest window of s only has one 'a', return empty string.

**Constraints:**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10⁵`
- `s` and `t` consist of uppercase and lowercase English letters.

## Test Cases

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
```

{% snippet solution_test.py %}

## Thoughts

设当前窗口的左右边界分别是 i 和 j，如果当前子串已经包含 `t` 中所有字符则右移 i，否则右移 j。

事先统计出 `t` 中出现的所有字符及数量，在移动 i、j 的时候同步更新子串中的字符种类及数量。

设 `t` 中有 `k` 种不同的字符，则时间复杂度是 `O(n+km)`，空间复杂度 `O(k)`。

当 `k` 比较大时，每移动一次 i 或 j 都比一次窗口内各种字符的数量与 `t` 是否一致就比较浪费，比如移入或移出的字符并不在 `t` 内，或者移出了一个数量已经超出需求很多的字符，或者移入了一个需要的字符但还有很多其他也需要的字符。要把每次移动 i 或 j 时的处理时间降到 `O(1)`。

可以再维护一个字符的集合，表示窗口内缺少的字符。在移动 i、j 并更新窗口内字符数量时，直接判定当前字符是否还需要，并相应地加入或移出集合，这样每次判定就只需要常数时间。

如果控制好字符加入和移出集合的时机，确保不会重复加入和移出不存在的字符，那就不需要真的放一个集合，只需要记录还缺少的字符数量，可以省掉集合的存储空间和相关操作的时长。

整体的时间复杂度是 `O(n+m)`，空间复杂度 `O(k)`。

## Code

> 👇 单一循环体

{% snippet solution.py %}

> 👇 循环套循环

{% snippet solution2.py %}
