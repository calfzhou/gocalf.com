---
title: 689. Maximum Sum of 3 Non-Overlapping Subarrays
notebook: coding
tags:
- hard
date: 2024-12-28 19:55:39
updated: 2024-12-28 19:55:39
---
## Problem

Given an integer array `nums` and an integer `k`, find three non-overlapping subarrays of length `k` with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (**0-indexed**). If there are multiple answers, return the lexicographically smallest one.

<https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/>

**Example 1:**

> Input: `nums = [1,2,1,2,6,7,5,1], k = 2`
> Output: `[0,3,5]`
> Explanation: Subarrays `[1, 2]`, `[2, 6]`, `[7, 5]` correspond to the starting indices `[0, 3, 5]`.
> We could have also taken `[2, 1]`, but an answer of `[1, 3, 5]` would be lexicographically larger.

**Example 2:**

> Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
> Output: [0,2,4]

**Constraints:**

- `1 <= nums.length <= 2 * 10⁴`
- `1 <= nums[i] < 216`
- `1 <= k <= floor(nums.length / 3)`

## Test Cases

```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
```

{% asset_code coding/689-maximum-sum-of-3-non-overlapping-subarrays/solution_test.py %}

## Thoughts

不能直接贪心最大的 k-subarray，比如 Example 1 中，如果直接贪心，会取到 `[6, 7]`，然后是 `[5, 1]`，最后是 `[1, 2]`，总和只有 22。而最优解（`[1, 2]`、`[2, 6]`、`[7, 5]`）的总和是 23。

对于某个确定的中间子数组，应该选它左边和最大的一个子数组与它右边和最大的一个子数组。遍历所有可能位于中间的子数组，找出总和最大的组合即可。

显然中间子数组的起点下标的区间范围是 `[k, n-2k]`。如果当前中间子数组是 `nums[m:m+k]`，那么左边子数组的起点下标区间范围是 `[0, m-k]`，右边子数组的起点下标区间范围是 `[m+k, n-k]`。

利用动态规划的思想缓存一些中间结果减少计算量。

先对数组扫描一次，记录所有长度为 k 的子数组的和。如果已经知道子数组 `nums[i:i+k]` 的和，那么可以用常数时间计算 `nums[i+1:i+1+k]` 的和，即 `sum(nums[i+1:i+1+k]) = sum(nums[i:i+k]) - nums[i] + nums[i+k]`。

如果是从左到右扫描，还可以同时记录所有位置左边所有子数组中和最大的。但右边的暂时无法得到。

然后再反方向扫描，这一次可以得到当前位置右边所有子数组中和最大的，同时对于所有可能在中间的子数组，直接可以确定其左边最大的子数组以及右边最大的子数组分别在哪里。

时间复杂度 `O(n)`，空间复杂度 `O(n - k)`。

## Code

{% asset_code coding/689-maximum-sum-of-3-non-overlapping-subarrays/solution.py %}
