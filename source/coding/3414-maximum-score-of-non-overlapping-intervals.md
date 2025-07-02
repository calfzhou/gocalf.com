---
title: 3414. Maximum Score of Non-overlapping Intervals
notebook: coding
tags:
- hard
katex: true
date: 2025-01-13 22:31:19
updated: 2025-01-13 22:31:19
---
## Problem

You are given a 2D integer array `intervals`, where `intervals[i] = [lᵢ, rᵢ, weightᵢ]`. Interval `i` starts at position `lᵢ` and ends at `rᵢ`, and has a weight of `weightᵢ`. You can choose _up to_ 4 **non-overlapping** intervals. The **score** of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from `intervals` with **maximum** score, representing your choice of non-overlapping intervals.

> An array `a` is **lexicographically smaller** than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is less than the corresponding element in `b`.
>
> If the first `min(a.length, b.length)` elements do not differ, then the shorter array is the lexicographically smaller one.

Two intervals are said to be **non-overlapping** if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

<https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/>

**Example 1:**

> Input: `intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]`
> Output: `[2,3]`
> Explanation:
> You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

**Example 2:**

> Input: `intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]`
> Output: `[1,3,5,6]`
> Explanation:
> You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

**Constraints:**

- `1 <= intevals.length <= 5 * 10⁴`
- `intervals[i].length == 3`
- `intervals[i] = [lᵢ, rᵢ, weightᵢ]`
- `1 <= lᵢ <= rᵢ <= 10⁹`
- `1 <= weightᵢ <= 10⁹`

## Test Cases

``` python
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
```

{% asset_code coding/assets/3414-maximum-score-of-non-overlapping-intervals/solution_test.py %}

## Thoughts

跟 [435. Non-overlapping Intervals](435-non-overlapping-intervals) 类似，但是增加了权重，且限制最多只能选 4 个区间（另外 overlap 的判定也有不同，本题单个端点重合的也算 overlap）。

由于权重的不确定性，[435. Non-overlapping Intervals](435-non-overlapping-intervals) 中的 [贪心算法](435-non-overlapping-intervals#Faster) 不再可用（`res[j] <= res[i]` 不再成立）。只能按照普通的动态规划去计算（本题中用 dp 替代 res）。

依然先对所有区间按右端点排序。因为结果需要返回选中的区间下标，所以要对下标数组排序。

定义 `dp(i, k)` 表示对排序后的 `intervals[0...i]` 选取最多 k（`1 ≤ k ≤ 4`）个区间所能得到的最大 score。

显然对于区间 i，可以不选它，那么 `dp(i, k) = dp(i - 1, k)`；或者选它，那么 `dp(i, k) = dp(j, k - 1) + weightᵢ`。其中 j 是最后一个不与区间 i 有 overlap 的区间。即所有的 `0 <= p <= j`，区间 p 与 i 不 overlap（p 的右端点小于 i 的左端点）。所有的 `j < p < i`，区间 p 与 i overlap（p 的 右端点 **大于等于** i 的左端点）。可以对 `intervals[0:i]` 的所有右端点（已经排序了）用二分搜索找到区间 i 左端点的插入位置。

所以：

$$
dp(i,k)=\max\begin{cases}
  dp(i-1,k) \\
  dp(j,k-1) + weight_i
\end{cases}
$$

初值为 `dp(i, -1) = 0`，`dp(-1, k) = 0`。最终结果为 `dp(n - 1, 4)`。

因为要返回 score 最大的区间选取的结果，需要同步记录当前每个 dp 值对应的区间选择。

有一点需要注意，当 `dp(j, k - 1) + weightᵢ = dp(i - 1, k)` 时，选不选区间 i 取决于这两种方案分别的选择区间数组的 **lexicographically order**，即把两种方案各自选取的区间按下标排序后比较，留下标数组较小的那个方案。另外最终返回的区间数组也要按照区间的原始下标排序。

时间复杂度 `O(n log n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/3414-maximum-score-of-non-overlapping-intervals/solution.py %}
