---
title: 954. Array of Doubled Pairs
notebook: coding
tags:
- medium
date: 2024-12-09 16:19:51
updated: 2024-12-09 16:19:51
---
## Problem

Given an integer array of even length `arr`, return `true` _if it is possible to reorder_ `arr` _such that_ `arr[2 * i + 1] = 2 * arr[2 * i]` _for every_ `0 <= i < len(arr) / 2`_, or_ `false` _otherwise_.

<https://leetcode.com/problems/array-of-doubled-pairs/>

**Example 1:**

> Input: `arr = [3,1,3,6]`
> Output: `false`

**Example 2:**

> Input: `arr = [2,1,2,6]`
> Output: `false`

**Example 3:**

> Input: `arr = [4,-2,2,-4]`
> Output: `true`
> Explanation: We can take two groups, `[-2,-4]` and `[2,4]` to form `[-2,-4,2,4]` or `[2,4,-2,-4]`.

**Constraints:**

- `2 <= arr.length <= 3 * 10⁴`
- `arr.length` is even.
- `-10⁵ <= arr[i] <= 10⁵`

## Test Cases

``` python
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
```

{% asset_code coding/954-array-of-doubled-pairs/solution_test.py %}

## Thoughts

对于 `arr` 中任意一个值 `val`，`val * 2` 或 `val / 2` 需要也在 `arr` 中，把 `val` 和对应的值拿掉，剩下的数组也满足相同性质。但是事先不知道应该是哪种可能，如果直接做判断，可能会把其他 pair 错误地拆开导致最终判断失误。

考虑对 `arr` 排序。对于正数 `val`，显然有 `0 < val/2 < val < val*2`；反之对于负数 `val`，有 `val*2 < val < val/2 < 0`。按从小到大的顺序扫描剩下的值，根据其正负性，可以确定应该找 `val / 2` 还是 `val * 2`。也可以按照绝对值排序，那么按绝对值从小到大扫描的时候，始终都检查 `val * 2` 即可。

用 [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) 或类似结构记录 `arr` 中每个数字的次数。从 `arr` 中移除的动作可以通过在计数中减一来替代实现。而且可以直接对 `Counter` 进行排序，当 `arr` 中重复的元素很多时，能节省不少排序的时间。

时间复杂度 `O(n log n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/954-array-of-doubled-pairs/solution.py %}
