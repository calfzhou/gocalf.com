---
title: 171. Excel Sheet Column Number
notebook: coding
tags:
- easy
date: 2025-01-02 23:23:27
updated: 2025-01-02 23:23:27
---
## Problem

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return _its corresponding column number_.

For example:

> A -> 1
> B -> 2
> C -> 3
> ...
> Z -> 26
> AA -> 27
> AB -> 28
> ...

<https://leetcode.com/problems/excel-sheet-column-number/>

**Example 1:**

> Input: `columnTitle = "A"`
> Output: `1`

**Example 2:**

> Input: `columnTitle = "AB"`
> Output: `28`

**Example 3:**

> Input: `columnTitle = "ZY"`
> Output: `701`

**Constraints:**

- `1 <= columnTitle.length <= 7`
- `columnTitle` consists only of uppercase English letters.
- `columnTitle` is in the range `["A", "FXSHRXW"]`.

## Test Cases

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
```

{% snippet solution_test.py %}

## Thoughts

[168. Excel Sheet Column Title](../168-excel-sheet-column-title/index.md) 的反函数。

把每一个字母翻译成 1 到 26 的整数，乘以 26 的相应次幂即可。

[168. Excel Sheet Column Title](../168-excel-sheet-column-title/index.md) 代码中的 `columnNumber - 1` 对应于这里的 `ord(c) - ord('A') + 1 = ord(c) - 64`。

## Code

{% snippet solution.py %}
