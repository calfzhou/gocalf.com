---
title: 3066. Minimum Operations to Exceed Threshold Value II
notebook: coding
tags:
- medium
date: 2025-01-14 10:02:43
updated: 2025-01-14 10:02:43
---
## Problem

You are given a **0-indexed** integer array `nums`, and an integer `k`.

In one operation, you will:

- Take the two smallest integers `x` and `y` in `nums`.
- Remove `x` and `y` from `nums`.
- Add `min(x, y) * 2 + max(x, y)` anywhere in the array.

**Note** that you can only apply the described operation if `nums` contains at least two elements.

Return _the **minimum** number of operations needed so that all elements of the array are greater than or equal to_ `k`.

<https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/>

**Example 1:**

> Input: `nums = [2,11,10,1,3], k = 10`
> Output: `2`
> Explanation: In the first operation, we remove elements 1 and 2, then add `1 * 2 + 2` to `nums`. `nums` becomes equal to `[4, 11, 10, 3]`.
> In the second operation, we remove elements 3 and 4, then add `3 * 2 + 4` to `nums`. `nums` becomes equal to `[10, 11, 10]`.
> At this stage, all the elements of `nums` are greater than or equal to 10 so we can stop.
> It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.

**Example 2:**

> Input: `nums = [1,1,2,4,9], k = 20`
> Output: `4`
> Explanation: After one operation, `nums` becomes equal to `[2, 4, 9, 3]`.
> After two operations, `nums` becomes equal to `[7, 4, 9]`.
> After three operations, `nums` becomes equal to `[15, 9]`.
> After four operations, `nums` becomes equal to `[33]`.
> At this stage, all the elements of `nums` are greater than 20 so we can stop.
> It can be shown that 4 is the minimum number of operations needed so that all elements of the array are greater than or equal to 20.

**Constraints:**

- `2 <= nums.length <= 2 * 10⁵`
- `1 <= nums[i] <= 10⁹`
- `1 <= k <= 10⁹`
- The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are greater than or equal to `k`.

## Test Cases

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
```

{% asset_code coding/3066-minimum-operations-to-exceed-threshold-value-ii/solution_test.py %}

## Thoughts

[3065. Minimum Operations to Exceed Threshold Value I](../3065-minimum-operations-to-exceed-threshold-value-i/index.md) 的进阶版，把最小的两个数拿掉之后还会再放回来一个数。

直接用模拟操作的方法。

用最小堆比较合适，先基于 nums 构建最小堆。如果堆顶数字大于等于 k 就可以结束，否则取出堆顶数字 x 即为当前 nums 中的最小值，取走 x 后堆顶的值 y 即为第二小的值，显然 `min(x, y) = x`、`max(x, y) = y`。用 `2x + y` 替换掉此时的堆顶（y）。重复操作直到堆顶数字大于等于 k。

最开始构建堆的时间为 `O(n log n)`。模拟过程最多循环 n 次，每次两次堆操作时间为 `O(log n)`。总的时间复杂度 `O(n log n)`。直接利用 nums 的空间，附加的空间复杂度 `O(1)`。

## Code

{% asset_code coding/3066-minimum-operations-to-exceed-threshold-value-ii/solution.py %}
