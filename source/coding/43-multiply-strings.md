---
title: 43. Multiply Strings
notebook: coding
tags:
- medium
date: 2024-12-19 21:16:44
updated: 2024-12-19 21:16:44
---
## Problem

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

<https://leetcode.com/problems/multiply-strings/>

**Example 1:**

> Input: num1 = "2", num2 = "3"
> Output: "6"

**Example 2:**

> Input: num1 = "123", num2 = "456"
> Output: "56088"

**Constraints:**

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## Test Cases

``` python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
```

{% asset_code coding/assets/43-multiply-strings/solution_test.py %}

## Thoughts

直接像乘法竖式计算那样逐位相乘即可。注意一个 m 位数和一个 n 位数相乘（不考虑有 0 的情况），乘积要么是 `m + n` 位数，要么是 `m + n - 1` 位数。

时间复杂度 `O(m * n)`，空间复杂度 `O(m + n)`。

## Code

{% asset_code coding/assets/43-multiply-strings/solution.py %}
