---
title: 1338. Reduce Array Size to The Half
notebook: coding
tags:
- medium
date: 2024-12-15 10:20:10
updated: 2024-12-15 10:20:10
---
## Problem

You are given an integer array `arr`. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return _the minimum size of the set so that **at least** half of the integers of the array are removed_.

<https://leetcode.cn/problems/reduce-array-size-to-the-half/>

**Example 1:**

> Input: `arr = [3,3,3,3,5,5,5,2,2,7]`
> Output: `2`
> Explanation: Choosing `{3,7}` will make the new array `[5,5,5,2,2]` which has size 5 (i.e equal to half of the size of the old array).
> Possible sets of size 2 are `{3,5},{3,2},{5,2}`.
> Choosing set `{2,7}` is not possible as it will make the new array `[3,3,3,3,5,5,5]` which has a size greater than half of the size of the old array.

**Example 2:**

> Input: `arr = [7,7,7,7,7,7]`
> Output: `1`
> Explanation: The only possible set you can choose is `{7}`. This will make the new array empty.

**Constraints:**

- `2 <= arr.length <= 10⁵`
- `arr.length` is even.
- `1 <= arr[i] <= 10⁵`

## Test Cases

``` python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
```

{% asset_code coding/1338-reduce-array-size-to-the-half/solution_test.py %}

## Thoughts

统计 `arr` 中每个不同数字出现的次数，对这些次数倒排序，从次数最多的开始取，直到大于等于 `arr` 长度的一半即可。

## Code

{% asset_code coding/1338-reduce-array-size-to-the-half/solution.py %}
