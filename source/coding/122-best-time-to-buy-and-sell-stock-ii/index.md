---
title: 122. Best Time to Buy and Sell Stock II
notebook: coding
tags:
- medium
katex: true
date: 2024-12-15 22:47:02
updated: 2024-12-18 21:43:33
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

[121. Best Time to Buy and Sell Stock](../121-best-time-to-buy-and-sell-stock/index.md) 的进阶版，可以买入卖出多次了（且同一天内可以既买也卖，但最多只能持有一份）。

如果明天的价格高，那么就今天买、明天卖，赚了这一笔差价。否则（明天价格低），今天就不买。

扫描数组，只要 `nums[i+1]` 比 `nums[i]` 大，就在第 i 天买入并在第 `i + 1` 天卖出，将差值累加都已有收益上。最终得到总的收益。

> 感觉比 [121. Best Time to Buy and Sell Stock](../121-best-time-to-buy-and-sell-stock/index.md) 简单呢。

## Code

{% asset_code coding/122-best-time-to-buy-and-sell-stock-ii/solution.py %}

## DP

为了后续的进阶题目（如 [309. Best Time to Buy and Sell Stock with Cooldown](../309-best-time-to-buy-and-sell-stock-with-cooldown/index.md)、[714. Best Time to Buy and Sell Stock with Transaction Fee](../714-best-time-to-buy-and-sell-stock-with-transaction-fee/index.md)）扩展起来方便，这里也用常规动态规划的方式解一下。

在 [188. Best Time to Buy and Sell Stock IV](../188-best-time-to-buy-and-sell-stock-iv/index.md) 中定义了状态量 `buy` 和 `sell`，为了能够控制最大交易次数，引入了日期和交易次数两个维度。[123. Best Time to Buy and Sell Stock III](../123-best-time-to-buy-and-sell-stock-iii/index.md) 中的 DP 相当于 `k = 2` 的特例。[121. Best Time to Buy and Sell Stock](../121-best-time-to-buy-and-sell-stock/index.md) 中虽然没有显式使用 DP，但两个局部变量 `min_price` 和 `max_profit` 相当于 `k = 1` 的特例。

这里不限制交易次数，那就更简单了，状态量反倒可以退化回到只有一个日期维度。

之前用 `buy` 和 `sell` 做变量名，更强调「买入」和「卖出」的动作，这里改用 `hold` 和 `empty` 更贴合「状态」的概念。`hold(i)` 表示在第 i 天结束前，如果持有股票的话，最大的现金余额（同样设可以借钱买股票，初始余额为 0）。`empty(i)` 表示在第 i 天结束前，不持有股票的话，最大的现金余额。显然这里并不限制是第几次买入，或者卖出了几次。

状态转移函数则为：

$$
\begin{cases}
  hold_i=\max\{hold_{i-1},empty_{i-1}-prices[i]\} \\
  empty_i=\max\{empty_{i-1},hold_{i-1}+prices[i]\}
\end{cases}
$$

也就是说，持仓时的最大值，要么是昨天就已经持仓了，今天保持持仓；要么是昨天是空仓，今天买入；两种情况取最大。空仓时的最大值，要么是昨天已经空仓了，今天保持空仓；要么是昨天持仓，今天卖出；两种情况取最大。

初始值定义 `hold(0) = -prices[0]`，`empty(0) = 0`。最终结果取 `empty(n)`。

实际计算时，只需要保留前一天的状态值，空间复杂度 `O(1)`，时间复杂度 `O(n)`。

显然这里的 `hold` 和 `empty` 跟 [188. Best Time to Buy and Sell Stock IV](../188-best-time-to-buy-and-sell-stock-iv/index.md) 中的 `buy` 和 `sell` 内核是完全一致的。

其实上边的解法中，变量 prev 就等价于这里的 hold，`max_profit` 就等价于这里的 `empty`。

{% asset_code coding/122-best-time-to-buy-and-sell-stock-ii/solution2.py %}
