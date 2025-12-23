---
title: 1749. Maximum Absolute Sum of Any Subarray
notebook: coding
tags:
- medium
date: 2025-02-26 15:25:24
updated: 2025-02-26 15:25:24
---
## Problem

You are given an integer array `nums`. The **absolute sum** of a subarray `[numsₗ, numsₗ₊₁, ..., numsᵣ₋₁, numsᵣ]` is `abs(numsₗ + numsₗ₊₁ + ... + numsᵣ₋₁ + numsᵣ)`.

Return _the **maximum** absolute sum of any **(possibly empty)** subarray of_ `nums`.

Note that `abs(x)` is defined as follows:

- If `x` is a negative integer, then `abs(x) = -x`.
- If `x` is a non-negative integer, then `abs(x) = x`.

<https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/>

**Example 1:**

> Input: `nums = [1,-3,2,3,-4]`
> Output: `5`
> Explanation: The subarray `[2,3]` has absolute sum `= abs(2+3) = abs(5) = 5`.

**Example 2:**

> Input: `nums = [2,-5,1,-4,3,-2]`
> Output: `8`
> Explanation: The subarray `[-5,1,-4]` has absolute sum `= abs(-5+1-4) = abs(-8) = 8`.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-104 <= nums[i] <= 10⁴`

## Test Cases

``` python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
```

{% asset_code coding/assets/1749-maximum-absolute-sum-of-any-subarray/solution_test.py %}

## Thoughts

可以直接搬 [53. Maximum Subarray](../53-maximum-subarray/index.md) 的代码，在求子数组最大和 `largest` 的同时，用完全类似的方法求出子数组的最小和 `smallest`。最终结果即为 `max{largest, smallest}`。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/1749-maximum-absolute-sum-of-any-subarray/solution.py %}

## Another Way

从 nums 最左端开始，计算出前 0 个数字（即空数组）之和、前 1 个数字之和、前 2 个数字之和、……、前 `n - 1` 个数字之和、以及所有（n 个）数字之和。取这 `n + 1` 个前缀和中的最大值 mx 与最小值 mn，那么 `mx - mn` 即为绝对值最大的子数组之和。

时间复杂度 `O(n)`，空间复杂度 `O(n)`（也可以直接边累加边求 mx 和 mn，那么空间复杂度也是 `O(1)`）。

{% asset_code coding/assets/1749-maximum-absolute-sum-of-any-subarray/solution2.py %}
