---
title: 152. Maximum Product Subarray
notebook: coding
tags:
- medium
date: 2024-11-15 01:06:19
updated: 2024-11-15 01:06:19
---
## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return _the product_.

> A **subarray** is a contiguous **non-empty** sequence of elements within an array.

The test cases are generated so that the answer will fit in a **32-bit** integer.

<https://leetcode.com/problems/maximum-product-subarray/>

**Example 1:**

> Input: `nums = [2,3,-2,4]`
> Output: `6`
> Explanation: `[2,3]` has the largest product 6.

**Example 2:**

> Input: `nums = [-2,0,-1]`
> Output: `0`
> Explanation: The result cannot be 2, because `[-2,-1]` is not a subarray.

**Constraints:**

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

## Test Cases

{% asset_code coding/152-maximum-product-subarray/solution_test.py %}

## Thoughts

对于非零整数，相乘的数字个数越多，乘积的绝对值也会越大，决定是极大还是极小的关键就是负数个数的奇偶性。所以只要负数个数是偶数，数字越多越好。

0 乘以任何数结果都是 0，所以要先把 0 排除。用 0 所在的位置把整个数组切割成若干个不含零的小段，求每个小段能得到的最大乘积即可。

一个不含 0 的数组，如果负数个数是偶数，那么全部相乘，乘积最大。

如果只有一个负数，负数左边部分的乘积，与其右边部分的乘积，取最大即可。

如果有超过一个的奇数个负数，易知以最两头的负数之一分割数组，有可能得到最大乘积，而不能用任何中间的负数分割。设 `0 <= i < j < n` 是最两头的负数的位置，最大乘积只可能出自 `Π(nums[0:j])` 或 `Π(nums[i+1:n])`。

时间复杂度 `O(n)`。

## Code

{% asset_code coding/152-maximum-product-subarray/solution.py %}
