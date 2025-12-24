---
title: 33. Search in Rotated Sorted Array
notebook: coding
tags:
- medium
date: 2024-11-15 18:35:36
updated: 2024-11-15 18:35:36
---
## Problem

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of_ `target` _if it is in_ `nums`_, or_ `-1` _if it is not in_ `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

<https://leetcode.com/problems/search-in-rotated-sorted-array/>

**Example 1:**

> Input: `nums = [4,5,6,7,0,1,2], target = 0`
> Output: `4`

**Example 2:**

> Input: `nums = [4,5,6,7,0,1,2], target = 3`
> Output: `-1`

**Example 3:**

> Input: `nums = [1], target = 0`
> Output: `-1`

**Constraints:**

- `1 <= nums.length <= 5000`
- `-10⁴ <= nums[i] <= 10⁴`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10⁴ <= target <= 10⁴`

## Test Cases

``` python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
```

{% asset_code coding/33-search-in-rotated-sorted-array/solution_test.py %}

## Thoughts

算是 [153. Find Minimum in Rotated Sorted Array](../153-find-minimum-in-rotated-sorted-array/index.md) 的微量进阶版。

在二分的过程中，如果当前子数组已经是完全有序的（`nums[l] < nums[r]`），直接按二分法继续搜索即可。

否则，根据 [problem 153](../153-find-minimum-in-rotated-sorted-array/index.md) 也可以知道子数组的最小值（或最大值）在哪半边。

不妨设最小值在右半边，那么左半边是 `nums[l]` 到 `nums[m]` 的有序子数组，而右半边的值要么大于 `nums[m]` 要么小于 `nums[r]`。看 `target` 和这三个值的大小关系，便可以确定下一步应该在哪个半边继续搜索。

各种情况如下图示（`L = nums[l], M = nums[m], R = nums[r]`）。

{% invert %}
{% diagramsnet cases.drawio %}
{% endinvert %}

其中 t1、t3、t6、t7 四种情况下，需要进入左半边，而 t2、t4、t5、t8 情况需要进入右半边。每种情况的判定条件根据图示可以确定下来。

## Code

{% asset_code coding/33-search-in-rotated-sorted-array/solution.py %}

这里 `while` 循环的条件可以直接用 `while l <= r`（[problem 153](../153-find-minimum-in-rotated-sorted-array/index.md) 用的是 `while l < r - 1` 加收尾处理）。
