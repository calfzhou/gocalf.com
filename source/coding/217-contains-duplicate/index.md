---
title: 217. Contains Duplicate
notebook: coding
tags:
- easy
date: 2024-11-23 13:11:24
updated: 2024-11-23 13:11:24
---
## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

<https://leetcode.com/problems/contains-duplicate/>

**Example 1:**

> Input: `nums = [1,2,3,1]`
> Output: `true`
> Explanation:
> The element 1 occurs at the indices 0 and 3.

**Example 2:**

> Input: `nums = [1,2,3,4]`
> Output: `false`
> Explanation:
> All elements are distinct.

**Example 3:**

> Input: `nums = [1,1,1,3,3,4,3,2,4,2]`
> Output: `true`

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`

## Test Cases

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
```

{% asset_code coding/217-contains-duplicate/solution_test.py %}

## Thoughts

用集合检查数字是否已经见过。

## Code

{% asset_code coding/217-contains-duplicate/solution.py %}
