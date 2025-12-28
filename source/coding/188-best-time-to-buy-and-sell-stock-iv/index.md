---
title: 188. Best Time to Buy and Sell Stock IV
notebook: coding
tags:
- hard
katex: true
date: 2024-12-18 20:55:31
updated: 2024-12-18 20:55:31
---
## Problem

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/>

**Example 1:**

> Input: `k = 2, prices = [2,4,1]`
> Output: `2`
> Explanation: Buy on day 1 (`price = 2`) and sell on day 2 (`price = 4`), `profit = 4-2 = 2`.

**Example 2:**

> Input: `k = 2, prices = [3,2,6,5,0,3]`
> Output: `7`
> Explanation: Buy on day 2 (`price = 2`) and sell on day 3 (`price = 6`), `profit = 6-2 = 4`. Then buy on day 5 (`price = 0`) and sell on day 6 (`price = 3`), `profit = 3-0 = 3`.

**Constraints:**

- `1 <= k <= 100`
- `1 <= prices.length <= 1000`
- `0 <= prices[i] <= 1000`

## Test Cases

``` python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
```

{% asset_code coding/188-best-time-to-buy-and-sell-stock-iv/solution_test.py %}

## Thoughts

同系列问题：

- [121. Best Time to Buy and Sell Stock](../121-best-time-to-buy-and-sell-stock/index.md) 交易最多 1 次
- [122. Best Time to Buy and Sell Stock II](../122-best-time-to-buy-and-sell-stock-ii/index.md) 交易任意多次
- [123. Best Time to Buy and Sell Stock III](../123-best-time-to-buy-and-sell-stock-iii/index.md) 交易最多 2 次

本题是交易至多指定的 k 次。

在 [123. Best Time to Buy and Sell Stock III](../123-best-time-to-buy-and-sell-stock-iii/index.md) 中特别定义了 [动态规划的状态及其转移函数](../123-best-time-to-buy-and-sell-stock-iii/index.md#DP)，虽然对那道题的帮助不是很大，但稍加扩展就可以直接应用于本题。

定义 `buy(i, j)` 表示在第 i 天结束前，（至少买入 1 次）至多买入 j 次，最大的现金余额（同样设可以借钱买股票，初始余额为 0），`sell(i, j)` 表示在第 i 天结束前，至多卖出 j 次，最大的现金余额。

> 显然 `buy(i, 1) = buy1(i)`，`buy(i, 2) = buy2(i)`，`sell(i, 1) = sell1(i)`，`sell(i, 2) = sell2(i)`。

递推关系也类似地调整为：

$$
\begin{cases}
  buy_{1,j}=-prices[0] \\
  sell_{1,j}=0 \\
  buy_{i,1}=\max\{buy_{i-1,j},-prices[i]\} \\
  buy_{i,j}=\max\{buy_{i-1,j},sell_{i-1,j-1}-prices[i]\} \\
  sell_{i,j}=\max\{sell_{i-1,j},buy_{i-1,j}+prices[i]\}
\end{cases}
$$

同样只需要保留前一天的 k 对 buy 和 sell 值即可。

> 小心 k-刺客：如果有 n 天，则最多可以交易 $\lfloor n/2\rfloor$ 次。如果给定的 k 过大，可以先把 k 改成 $\lfloor n/2\rfloor$。另外如果 k 是 0，直接返回 0 即可。

## Code

{% asset_code coding/188-best-time-to-buy-and-sell-stock-iv/solution.py %}
