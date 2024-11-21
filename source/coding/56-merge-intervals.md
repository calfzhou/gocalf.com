---
title: 56. Merge Intervals
notebook: coding
tags:
- medium
date: 2024-11-18 20:55:28
updated: 2024-11-18 20:55:28
---
## Problem

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return _an array of the non-overlapping intervals that cover all the intervals in the input_.

<https://leetcode.com/problems/merge-intervals/>

**Example 1:**

> Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
> Output: `[[1,6],[8,10],[15,18]]`
> Explanation: Since intervals `[1,3]` and `[2,6]` overlap, merge them into `[1,6]`.

**Example 2:**

> Input: intervals = `[[1,4],[4,5]]`
> Output: `[[1,5]]`
> Explanation: Intervals `[1,4]` and `[4,5]` are considered overlapping.

**Constraints:**

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Test Cases

``` python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
```

{% asset_code coding/56-merge-intervals/solution_test.py %}

## Thoughts

按左端点排序所有的区间。

第一个区间就是合并后的第一个区间。任何时候，对于下一个原区间，看跟最后一个合并的区间是否有重叠。如果重叠就合并到一起（右端点取二者较大），否则就形成新的合并区间。

## Code

{% asset_code coding/56-merge-intervals/solution.py %}
