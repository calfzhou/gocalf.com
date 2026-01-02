---
title: 55. Jump Game
notebook: coding
tags:
- medium
date: 2024-11-18 19:04:15
updated: 2024-11-18 19:04:15
---
## Problem

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` _if you can reach the last index, or_ `false` _otherwise_.

<https://leetcode.com/problems/jump-game/>

**Example 1:**

> Input: `nums = [2,3,1,1,4]`
> Output: `true`
> Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Example 2:**

> Input: `nums = [3,2,1,0,4]`
> Output: `false`
> Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `0 <= nums[i] <= 10⁵`

## Test Cases

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
```

{% snippet solution_test.py %}

## Thoughts

从最右侧 `r = n - 1` 开始看。令 `l = r - 1`，如果 `nums[l] >= r - l` 说明从 l 可以跳到 r，那就令 `r = l` 继续。否则令 `l = l - 1` 继续。

最终如果 r 没有到达 0，说明最远也跳不到 r，更到不了终点，返回 `false`。

## Code

{% snippet solution.py %}
