---
title: 540. Single Element in a Sorted Array
notebook: coding
tags:
- medium
date: 2024-11-10 02:15:43
updated: 2024-11-10 02:15:43
---
## Problem

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return _the single element that appears only once_.

Your solution must run in `O(log n)` time and `O(1)` space.

<https://leetcode.cn/problems/single-element-in-a-sorted-array/>

**Example 1:**

> Input: `nums = [1,1,2,3,3,4,4,8,8]`
> Output: 2

**Example 2:**

> Input: `nums = [3,3,7,7,10,11,11]`
> Output: 10

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `0 <= nums[i] <= 10⁵`

## Test Cases

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

限制了 `O(log n)` 时间，加上数组是有序的，考虑二分法。

n 一定是个奇数，假设 `n = 2 * m + 1`

用正中位置把数组分成三份：左边 m 个数，正中的数，右边 m 个数。

如果正中的数与其左边和右边都不相等，那就是 the single element。

否则假设它跟左半边的最后一个数字相同，排除掉该数字后，剩下左边 m-1 个数，右边 m 个数。

目标 single element 在哪边，哪边的元素个数就是奇数，对那边的子数组重复类似的操作即可。

时间复杂度 `O(log n)`，空间复杂度 `O(1)`。

## Code

{% asset_code solution.py %}
