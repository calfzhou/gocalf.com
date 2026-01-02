---
title: 2931. Maximum Spending After Buying Items
notebook: coding
tags:
- hard
date: 2024-12-12 11:06:08
updated: 2024-12-12 11:06:08
---
## Problem

You are given a **0-indexed** `m * n` integer matrix `values`, representing the values of `m * n` different items in `m` different shops. Each shop has `n` items where the `jᵗʰ` item in the `iᵗʰ` shop has a value of `values[i][j]`. Additionally, the items in the `iᵗʰ` shop are sorted in non-increasing order of value. That is, `values[i][j] >= values[i][j + 1]` for all `0 <= j < n - 1`.

On each day, you would like to buy a single item from one of the shops. Specifically, On the `dᵗʰ` day you can:

- Pick any shop `i`.
- Buy the rightmost available item `j` for the price of `values[i][j] * d`. That is, find the greatest index `j` such that item `j` was never bought before, and buy it for the price of `values[i][j] * d`.

**Note** that all items are pairwise different. For example, if you have bought item `0` from shop `1`, you can still buy item `0` from any other shop.

Return _the **maximum amount of money that can be spent** on buying all_ `m * n` _products_.

<https://leetcode.cn/problems/maximum-spending-after-buying-items/>

**Example 1:**

> Input: `values = [[8,5,2],[6,4,1],[9,7,3]]`
> Output: `285`
> Explanation: On the first day, we buy product 2 from shop 1 for a price of `values[1][2] * 1 = 1`.
> On the second day, we buy product 2 from shop 0 for a price of `values[0][2] * 2 = 4`.
> On the third day, we buy product 2 from shop 2 for a price of `values[2][2] * 3 = 9`.
> On the fourth day, we buy product 1 from shop 1 for a price of `values[1][1] * 4 = 16`.
> On the fifth day, we buy product 1 from shop 0 for a price of `values[0][1] * 5 = 25`.
> On the sixth day, we buy product 0 from shop 1 for a price of `values[1][0] * 6 = 36`.
> On the seventh day, we buy product 1 from shop 2 for a price of `values[2][1] * 7 = 49`.
> On the eighth day, we buy product 0 from shop 0 for a price of `values[0][0] * 8 = 64`.
> On the ninth day, we buy product 0 from shop 2 for a price of `values[2][0] * 9 = 81`.
> Hence, our total spending is equal to 285.
> It can be shown that 285 is the maximum amount of money that can be spent buying all `m * n` products.

**Example 2:**

> Input: `values = [[10,8,6,4,2],[9,7,5,3,2]]`
> Output: `386`
> Explanation: On the first day, we buy product 4 from shop 0 for a price of `values[0][4] * 1 = 2`.
> On the second day, we buy product 4 from shop 1 for a price of `values[1][4] * 2 = 4`.
> On the third day, we buy product 3 from shop 1 for a price of `values[1][3] * 3 = 9`.
> On the fourth day, we buy product 3 from shop 0 for a price of `values[0][3] * 4 = 16`.
> On the fifth day, we buy product 2 from shop 1 for a price of `values[1][2] * 5 = 25`.
> On the sixth day, we buy product 2 from shop 0 for a price of `values[0][2] * 6 = 36`.
> On the seventh day, we buy product 1 from shop 1 for a price of `values[1][1] * 7 = 49`.
> On the eighth day, we buy product 1 from shop 0 for a price of `values[0][1] * 8 = 64`.
> On the ninth day, we buy product 0 from shop 1 for a price of `values[1][0] * 9 = 81`.
> On the tenth day, we buy product 0 from shop 0 for a price of `values[0][0] * 10 = 100`.
> Hence, our total spending is equal to 386.
> It can be shown that 386 is the maximum amount of money that can be spent buying all `m * n` products.

**Constraints:**

- `1 <= m == values.length <= 10`
- `1 <= n == values[i].length <= 10⁴`
- `1 <= values[i][j] <= 10⁶`
- `values[i]` are sorted in non-increasing order.

## Test Cases

```python
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

复杂的应用问题背后实际上就是个多路归并排序的问题，跟 [23. Merge k Sorted Lists](../23-merge-k-sorted-lists/index.md) 和 [632. Smallest Range Covering Elements from K Lists](../632-smallest-range-covering-elements-from-k-lists/index.md) 的内核完全一致，都是借助最小堆对若干个有序序列做合并。

因为根据题意，只要每天都买剩余产品中最便宜的那个，最终的花费就是最大的（有钱没处花？）。

这次不手写堆的内部逻辑了，直接用 Python 内置的 [heapq](https://docs.python.org/3/library/heapq.html) 代劳。

堆的大小为 m，整体时间复杂度是 `O(mn log m)`，空间复杂度 `O(m)`。

不过这道题限定 `m ≤ 10`，这么小的量级，最小堆的时间复杂度虽然低，但是常数系数过大导致实际运行速度并不快。反倒把 `m * n` 个数放进一个大数组直接排序更快，时间复杂度是 `O(mn log(mn))`，空间复杂度是 `O(mn)`（提交之后，直接排序的耗时只有用最小堆的三分之一）。

## Code

### Merge Sort with Min Heap

{% snippet solution.py %}

### Sort All Directly

{% snippet solution2.py %}
