---
title: 3261. Count Substrings That Satisfy K-Constraint II
notebook: coding
tags:
- hard
katex: true
date: 2024-11-13 22:54:53
updated: 2024-11-13 22:54:53
---
## Problem

You are given a **binary** string `s` and an integer `k`.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

- The number of `0`'s in the string is at most `k`.
- The number of `1`'s in the string is at most `k`.

Return an integer array `answer`, where `answer[i]` is the number of substrings of `s[li..ri]` that satisfy the **k-constraint**.

> A substring is a contiguous non-empty sequence of characters within a string.

<https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/description/>

**Example 1:**

> Input: `s = "0001111", k = 2, queries = [[0,6]]`
> Output: `[26]`
> Explanation:
> For the query `[0, 6]`, all substrings of `s[0..6] = "0001111"` satisfy the k-constraint except for the substrings `s[0..5] = "000111"` and `s[0..6] = "0001111"`.

**Example 2:**

> Input: `s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]`
> Output: `[15,9,3]`
> Explanation:
> The substrings of `s` with a length greater than 3 do not satisfy the k-constraint.

**Constraints:**

- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= k <= s.length`
- `1 <= queries.length <= 10^5`
- `queries[i] == [l_i, r_i]`
- `0 <= l_i <= r_i < s.length`
- All queries are distinct.

## Test Cases

{% asset_code coding/3261-count-substrings-that-satisfy-k-constraint-ii/solution_test.py %}

## Thoughts

[3258. Count Substrings That Satisfy K-Constraint I](/coding/3258-count-substrings-that-satisfy-k-constraint-i) 的进阶版。

设 `s` 长度为 `n`，`queries` 长度为 `q`。

如果对 `queries` 中的每个值，直接用 [problem 3258](/coding/3258-count-substrings-that-satisfy-k-constraint-i) 的逻辑处理，时间复杂度为 `O(q*n)`。

太慢了。多次查询时，大量计算是重复的，可缓存一些中间结果。

对于给定的查询边界 $1\le l\le r\le n$，k-子串（符合 k-constraint 的子串）总数是以 $s_{l,r}$ 中每个位置开头且右端不会超出 r 的 k-子串数总和。

以 i 开头的子串，如果 $s_{i,j-1}$ 符合 k-约束但 $s_{i,j}$ 不符合，那么更长的子串也都不符合。

所以对于每一个 i，记录相应的 j，记为 $j_i$。当 $l\le i\le r$ 时，可以计数以 i 开头但右端不会超出 r 的 k-子串数量。

于是：

$$
count_{l,r}=\sum_{i=l}^r(min(j_i,r)-i)
$$

辅助的空间复杂度 `O(n)`，时间复杂度 `O(n + q*t)`，其中 t 是 `queries` 的平均区间长度。

还是太慢，如果 t ≈ n，时间复杂度就还是 `O(q*n)`。而且对于两个重叠的 query 区间，重叠部分有些累加过程是重复的。

对于当前的 i、j，如果 $s_{i,j}$ 符合 k-约束，在移动 j 之前算一下右端不超过 j 的 k-子串总数（记为 $total_j$），显然等于右端不超过 j - 1 的 k-子串总数，再加上右端刚好是 j 的 k-子串数量。而后者等于 j - i + 1。于是有：

$$
total_j=total_{j-1}+(j-i+1)
$$

对于区间 `[l, r]`，$total_r-total_{l-1}$ 是右端点落在 `[l, r]` 内的 k-子串总数。

注意这并不是题目要求的区间 `[l, r]` 内的 k-子串总数，因为题目还要求左端点也在区间内。

对于左端点 l，以 l 开头的 k-子串最远不会到达 $j_l$。反过来看就是说所有右端能落在 $j_l$ 的 k-子串，左端一定在 `[l, r]` 区间内。

把区间 `[l, r]` 分成两半：$[l,j_l)$ 和 $[j_l, r]$（需要小心 $j_l$ 超过 r 的情况，此处略）。右端点落在右半段的 k-子串，其左端点一定在 `[l, r]` 内，总数为 $total_r-total_{j_l-1}$。而左半段，显然其中所有的子串都符合 k-约束，共 $(j_l-l)*(j_l-l+1)/2$ 个。

这样对于任意区间，可以用常数时间求出其中包含的 k-子串总数。那么整个问题的求解时间复杂度为 `O(n+q)`，空间复杂度为 `O(n)`。

## Code

{% asset_code coding/3261-count-substrings-that-satisfy-k-constraint-ii/solution.py %}
