---
title: 300. Longest Increasing Subsequence
notebook: coding
tags:
- medium
date: 2024-11-17 09:19:04
updated: 2024-11-17 09:19:04
katex: true
---
## Problem

Given an integer array `nums`, return _the length of the longest **strictly increasing subsequence**_.

> A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

<https://leetcode.com/problems/longest-increasing-subsequence/description/>

**Example 1:**

> Input: `nums = [10,9,2,5,3,7,101,18]`
> Output: `4`
> Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

**Example 2:**

> Input: `nums = [0,1,0,3,2,3]`
> Output: `4`

**Example 3:**

> Input: `nums = [7,7,7,7,7,7,7]`
> Output: `1`

**Constraints:**

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## Test Cases

{% asset_code coding/300-longest-increasing-subsequence/solution_test.py %}

## Thoughts

### 正向思路

先看第一个数字（如 10），它自己可以构成一个 inc-sub (increasing subsequence)，长度为 1。

再看第二个数字（如 9），有两个选择：

1. 跟 10 组成新的 inc-sub，长度比 10 自己构成的 inc-sub 多 1。但是不满足单调递增，pass。
2. 自己成为一个独立的 inc-sub，长度为 1。

可见如果 inc-sub 以第二个数字（9）结束，长度只能是 1。

再看第三个数字（2），有三个选择：

1. 跟在 10 结尾的 inc-sub 后边——不递增，pass。
2. 跟在 9 结尾的 inc-sub 后边——不递增，pass。
3. 自己独立，长度为 1。

因此以其作为结尾的 inc-sub，长度只能是 1。

再看第四个数字（5），有四个选择：

1. 跟在 10 结尾的 inc-sub 后边——不递增，pass。
2. 跟在 9 结尾的 inc-sub 后边——不递增，pass。
3. 跟在 3 结尾的 inc-sub 后边，长度比以 3 结尾的最长的 inc-sub 多 1，为 2。
4. 自己独立，长度为 1。

可见以其作为结尾的 inc-sub，最长可以是 2。

### 动态规划

以此类推，需要记录任意的 i（`0 <= i < n`），以其作为结束的 inc-sub 的最大长度，记为 `l[i]`。注意关键点是「以其作为结束的」。

根据前边的推理可知：

$$
l[i+1]=max\{1, \forall 0\le p\le i\land nums[i+1]>nums[p]:l[p]+1\}
$$

求出所有的 `l[i]` 之后，注意 `l[n-1]` 并不是答案，这只是以 `nums[n-1]` 结束的 inc-sub 的最大长度。

题目的答案是 $max_{0\le i<n}l[i]$。

空间复杂度是 `O(n)`，时间复杂度是 `O(n^2)`。

## Code

{% asset_code coding/300-longest-increasing-subsequence/solution.py %}

## Faster

TODO
