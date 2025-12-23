---
title: 3095. Shortest Subarray With OR at Least K I
notebook: coding
tags:
- easy
date: 2025-01-16 15:51:49
updated: 2025-01-16 15:51:49
---
## Problem

You are given an array `nums` of **non-negative** integers and an integer `k`.

An array is called **special** if the bitwise `OR` of all of its elements is **at least** `k`.

Return _the length of the **shortest** **special** **non-empty** subarray of_ `nums`, _or return_ `-1` _if no special subarray exists_.

> A **subarray** is a contiguous **non-empty** sequence of elements within an array.

<https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/>

**Example 1:**

> Input: `nums = [1,2,3], k = 2`
> Output: `1`
> Explanation:
> The subarray `[3]` has `OR` value of `3`. Hence, we return `1`.
> Note that `[2]` is also a special subarray.

**Example 2:**

> Input: `nums = [2,1,8], k = 10`
> Output: `3`
> Explanation:
> The subarray `[2,1,8]` has `OR` value of `11`. Hence, we return `3`.

**Example 3:**

> Input: `nums = [1,2], k = 0`
> Output: `1`
> Explanation:
> The subarray `[1]` has `OR` value of `1`. Hence, we return `1`.

**Constraints:**

- `1 <= nums.length <= 50`
- `0 <= nums[i] <= 50`
- `0 <= k < 64`

## Test Cases

``` python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
```

{% asset_code coding/3095-shortest-subarray-with-or-at-least-k-i/solution_test.py %}

## Thoughts

用滑动窗口。设当前窗口为 `[l, r)`，记 res 为 `nums[l:r]` 各个数字 `OR` 的结果。

如果 `res < k`，需要扩大窗口，取 `res = res | nums[r]`。因为 `OR` 运算会丢失一些信息，为了在缩小窗口的时候能快速更新 res，此时就要记录 res 的每个二进制位的贡献量。用 counts 数组记录 res 的每一个二进制位有几个贡献数字，也就是对 `nums[r]` 的每一个二进制 1 的位，在 counts 对应位置加一。然后给 r 增加 1 以扩大窗口。

如果 `res >= k`，当前窗口大小为 `r - l`，记录下窗口大小的最小值。然后缩小窗口，把 `nums[l]` 去掉，需要更新 res 的值。不妨设 res 的新值为 `res'`，那么 `res = nums[l] | res'`。这个值无法直接算出来，需要借助前边维护的 counts 数组，对 `nums[l]` 的每一个二进制 1 的位，在 counts 对应位置减一，如果该位的计数降为 0，就可以把 res 里对应位置为 0。然后给 l 增加 1 以缩小窗口。

时间复杂度 `O(n log k)`，空间复杂度 `O(log k)`。

> PS: `O(n)` 时间的算法参见 [3097. Shortest Subarray With OR at Least K II](../3097-shortest-subarray-with-or-at-least-k-ii/index.md)，同样适用本题。

## Code

{% asset_code coding/3095-shortest-subarray-with-or-at-least-k-i/solution.py %}
