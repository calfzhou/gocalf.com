---
title: 53. Maximum Subarray
notebook: coding
tags:
- medium
katex: true
date: 2024-11-18 17:51:38
updated: 2025-01-08 17:35:14
---
## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return _its sum_.

> A **subarray** is a contiguous **non-empty** sequence of elements within an array.

<https://leetcode.com/problems/maximum-subarray/>

**Example 1:**

> Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
> Output: `6`
> Explanation: The subarray `[4,-1,2,1]` has the largest sum 6.

**Example 2:**

> Input: `nums = [1]`
> Output: `1`
> Explanation: The subarray `[1]` has the largest sum 1.

**Example 3:**

> Input: `nums = [5,4,-1,7,8]`
> Output: `23`
> Explanation: The subarray `[5,4,-1,7,8]` has the largest sum 23.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

## Test Cases

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

如果一个 subarray 的和大于 0，把它与下一个数相加的结果一定比下一个数自身大。反之，应该从下一个数开启新的 subarray。

记录当前 subarray 的总和，如果把下一个数加入进来，总和仍然大于 0，就可以继续。否则把 subarray 清空，总和恢复为 0，从再下一个数开始尝试建立新的 subarray。过程中记录见到的最大的总和。

## Code

{% snippet solution.py %}

## Another DP

在 [1186. Maximum Subarray Sum with One Deletion](../1186-maximum-subarray-sum-with-one-deletion/index.md) 中提到上边计算逻辑的状态定义和状态转移：`s(i)` 表示以 i 为右端点的最大 subarray 和（至少包含 `nums[i]`），即：

$$
\begin{cases}
  s(0)=nums[0] \\
  s(i)=\max\{s(i-1),0\}+nums[i]
\end{cases}
$$

那么 nums 的最大 subarray 和为 $largest=\max_{0\le i<n}{s(i)}$。

上边代码在关于 i 的循环开始的时候计算了 `s(i)`，在循环结束前把 `max{s(i), 0}` 先算好，到 `i + 1` 的循环里直接用。也可以写成如下形式，逻辑是完全一致的，跟公式更接近一些：

{% snippet solution2.py %}

为了能理解 [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/index.md)，这里对上述 DP 做一些调整，可以得到相同的结果。

这次直接记录数组的前缀和，即 `ps(i) = Σnums[0...i]`，同时用 `low(i)` 记录 `ps(0)...ps(i)` 的（小于等于零的）最小值，即：

$$
\begin{array}{rcl}
  ps(i) & = &\sum_{j=0}^{i}nums[j] \\
  low(i) & = & \min\{0, \min_{0\le j\le i}ps(j)\}
\end{array}
$$

显然 $s(i)=ps(i)-low(i-1)$。可得 $largest=\max_{0\le i<n}{s(i)}=\max_{0\le i<n}\{ps(i)-low(i-1)\}$（令 `low(-1) = 0`）。

{% snippet solution3.py %}

> 这样改造之后，[problem 3410](../3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/index.md) 比较容易在此基础上进行扩展。
