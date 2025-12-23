---
title: 1726. Tuple with Same Product
notebook: coding
tags:
- medium
date: 2025-02-06 10:55:52
updated: 2025-02-06 10:55:52
---
## Problem

Given an array `nums` of **distinct** positive integers, return _the number of tuples_ `(a, b, c, d)` _such that_ `a * b = c * d` _where_ `a`_,_ `b`_,_ `c`_, and_ `d` _are elements of_ `nums`_, and_ `a != b != c != d`_._

<https://leetcode.com/problems/tuple-with-same-product/>

**Example 1:**

> Input: `nums = [2,3,4,6]`
> Output: `8`
> Explanation: There are 8 valid tuples:
>
> ``` cpp
> (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
> (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
> ```

**Example 2:**

> Input: `nums = [1,2,4,5,10]`
> Output: `16`
> Explanation: There are 16 valid tuples:
>
> ``` cpp
> (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
> (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
> (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
> (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
> ```

**Constraints:**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10⁴`
- All elements in `nums` are **distinct**.

## Test Cases

``` python
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
```

{% asset_code coding/assets/1726-tuple-with-same-product/solution_test.py %}

## Thoughts

枚举 nums 中所有可能的数字对，计算每个数字对之积，并统计每个可能的乘积能对应多少个数字对。

设某个乘积共有 m 个可能的数字对，因为 nums 中的数字是各不相同的正整数，可知这 m 个数字对是由各不相同的共 `2m` 个数字构成的。从 m 个数字对中任选两个做排列，有 `m * (m - 1)` 种可能，选中的每对数字都可以有两种顺序，所以总共有 `4 * m * (m - 1)` 种可能。

时间复杂度 `O(n²)`，空间复杂度 `O(n²)`。

## Code

{% asset_code coding/assets/1726-tuple-with-same-product/solution.py %}
