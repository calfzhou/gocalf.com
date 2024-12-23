---
title: 2940. Find Building Where Alice and Bob Can Meet
notebook: coding
tags:
- hard
date: 2024-12-22 16:30:11
updated: 2024-12-22 16:30:11
---
## Problem

You are given a **0-indexed** array `heights` of positive integers, where `heights[i]` represents the height of the `iᵗʰ` building.

If a person is in building `i`, they can move to any other building `j` if and only if `i < j` and `heights[i] < heights[j]`.

You are also given another array `queries` where `queries[i] = [aᵢ, bᵢ]`. On the `iᵗʰ` query, Alice is in building `aᵢ` while Bob is in building `bᵢ`.

Return _an array_ `ans` _where_ `ans[i]` _is **the index of the leftmost building** where Alice and Bob can meet on the_ `iᵗʰ` _query_. _If Alice and Bob cannot move to a common building on query_ `i`, _set_ `ans[i]` _to_ `-1`.

<https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/>

**Example 1:**

> Input: `heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]`
> Output: `[2,5,-1,5,2]`
> Explanation: In the first query, Alice and Bob can move to building 2 since `heights[0] < heights[2]` and `heights[1] < heights[2]`.
> In the second query, Alice and Bob can move to building 5 since `heights[0] < heights[5]` and `heights[3] < heights[5]`.
> In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
> In the fourth query, Alice and Bob can move to building 5 since `heights[3] < heights[5]` and `heights[4] < heights[5]`.
> In the fifth query, Alice and Bob are already in the same building.
> For `ans[i] != -1`, It can be shown that `ans[i]` is the leftmost building where Alice and Bob can meet.
> For `ans[i] == -1`, It can be shown that there is no building where Alice and Bob can meet.

**Example 2:**

> Input: `heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]`
> Output: `[7,6,-1,4,6]`
> Explanation: In the first query, Alice can directly move to Bob's building since `heights[0] < heights[7]`.
> In the second query, Alice and Bob can move to building 6 since `heights[3] < heights[6]` and `heights[5] < heights[6]`.
> In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
> In the fourth query, Alice and Bob can move to building 4 since `heights[3] < heights[4]` and `heights[0] < heights[4]`.
> In the fifth query, Alice can directly move to Bob's building since `heights[1] < heights[6]`.
> For `ans[i] != -1`, It can be shown that `ans[i]` is the leftmost building where Alice and Bob can meet.
> For `ans[i] == -1`, It can be shown that there is no building where Alice and Bob can meet.

**Constraints:**

- `1 <= heights.length <= 5 * 10⁴`
- `1 <= heights[i] <= 10⁹`
- `1 <= queries.length <= 5 * 10⁴`
- `queries[i] = [aᵢ, bᵢ]`
- `0 <= aᵢ, bᵢ <= heights.length - 1`

## Test Cases

``` python
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
```

{% asset_code coding/2940-find-building-where-alice-and-bob-can-meet/solution_test.py %}

## Thoughts

对于任意 `queries[i] = [aᵢ, bᵢ]`，首先如果 `aᵢ = bᵢ` 则结果为 `aᵢ`（或 `bᵢ`）。如果 `aᵢ > bᵢ`，则把它俩交换一下，不影响结果。不妨设 `aᵢ < bᵢ`，如果 `heights[aᵢ] < heights[bᵢ]`，则结果为 `bᵢ`。所以只需要考虑 `heights[aᵢ] ≥ heights[bᵢ]` 的情况，这时候需要在 `bᵢ` 右侧找到第一个大于 `heights[aᵢ]` 的值。

跟 [1847. Closest Room](1847-closest-room) 几乎一样，`bᵢ` 就相当于 `preferred`，`heights[aᵢ]` 相当于 `minSize`。唯一的区别是本题要求「大于」`heights[aᵢ]` 而不是「大于等于」，要求「大于」 `bᵢ` 而不是「最接近」。

直接在 [problem 1847](1847-closest-room) 的代码上微调一下就行了。利用 Python 内置的 list 作为有序集合，虽然理论上时间复杂度不低，但提交后 beats 100%。

如果有序集合可以用 `O(log n)` 时间完成插入，总的时间复杂度是 `O(n log n + m log m + m log n)`，其中 n 是 heights 的数量，m 是 queries 的数量。空间复杂度 `O(n + m)`。

## Code

{% asset_code coding/2940-find-building-where-alice-and-bob-can-meet/solution.py %}