---
title: 349. Intersection of Two Arrays
notebook: coding
tags:
- easy
date: 2025-01-30 21:08:44
updated: 2025-01-30 21:08:44
---
## Problem

Given two integer arrays `nums1` and `nums2`, return _an array of their intersection_. Each element in the result must be **unique** and you may return the result in **any order**.

<https://leetcode.cn/problems/intersection-of-two-arrays/>

**Example 1:**

> Input: `nums1 = [1,2,2,1], nums2 = [2,2]`
> Output: `[2]`

**Example 2:**

> Input: `nums1 = [4,9,5], nums2 = [9,4,9,8,4]`
> Output: `[9,4]`
> Explanation: `[4,9]` is also accepted.

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Test Cases

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
```

{% asset_code coding/349-intersection-of-two-arrays/solution_test.py %}

## Thoughts

用集合记录两个数组的数字，求交集即可。

时间复杂度 `O(m + n)`，空间复杂度 `O(m + n)`。

## Code

{% asset_code coding/349-intersection-of-two-arrays/solution.py %}
