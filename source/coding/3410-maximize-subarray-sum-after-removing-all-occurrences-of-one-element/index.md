---
title: 3410. Maximize Subarray Sum After Removing All Occurrences of One Element
notebook: coding
tags:
- hard
date: 2025-01-08 17:37:47
updated: 2025-01-08 17:37:47
---
## Problem

You are given an integer array `nums`.

You can do the following operation on the array **at most** once:

- Choose **any** integer `x` such that `nums` remains **non-empty** on removing all occurrences of `x`.
- Remove **all** occurrences of `x` from the array.

Return the **maximum** subarray sum across **all** possible resulting arrays.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

<https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/>

**Example 1:**

> Input: `nums = [-3,2,-2,-1,3,-2,3]`
> Output: `7`
> Explanation:
> We can have the following arrays after at most one operation:
>
> - The original array is `nums = [-3, 2, -2, -1,` {% u 3, -2, 3 %}`]`. The maximum subarray sum is `3 + (-2) + 3 = 4`.
> - Deleting all occurences of `x = -3` results in `nums = [2, -2, -1,` {% u 3, -2, 3 %}`]`. The maximum subarray sum is `3 + (-2) + 3 = 4`.
> - Deleting all occurences of `x = -2` results in `nums = [-3,` {% u 2, -1, 3, 3 %}`]`. The maximum subarray sum is `2 + (-1) + 3 + 3 = 7`.
> - Deleting all occurences of `x = -1` results in `nums = [-3, 2, -2,` {% u 3, -2, 3 %}`]`. The maximum subarray sum is `3 + (-2) + 3 = 4`.
> - Deleting all occurences of `x = 3` results in `nums = [-3,` {% u 2 %}`, -2, -1, -2]`. The maximum subarray sum is 2.
>
> The output is `max(4, 4, 7, 4, 2) = 7`.

**Example 2:**

> Input: `nums = [1,2,3,4]`
> Output: `10`
> Explanation:
> It is optimal to not perform any operations.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁶ <= nums[i] <= 10⁶`

## Test Cases

``` python
class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
```

{% asset_code coding/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/solution_test.py %}

## Thoughts

系列问题：

- [53. Maximum Subarray](../53-maximum-subarray/index.md) 普通的最大 subarray 问题
- [1186. Maximum Subarray Sum with One Deletion](../1186-maximum-subarray-sum-with-one-deletion/index.md) 允许最多删除一个位置的数字

本题是允许最多删除一个数字的所有 occurrences。

显然只有删掉某个负数，才有可能得到更大的最大子数组。

如果直接 [遍历每个负数，计算其所有 occurrences 被删掉之后的最大子数组](solution_slow.py)，时间复杂度是 `O(n²)`，肯定会超时。这里有大量的重复计算。

沿用前两题中 [第二种 DP](../1186-maximum-subarray-sum-with-one-deletion/index.md#Another-DP) 的定义，`ps(i) = Σnums[0...i]` 和 `low(i)`（`nums[0...i]` 的（小于等于零的）最小前缀和）。调整 `low2(i)` 的含义为 `arr[0...i]` 的（小于等于零的）最小前缀和再加上额外被删掉的数字的所有 occurrences 所能得到的最小值（在 `ps(i)` 中减去此值，就是以 i 为右端点但是删掉至多一个数字的所有 occurrences 之后的最大 subarray 和）。

在 [problem 1186](../1186-maximum-subarray-sum-with-one-deletion/index.md) 中只允许删除一个位置的数字，low2 的状态转移为：

$$
low2(i)=\min\begin{cases}
  low(i-2)+arr[i] \\
  low2(i-1)
\end{cases}
$$

其中 $low(i-2)+arr[i]$ 对应了删掉 `arr[i]`（那就至少保留 `arr[i-1]`）的情况。但在本题，如果删除 `arr[i] = v`，则还需要删掉 i 左边其他的 v。也就是 `low(i - 2)` 对应的子数组右边的其他 v 也要加上去。用一个关于 v 的字典来记录这个信息：

$$
low2'(v,i)=\min\begin{cases}
  low2'(v,j)+v \\
  low(i-2)+v
\end{cases}
$$

其中 j 是 i 左边的最靠右的值为 v 的位置。这里有个小技巧是并没有刻意记录有几个 v 需要删掉，而是记录上一次遇见 v 的时候，需要从 ps 里减去的值是多少。

这样本题的 low2 的状态转移为：

$$
low2(i)=\min\begin{cases}
  low2'(v,i) \\
  low2(i-1)
\end{cases}
$$

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/solution.py %}
