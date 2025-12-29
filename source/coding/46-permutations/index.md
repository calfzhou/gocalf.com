---
title: 46. Permutations
notebook: coding
tags:
- easy
date: 2025-02-06 09:26:43
updated: 2025-02-06 09:26:43
---
## Problem

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

> A permutation is a rearrangement of all the elements of an array.

<https://leetcode.cn/problems/permutations/>

**Example 1:**

> Input: `nums = [1,2,3]`
> Output: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

**Example 2:**

> Input: `nums = [0,1]`
> Output: `[[0,1],[1,0]]`

**Example 3:**

> Input: `nums = [1]`
> Output: `[[1]]`

**Constraints:**

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Test Cases

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
```

{% asset_code coding/46-permutations/solution_test.py %}

## Thoughts

用回溯法。

排列的第一个数字有 n 种选择，第二个数字有 `n - 1` 种选择，……。一共有 `n!` 种不同的排列。

时间复杂度 `O(n!)`，额外的空间复杂度 `O(n²)`（因为目前的实现，每一层递归需要用 `O(n)` 辅助空间。

也可以只用 `O(n)` 辅助空间，记录每个数字是否已经用在当前排列，而时间复杂度为 `O(nⁿ)`。

## Code

{% asset_code coding/46-permutations/solution.py %}
