---
title: 15. 3Sum
notebook: coding
tags:
- medium
katex: true
date: 2024-11-13 11:40:03
updated: 2024-11-13 11:40:03
---
## Problem

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

<https://leetcode.com/problems/3sum/>

**Example 1:**

> Input: `nums = [-1,0,1,2,-1,-4]`
> Output: `[[-1,-1,2],[-1,0,1]]`
> Explanation:
> `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`.
> `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`.
> `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`.
> The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`.
> Notice that the order of the output and the order of the triplets does not matter.

**Example 2:**

> Input: nums = `[0,1,1]`
> Output: `[]`
> Explanation: The only possible triplet does not sum up to 0.

**Example 3:**

> Input: `nums = [0,0,0]`
> Output: `[[0,0,0]]`
> Explanation: The only possible triplet sums up to 0.

**Constraints:**

- `3 <= nums.length <= 3000`
- `-10⁵ <= nums[i] <= 10⁵`

## Test Cases

``` python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
```

{% asset_code coding/assets/15-3sum/solution_test.py %}

## Thoughts

先把数组排序，因为输出的每组三个数值而非数组下标，所以不用记录原始的数组下标。

为了避免产生重复的三元组，额外限制 `nums[i] <= nums[j] <= nums[k]`。

两重遍历所有的 i、j 组合 $0\le i<j<n-1$，用二分法在 `nums[j+1:n]` 中查找 `0 - i - j`。时间复杂度 `O(n² log n)`，空间复杂度 `O(n)`。

简单直接，但是不高效，没有充分利用到 **和为零** 的特点。

三个数之和为零，有几种可能：

1. 三个数全是 0（要求 `nums` 至少有三个 0）。
2. 一个数是 0，另外两个数一正一负（`nums` 至少有一个 0）。
3. 两个负数，一个正数。
4. 一个负数，两个正数。

由此，整个处理过程是：

1. 把 `nums` 分成正数和负数两个子数组，同时记录 0 的个数，`O(n)` 时间，`O(n)` 空间。
2. 对两个子数组分别排序，`O(n log n)` 时间。
3. 如果 0 的个数大于 2，记录 `[0, 0, 0]` 为可行解。
4. 如果 0 的个数大于 0，用类似归并排序的方式，同时遍历负数和正数子数组，找出所有绝对值相等的正负数对，`O(n)` 时间。
5. 用两重循环遍历所有的负数对组合，内循环的时候也用归并法同步遍历正数子数组，找到与两个负数之和绝对值相等的正数，`O(n²)` 时间。
6. 同理，找出一负两正的组合，`O(n²)` 时间。

整体时间复杂度为 `O(n²)`。

## Code

{% asset_code coding/assets/15-3sum/solution.py %}

## Simpler

上边处理得点儿复杂。其实也不用特别考虑正负数，这不是加法特点引起的，只是和为 **零** 的特例。

先只看两数之和为 0（或任意目标值）的问题。只需要对数组排序，然后两个下标分别指向数组的首尾。

如果和小于目标值，需要把左边的下标往右移；反之把右边的下标往左移。如果等于目标值，那就找到一组解，然后同时向中间移动两个下标。直到两个下标相遇或者在目标值的同侧（跟上边归并处理的逻辑一致）。

而扩展到三个数，只需要先固定第一个数，然后对其右边的子数组，按上述方法找到与第一个数字之和为 0 的每一对数即可。

遍历一遍第一个数，每次遍历需要 `O(n)` 时间，总的时间复杂度是 `O(n²)`。

代码简洁不少，但速度却慢了不少。可能因为这次是整个数组排序，遍历的时候比较次数也更多一些。

{% asset_code coding/assets/15-3sum/solution2.py %}

## Faster

还是看两数之和为定值的问题，可以不对数组排序，但把所有的数存入哈希表，遍历每一个数，在哈希表中查另一个数是否存在。

整体时间复杂度还是 `O(n²)`，不过省去了整体排序的时间，其他判断的时间也能减少不少。

{% asset_code coding/assets/15-3sum/solution3.py %}
