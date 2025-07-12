---
title: 503. Next Greater Element II
notebook: coding
tags:
- medium
date: 2024-12-18 17:04:11
updated: 2024-12-18 23:33:05
---
## Problem

Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return _the **next greater number** for every element in_ `nums`.

The **next greater number** of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

<https://leetcode.com/problems/next-greater-element-ii/>

**Example 1:**

> Input: `nums = [1,2,1]`
> Output: `[2,-1,2]`
> Explanation: The first 1's next greater number is 2;
> The number 2 can't find next greater number.
> The second 1's next greater number needs to search circularly, which is also 2.

**Example 2:**

> Input: `nums = [1,2,3,4,3]`
> Output: `[2,3,4,-1,4]`

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`

## Test Cases

``` python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
```

{% asset_code coding/assets/503-next-greater-element-ii/solution_test.py %}

## Thoughts

[496. Next Greater Element I](496-next-greater-element-i) 的进阶版，数组变成循环数组，可以跨过数组最右端，从最左端重入数组继续查找 next greater 元素。

假设把 nums 复制一份，拼在原数组的右边，形成 2n 大小的新数组，就能实现循环找 next greater 的效果。实践中不用真的复制，只需要用 [1475. Final Prices With a Special Discount in a Shop](1475-final-prices-with-a-special-discount-in-a-shop#O-n) 中提到的单调栈对 nums 处理两遍，效果是一样的。

需要注意在 [problem 496](496-next-greater-element-i) 中，nums2 中的元素各不相同，所以不用特别考虑相等的边界情况。本题 nums 中可能有相等的元素，循环两遍更会产生相等元素，需要处理好相等的边界条件。

## Code

### Backward Iteration

{% asset_code coding/assets/503-next-greater-element-ii/solution.py %}

### Forward Iteration

{% asset_code coding/assets/503-next-greater-element-ii/solution2.py %}
