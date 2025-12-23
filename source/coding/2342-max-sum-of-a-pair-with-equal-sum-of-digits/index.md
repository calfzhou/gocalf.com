---
title: 2342. Max Sum of a Pair With Equal Sum of Digits
notebook: coding
tags:
- medium
date: 2025-02-12 10:09:30
updated: 2025-02-12 10:09:30
---
## Problem

You are given a **0-indexed** array `nums` consisting of **positive** integers. You can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the number `nums[i]` is equal to that of `nums[j]`.

Return _the **maximum** value of_ `nums[i] + nums[j]` _that you can obtain over all possible indices_ `i` _and_ `j` _that satisfy the conditions._

<https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/>

**Example 1:**

> Input: `nums = [18,43,36,13,7]`
> Output: `54`
> Explanation: The pairs `(i, j)` that satisfy the conditions are:
>
> - `(0, 2)`, both numbers have a sum of digits equal to 9, and their sum is `18 + 36 = 54`.
> - `(1, 4)`, both numbers have a sum of digits equal to 7, and their sum is `43 + 7 = 50`.
>
> So the maximum sum that we can obtain is 54.

**Example 2:**

> Input: `nums = [10,12,19,14]`
> Output: `-1`
> Explanation: There are no two numbers that satisfy the conditions, so we return -1.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`

## Test Cases

``` python
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
```

{% asset_code coding/2342-max-sum-of-a-pair-with-equal-sum-of-digits/solution_test.py %}

## Thoughts

先按 "sum of digits of the number" 把 nums 分组，用一个字典记录分组结果。

每组数字只需要保留最大的两个，以便得到这一组数字的最大和，所以字典的值可以用大小不超过 2 的最小堆。

对所有的数字分组之后，遍历所有分组，如果一个分组里有至少两个数字，就可以计算这一组数字的最大和。所有组的最大和取最大即可。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/2342-max-sum-of-a-pair-with-equal-sum-of-digits/solution.py %}
