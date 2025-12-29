---
title: 227. Basic Calculator II
notebook: coding
tags:
- medium
date: 2024-12-20 16:02:58
updated: 2024-12-20 16:02:58
---
## Problem

Given a string `s` which represents an expression, _evaluate this expression and return its value_.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2³¹, 2³¹ - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

<https://leetcode.com/problems/basic-calculator-ii/>

**Example 1:**

> Input: s = "3+2*2"
> Output: 7

**Example 2:**

> Input: s = " 3/2 "
> Output: 1

**Example 3:**

> Input: s = " 3+5 / 2 "
> Output: 5

**Constraints:**

- `1 <= s.length <= 3 * 10⁵`
- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.
- `s` represents **a valid expression**.
- All the integers in the expression are non-negative integers in the range `[0, 2³¹ - 1]`.
- The answer is **guaranteed** to fit in a **32-bit integer**.

## Test Cases

```python
class Solution:
    def calculate(self, s: str) -> int:
```

{% asset_code coding/227-basic-calculator-ii/solution_test.py %}

## Thoughts

跟 [224. Basic Calculator](../224-basic-calculator/index.md)，增加了高优先级的乘除法，但是去掉了括号和一元取反运算，其实是要简单一些。

可以直接套用 [224. Basic Calculator](../224-basic-calculator/index.md) 中的基于逆波兰表达式的计算逻辑，其中 `tokenize` 方法完全一样，`reverse_polish` 方法中的运算符表里增加 `*` 和 `/`，级别比 `+` 和 `-` 高即可，去掉关于括号、一元负号的逻辑，最后在 `calculate` 方法中增加乘法和除法的计算。

## Code

{% asset_code coding/227-basic-calculator-ii/solution.py %}

## Directly

没有括号的加减乘除混合运算也非常简单，也是相当于若干个数字相加，只不过遇到乘除法的时候，就先计算乘除法。

用数组记录所有待相加的数字，其中加号后边的数字直接放入数组，减号后边的数字取反后放入数组。如果是乘号或除号，则取出数组末尾的数字，跟运算符后边的数字相乘或相除，再把结果放回数组。最终对数组求和即可。

需要小心的是负数的除法。题目要求的是除法运算的结果只保留整数部分，即 `3 / 2 = 1.5 → 1`、`-3 / 2 = -1.5 → -1`。但 Python 中的整除运算（`//`）不符合这个要求（`-3 // 2 = -2`），需要用 [`math.trunc`](https://docs.python.org/3/library/math.html#math.trunc) 函数，`trunc(-3 / 2) = -1`。

{% asset_code coding/227-basic-calculator-ii/solution2.py %}
