---
title: 3395. Subsequences with a Unique Middle Mode I
notebook: coding
tags:
- hard
- todo
date: 2025-01-04 22:29:23
updated: 2025-01-04 22:29:23
---
## Problem

> 唯一中间众数子序列。

Given an integer array `nums`, find the number of subsequences of size 5 of `nums` with a **unique middle mode**.

> A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Since the answer may be very large, return it **modulo** `10⁹ + 7`.

A **mode** of a sequence of numbers is defined as the element that appears the **maximum** number of times in the sequence.

> **众数** 指的是一个数字序列中出现次数 **最多** 的元素。

A sequence of numbers contains a **unique mode** if it has only one mode.

> 如果一个数字序列众数只有一个，我们称这个序列有 **唯一众数** 。

A sequence of numbers `seq` of size 5 contains a **unique middle mode** if the _middle element_ (`seq[2]`) is a **unique mode**.

> 一个大小为 5 的数字序列 `seq` ，如果它中间的数字（`seq[2]`）是唯一众数，那么称它是 **唯一中间众数** 序列。

<https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/>

**Example 1:**

> Input: `nums = [1,1,1,1,1,1]`
> Output: `6`
> Explanation:
> `[1, 1, 1, 1, 1]` is the only subsequence of size 5 that can be formed, and it has a unique middle mode of 1. This subsequence can be formed in 6 different ways, so the output is 6.

**Example 2:**

> Input: `nums = [1,2,2,3,3,4]`
> Output: `4`
> Explanation:
> `[1, 2, 2, 3, 4]` and `[1, 2, 3, 3, 4]` each have a unique middle mode because the number at index 2 has the greatest frequency in the subsequence. `[1, 2, 2, 3, 3]` does not have a unique middle mode because 2 and 3 appear twice.

**Example 3:**

> Input: nums = [0,1,2,3,4,5,6,7,8]
> Output: 0
> Explanation:
> There is no subsequence of length 5 with a unique middle mode.

**Constraints:**

- `5 <= nums.length <= 1000`
- `-10⁹ <= nums[i] <= 10⁹`

## Test Cases

``` python
class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
```

{% asset_code coding/3395-subsequences-with-a-unique-middle-mode-i/solution_test.py %}

## Thoughts

> 虽然几个测试用例都刚好是非递减排列的 nums，但题目中并没有给出这个条件，输入的 nums 可以是任意顺序的。

以任意位置 i（`2 ≤ i < n - 2`）作为子序列的中间位置，计算符合「唯一中间众数」的子序列个数。

位置 i 的左边有 `l = i` 个数字，右边有 `r = n - i` 个数字。从左右两边各任选两个数字，组成一个子序列，一共有 `C(l, 2) * C(r, 2)` 种方案。但所有这些方案中有一些不符合「唯一中间众数」的要求，需要排除掉。不妨设 `nums[i] = a`。

1. 子序列的左边和右边都没有 a：共 `(l - al) * (r - ar)` 种。
   - al 表示 nums 中 i 左边 a 的个数，ar 表示 i 右边 a 的个数。
2. 子序列的一边是 a 和一个任意其他（非 a）数字 b，另一边是 b 和任意其他（非 a、非 b）数字 c。
   1. a 在左边：共 `al * bl * br * (r - ar - br)` 种。
   2. a 在右边：共 `bl * (l - al - bl) * ar * br` 种。
3. 子序列的一边是两个任意其他（非 a）数字 b，另一边有一个 a（另一个数字可以是 b，也可以是除 a、b 外的任何数字）。
   1. a 在左边：共 `al * (l - al) * C(br, 2)` 种。
   2. a 在右边：共 `C(bl, 2) * ar * (r - ar)` 种。

可以先遍历一遍 nums，记录所有数字的总数，然后在遍历 i 的过程中，根据 `nums[i]` 的值不断更新 i 左边和右边各个数字的个数。

设 nums 种共有 K 个各不相同的数字，时间复杂度 `O(K * n) ≈ O(n²)`，空间复杂度 `O(K) ≈ O(n)`。

## Code

{% asset_code coding/3395-subsequences-with-a-unique-middle-mode-i/solution.py %}

> 这里其实有大量计算是重复的，因为 bl、br 并不是每次都变，还可以进一步优化。TODO。
