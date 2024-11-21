---
title: 53. Maximum Subarray
notebook: coding
tags:
- medium
date: 2024-11-18 17:51:38
updated: 2024-11-18 17:51:38
---
## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return _its sum_.

> A **subarray** is a contiguous **non-empty** sequence of elements within an array.

<https://leetcode.com/problems/maximum-subarray/>

**Example 1:**

> Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
> Output: `6`
> Explanation: The subarray `[4,-1,2,1]` has the largest sum 6.

**Example 2:**

> Input: `nums = [1]`
> Output: `1`
> Explanation: The subarray `[1]` has the largest sum 1.

**Example 3:**

> Input: `nums = [5,4,-1,7,8]`
> Output: `23`
> Explanation: The subarray `[5,4,-1,7,8]` has the largest sum 23.

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Test Cases

{% asset_code coding/53-maximum-subarray/solution_test.py %}

## Thoughts

如果一个 subarray 的和大于 0，把它与下一个数相加的结果一定比下一个数自身大。反之，应该从下一个数开启新的 subarray。

记录当前 subarray 的总和，如果把下一个数加入进来，总和仍然大于 0，就可以继续。否则把 subarray 清空，总和恢复为 0，从再下一个数开始尝试建立新的 subarray。过程中记录见到的最大的总和。

## Code

{% asset_code coding/53-maximum-subarray/solution.py %}
