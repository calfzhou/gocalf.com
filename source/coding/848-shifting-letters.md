---
title: 848. Shifting Letters
notebook: coding
tags:
- medium
date: 2025-01-05 10:55:45
updated: 2025-01-05 10:55:45
---
## Problem

You are given a string `s` of lowercase English letters and an integer array `shifts` of the same length.

Call the `shift()` of a letter, the next letter in the alphabet, (wrapping around so that `'z'` becomes `'a'`).

- For example, `shift('a') = 'b'`, `shift('t') = 'u'`, and `shift('z') = 'a'`.

Now for each `shifts[i] = x`, we want to shift the first `i + 1` letters of `s`, `x` times.

Return _the final string after all such shifts to s are applied_.

<https://leetcode.com/problems/shifting-letters/>

**Example 1:**

> Input: `s = "abc", shifts = [3,5,9]`
> Output: `"rpl"`
> Explanation: We start with `"abc".`
> After shifting the first 1 letters of s by 3, we have `"dbc"`.
> After shifting the first 2 letters of s by 5, we have `"igc"`.
> After shifting the first 3 letters of s by 9, we have `"rpl"`, the answer.

**Example 2:**

> Input: `s = "aaa", shifts = [1,2,3]`
> Output: `"gfd"`

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters.
- `shifts.length == s.length`
- `0 <= shifts[i] <= 10⁹`

## Test Cases

``` python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
```

{% asset_code coding/848-shifting-letters/solution_test.py %}

## Thoughts

第 i 个字符一共需要 shift `Σshifts[:i+1]` 次。先逆序遍历一遍 shifts，逐个向前累加即可。

## Code

{% asset_code coding/848-shifting-letters/solution.py %}
