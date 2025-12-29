---
title: 796. Rotate String
notebook: coding
tags:
- easy
date: 2024-11-27 19:19:01
updated: 2024-11-27 19:19:01
---
## Problem

Given two strings `s` and `goal`, return `true` _if and only if_ `s` _can become_ `goal` _after some number of **shifts** on_ `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

<https://leetcode.com/problems/rotate-string/>

**Example 1:**

> Input: `s = "abcde", goal = "cdeab"`
> Output: `true`

**Example 2:**

> Input: `s = "abcde", goal = "abced"`
> Output: `false`

**Constraints:**

- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters.

## Test Cases

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
```

{% asset_code coding/796-rotate-string/solution_test.py %}

## Thoughts

先比较 `s` 和 `goal`，如果不相同则移位一次 `s` 再继续比较。不用真的移动，可以利用下标。

时间复杂度 `O(n²)`。

## Code

{% asset_code coding/796-rotate-string/solution.py %}
