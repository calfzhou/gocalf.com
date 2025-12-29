---
title: 3046. Split the Array
notebook: coding
tags:
- easy
date: 2024-12-28 00:28:20
updated: 2024-12-28 00:28:20
---
## Problem

You are given an integer array `nums` of **even** length. You have to split the array into two parts `nums1` and `nums2` such that:

- `nums1.length == nums2.length == nums.length / 2`.
- `nums1` should contain **distinct** elements.
- `nums2` should also contain **distinct** elements.

Return `true` _if it is possible to split the array, and_ `false` _otherwise_.

<https://leetcode.cn/problems/split-the-array/>

**Example 1:**

> Input: `nums = [1,1,2,2,3,4]`
> Output: `true`
> Explanation: One of the possible ways to split nums is `nums1 = [1,2,3]` and `nums2 = [1,2,4]`.

**Example 2:**

> Input: `nums = [1,1,1,1]`
> Output: `false`
> Explanation: The only possible way to split nums is `nums1 = [1,1]` and `nums2 = [1,1]`. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.

**Constraints:**

- `1 <= nums.length <= 100`
- `nums.length % 2 == 0`
- `1 <= nums[i] <= 100`

## Test Cases

```python
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
```

{% asset_code coding/3046-split-the-array/solution_test.py %}

## Thoughts

扫描数组，用字典记录每一个数字的次数，如果任何一个数字的次数超过 2 就返回 false。

可以用 Python 自带的 [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter)。但如果自己写循环处理，有可能更早地发现无法拆分，能节省一些时间。

## Code

{% asset_code coding/3046-split-the-array/solution.py %}
