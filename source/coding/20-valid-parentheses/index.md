---
title: 20. Valid Parentheses
notebook: coding
tags:
- easy
date: 2024-11-14 18:17:00
updated: 2024-11-14 18:17:00
---
## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

<https://leetcode.com/problems/valid-parentheses/>

**Example 1:**

> Input: `s = "()"`
> Output: `true`

**Example 2:**

> Input: `s = "()[]{}"`
> Output: `true`

**Example 3:**

> Input: `s = "(]"`
> Output: `false`

**Example 4:**

> Input: `s = "([])"`
> Output: `true`

**Constraints:**

- `1 <= s.length <= 10⁴`
- `s` consists of parentheses only `'()[]{}'`.

## Test Cases

```python
class Solution:
    def isValid(self, s: str) -> bool:
```

{% asset_code solution_test.py %}

## Thoughts

栈的典型使用场景。

从左向右扫描 s，如果当前字符是左括号就入栈，如果是右括号就出栈并判断出栈的括号类型跟当前的是否一致，不一致则 not valid。如果看到右括号时栈为空，not valid。如果最后栈没被清空，也 not valid。

显然如果 s 的长度是奇数，一定 not valid。

时间复杂度和空间复杂度都是 `O(n)`。

## Code

{% asset_code solution.py %}
