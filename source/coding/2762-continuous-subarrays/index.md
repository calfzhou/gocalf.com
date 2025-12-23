---
title: 2762. Continuous Subarrays
notebook: coding
tags:
- medium
date: 2024-12-14 12:12:44
updated: 2024-12-14 12:12:44
---
## Problem

You are given a **0-indexed** integer array `nums`. A subarray of `nums` is called **continuous** if:

- Let `i`, `i + 1`, ..., `j` be the indices in the subarray. Then, for each pair of indices `i <= i₁, i₂ <= j`, `0 <= |nums[i₁] - nums[i₂]| <= 2`.

Return _the total number of **continuous** subarrays._

A subarray is a contiguous **non-empty** sequence of elements within an array.

<https://leetcode.com/problems/continuous-subarrays/>

**Example 1:**

> Input: `nums = [5,4,2,4]`
> Output: `8`
> Explanation:
> Continuous subarray of size 1: `[5], [4], [2], [4]`.
> Continuous subarray of size 2: `[5,4], [4,2], [2,4]`.
> Continuous subarray of size 3: `[4,2,4]`.
> Thereare no subarrys of size 4.
> Total continuous subarrays `= 4 + 3 + 1 = 8`.
> It can be shown that there are no more continuous subarrays.

**Example 2:**

> Input: `nums = [1,2,3]`
> Output: `6`
> Explanation:
> Continuous subarray of size 1: `[1], [2], [3]`.
> Continuous subarray of size 2: `[1,2], [2,3]`.
> Continuous subarray of size 3: `[1,2,3]`.
> Total continuous subarrays `= 3 + 2 + 1 = 6`.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`

## Test Cases

``` python
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
```

{% asset_code coding/2762-continuous-subarrays/solution_test.py %}

## Thoughts

用滑动窗口扫描数组，跟 [3258. Count Substrings That Satisfy K-Constraint I](../3258-count-substrings-that-satisfy-k-constraint-i/index.md) 几乎一致。但是在 [problem 3258](../3258-count-substrings-that-satisfy-k-constraint-i/index.md) 中每次是统计 i 开头的子串数，这里改成统计 j 结尾的子数组数，这样最会留个尾数需要加。

移窗过程中的操作类似于 [76. Minimum Window Substring](../76-minimum-window-substring/index.md)，用哈希表记录当前窗口中不同数字的个数。可以用常数时间判定当前窗口是否符合要求，当窗口移动时也用常数时间更新哈希表。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/2762-continuous-subarrays/solution.py %}
