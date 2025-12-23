---
title: 3254. Find the Power of K-Size Subarrays I
notebook: coding
tags:
- medium
date: 2024-11-27 16:48:54
updated: 2024-11-27 16:48:54
---
## Problem

You are given an array of integers `nums` of length `n` and a _positive_ integer `k`.

The **power** of an array is defined as:

- Its **maximum** element if _all_ of its elements are **consecutive** and **sorted** in **ascending** order.
- `-1` otherwise.

You need to find the **power** of all subarrays of `nums` of size `k`.

> A **subarray** is a contiguous **non-empty** sequence of elements within an array.

Return an integer array `results` of size `n - k + 1`, where `results[i]` is the _power_ of `nums[i..(i + k - 1)]`.

<https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/>

**Example 1:**

> Input: `nums = [1,2,3,4,3,2,5], k = 3`
> Output: `[3,4,-1,-1,-1]`
> Explanation:
> There are 5 subarrays of `nums` of size 3:
>
> - `[1, 2, 3]` with the maximum element 3.
> - `[2, 3, 4]` with the maximum element 4.
> - `[3, 4, 3]` whose elements are not consecutive.
> - `[4, 3, 2]` whose elements are not sorted.
> - `[3, 2, 5]` whose elements are not consecutive.

**Example 2:**

> Input: `nums = [2,2,2,2,2], k = 4`
> Output: `[-1,-1]`

**Example 3:**

> Input: `nums = [3,2,3,2,3,2], k = 2`
> Output: `[-1,3,-1,3,-1]`

**Constraints:**

- `1 <= n == nums.length <= 500`
- `1 <= nums[i] <= 10⁵`
- `1 <= k <= n`

## Test Cases

``` python
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
```

{% asset_code coding/assets/3254-find-the-power-of-k-size-subarrays-i/solution_test.py %}

## Thoughts

跟 [3208. Alternating Groups II](../3208-alternating-groups-ii/index.md) 基本是同一个问题，只是数组首尾不再相接，连续条件从颜色交替变为 `+1` 递增。直接在其代码基础上修改一下就行了。

时间复杂度 `O(n)`（没有首尾相接，所以不需要 `O(n + k)`）。

## Code

{% asset_code coding/assets/3254-find-the-power-of-k-size-subarrays-i/solution.py %}
