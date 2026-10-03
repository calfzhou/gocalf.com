---
title: 2239. Find Closest Number to Zero
notebook: coding
tags:
- easy
date: 2025-01-20 21:00:20
updated: 2025-01-20 21:00:20
---
## Problem

Given an integer array `nums` of size `n`, return _the number with the value **closest** to_ `0` _in_ `nums`. If there are multiple answers, return _the number with the **largest** value_.

<https://leetcode.cn/problems/find-closest-number-to-zero/>

**Example 1:**

> Input: `nums = [-4,-2,1,4,8]`
> Output: `1`
> Explanation:
> The distance from -4 to 0 is `|-4| = 4`.
> The distance from -2 to 0 is `|-2| = 2`.
> The distance from 1 to 0 is `|1| = 1`.
> The distance from 4 to 0 is `|4| = 4`.
> The distance from 8 to 0 is `|8| = 8`.
> Thus, the closest number to 0 in the array is 1.

**Example 2:**

> Input: `nums = [2,-1,1]`
> Output: `1`
> Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

**Constraints:**

- `1 <= n <= 1000`
- `-10⁵ <= nums[i] <= 10⁵`

## Test Cases

```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

直接遍历 nums，记录绝对值最小的数字。如果绝对值相等，则保留较大的。

## Code

{% snippet solution.py %}
