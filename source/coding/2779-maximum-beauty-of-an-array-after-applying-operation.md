---
title: 2779. Maximum Beauty of an Array After Applying Operation
notebook: coding
tags:
- medium
date: 2024-12-11 11:50:48
updated: 2024-12-11 11:50:48
---
## Problem

You are given a **0-indexed** array `nums` and a **non-negative** integer `k`.

In one operation, you can do the following:

- Choose an index `i` that **hasn't been chosen before** from the range `[0, nums.length - 1]`.
- Replace `nums[i]` with any integer from the range `[nums[i] - k, nums[i] + k]`.

The **beauty** of the array is the length of the longest subsequence consisting of equal elements.

Return _the **maximum** possible beauty of the array_ `nums` _after applying the operation any number of times._

**Note** that you can apply the operation to each index **only once**.

A **subsequence** of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the order of the remaining elements.

<https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/>

**Example 1:**

> Input: `nums = [4,6,1,2], k = 2`
> Output: `3`
> Explanation: In this example, we apply the following operations:
>
> - Choose index 1, replace it with 4 (from range `[4,8]`), `nums = [4,4,1,2]`.
> - Choose index 3, replace it with 4 (from range `[0,4]`), `nums = [4,4,1,4]`.
>
> After the applied operations, the beauty of the array `nums` is 3 (subsequence consisting of indices 0, 1, and 3).
> It can be proven that 3 is the maximum possible length we can achieve.

**Example 2:**

> Input: `nums = [1,1,1,1], k = 10`
> Output: `4`
> Explanation: In this example we don't have to apply any operations.
> The beauty of the array `nums` is 4 (whole array).

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `0 <= nums[i], k <= 10⁵`

## Test Cases

``` python
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
```

{% asset_code coding/assets/2779-maximum-beauty-of-an-array-after-applying-operation/solution_test.py %}

## Thoughts

相当于把 `nums` 中所有的数字摆放在数轴上，拿一个长度为 `2 * k` 的区间去覆盖，看最多可以覆盖到多少个数字。

所以先对 `nums` 排序。然后用移动窗口从左到右扫描，让窗口（在数轴上的）宽度始终保持不超过 `2 * k`，记录窗口内的数字个数的最大值即可。

时间复杂度 `O(n log n)`，空间复杂度 `O(1)`（对 `nums` 做 in-place 排序）。

## Code

{% asset_code coding/assets/2779-maximum-beauty-of-an-array-after-applying-operation/solution.py %}

一个可选的优化是窗口在移动过程中，即使（在数轴上的）宽度已经超过 `2 * k`，也并不需要真的缩小窗口，而是维持之前的大小继续往右移动。直到移动到某个位置，（在数轴上的）宽度又小于 `2 * k`，再扩大窗口。也就是说窗口的大小只增不减，直接用自身记录可行窗口的最大大小。

实现的时候实际记录的是窗口的左端点。随着右端点的不断右移，如果可以扩大窗口，就保持左端点不动；否则就同步右移左端点（保持窗口大小不动）。

时间复杂度不变，可以减少一些操作次数。

{% asset_code coding/assets/2779-maximum-beauty-of-an-array-after-applying-operation/solution2.py %}
