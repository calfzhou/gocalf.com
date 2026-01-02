---
title: 1742. Maximum Number of Balls in a Box
notebook: coding
tags:
- easy
date: 2025-02-13 10:07:26
updated: 2025-02-13 10:07:26
---
## Problem

You are working in a ball factory where you have `n` balls numbered from `lowLimit` up to `highLimit` **inclusive** (i.e., `n == highLimit - lowLimit + 1`), and an infinite number of boxes numbered from `1` to `infinity`.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number `321` will be put in the box number `3 + 2 + 1 = 6` and the ball number `10` will be put in the box number `1 + 0 = 1`.

Given two integers `lowLimit` and `highLimit`, return _the number of balls in the box with the most balls._

<https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/>

**Example 1:**

> Input: `lowLimit = 1, highLimit = 10`
> Output: `2`
> Explanation:
>
> ```text
> Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
> Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
> ```
>
> Box 1 has the most number of balls with 2 balls.

**Example 2:**

> Input: lowLimit = 5, highLimit = 15
> Output: 2
> Explanation:
>
> ```text
> Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
> Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
> ```
>
> Boxes 5 and 6 have the most number of balls with 2 balls in each.

**Example 3:**

> Input: lowLimit = 19, highLimit = 28
> Output: 2
> Explanation:
>
> ```text
> Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
> Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
> ```
>
> Box 10 has the most number of balls with 2 balls.

**Constraints:**

- `1 <= lowLimit <= highLimit <= 10⁵`

## Test Cases

```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
```

{% snippet solution_test.py %}

## Thoughts

跟 [2342. Max Sum of a Pair With Equal Sum of Digits](../2342-max-sum-of-a-pair-with-equal-sum-of-digits/index.md) 类似，按 “sum of digits of the number” 把 `[lowLimit, highLimit]` 区间的所有数字分组，记录每组的数字个数，然后取最大即可。

一个小的优化是，对于连续的正整数，如果个位是从 0 到 9，则对应的 “sum of digits of the number” 也是连续递增的。利用这个规则可以节省 90% 左右的计算量。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% snippet solution.py %}
