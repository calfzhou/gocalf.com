---
title: 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
notebook: coding
tags:
- easy
date: 2025-02-03 11:45:38
updated: 2025-02-03 11:45:38
---
## Problem

You are given an array of integers `nums`. Return _the length of the **longest** subarray of_ `nums` _which is either **strictly increasing** or **strictly decreasing**_.

> A **subarray** is a contiguous **non-empty** sequence of elements within an array.
>
> An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
>
> An array is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

<https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/>

**Example 1:**

> Input: `nums = [1,4,3,3,2]`
> Output: `2`
> Explanation:
> The strictly increasing subarrays of nums are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, and `[1,4]`.
> The strictly decreasing subarrays of nums are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, and `[4,3]`.
> Hence, we return 2.

**Example 2:**

> Input: `nums = [3,3,3,3]`
> Output: `1`
> Explanation:
> The strictly increasing subarrays of nums are `[3]`, `[3]`, `[3]`, and `[3]`.
> The strictly decreasing subarrays of nums are `[3]`, `[3]`, `[3]`, and `[3]`.
> Hence, we return 1.

**Example 3:**

> Input: `nums = [3,2,1]`
> Output: `3`
> Explanation:
> The strictly increasing subarrays of nums are `[3]`, `[2]`, and `[1]`.
> The strictly decreasing subarrays of nums are `[3]`, `[2]`, `[1]`, `[3,2]`, `[2,1]`, and `[3,2,1]`.
> Hence, we return 3.

**Constraints:**

- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 50`

## Test Cases

``` python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
```

{% asset_code coding/assets/3105-longest-strictly-increasing-or-strictly-decreasing-subarray/solution_test.py %}

## Thoughts

一个直观的思路是先统计 nums 中最长的严格递增子数组的长度，再统计最长的严格递减子数组的长度，二者取较大的。也可以在一次循环里完成，增加一个状态记录当前是在严格递增子数组中还是严格递减子数组中。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/3105-longest-strictly-increasing-or-strictly-decreasing-subarray/solution.py %}
