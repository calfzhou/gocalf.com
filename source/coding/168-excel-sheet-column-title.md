---
title: 168. Excel Sheet Column Title
notebook: coding
tags:
- easy
date: 2025-01-02 23:07:44
updated: 2025-01-02 23:07:44
---
## Problem

Given an integer `columnNumber`, return _its corresponding column title as it appears in an Excel sheet_.

For example:

> A -> 1
> B -> 2
> C -> 3
> ...
> Z -> 26
> AA -> 27
> AB -> 28
> ...

<https://leetcode.com/problems/excel-sheet-column-title/>

**Example 1:**

> Input: `columnNumber = 1`
> Output: `"A"`

**Example 2:**

> Input: `columnNumber = 28`
> Output: `"AB"`

**Example 3:**

> Input: `columnNumber = 701`
> Output: `"ZY"`

**Constraints:**

- `1 <= columnNumber <= 2³¹ - 1`

## Test Cases

``` python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
```

{% asset_code coding/assets/168-excel-sheet-column-title/solution_test.py %}

## Thoughts

有点儿像 26 进制但并不是，数值是从 1 开始，而非 0。也不是简单地偏移一位，因为如果把 A 看作 0，并不会有 AA 这样的 26 进制数。

实际上 column title 从右到左的每一位，都相当于是对 26 取余数的结果映射到大写字母表。当然取余数取不到 26，而且还要处理 0，一个简单的办法就是每次都给数字减去 1，然后再对 26 取余数。

## Code

{% asset_code coding/assets/168-excel-sheet-column-title/solution.py %}
