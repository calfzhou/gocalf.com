---
title: 153. Find Minimum in Rotated Sorted Array
notebook: coding
tags:
- medium
date: 2024-11-15 12:27:09
updated: 2024-11-15 12:27:09
---
## Problem

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return _the minimum element of this array_.

You must write an algorithm that runs in `O(log n) time`.

<https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/>

**Example 1:**

> Input: `nums = [3,4,5,1,2]`
> Output: `1`
> Explanation: The original array was `[1,2,3,4,5]` rotated 3 times.

**Example 2:**

> Input: `nums = [4,5,6,7,0,1,2]`
> Output: `0`
> Explanation: The original array was `[0,1,2,4,5,6,7]` and it was rotated 4 times.

**Example 3:**

> Input: `nums = [11,13,15,17]`
> Output: `11`
> Explanation: The original array was `[11,13,15,17]` and it was rotated 4 times.

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Test Cases

{% asset_code coding/153-find-minimum-in-rotated-sorted-array/solution_test.py %}

## Thoughts

还是二分搜索的逻辑。

看数组中间位置的元素值，如果比两端的值都大，那么应该去右半边（不含中间位置）继续搜索。如果比两端的值都小，应该去左半边（含中间位置）继续搜索。如果介于两端的值之间，那么左端点就是最小值。

当子数组缩短到不超过 2 个元素的时候就可以停止，最后的一个元素，或者最后两个元素的较小值，就是整个数组的最小值。这样写代码的时候可以简化边界值的处理（运行速度也是更快的）。

时间复杂度 `O(log n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/153-find-minimum-in-rotated-sorted-array/solution.py %}
