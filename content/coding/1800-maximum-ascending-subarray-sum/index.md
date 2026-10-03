---
title: 1800. Maximum Ascending Subarray Sum
notebook: coding
tags:
- easy
date: 2025-02-04 15:14:11
updated: 2025-02-04 15:14:11
---
## Problem

Given an array of positive integers `nums`, return the _maximum possible sum of an **ascending** subarray in_ `nums`.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray `[numsl, numsl+1, ..., numsr-1, numsr]` is **ascending** if for all `i` where `l <= i < r`, `numsi < numsi+1`. Note that a subarray of size `1` is **ascending**.

<https://leetcode.com/problems/maximum-ascending-subarray-sum/>

**Example 1:**

> Input: `nums = [10,20,30,5,10,50]`
> Output: `65`
> Explanation: `[5,10,50]` is the ascending subarray with the maximum sum of 65.

**Example 2:**

> Input: `nums = [10,20,30,40,50]`
> Output: `150`
> Explanation: `[10,20,30,40,50]` is the ascending subarray with the maximum sum of 150.

**Example 3:**

> Input: `nums = [12,17,15,13,10,11,12]`
> Output: `33`
> Explanation: `[10,11,12]` is the ascending subarray with the maximum sum of 33.

**Constraints:**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Test Cases

```python
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

直接遍历数组，记录当前连续递增子数组之和，如果下一个数字仍然是递增则累加到和，否则重置和。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% snippet solution.py %}
