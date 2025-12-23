---
title: 2381. Shifting Letters II
notebook: coding
tags:
- medium
date: 2025-01-05 16:31:35
updated: 2025-01-05 16:31:35
---
## Problem

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [startᵢ, endᵢ, directionᵢ]`. For every `i`, **shift** the characters in `s` from the index `startᵢ` to the index `endᵢ` (**inclusive**) forward if `directionᵢ = 1`, or shift the characters backward if `directionᵢ = 0`.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return _the final string after all such shifts to_ `s` _are applied_.

<https://leetcode.com/problems/shifting-letters-ii/>

**Example 1:**

> Input: `s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]`
> Output: `"ace"`
> Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now `s = "zac"`.
> Secondly, shift the characters from index 1 to index 2 forward. Now `s = "zbd"`.
> Finally, shift the characters from index 0 to index 2 forward. Now `s = "ace"`.

**Example 2:**

> Input: `s = "dztz", shifts = [[0,0,0],[1,1,1]]`
> Output: `"catz"`
> Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now `s = "cztz"`.
> Finally, shift the characters from index 1 to index 1 forward. Now `s = "catz"`.

**Constraints:**

- `1 <= s.length, shifts.length <= 5 * 10⁴`
- `shifts[i].length == 3`
- `0 <= startᵢ <= endᵢ < s.length`
- `0 <= directionᵢ <= 1`
- `s` consists of lowercase English letters.

## Test Cases

``` python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
```

{% asset_code coding/assets/2381-shifting-letters-ii/solution_test.py %}

## Thoughts

[848. Shifting Letters](848-shifting-letters) 的进阶版。

一个 `[startᵢ, endᵢ, directionᵢ]`，是对 `s[startᵢ:endᵢ+1]` 的每个字符往 `directionᵢ` 方向 shift，也可以看作是先对 `s[startᵢ:]` 每个字符按 `directionᵢ` 方向 shift 一次，再对 `s[endᵢ+1:]` 每个字符反方向 shift 一次。这样把 `startᵢ` 和 `endᵢ` 解耦，跟 [848. Shifting Letters](848-shifting-letters) 就几乎一模一样了。

用数组记录每个位置，从其开始的每个字符要往哪个方向 shift 多少次（用正数表示 forward，负数表示 backward）。从 `i = 0` 开始遍历 s，同时累计需要 shift 的最终次数，对当前字符执行 shift，结果再拼成新的字符串即可。

时间复杂度 `O(m + n)`，空间复杂度 `O(m + n)`，其中 m、n 分别是 shifts 和 s 的长度。

## Code

{% asset_code coding/assets/2381-shifting-letters-ii/solution.py %}
