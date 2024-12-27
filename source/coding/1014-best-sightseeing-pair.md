---
title: 1014. Best Sightseeing Pair
notebook: coding
tags:
- medium
date: 2024-12-27 11:06:44
updated: 2024-12-27 11:06:44
---
## Problem

You are given an integer array `values` where `values[i]` represents the value of the `iᵗʰ` sightseeing spot. Two sightseeing spots `i` and `j` have a **distance** `j - i` between them.

The score of a pair (`i < j`) of sightseeing spots is `values[i] + values[j] + i - j`: the sum of the values of the sightseeing spots, minus the distance between them.

Return _the maximum score of a pair of sightseeing spots_.

<https://leetcode.com/problems/best-sightseeing-pair/>

**Example 1:**

> Input: `values = [8,1,5,2,6]`
> Output: `11`
> Explanation: `i = 0`, `j = 2`, `values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11`

**Example 2:**

> Input: `values = [1,2]`
> Output: `2`

**Constraints:**

- `2 <= values.length <= 5 * 10⁴`
- `1 <= values[i] <= 1000`

## Test Cases

``` python
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
```

{% asset_code coding/1014-best-sightseeing-pair/solution_test.py %}

## Thoughts

把分数的算式改写为 `(values[i] + i) + (values[j] - j)`。对于任何 j，想要分数最高，需要与它左边 `values[i] + i` 最大的那个结对。从左向右扫描数组的时候，可以记录已知的 `values[i] + i` 的最大值。最后对所有的 j，取结对分数最大的即可。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/1014-best-sightseeing-pair/solution.py %}
