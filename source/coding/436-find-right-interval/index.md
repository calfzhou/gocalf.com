---
title: 436. Find Right Interval
notebook: coding
tags:
- medium
date: 2025-01-02 21:26:01
updated: 2025-01-02 21:26:01
---
## Problem

You are given an array of `intervals`, where `intervals[i] = [startᵢ, endᵢ]` and each `startᵢ` is **unique**.

The **right interval** for an interval `i` is an interval `j` such that `startⱼ >= endᵢ` and `startⱼ` is **minimized**. Note that `i` may equal `j`.

Return _an array of **right interval** indices for each interval `i`_. If no **right interval** exists for interval `i`, then put `-1` at index `i`.

<https://leetcode.com/problems/find-right-interval/>

**Example 1:**

> Input: `intervals = [[1,2]]`
> Output: `[-1]`
> Explanation: There is only one interval in the collection, so it outputs -1.

**Example 2:**

> Input: `intervals = [[3,4],[2,3],[1,2]]`
> Output: `[-1,0,1]`
> Explanation: There is no right interval for `[3,4]`.
> The right interval for `[2,3]` is `[3,4]` since `start0 = 3` is the smallest start that is `>= end1 = 3`.
> The right interval for `[1,2]` is `[2,3]` since `start1 = 2` is the smallest start that is `>= end2 = 2`.

**Example 3:**

> Input: `intervals = [[1,4],[2,3],[3,4]]`
> Output: `[-1,2,-1]`
> Explanation: There is no right interval for `[1,4]` and `[3,4]`.
> The right interval for `[2,3]` is `[3,4]` since `start2 = 3` is the smallest start that is `>= end1 = 3`.

**Constraints:**

- `1 <= intervals.length <= 2 * 10⁴`
- `intervals[i].length == 2`
- `-10⁶ <= startᵢ <= endᵢ <= 10⁶`
- The start point of each interval is **unique**.

## Test Cases

``` python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
```

{% asset_code coding/436-find-right-interval/solution_test.py %}

## Thoughts

对所有的区间按起点坐标排序，然后对某个区间，用二分搜索查找区间终点的插入位置，此位置对应的区间即为其「右区间」。因为区间一定不会出现在区间起点的左边，所以可以只对排序后当前区间开始的右半个数组做二分搜索（代码中 `lo=idx` 参数）。

时间复杂度 `O(n log n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/436-find-right-interval/solution.py %}
