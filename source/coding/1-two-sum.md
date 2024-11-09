---
title: 1. Two Sum
notebook: coding
tags:
- easy
date: 2024-11-09 20:49:16
updated: 2024-11-09 20:49:16
---
## Problem

<https://leetcode.com/problems/two-sum/description/>

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

Example 1:

> Input: nums = [2,7,11,15], target = 9
> Output: [0,1]
> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

> Input: nums = [3,2,4], target = 6
> Output: [1,2]

Example 3:

> Input: nums = [3,3], target = 6
> Output: [0,1]

**Constraints:**

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than `O(n^2)` time complexity?

## Test Cases

[solution_test.py](1-two-sum/solution_test.py)

## Thoughts

一方面是要找到那两个相加等于目标值的数，另一方面需要能记录到这两数的原始索引下标。

### 排序

用 `O(n log n)` 时间对数组排序。

从最小的数字开始遍历，直到 `target / 2`（包含）。

对于一个数字 v，用二分法，在后半数组中查找 target - v。二分查找是 `O(log n)`，总共也是 `O(n log n)`。

需要记录数字在排序前的数组下标。

[solution.py](1-two-sum/solution.py)

### 哈希

可以利用哈希表 `O(1)` 查询时间的特点，把所有数字放进哈希表，然后直接利用哈希表查找 target - v 是否存在。

因为题目限定了有唯一解，所以不用管重复的数字。唯一需要考虑的是，当 target 是偶数时，可能有两个 `target / 2`。

时间复杂度为 `O(n)`。

[solution2.py](1-two-sum/solution2.py)
