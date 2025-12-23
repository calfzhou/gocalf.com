---
title: 81. Search in Rotated Sorted Array II
notebook: coding
tags:
- medium
date: 2025-02-01 21:10:28
updated: 2025-02-01 21:10:28
---
## Problem

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` _if_ `target` _is in_ `nums`_, or_ `false` _if it is not in_ `nums`_._

You must decrease the overall operation steps as much as possible.

<https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/>

**Example 1:**

> Input: `nums = [2,5,6,0,0,1,2], target = 0`
> Output: `true`

**Example 2:**

> Input: `nums = [2,5,6,0,0,1,2], target = 3`
> Output: `false`

**Constraints:**

- `1 <= nums.length <= 5000`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums` is guaranteed to be rotated at some pivot.
- `-10⁴ <= target <= 10⁴`

**Follow up:** This problem is similar to [33. Search in Rotated Sorted Array](../33-search-in-rotated-sorted-array/index.md), but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## Test Cases

``` python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
```

{% asset_code coding/assets/81-search-in-rotated-sorted-array-ii/solution_test.py %}

## Thoughts

[33. Search in Rotated Sorted Array](../33-search-in-rotated-sorted-array/index.md) 的进阶版，nums 中可能存在重复元素。

直接把 [problem 33](../33-search-in-rotated-sorted-array/index.md) 的代码搬过来（修改返回值为 bool）是不行的，有些 case 会失败。比如 `nums = [1,0,1,1,1]`、`target = 0`，那么初始时 `l = 0`、`r = 4`、`m = 2`，那么 `nums[l] == nums[m] == nums[r] == 1 ≠ 0`，无法确定数组的最小值（或最大值）在哪半边。一个简单的办法是同时收缩一点点两个边界，即令 `l = l + 1`、`r = r - 1`。

最坏情况下，每次都只能收缩一点点左右边界，时间复杂度 `O(n)`；但平均情况下时间复杂度 `O(log n)`。空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/81-search-in-rotated-sorted-array-ii/solution.py %}
