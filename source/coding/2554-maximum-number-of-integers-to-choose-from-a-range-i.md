---
title: 2554. Maximum Number of Integers to Choose From a Range I
notebook: coding
tags:
- medium
date: 2024-12-06 10:44:25
updated: 2024-12-06 10:44:25
---
## Problem

You are given an integer array `banned` and two integers `n` and `maxSum`. You are choosing some number of integers following the below rules:

- The chosen integers have to be in the range `[1, n]`.
- Each integer can be chosen **at most once**.
- The chosen integers should not be in the array `banned`.
- The sum of the chosen integers should not exceed `maxSum`.

Return _the **maximum** number of integers you can choose following the mentioned rules_.

<https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/>

**Example 1:**

> Input: `banned = [1,6,5], n = 5, maxSum = 6`
> Output: `2`
> Explanation: You can choose the integers `2` and `4`.
> `2` and `4` are from the range `[1, 5]`, both did not appear in banned, and their sum is `6`, which did not exceed `maxSum`.

**Example 2:**

> Input: `banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1`
> Output: `0`
> Explanation: You cannot choose any integer while following the mentioned conditions.

**Example 3:**

> Input: `banned = [11], n = 7, maxSum = 50`
> Output: `7`
> Explanation: You can choose the integers `1`, `2`, `3`, `4`, `5`, `6`, and `7`.
> They are from the range `[1, 7]`, all did not appear in banned, and their sum is `28`, which did not exceed `maxSum`.

**Constraints:**

- `1 <= banned.length <= 10⁴`
- `1 <= banned[i], n <= 10⁴`
- `1 <= maxSum <= 10⁹`

## Test Cases

``` python
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
```

{% asset_code coding/2554-maximum-number-of-integers-to-choose-from-a-range-i/solution_test.py %}

## Thoughts

直接把 `banned` 里的数字都加到哈希表中，然后从 1 遍历到 n 并跳过 `banned` 中的值，累加，直到总和超过 `maxSum` 为止。

## Code

{% asset_code coding/2554-maximum-number-of-integers-to-choose-from-a-range-i/solution.py %}
