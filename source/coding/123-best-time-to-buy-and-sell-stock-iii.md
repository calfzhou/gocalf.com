---
title: 123. Best Time to Buy and Sell Stock III
notebook: coding
tags:
- hard
- todo
date: 2024-12-16 00:25:54
updated: 2024-12-16 00:25:54
---
## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/>

**Example 1:**

> Input: `prices = [3,3,5,0,0,3,1,4]`
> Output: `6`
> Explanation: Buy on day 4 (`price = 0`) and sell on day 6 (`price = 3`), `profit = 3-0 = 3`.
> Then buy on day 7 (`price = 1`) and sell on day 8 (`price = 4`), `profit = 4-1 = 3`.

**Example 2:**

> Input: `prices = [1,2,3,4,5]`
> Output: `4`
> Explanation: Buy on day 1 (`price = 1`) and sell on day 5 (`price = 5`), `profit = 5-1 = 4`.
> Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

**Example 3:**

> Input: `prices = [7,6,4,3,1]`
> Output: `0`
> Explanation: In this case, no transaction is done, i.e. max profit `= 0`.

**Constraints:**

- `1 <= prices.length <= 10⁵`
- `0 <= prices[i] <= 10⁵`

## Test Cases

``` python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

{% asset_code coding/123-best-time-to-buy-and-sell-stock-iii/solution_test.py %}

## Thoughts

[121. Best Time to Buy and Sell Stock](121-best-time-to-buy-and-sell-stock) 和 [122. Best Time to Buy and Sell Stock II](122-best-time-to-buy-and-sell-stock-ii) 的进阶版，限制最多只能买卖两次（但依然最多只能持有一份）。

想到一个比较巧妙的办法。首先按 [121. Best Time to Buy and Sell Stock](121-best-time-to-buy-and-sell-stock) 中的方法计算出单次交易所能获得的最大收益，但稍微调整一下，同时返回最大收益所对应的买入和卖出的日子。然后在这笔交易的买入日之前的日子中，再计算一次能获得的最大收益；再这笔交易的卖出日之后的日子中，也计算一次能获得的最大收益。前后的两次交易，取收益较大的那笔，跟最大收益的交易合起来，可以得到两次交易的最大收益。

当然这个贪心是不完备的，还少了一种可能性，就是把最大收益的交易拆成两笔，因为中间可能有下跌的时间段，如果能在下跌前卖出，在下跌后再次买入，也能得到更大的收益。一个简单的办法是计算从买入日的第二天，到卖出日的前一天，只交易一次的最大损失，把这笔损失避免掉即可。实际计算的时候可以假设时间逆转了（逆序遍历 `prices` 数组），得到的最大收益其实就是最大损失的相反数。

于是总共需要调用四次 [problem 121](121-best-time-to-buy-and-sell-stock) 的 solution，总共时间复杂度 `O(n)`，空间复杂度 `O(1)`。

提交后运行时间 `99+%`。

## Code

{% asset_code coding/123-best-time-to-buy-and-sell-stock-iii/solution.py %}

更加「动态规划」的方法之后补充。
