---
title: 1029. Two City Scheduling
notebook: coding
tags:
- medium
date: 2025-01-01 19:36:41
updated: 2025-01-01 19:36:41
---
## Problem

A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCostᵢ, bCostᵢ]`, the cost of flying the `iᵗʰ` person to city `a` is `aCostᵢ`, and the cost of flying the `iᵗʰ` person to city `b` is `bCostᵢ`.

Return _the minimum cost to fly every person to a city_ such that exactly `n` people arrive in each city.

<https://leetcode.com/problems/two-city-scheduling/>

**Example 1:**

> Input: `costs = [[10,20],[30,200],[400,50],[30,20]]`
> Output: `110`
> Explanation:
> The first person goes to city A for a cost of 10.
> The second person goes to city A for a cost of 30.
> The third person goes to city B for a cost of 50.
> The fourth person goes to city B for a cost of 20.
>
> The total minimum cost is `10 + 30 + 50 + 20 = 110` to have half the people interviewing in each city.

**Example 2:**

> Input: `costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]`
> Output: `1859`

**Example 3:**

> Input: `costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]`
> Output: `3086`

**Constraints:**

- `2 * n == costs.length`
- `2 <= costs.length <= 100`
- `costs.length` is even.
- `1 <= aCostᵢ, bCostᵢ <= 1000`

## Test Cases

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
```

{% asset_code coding/1029-two-city-scheduling/solution_test.py %}

## Thoughts

不妨先让所有人都去城市 A，总成本为 `ΣaCostᵢ`。然后需要把 n 个人改派到城市 B。如果把第 i 个人改派到城市 B，成本的变化为 `bCostᵢ - aCostᵢ`，显然这个值越小越好。

所以对 costs 按照 `bCostᵢ - aCostᵢ` 排序，前边 n 个人去城市 B，后边 n 个人去城市 A，这样总的成本最低。

时间复杂度 `O(n log n)`。用 in-place 排序，附加的空间复杂度 `O(1)`。

## Code

{% asset_code coding/1029-two-city-scheduling/solution.py %}
