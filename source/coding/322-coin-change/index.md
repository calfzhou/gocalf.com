---
title: 322. Coin Change
notebook: coding
tags:
- medium
date: 2024-11-19 23:42:33
updated: 2024-11-19 23:42:33
katex: true
---
## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

<https://leetcode.com/problems/coin-change/>

**Example 1:**

> Input: `coins = [1,2,5], amount = 11`
> Output: `3`
> Explanation: `11 = 5 + 5 + 1`

**Example 2:**

> Input: `coins = [2], amount = 3`
> Output: `-1`

**Example 3:**

> Input: `coins = [1], amount = 0`
> Output: `0`

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2³¹ - 1`
- `0 <= amount <= 10⁴`

## Test Cases

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
```

{% asset_code coding/322-coin-change/solution_test.py %}

## Thoughts

任取一种硬币 i，如果金额 `amount - coins[i]` 可以由最少 m 枚硬币组合而成，那么给这堆硬币再增加一枚硬币 i（共 `m + 1` 枚），就可以组合出金额 `amount`。所有可能的组合方式中，取最小的那个就是所求的值。而如果找不到这样的组合，就说明金额 `amount` 无法由 `coins` 组合出来。

记组合出金额 `a` 的最少硬币数量为 `mc[a]`，有（其中 `∞` 表示组合不出来）：

$$
mc[a]=\begin{cases}
  0 & \text{if }a=0 \\
  \infty & \text{if }0<a<\min_i\{coins[i]\} \\
  1+\min_i\{mc[a-coins[i]]\mid coins[i]\le a\} & \text{otherwise} \\
\end{cases}
$$

这样从 `mc[0]` 开始一直推算到 `mc[amount]` 即可。最后如果 `mc[amount] = ∞`，按要求返回 `-1` 即可（实践中可以用 `amount + 1` 替代 `∞`，只要结果大于 `amount` 就是组合不出来的意思）。

时间复杂度是 `O(amount * C)`（`C` 是不同面值的硬币种类数量），空间复杂度是 `O(amount)`。

可以发现在计算 `mc[a]` 的时候，最多只会用到 $a-c_{max}$ 及之后的值（其中 $c_{max}=\max_i\{coins[i]\}$ 即硬币的最大面值）。所以保存 `mc` 中间结果的时候，只需要始终保留最新的 $c_{max}$ 个值即可，空间复杂度为 $O(c_{max})$。

## Code

{% asset_code coding/322-coin-change/solution.py %}
