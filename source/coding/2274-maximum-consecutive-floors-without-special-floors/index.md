---
title: 2274. Maximum Consecutive Floors Without Special Floors
notebook: coding
tags:
- medium
date: 2025-01-06 00:20:47
updated: 2025-01-06 00:20:47
---
## Problem

Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be **special floors**, used for relaxation only.

You are given two integers `bottom` and `top`, which denote that Alice has rented all the floors from `bottom` to `top` (**inclusive**). You are also given the integer array `special`, where `special[i]` denotes a special floor that Alice has designated for relaxation.

Return _the **maximum** number of consecutive floors without a special floor_.

<https://leetcode.cn/problems/maximum-consecutive-floors-without-special-floors/>

**Example 1:**

> Input: `bottom = 2, top = 9, special = [4,6]`
> Output: `3`
> Explanation: The following are the ranges (inclusive) of consecutive floors without a special floor:
>
> - `(2, 3)` with a total amount of 2 floors.
> - `(5, 5)` with a total amount of 1 floor.
> - `(7, 9)` with a total amount of 3 floors.
>
> Therefore, we return the maximum number which is 3 floors.

**Example 2:**

> Input: `bottom = 6, top = 8, special = [7,6,8]`
> Output: `0`
> Explanation: Every floor rented is a special floor, so we return 0.

**Constraints:**

- `1 <= special.length <= 10⁵`
- `1 <= bottom <= special[i] <= top <= 10⁹`
- All the values of `special` are **unique**.

## Test Cases

```python
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

直接对 special 排序，然后计算上下两个 special 楼层之间的间隔。另外再计算最下边的 special 楼层到 bottom（含）的距离，以及 top（含）到最上边 special 楼层的距离。取最大即可。

## Code

{% asset_code solution.py %}
