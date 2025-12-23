---
title: 714. Best Time to Buy and Sell Stock with Transaction Fee
notebook: coding
tags:
- medium
katex: true
date: 2024-12-18 22:06:17
updated: 2024-12-18 22:06:17
---
## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**Note:**

- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- The transaction fee is only charged once for each stock purchase and sale.

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/>

**Example 1:**

> Input: `prices = [1,3,2,8,4,9], fee = 2`
> Output: `8`
> Explanation: The maximum profit can be achieved by:
>
> - Buying at `prices[0] = 1`
> - Selling at `prices[3] = 8`
> - Buying at `prices[4] = 4`
> - Selling at `prices[5] = 9`
>
> The total profit is `((8 - 1) - 2) + ((9 - 4) - 2) = 8`.

**Example 2:**

> Input: `prices = [1,3,7,5,10,3], fee = 3`
> Output: `6`

**Constraints:**

- `1 <= prices.length <= 5 * 10⁴`
- `1 <= prices[i] < 5 * 10⁴`
- `0 <= fee < 5 * 10⁴`

## Test Cases

``` python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
```

{% asset_code coding/assets/714-best-time-to-buy-and-sell-stock-with-transaction-fee/solution_test.py %}

## Thoughts

系列问题：

- [121. Best Time to Buy and Sell Stock](../121-best-time-to-buy-and-sell-stock/index.md) 最多交易 1 次
- [122. Best Time to Buy and Sell Stock II](../122-best-time-to-buy-and-sell-stock-ii/index.md) 交易任意多次
- [123. Best Time to Buy and Sell Stock III](../123-best-time-to-buy-and-sell-stock-iii/index.md) 最多交易 2 次
- [188. Best Time to Buy and Sell Stock IV](../188-best-time-to-buy-and-sell-stock-iv/index.md) 最多交易 k 次
- [309. Best Time to Buy and Sell Stock with Cooldown](../309-best-time-to-buy-and-sell-stock-with-cooldown/index.md) 交易任意多次，有冷静期

这次是在 [122. Best Time to Buy and Sell Stock II](../122-best-time-to-buy-and-sell-stock-ii/index.md)（交易任意多次）的基础上，增加了每次交易的交易费。

在 [122. Best Time to Buy and Sell Stock II](../122-best-time-to-buy-and-sell-stock-ii/index.md) 中已经定义了 [动态规划的状态及其转移函数](../122-best-time-to-buy-and-sell-stock-ii/index.md#DP)，那么直接在转移函数上，把交易费的影响加上去即可。更新后的转移函数为：

$$
\begin{cases}
  hold_i=\max\{hold_{i-1},empty_{i-1}-prices[i]\} \\
  empty_i=\max\{empty_{i-1},hold_{i-1}+prices[i]-fee\}
\end{cases}
$$

这里在卖出的时候扣除交易费。

同样是 `O(n)` 时间，`O(1)` 空间。

## Code

{% asset_code coding/assets/714-best-time-to-buy-and-sell-stock-with-transaction-fee/solution.py %}
