---
title: 624. Maximum Distance in Arrays
notebook: coding
tags:
- medium
date: 2025-02-19 10:06:46
updated: 2025-02-19 10:06:46
---
## Problem

You are given `m` `arrays`, where each array is sorted in **ascending order**.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference `|a - b|`.

Return _the maximum distance_.

<https://leetcode.cn/problems/maximum-distance-in-arrays/>

**Example 1:**

> Input: `arrays = [[1,2,3],[4,5],[1,2,3]]`
> Output: `4`
> Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

**Example 2:**

> Input: `arrays = [[1],[1]]`
> Output: `0`

**Constraints:**

- `m == arrays.length`
- `2 <= m <= 10⁵`
- `1 <= arrays[i].length <= 500`
- `-10⁴ <= arrays[i][j] <= 10⁴`
- `arrays[i]` is sorted in **ascending order**.
- There will be at most `10⁵` integers in all the arrays.

## Test Cases

```python
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

先取所有数组最大值（最后一个数字）的最大值记为 mx，所有数组最小值（第一个数字）的最小值记为 mn。

如果 mx 和 mn 来自不同的数组，那么结果为 `mx - mn`。

否则需要取所有数组最大值的第二大记为 mx2，所有数组最小值的第二小记为 mn2，那么结果为 `max{mx - mn2, mx2 - mn}`。

时间复杂度 `O(m)`，空间复杂度 `O(1)`。

## Code

{% snippet solution.py %}
