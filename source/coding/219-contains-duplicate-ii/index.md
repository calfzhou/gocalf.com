---
title: 219. Contains Duplicate II
notebook: coding
tags:
- easy
date: 2025-01-29 22:36:39
updated: 2025-01-29 22:36:39
---
## Problem

Given an integer array `nums` and an integer `k`, return `true` _if there are two **distinct indices**_ `i` _and_ `j` _in the array such that_ `nums[i] == nums[j]` _and_ `abs(i - j) <= k`.

<https://leetcode.cn/problems/contains-duplicate-ii/>

**Example 1:**

> Input: `nums = [1,2,3,1], k = 3`
> Output: `true`

**Example 2:**

> Input: `nums = [1,0,1,1], k = 1`
> Output: `true`

**Example 3:**

> Input: `nums = [1,2,3,1,2,3], k = 2`
> Output: `false`

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`
- `0 <= k <= 10⁵`

## Test Cases

``` python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
```

{% asset_code coding/assets/219-contains-duplicate-ii/solution_test.py %}

## Thoughts

跟 [217. Contains Duplicate](../217-contains-duplicate/index.md) 差不多，增加了对元素下标间距的限制。可以把集合改成字典，记录见到的数字所在的下标，如果再次见到相同的数字，比较一下两次的下标即可。

## Code

{% asset_code coding/assets/219-contains-duplicate-ii/solution.py %}
