---
title: 581. Shortest Unsorted Continuous Subarray
notebook: coding
tags:
- medium
date: 2025-01-02 10:28:34
updated: 2025-01-02 10:28:34
---
## Problem

Given an integer array `nums`, you need to find one **continuous subarray** such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return _the shortest such subarray and output its length_.

<https://leetcode.com/problems/shortest-unsorted-continuous-subarray/>

**Example 1:**

> Input: `nums = [2,6,4,8,10,9,15]`
> Output: `5`
> Explanation: You need to sort `[6, 4, 8, 10, 9]` in ascending order to make the whole array sorted in ascending order.

**Example 2:**

> Input: `nums = [1,2,3,4]`
> Output: `0`

**Example 3:**

> Input: `nums = [1]`
> Output: `0`

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `-10⁵ <= nums[i] <= 10⁵`

**Follow up:** Can you solve it in `O(n)` time complexity?

## Test Cases

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

先从左到右遍历数组，找到第一个比右边数字大的位置，记为 l。如果 `l = n - 1` 说明数组已经是有序的了，直接返回 0。

再从右到左遍历数组，找到（最右边）第一个比左边数字小的位置，记为 r。

显然至少区间 `[l, r]` 需要重新排序。

但也有可能范围更大。先找出 `nums[l:r+1]` 的最小值和最大值，分别记为 `sub_min` 和 `sub_max`。

然后从 l 开始向左，找到小于等于 `sub_min` 的最大数字的位置更新到 l（直接遍历就行，也可以用二分法，总时间复杂度不变，运行时间可能会略少一些）。从 r 向右，找到大于等于 `sum_max` 的最小数字的位置更新到 r。更新后的区间 `[l, r]` 就是需要重排的最小区间范围，大小为 `r - l + 1`。

总的时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% snippet solution.py %}
