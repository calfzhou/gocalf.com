---
title: 1128. Number of Equivalent Domino Pairs
notebook: coding
tags:
- easy
date: 2025-01-03 11:23:59
updated: 2025-01-03 11:23:59
---
## Problem

Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j] = [c, d]` if and only if either (`a == c` and `b == d`), or (`a == d` and `b == c`) - that is, one domino can be rotated to be equal to another domino.

Return _the number of pairs_ `(i, j)` _for which_ `0 <= i < j < dominoes.length`_, and_ `dominoes[i]` _is **equivalent to**_ `dominoes[j]`.

<https://leetcode.com/problems/number-of-equivalent-domino-pairs/>

**Example 1:**

> Input: `dominoes = [[1,2],[2,1],[3,4],[5,6]]`
> Output: `1`

**Example 2:**

> Input: `dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]`
> Output: `3`

**Constraints:**

- `1 <= dominoes.length <= 4 * 10⁴`
- `dominoes[i].length == 2`
- `1 <= dominoes[i][j] <= 9`

## Test Cases

``` python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
```

{% asset_code coding/1128-number-of-equivalent-domino-pairs/solution_test.py %}

## Thoughts

把所有的多米诺骨牌都翻转成小面在前（即 `a ≤ b`），然后统计各种牌的数量。如果某种牌有 k 个，当 `k > 1` 时，其中任意两个都是一对，共有 `k * (k - 1) / 2` 对。

累加每种牌的对数即可。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/1128-number-of-equivalent-domino-pairs/solution.py %}
