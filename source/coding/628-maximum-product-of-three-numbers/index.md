---
title: 628. Maximum Product of Three Numbers
notebook: coding
tags:
- easy
date: 2025-01-03 12:29:47
updated: 2025-01-03 12:29:47
---
## Problem

Given an integer array `nums`, _find three numbers whose product is maximum and return the maximum product_.

<https://leetcode.com/problems/maximum-product-of-three-numbers/>

**Example 1:**

> Input: `nums = [1,2,3]`
> Output: `6`

**Example 2:**

> Input: `nums = [1,2,3,4]`
> Output: `24`

**Example 3:**

> Input: `nums = [-1,-2,-3]`
> Output: `-6`

**Constraints:**

- `3 <= nums.length <= 10⁴`
- `-1000 <= nums[i] <= 1000`

## Test Cases

``` python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
```

{% asset_code coding/628-maximum-product-of-three-numbers/solution_test.py %}

## Thoughts

看 nums 中正数的数量在各种情况下，最大乘积如何得到：

- 如果有 `≥ 3` 个正数，要么是三个最大正数之积，要么是最大正数乘以两个最小负数。
- 如果有 2 个正数，要么是两个最大正数乘以最大非正数，要么是两个最小负数乘以最大正数。
- 如果有 1 个正数，此正数乘以两个最小非正数。
- 如果没有正数，取三个最大非正数之积。

可见不管哪种情况，最大乘积的来源，要么是三个最大数字相乘，要么是最大数字乘以两个最小数字。

可以直接（in-place）排序，然后取三个最大和两个最小，时间复杂度 `O(n log n)`。

或者用大小为 3 的最小堆和大小为 2 的最大堆（用负数模拟）找出三个最大和两个最小，时间复杂度 `O(n)`。

空间复杂度都是 `O(1)`。

## Code

{% asset_code coding/628-maximum-product-of-three-numbers/solution.py %}
