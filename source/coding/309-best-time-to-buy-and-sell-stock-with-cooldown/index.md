---
title: 309. Best Time to Buy and Sell Stock with Cooldown
notebook: coding
tags:
- medium
katex: true
date: 2024-12-18 21:54:59
updated: 2024-12-18 21:54:59
---
## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/>

**Example 1:**

> Input: `prices = [1,2,3,0,2]`
> Output: `3`
> Explanation: `transactions = [buy, sell, cooldown, buy, sell]`

**Example 2:**

> Input: `prices = [1]`
> Output: `0`

**Constraints:**

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Test Cases

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

系列问题：

- [121. Best Time to Buy and Sell Stock](../121-best-time-to-buy-and-sell-stock/index.md) 最多交易 1 次
- [122. Best Time to Buy and Sell Stock II](../122-best-time-to-buy-and-sell-stock-ii/index.md) 交易任意多次
- [123. Best Time to Buy and Sell Stock III](../123-best-time-to-buy-and-sell-stock-iii/index.md) 最多交易 2 次
- [188. Best Time to Buy and Sell Stock IV](../188-best-time-to-buy-and-sell-stock-iv/index.md) 最多交易 k 次

这次是在 [122. Best Time to Buy and Sell Stock II](../122-best-time-to-buy-and-sell-stock-ii/index.md)（交易任意多次）的基础上，增加了 cooldown 一天的要求。

在 [122. Best Time to Buy and Sell Stock II](../122-best-time-to-buy-and-sell-stock-ii/index.md) 中已经定义了 [动态规划的状态及其转移函数](../122-best-time-to-buy-and-sell-stock-ii/index.md#DP)，那么直接在转移函数上，把冷静期的影响加上去即可。更新后的转移函数为：

$$
\begin{cases}
  hold_i=\max\{hold_{i-1},empty_{i-2}-prices[i]\} \\
  empty_i=\max\{empty_{i-1},hold_{i-1}+prices[i]\}
\end{cases}
$$

> 注意 `hold(i)` 的式子变了，因为在前一次卖出到今天买入，之间至少要隔开一天。

同样是 `O(n)` 时间，`O(1)` 空间。

## Code

{% asset_code solution.py %}
