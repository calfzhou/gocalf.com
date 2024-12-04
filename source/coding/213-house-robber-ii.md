---
title: 213. House Robber II
notebook: coding
tags:
- medium
date: 2024-11-23 12:10:13
updated: 2024-11-23 12:10:13
---
## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

<https://leetcode.com/problems/house-robber-ii/>

**Example 1:**

> Input: `nums = [2,3,2]`
> Output: `3`
> Explanation: You cannot rob house 1 (`money = 2`) and then rob house 3 (`money = 2`), because they are adjacent houses.

**Example 2:**

> Input: `nums = [1,2,3,1]`
> Output: `4`
> Explanation: Rob house 1 (`money = 1`) and then rob house 3 (`money = 3`).
> Total amount you can rob `= 1 + 3 = 4`.

**Example 3:**

> Input: `nums = [1,2,3]`
> Output: `3`

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Test Cases

``` python
class Solution:
    def rob(self, nums: List[int]) -> int:
```

{% asset_code coding/213-house-robber-ii/solution_test.py %}

## Thoughts

[198. House Robber](198-house-robber) 的进阶版，限制第一个和最后一个房间也不能同时抢。

看如果不抢房间 0 能得到的最大金额，再看如果不抢房间 `n - 1` 能得到的最大金额，二者取较大即可。

注意，应该是「不抢 0 或者 不抢 `n - 1`」，而不是「抢 0 或者 抢 `n - 1`」，因为后者会漏掉「既不抢 0 也不抢 `n - 1`」这个可能性，而通过 [problem 198](198-house-robber) 的分析知道，两个相邻房间并不一定要都抢。

「不抢 0」对应于子问题 `nums[1:n]` 的解，而「不抢 `n - 1`」对应于子问题 `nums[0:n-1]` 的解。

当 `n = 1` 时需要特殊处理，因为这时候「不抢 0 或者 不抢 `n - 1`」的选择会丢到「抢 `0 = n - 1`」这个可能性。

## Code

{% asset_code coding/213-house-robber-ii/solution.py %}
