---
title: 90. Subsets II
notebook: coding
tags:
- easy
date: 2025-02-05 09:55:31
updated: 2025-02-05 09:55:31
---
## Problem

Given an integer array `nums` that may contain duplicates, return _all possible subsets (the power set)_.

> A **subset** of an array is a selection of elements (possibly none) of the array.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

<https://leetcode.cn/problems/subsets-ii/>

**Example 1:**

> Input: `nums = [1,2,2]`
> Output: `[[],[1],[1,2],[1,2,2],[2],[2,2]]`

**Example 2:**

> Input: `nums = [0]`
> Output: `[[],[0]]`

**Constraints:**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Test Cases

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
```

{% asset_code coding/90-subsets-ii/solution_test.py %}

## Thoughts

[78. Subsets](../78-subsets/index.md) 的进阶版，nums 中可能有重复的元素，但是结果中不能有重复的子集。

在 [problem 78](../78-subsets/index.md) 中，每个数字的词频为 1，只有选中和不选中两种可能。本题因为可能有重复的数字，先统计每个数字的次数。设一个数字 a 的词频为 k，那么子集中可以有 0 个 a、1 个 a、……、k 个 a 共 `k + 1` 中可能。

用回溯法，对每个数字穷举每种可能下可以得到的所有子集。

时间复杂度 `O(2^n)`，额外的空间复杂度 `O(n)`。

## Code

{% asset_code coding/90-subsets-ii/solution.py %}
