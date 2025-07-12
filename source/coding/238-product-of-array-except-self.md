---
title: 238. Product of Array Except Self
notebook: coding
tags:
- medium
date: 2024-11-24 23:20:49
updated: 2024-11-24 23:20:49
katex: true
---
## Problem

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

<https://leetcode.com/problems/product-of-array-except-self/>

**Example 1:**

> Input: `nums = [1,2,3,4]`
> Output: `[24,12,8,6]`

**Example 2:**

> Input: `nums = [-1,1,0,-3,3]`
> Output: `[0,0,9,0,0]`

**Constraints:**

- `2 <= nums.length <= 10⁵`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## Test Cases

``` python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
```

{% asset_code coding/assets/238-product-of-array-except-self/solution_test.py %}

## Thoughts

`answer[i]` 可以由其左半边子数组之积，乘以右半边子数组之积得到，即 `ans[i] = prod(nums[:i]) * prod(nums[i+1:])`。

记 `pl[i] = prod(nums[:i])`，`pr[i] = prod(nums[i+1:])`，可以得到递推式：

$$
pl[i]=\begin{cases}
  1 & \text{if }i=0 \\
  pl[i-1]\times nums[i-1] & \text{otherwise}
\end{cases}
$$

$$
pr[i]=\begin{cases}
  1 & \text{if }i=n-1 \\
  pr[i+1]\times nums[i+1] & \text{otherwise}
\end{cases}
$$

按递推时初始化好 `pl` 和 `pr` 的所有值，然后遍历 i 计算所有的 `answer`。时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/238-product-of-array-except-self/solution.py %}

## Follow Up

如果限制 `O(1)` 空间，不能再禁用除法了吧（前边禁用除法感觉是为了强行动态规划）。

如果数组中没有零，则 `ans[i] = prod(nums) // nums[i]`。只需要 `O(1)` 空间存储这个数组之积。

如果数组中刚好有一个零，则对于所有 `nums[i] != 0` 的 i，都有 `ans[i] = 0`。而唯一的零对应的 `answer` 为所有非零数字之积。

如果数组中有超过一个零，则 `answer` 为全零数组。

{% asset_code coding/assets/238-product-of-array-except-self/solution2.py %}
