---
title: 57. Insert Interval
notebook: coding
tags:
- medium
date: 2024-11-18 22:38:58
updated: 2024-11-18 22:38:58
---
## Problem

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [startᵢ, endᵢ]` represent the start and the end of the `iᵗʰ` interval and `intervals` is sorted in ascending order by `startᵢ`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `startᵢ` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` _after the insertion_.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

<https://leetcode.com/problems/insert-interval/>

**Example 1:**

> Input: `intervals = [[1,3],[6,9]], newInterval = [2,5]`
> Output: `[[1,5],[6,9]]`

**Example 2:**

> Input: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]`
> Output: `[[1,2],[3,10],[12,16]]`
> Explanation: Because the new interval `[4,8]` overlaps with `[3,5],[6,7],[8,10]`.

**Constraints:**

- `0 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= startᵢ <= endᵢ <= 10⁵`
- `intervals` is sorted by `startᵢ` in **ascending** order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10⁵`

## Test Cases

``` python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
```

{% asset_code coding/57-insert-interval/solution_test.py %}

## Thoughts

可以用二分法在原区间数组中，找出右端点小于（不等于）`start` 的最后一个区间（都小于则算 -1），记为 `after`。

看 `after` 之后的区间，逐个与 `newInterval` 比较，如果与 `newInterval` 重叠则合并到 `newInterval`。最后用 `newInterval` 替换掉这些区间即可。

虽然查找是 `O(log n)` 时间，但跟后边的区间判定是否重叠，以及把 `newInterval` 替换进去可能造成后边的数组元素往前移动，最终时间复杂度还是 `O(n)`。

实际上题目没有要求 in-place 插入，那就直接开新数组即可，也就不需要二分查找了，从头开始逐个比较即可。

## Code

{% asset_code coding/57-insert-interval/solution.py %}

依然使用了二分查找，练一下用二分法查找小于目标值的最大的元素。
