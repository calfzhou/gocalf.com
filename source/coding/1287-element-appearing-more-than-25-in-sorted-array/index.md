---
title: 1287. Element Appearing More Than 25% In Sorted Array
notebook: coding
tags:
- easy
date: 2025-02-17 11:03:18
updated: 2025-02-17 11:03:18
---
## Problem

Given an integer array **sorted** in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

<https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/>

**Example 1:**

> Input: `arr = [1,2,2,6,6,6,6,7,10]`
> Output: `6`

**Example 2:**

> Input: `arr = [1,1]`
> Output: `1`

**Constraints:**

- `1 <= arr.length <= 10⁴`
- `0 <= arr[i] <= 10⁵`

## Test Cases

```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
```

{% asset_code coding/1287-element-appearing-more-than-25-in-sorted-array/solution_test.py %}

## Thoughts

> 此题如果按照 easy 难度去做，应该直接遍历一遍 arr 吧。

先看一些特例：

- 如果 arr 的长度为 1，那么这唯一的元素即为所求。
- 如果 arr 的长度小于 8，那么所求的数字应该会出现超过一次，且不会有其他数字出现超过一次，可以遍历 arr，找到与前一个数字相等的数字，即为所求。

对于一般的情况，看 arr 的 25%、50% 和 75% 分位点，所求的数字一定是这三个数字中的某一个，只需要分别统计这三个数字的总次数，看超过 25% 的是谁。对于任意的 n，显然所求数字的最小次数为 `n // 4 + 1`。

对于指定的数字 num（`num ∈ arr`），可以用两次二分法找出 arr 中 num 的左右边界 `[l, r)`，其中 `arr[l]` 是第一个 num，`arr[r]` 是最后一个 num 右边的位置。用 Python 的 [`bisect_left`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left) 可以得到 l，[`bisect_right`](https://docs.python.org/3/library/bisect.html#bisect.bisect_right) 可以得到 r，`r - l` 即为 num 的次数。

> 实际上不也可以不管前边提到的「特例」，直接看三个分位点数字的个数即可。

时间复杂度 `O(log n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/1287-element-appearing-more-than-25-in-sorted-array/solution.py %}
