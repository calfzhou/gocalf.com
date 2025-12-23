---
title: 371. Sum of Two Integers
notebook: coding
tags:
- medium
date: 2024-11-25 22:08:36
updated: 2024-11-25 22:08:36
katex: true
---
## Problem

Given two integers `a` and `b`, return _the sum of the two integers without using the operators_ `+` _and_ `-`.

<https://leetcode.com/problems/sum-of-two-integers/>

**Example 1:**

> Input: `a = 1, b = 2`
> Output: `3`

**Example 2:**

> Input: `a = 2, b = 3`
> Output: `5`

**Constraints:**

- `-1000 <= a, b <= 1000`

## Test Cases

``` python
class Solution:
    def getSum(self, a: int, b: int) -> int:
```

{% asset_code coding/assets/371-sum-of-two-integers/solution_test.py %}

## Thoughts

看单个二进制位（其中 `r` 表示相加结果的低位，`c` 表示进位）：

$$
\begin{array}{cc:cc}
  a & b & c & r \\
  \hline
  0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 1 \\
  1 & 0 & 0 & 1 \\
  1 & 1 & 1 & 0
\end{array}
$$

所以 $r=a\oplus b$，$c=a\land b$。`c` 比 `r` 要靠左一位，可以令 $c=(a\land b)\ll 1$。

更多的二进制位也是类似的，得到 $a+b=r+c=(a\oplus b)+((a\land b)\ll 1)$。

再对 `r` 和 `c` 按照相同的逻辑运算，知道待相加的两个数至少有一个变为 0（一般看 c）（TODO：最多循环多少次？）。

如果用 Python 实现就特殊一些，因为 Python 内置支持任意大的整数，负数的表达方式跟其他语言就不太一样，需要自行模拟其他语言里的有限二进制位整数。比如以 32 位为例，每次计算得到新的 `r` 和 `c`，需要跟一个 32 位的全 `1` 掩码做 bit-and，模拟普通的 32 位整数。返回计算结果前，如果结果是负数，也要再转换成 Python 格式的负数。

## Code

{% asset_code coding/assets/371-sum-of-two-integers/solution.py %}
