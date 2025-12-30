---
title: 45. Jump Game II
notebook: coding
tags:
- medium
- todo
katex: true
date: 2025-01-27 21:07:31
updated: 2025-01-27 21:07:31
---
## Problem

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

- `0 <= j <= nums[i]` and
- `i + j < n`

Return _the minimum number of jumps to reach_ `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

<https://leetcode.cn/problems/jump-game-ii/>

**Example 1:**

> Input: nums = [2,3,1,1,4]
> Output: 2
> Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Example 2:**

> Input: nums = [2,3,0,1,4]
> Output: 2

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

## Test Cases

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

跟 [55. Jump Game](../55-jump-game/index.md) 类似。

记 `dp(i)` 表示从位置 i 跳到 `n - 1` 的最少跳数，可知

$$
dp(i)=1+\min_{j=i+1}^{i+nums[i]}{dp(j)}
$$

即从位置 i 先跳一次到 j，再从 j 用最少次数跳到 `n - 1`。所有可能的跳法中取总次数最少的。

初值 `dp(n - 1) = 0`，结果取 `dp(0)`。

时间复杂度 `O(n * m)`，空间复杂度 `O(n)`，其中 m 是 nums 中数值的大小。

## Code

{% asset_code solution.py %}

## Faster

`O(n)` 时间的算法，TODO。
