---
title: 42. Trapping Rain Water
notebook: coding
tags:
- hard
- todo
date: 2025-01-19 21:47:00
updated: 2025-01-19 21:47:00
---
## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

<https://leetcode.com/problems/trapping-rain-water/>

**Example 1:**

![case1](case1.png)

> Input: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
> Output: `6`
> Explanation: The above elevation map (black section) is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, 6 units of rain water (blue section) are being trapped.

**Example 2:**

> Input: `height = [4,2,0,3,2,5]`
> Output: `9`

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 10⁴`
- `0 <= height[i] <= 10⁵`

## Test Cases

```python
class Solution:
    def trap(self, height: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

对于任意位置 i（`0 ≤ i < n`），记 `l_max(i) = max{height[:i+1]}`（i 及其左边最高的 bar），`r_max(i) = max[height[i:]]`（i 及其右边最高的 bar）。取 `bound = min{l_max(i), r_max(i)}`，显然 `bound ≥ height[i]`。如果 `bound > height[i]`，那么高出来的部分（`bound - height[i]`）都是可以有水的。

先从右向左遍历 height，记录所有的 `r_max(i)`。然后从左向右遍历，一边更新 `l_max(i)` 一边计算位置 i 的积水量，并累计总积水量。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% snippet solution.py %}

空间复杂度可以降到 `O(1)`，时间复杂度的系数也可以在降低，TODO。
