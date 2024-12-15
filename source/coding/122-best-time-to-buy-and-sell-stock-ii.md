---
title: 122. Best Time to Buy and Sell Stock II
notebook: coding
tags:
- medium
date: 2024-12-15 22:47:02
updated: 2024-12-15 22:47:02
---
## Problem

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Find and return _the **maximum** profit you can achieve_.

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/>

**Example 1:**

> Input: `prices = [7,1,5,3,6,4]`
> Output: `7`
> Explanation: Buy on day 2 (`price = 1`) and sell on day 3 (`price = 5`), `profit = 5-1 = 4`.
> Then buy on day 4 (`price = 3`) and sell on day 5 (`price = 6`), `profit = 6-3 = 3`.
> Total profit is `4 + 3 = 7`.

**Example 2:**

> Input: `prices = [1,2,3,4,5]`
> Output: `4`
> Explanation: Buy on day 1 (`price = 1`) and sell on day 5 (`price = 5`), `profit = 5-1 = 4`.
> Total profit is 4.

**Example 3:**

> Input: `prices = [7,6,4,3,1]`
> Output: `0`
> Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

**Constraints:**

- `1 <= prices.length <= 3 * 10⁴`
- `0 <= prices[i] <= 10⁴`

## Test Cases

``` python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

{% asset_code coding/122-best-time-to-buy-and-sell-stock-ii/solution_test.py %}

## Thoughts

[121. Best Time to Buy and Sell Stock](121-best-time-to-buy-and-sell-stock) 的进阶版，可以买入卖出多次了（且同一天内可以既买也卖，但最多只能持有一份）。

如果当前未持有股票，而明天的价格更高，那么今天就可以买入。

如果当前持有股票，而明天价格更低，那么今天就卖掉。

扫描数组，只要 `nums[i+1]` 比 `nums[i]` 大，就在第 i 天买入并在第 `i + 1` 天卖出，差值则为部分收益。累加所有收益即可。

## Code

{% asset_code coding/122-best-time-to-buy-and-sell-stock-ii/solution.py %}
