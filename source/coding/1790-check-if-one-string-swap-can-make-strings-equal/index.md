---
title: 1790. Check if One String Swap Can Make Strings Equal
notebook: coding
tags:
- easy
date: 2025-02-05 10:06:55
updated: 2025-02-05 10:06:55
---
## Problem

You are given two strings `s1` and `s2` of equal length. A **string swap** is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return `true` _if it is possible to make both strings equal by performing **at most one string swap** on **exactly one** of the strings._ Otherwise, return `false`.

<https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/>

**Example 1:**

> Input: `s1 = "bank", s2 = "kanb"`
> Output: `true`
> Explanation: For example, swap the first character with the last character of `s2` to make `"bank"`.

**Example 2:**

> Input: `s1 = "attack", s2 = "defend"`
> Output: `false`
> Explanation: It is impossible to make them equal with one string swap.

**Example 3:**

> Input: `s1 = "kelb", s2 = "kelb"`
> Output: `true`
> Explanation: The two strings are already equal, so no string swap operation is required.

**Constraints:**

- `1 <= s1.length, s2.length <= 100`
- `s1.length == s2.length`
- `s1` and `s2` consist of only lowercase English letters.

## Test Cases

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
```

{% asset_code solution_test.py %}

## Thoughts

先逐位比较 s1 和 s2，统计差异个数。

如果没有差异，即 s1 和 s2 全等，返回 true。

如果差异位数不等于 2，则无法通过一次交换把 s2 改成 s1，放回 false。

如果差异位数恰好为 2，则进一步检查这两个位置的两对字符是否刚好互换后相等即可。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code solution.py %}
