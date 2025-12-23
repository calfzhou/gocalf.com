---
title: 121. Best Time to Buy and Sell Stock
notebook: coding
tags:
- easy
date: 2024-11-25 23:53:15
updated: 2024-11-25 23:53:15
---
## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock/>

**Example 1:**

> Input: `prices = [7,1,5,3,6,4]`
> Output: `5`
> Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
> Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

> Input: `prices = [7,6,4,3,1]`
> Output: `0`
> Explanation: In this case, no transactions are done and the max profit = 0.

**Constraints:**

- `1 <= prices.length <= 10⁵`
- `0 <= prices[i] <= 10⁴`

## Test Cases

``` python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

{% asset_code coding/assets/121-best-time-to-buy-and-sell-stock/solution_test.py %}

## Thoughts

对于任意的一天，如果当天卖出，想要收益最大应该在之前最低价那天买入，二者差值记为最大收益（如果当天就是历史最低价，那就无法获得收益，相当于收益为 0）。然后看哪一天卖出的收益最大即可。

即对于 `1 <= i <= n`，`profit(i) = prices(i) - min{prices(1..i)}`，过程中记录可能的最大收益。

## Code

{% asset_code coding/assets/121-best-time-to-buy-and-sell-stock/solution.py %}
