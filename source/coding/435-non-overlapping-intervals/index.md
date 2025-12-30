---
title: 435. Non-overlapping Intervals
notebook: coding
tags:
- medium
katex: true
date: 2024-11-18 15:57:32
updated: 2024-11-18 15:57:32
---
## Problem

Given an array of intervals `intervals` where `intervals[i] = [startᵢ, endᵢ]`, return _the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping_.

**Note** that intervals which only touch at a point are **non-overlapping**. For example, `[1, 2]` and `[2, 3]` are non-overlapping.

<https://leetcode.com/problems/non-overlapping-intervals/>

**Example 1:**

> Input: `intervals = [[1,2],[2,3],[3,4],[1,3]]`
> Output: `1`
> Explanation: `[1,3]` can be removed and the rest of the intervals are non-overlapping.

**Example 2:**

> Input: `intervals = [[1,2],[1,2],[1,2]]`
> Output: `2`
> Explanation: You need to remove two `[1,2]` to make the rest of the intervals non-overlapping.

**Example 3:**

> Input: `intervals = [[1,2],[2,3]]`
> Output: `0`
> Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

**Constraints:**

- `1 <= intervals.length <= 10⁵`
- `intervals[i].length == 2`
- `-5 * 10⁴ <= startᵢ < endᵢ <= 5 * 10⁴`

## Test Cases

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

先对所有区间排序，排序后按顺序处理，判定是否 overlap 才比较快。按区间的右端点排序。

求最少移除的区间数，等同于求最多剩余的区间数，正向角度看更顺一些。

设区间总数为 n，对于 `0 <= i < n`，记录以 `intervals[i]` 为最后一个区间的条件下，最多互不重叠的区间数，记为 `c[i]`。

关键点是 `c[i]` 对应于「区间 i 一定被留下」。在思考的时候很容易会觉得「去掉区间 i 可能剩余的区间数更多」，导致在这里犹豫。实际上如果区间 i 确实应该被移除，前边还有 `c[i-1]`、`c[i-2]` 等等。

接下来看区间 `i + 1`，它的右端点一定大于等于前边所有区间的右端点，只需要比较左端点就能确定它是否与前边的某个区间有重叠。由于前边的区间都已经按右端点排序了，如果某个区间跟区间 `i + 1` 有重叠，那排在它后边的所有区间都与区间 `i + 1` 重叠。

对于某个区间 p（`0 <= p <= i`），如果它与区间 `i + 1` 重叠，则不存在 p 和 `i + 1` 都留下的方案，记为区间总数是 0。如果不重叠，那么同时留下 p 和 `i + 1` 的方案一共有 `c[p] + 1` 个区间。还有一种可能是前 i 个区间都不要，只留 `i + 1`，则共有 1 个区间。

设最后一个不与 `i + 1` 有重叠的区间为 j。即所有的 `0 <= p <= j`，区间 p 与 `i + 1` 不重叠。所有的 `j < p <= i`，区间 p 与 `i + 1` 重叠。

由此可以得出 `c[i + 1]` 的算式为：

$$
c[i+1]=\max\{1,c[p]+1\mid 0\le p \le j\}
$$

最终从 `c[0]` 到 `c[n-1]` 中取最大，就是最多剩余的区间数，和区间总数的差值记为最少移除的区间数。

时间复杂度 `O(n²)`，空间复杂度 `O(n)`。

太慢了。

对于 `0 <= p <= j`，并不需要每个都计算一次。考虑加一个记录值 `res[i]`，表示「前 i 个区间，最多互不重叠的区间数」。显然 `res[i]` 等于 `c[0]` 到 `c[i]` 的最大值。

可见 $res[j] = max_{0\le p\le j}{c[p]}$，从 `O(n)` 的求最大值计算降到 `O(1)` 的直接查表。

所以：

$$
\begin{cases}
c[i+1]=\max\{1,res[j]+1\} \\
res[i+1]=\max\{c[i+1],res[i]\}
\end{cases}
$$

唯一的问题是需要确定 j 的值，显然可以对 `intervals[0]` 到 `intervals[i]` 用二分法求出。

最后结果取 `n - res[n - 1]`。

时间复杂度 `O(n log n)`，其中排序和遍历都是 `O(n log n)`。空间复杂度还是 `O(n)`。

## Code

{% asset_code solution.py %}

## Faster

可能因为一直在想动态规划，导致思维定势了。回头再看这个递推的算式，即使从数学角度，也发现不需要这么麻烦。重新看一下这个式子：

$$
\begin{cases}
c[i+1]=\max\{1,res[j]+1\} \\
res[i+1]=\max\{c[i+1],res[i]\}
\end{cases}
$$

在 `res[i + 1]` 的算式中，把 `c[i + 1]` 代入，可得：

$$
res[i+1]=\max\{1,res[j]+1,res[i]\}
$$

首先跟 c 没关系了，其次显然有 `1 <= res[j] <= res[i]`，于是：

$$
res[i+1]=\begin{cases}
res[i] & \text{ if } res[j] < res[i] \\
res[i]+1 & \text{ if } res[j] == res[i]
\end{cases}
$$

其中 `res[j] < res[i]` 成立的条件是，`intervals[j+1]` 到 `intervals[i]` 中有被保留的区间，即区间 `i + 1` 与某个被保留的区间有重叠。

因此跟踪记录最新的 res 值，以及当前最后一个被保留的区间的右端点位置，如果区间 `i + 1` 会覆盖此位置，就直接丢弃，否则就保留。

开始以为是动态规划，其实是贪心法，也就是对于子问题 `intervals[0:i+1]`，区间 `i + 1` 是否保留的选择，跟整个问题 `intervals[0:n-1]` 是一致的。

虽然总的时间复杂度还是 `O(n log n)`，但遍历部分下降到 `O(n)`，还是能快一些。如果用 in-place 排序，附加的空间复杂度降为 `O(1)`。

{% asset_code solution2.py %}
