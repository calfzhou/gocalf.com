---
title: 164. Maximum Gap
notebook: coding
tags:
- medium
katex: true
date: 2024-12-31 23:34:10
updated: 2024-12-31 23:34:10
---
## Problem

Given an integer array `nums`, return _the maximum difference between two successive elements in its sorted form_. If the array contains less than two elements, return `0`.

You must write an algorithm that runs in linear time and uses linear extra space.

<https://leetcode.com/problems/maximum-gap/>

**Example 1:**

> Input: `nums = [3,6,9,1]`
> Output: `3`
> Explanation: The sorted form of the array is `[1,3,6,9]`, either `(3,6)` or `(6,9)` has the maximum difference 3.

**Example 2:**

> Input: `nums = [10]`
> Output: `0`
> Explanation: The array contains less than 2 elements, therefore return 0.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `0 <= nums[i] <= 10⁹`

## Test Cases

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

是要找出数组在排序之后，相邻元素之间最大的差值。

要求线性时间和空间复杂度，考虑用基数排序。题目限定 nums 的长度是 `O(10⁵)`，而 nums 中数字的大小是 `O(10⁹)`，一个数一个桶肯定不现实，空间开销太大了。

关键在于控制桶的大小，以便做到每个桶只占用常数空间。如果桶太大，排序后相邻元素的最大差值（后边简称「最大差值」）可能会出现在某个桶内，那就必须记录下桶内的所有数字，没有节省空间。如果桶太小，那么桶的数量就会很多，空间开销也大。

需要让桶的大小，刚好能够确保最大差值不会出现在某个桶内，这样就不用记录桶内所有的元素（只需要记录最大值和最小值）。

设 nums 中的最大值和最小值分别为 mx 和 mn。根据鸽笼原理易知，最大差值的下限为 $\lceil\frac{mx-mn}{n-1}\rceil$，以此大小（记为 sz）分桶，那么桶内数字的最大差值只能达到 `sz - 1`，题目所求的 nums 的最大差值一定出现在两个桶之间（后边桶内最小值减去前边桶内最大值）。

需要的桶的个数为 $\lfloor\frac{mx-mn}{sz}\rfloor+1=O(n)$。

> 小心 `sz = 0` 导致的除零刺客！当 `mx = mn` 时，直接返回 0 即可。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

> 不过实际提交的话，桶排序的的耗时是快排的 2 到 10 倍。因为 n 的上限只有 10⁵，`log(10⁵) ≈ 17`，比桶排序实操下来的常数系统小的多。

## Code

{% snippet solution.py %}
