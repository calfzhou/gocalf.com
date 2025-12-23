---
title: 78. Subsets
notebook: coding
tags:
- easy
date: 2025-02-05 09:09:36
updated: 2025-02-05 09:10:12
---
## Problem

Given an integer array `nums` of **unique** elements, return _all possible subsets (the power set)_.

> A **subset** of an array is a selection of elements (possibly none) of the array.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

<https://leetcode.cn/problems/subsets/>

**Example 1:**

> Input: `nums = [1,2,3]`
> Output: `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`

**Example 2:**

> Input: `nums = [0]`
> Output: `[[],[0]]`

**Constraints:**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Test Cases

``` python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
```

{% asset_code coding/assets/78-subsets/solution_test.py %}

## Thoughts

设 nums 中有 n 个元素，每个元素都可以被选中或不被选中，一共有 `2^n` 个各不相同的子集，对应了 0 到 `2^n` 的每一个整数。

可以直接从 0 遍历到 `2^n`，对于每个数字，以其二进制位 0 或 1 的情况确定是否选中对应位置元素构成一个子集。

时间复杂度 `O(2^n)`，额外的空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/78-subsets/solution.py %}
