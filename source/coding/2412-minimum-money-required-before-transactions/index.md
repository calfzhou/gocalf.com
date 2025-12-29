---
title: 2412. Minimum Money Required Before Transactions
notebook: coding
tags:
- hard
katex: true
date: 2025-01-25 21:51:40
updated: 2025-01-25 21:51:40
---
## Problem

You are given a **0-indexed** 2D integer array `transactions`, where `transactions[i] = [costᵢ, cashbackᵢ]`.

The array describes transactions, where each transaction must be completed exactly once in **some order**. At any given moment, you have a certain amount of `money`. In order to complete transaction `i`, `money >= costᵢ` must hold true. After performing a transaction, `money` becomes `money - costᵢ + cashbackᵢ`.

Return _the minimum amount of_ `money` _required before any transaction so that all of the transactions can be completed **regardless of the order** of the transactions._

<https://leetcode.cn/problems/minimum-money-required-before-transactions/>

**Example 1:**

> Input: `transactions = [[2,1],[5,0],[4,2]]`
> Output: `10`
> Explanation:
> Starting with `money = 10`, the transactions can be performed in any order.
> It can be shown that starting with `money < 10` will fail to complete all transactions in some order.

**Example 2:**

> Input: `transactions = [[3,0],[0,3]]`
> Output: `3`
> Explanation:
>
> - If transactions are in the order `[[3,0],[0,3]]`, the minimum money required to complete the transactions is 3.
> - If transactions are in the order `[[0,3],[3,0]]`, the minimum money required to complete the transactions is 0.
>
> Thus, starting with `money = 3`, the transactions can be performed in any order.

**Constraints:**

- `1 <= transactions.length <= 10⁵`
- `transactions[i].length == 2`
- `0 <= costᵢ, cashbackᵢ <= 10⁹`

## Test Cases

```python
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
```

{% asset_code coding/2412-minimum-money-required-before-transactions/solution_test.py %}

## Thoughts

关键是要找到对初始金额要求最高的交易顺序。

如果 `costᵢ > cashbackᵢ` 则 `transactions[i]` 是亏钱的，否则是赚钱（或不亏）的。显然应该先做亏钱的交易，如果能够完成，那么先做赚钱的交易也一定能完成。

统计所有亏钱交易总共会亏掉多少钱，记为 `total_lost`，易知：

$$
total\_lost=\sum_i{\max{\{cost_i-cashback_i,0\}}}
$$

初始金额 money 需要保证最后一笔亏钱交易的 cost 花掉之后（对应的 cashback 得到之前），余额大于等于 0。不妨设最后一笔亏钱的交易为 `transactions[j]`，可得 `money - total_lost - cashbackⱼ ≥ 0`，即 `money ≥ total_lost + cashbackⱼ`。为保证任何交易顺序都能完成，需要让 money 的下界最大，所以要求 `cashbackⱼ` 最大。

所有亏钱交易完成后，余额为 `money - total_lost`。剩下的都是不亏钱的交易，需要保证任何一笔交易开始前的余额大于等于该交易的 cost。显然只要 `money - total_lost` 大于等于不亏钱交易中最大的 cost 即可。设 cost 最大的不亏钱交易为 `transactions[k]`，有 `money - total_lost ≥ costₖ`，即 `money ≥ total_lost + costₖ`。

所以最终，初始金额的最小值取 `total_lost + max{cashbackⱼ, costₖ}`（其中 `cashbackⱼ` 是亏钱交易中的最大 cashback，`costₖ` 是不亏钱交易中的最小 cost），可以保证任意交易顺序都能全部完成。

只需要遍历一次 transactions，即可得到 `total_lost`、`cashbackⱼ` 和 `costₖ`。时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/2412-minimum-money-required-before-transactions/solution.py %}
