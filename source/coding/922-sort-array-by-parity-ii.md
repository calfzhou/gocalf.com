---
title: 922. Sort Array By Parity II
notebook: coding
tags:
- easy
date: 2025-02-04 14:43:00
updated: 2025-02-04 14:43:00
---
## Problem

Given an array of integers `nums`, half of the integers in `nums` are **odd**, and the other half are **even**.

Sort the array so that whenever `nums[i]` is odd, `i` is **odd**, and whenever `nums[i]` is even, `i` is **even**.

Return _any answer array that satisfies this condition_.

<https://leetcode.cn/problems/sort-array-by-parity-ii/>

**Example 1:**

> Input: `nums = [4,2,5,7]`
> Output: `[4,5,2,7]`
> Explanation: `[4,7,2,5]`, `[2,5,4,7]`, `[2,7,4,5]` would also have been accepted.

**Example 2:**

> Input: `nums = [2,3]`
> Output: `[2,3]`

**Constraints:**

- `2 <= nums.length <= 2 * 10⁴`
- `nums.length` is even.
- Half of the integers in `nums` are even.
- `0 <= nums[i] <= 1000`

**Follow Up:** Could you solve it in-place?

## Test Cases

``` python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
```

{% asset_code coding/922-sort-array-by-parity-ii/solution_test.py %}

## Thoughts

[905. Sort Array By Parity](905-sort-array-by-parity) 的进阶版。

用同样的逻辑处理，只是指针 i 指向偶数下标，j 指向奇数下标。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/922-sort-array-by-parity-ii/solution.py %}
