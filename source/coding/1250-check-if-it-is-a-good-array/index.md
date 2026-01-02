---
title: 1250. Check If It Is a Good Array
notebook: coding
tags:
- hard
date: 2024-12-28 21:47:40
updated: 2024-12-28 21:47:40
---
## Problem

Given an array `nums` of positive integers. Your task is to select some subset of `nums`, multiply each element by an integer and add all these numbers. The array is said to be **good** if you can obtain a sum of `1` from the array by any possible subset and multiplicand.

Return `True` if the array is **good** otherwise return `False`.

<https://leetcode.com/problems/check-if-it-is-a-good-array/>

**Example 1:**

> Input: `nums = [12,5,7,23]`
> Output: `true`
> Explanation: Pick numbers 5 and 7.
> `5*3 + 7*(-2) = 1`

**Example 2:**

> Input: `nums = [29,6,10]`
> Output: `true`
> Explanation: Pick numbers 29, 6 and 10.
> `29*1 + 6*(-3) + 10*(-1) = 1`

**Example 3:**

> Input: `nums = [3,6]`
> Output: `false`

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`

## Test Cases

```python
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
```

{% snippet solution_test.py %}

## Thoughts

这是道数学题。有个「裴蜀定理」（[Bézout's identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity)），说对于任何整数 a、b 和 m，关于未知数 x 和 y 的 线性丢番图方程（[Diophantine equation](https://en.wikipedia.org/wiki/Diophantine_equation)）（称为裴蜀等式）`a*x + b*y = m` 有整数解当且仅当 m 是 a 和 b 的最大公约数 d 的倍数。特别地，方程 `a*x + b*y = 1` 有整数解当且仅当整数 a 和 b 互质。

所以至少 nums 中有一对互质数，结果就为 `True`。可以直接计算 nums 中所有数字共同的最大公约数，如果为 1 则结果为 `True`，否则为 `False`。

Python 里 [`math.gcd`](https://docs.python.org/3/library/math.html#math.gcd) 方法可以直接计算一组数字的最大公约数。

如果不想用自带的函数，也可以自己实现 `gcd(a, b)`，通过辗转相除法计算 a 和 b 的最大公约数。将结果再与数组中下一个数求最大公约数，循环一遍就得到所有数字的最大公约数。

## Code

{% snippet solution.py %}

{% snippet solution2.py %}
