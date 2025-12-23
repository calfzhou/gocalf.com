---
title: 2080. Range Frequency Queries
notebook: coding
tags:
- medium
date: 2025-02-18 10:01:40
updated: 2025-02-18 10:01:40
---
## Problem

Design a data structure to find the **frequency** of a given value in a given subarray.

The **frequency** of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the `RangeFreqQuery` class:

- `RangeFreqQuery(int[] arr)` Constructs an instance of the class with the given **0-indexed** integer array `arr`.
- `int query(int left, int right, int value)` Returns the **frequency** of `value` in the subarray `arr[left...right]`.

A **subarray** is a contiguous sequence of elements within an array. `arr[left...right]` denotes the subarray that contains the elements of `nums` between indices `left` and `right` (**inclusive**).

<https://leetcode.cn/problems/range-frequency-queries/>

**Example 1:**

> Input
> `["RangeFreqQuery", "query", "query"]`
> `[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]`
> Output
> `[null, 1, 2]`
>
> Explanation
>
> ``` cpp
> RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
> rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
> rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.
> ```

**Constraints:**

- `1 <= arr.length <= 10⁵`
- `1 <= arr[i], value <= 10⁴`
- `0 <= left <= right < arr.length`
- At most `10⁵` calls will be made to `query`

## Test Cases

``` python
class RangeFreqQuery:

    def __init__(self, arr: List[int]):


    def query(self, left: int, right: int, value: int) -> int:



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```

{% asset_code coding/assets/2080-range-frequency-queries/solution_test.py %}

## Thoughts

在构造函数里对 arr 做预处理，记录下每个数字的所有出现的位置。每个数字的位置列表有有序数组，整体用字典。

查询时先看目标数字是否存在，不存在就直接返回 0。然后在该数字的位置列表中，用二分法查找 left 和 right 的插入位置，即找到大于等于 left 的最小的值、大于 right 的最小的值，这两个值在位置列表中的下标之差，就是 `arr[left...right]` 区间内指定数字的次数（跟 [1287. Element Appearing More Than 25% In Sorted Array](../1287-element-appearing-more-than-25-in-sorted-array/index.md) 类似）。

构造函数的时间复杂度 `O(n)`，`query` 方法的时间复杂度 `O(log n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/2080-range-frequency-queries/solution.py %}
