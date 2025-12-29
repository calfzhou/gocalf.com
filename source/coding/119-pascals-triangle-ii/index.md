---
title: 119. Pascal's Triangle II
notebook: coding
tags:
- easy
katex: true
date: 2025-01-28 21:15:24
updated: 2025-01-28 21:15:24
---
## Problem

Given an integer `rowIndex`, return the `rowIndexᵗʰ` (**0-indexed**) row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![pascal|240](pascal.gif "pascal"){.invert-when-dark}

<https://leetcode.cn/problems/pascals-triangle-ii/>

**Example 1:**

> Input: `rowIndex = 3`
> Output: `[1,3,3,1]`

**Example 2:**

> Input: `rowIndex = 0`
> Output: `[1]`

**Example 3:**

> Input: `rowIndex = 1`
> Output: `[1,1]`

**Constraints:**

- `0 <= rowIndex <= 33`

**Follow up:** Could you optimize your algorithm to use only `O(rowIndex)` extra space?

## Test Cases

``` python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
```

{% asset_code coding/119-pascals-triangle-ii/solution_test.py %}

## Thoughts

杨辉三角的的每个数字都是一个组合数，第 n（**0-indexed**）行第 m（**0-indexed**）个数字的值为 $\binom{n}{m}=\frac{n!}{m!(n-m)!}$。

因为要输出一整行，还可以看一下同一行前后数字的递推关系，易知

$$
\binom{n}{m}=\frac{n!}{m!(n-m)!}=\frac{n!(n-m+1)}{m(m-1)!(n-m+1)!}=\binom{n}{m-1}\frac{n-m+1}{m}
$$

这样就可以从第一个数（`1`）依次递推出整个数组。另外因为对称性，有 $\binom{n}{m}=\binom{n}{n-m}$，只需要计算前半个数组，后边个数组直接根据对称性填充即可。

时间复杂度 `O(n)`，附加的空间复杂度 `O(1)`。

## Code

{% asset_code coding/119-pascals-triangle-ii/solution.py %}
