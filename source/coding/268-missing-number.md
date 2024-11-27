---
title: 268. Missing Number
notebook: coding
tags:
- easy
date: 2024-11-12 18:36:18
updated: 2024-11-12 18:36:18
---
## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return _the only number in the range that is missing from the array._

<https://leetcode.com/problems/missing-number/>

**Example 1:**

> Input: `nums = [3,0,1]`
> Output: `2`
> Explanation: n = 3 since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in nums.

**Example 2:**

> Input: `nums = [0,1]`
> Output: `2`
> Explanation: n = 2 since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in nums.

**Example 3:**

> Input: `nums = [9,6,4,2,3,5,7,0,1]`
> Output: `8`
> Explanation: n = 9 since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in nums.

**Constraints:**

- `n == nums.length`
- `1 <= n <= 10⁴`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## Test Cases

``` python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
```

{% asset_code coding/268-missing-number/solution_test.py %}

## Thoughts

把提供的数字全部累加起来，结果与 0 到 n 的累加结果 `n * (n + 1) / 2` 比较，差值就是所求的数。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

也不用全加完了再求差，可以对于第 i 个数字，计算 i 与该数字之差，把差值累加起来即可。

## Code

{% asset_code coding/268-missing-number/solution.py %}
