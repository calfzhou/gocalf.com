---
title: 632. Smallest Range Covering Elements from K Lists
notebook: coding
tags:
- hard
date: 2024-11-24 15:44:27
updated: 2024-11-24 15:44:27
---
## Problem

You have `k` lists of sorted integers in **non-decreasing order**. Find the **smallest** range that includes at least one number from each of the `k` lists.

We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c` **or** `a < c` if `b - a == d - c`.

<https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/>

**Example 1:**

> Input: `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`
> Output: `[20,24]`
> Explanation:
> List 1: `[4, 10, 15, 24,26]`, `24` is in range `[20,24]`.
> List 2: `[0, 9, 12, 20]`, `20` is in range `[20,24]`.
> List 3: `[5, 18, 22, 30]`, `22` is in range `[20,24]`.

**Example 2:**

> Input: `nums = [[1,2,3],[1,2,3],[1,2,3]]`
> Output: `[1,1]`

**Constraints:**

- `nums.length == k`
- `1 <= k <= 3500`
- `1 <= nums[i].length <= 50`
- `-10⁵ <= nums[i][j] <= 10⁵`
- `nums[i]` is sorted in **non-decreasing** order.

## Test Cases

```python
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
```

{% snippet solution_test.py %}

## Thoughts

跟 [23. Merge k Sorted Lists](../23-merge-k-sorted-lists/index.md) 差不多。

同样拿 k 个数组的第一个数字构建大小为 k 的最小堆。堆顶数值就是当前区间的左端点。右端点可以在这 k 个数字进堆的时候记录下来最大值得到。

每次用堆顶对应数组的下一个数字替换堆顶，并恢复堆，此时堆的最小值和最大值就是新区间的边界。最小值直接取自堆顶，最大值则在原本最大值和刚替换进来的数字之间取较大的。

如果堆顶对应数组元素都用完了则停止。

时间复杂度 `O(k * n * log k)`，其中 n 是 `nums` 的平均长度。空间复杂度 `O(k)`。

## Code

{% snippet solution.py %}
