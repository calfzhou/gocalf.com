---
title: 983. Minimum Cost For Tickets
notebook: coding
tags:
- medium
katex: true
date: 2024-12-31 11:48:02
updated: 2024-12-31 11:48:02
---
## Problem

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array `days`. Each day is an integer from `1` to `365`.

Train tickets are sold in **three different ways**:

- a **1-day** pass is sold for `costs[0]` dollars,
- a **7-day** pass is sold for `costs[1]` dollars, and
- a **30-day** pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel.

- For example, if we get a **7-day** pass on day `2`, then we can travel for `7` days: `2`, `3`, `4`, `5`, `6`, `7`, and `8`.

Return _the minimum number of dollars you need to travel every day in the given list of days_.

<https://leetcode.com/problems/minimum-cost-for-tickets/>

**Example 1:**

> Input: days = [1,4,6,7,8,20], costs = [2,7,15]
> Output: 11
> Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
> On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
> On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
> On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
> In total, you spent $11 and covered all the days of your travel.

**Example 2:**

> Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
> Output: 17
> Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
> On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
> On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
> In total, you spent $17 and covered all the days of your travel.

**Constraints:**

- `1 <= days.length <= 365`
- `1 <= days[i] <= 365`
- `days` is in strictly increasing order.
- `costs.length == 3`
- `1 <= costs[i] <= 1000`

## Test Cases

``` python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
```

{% asset_code coding/assets/983-minimum-cost-for-tickets/solution_test.py %}

## Thoughts

如果某一天要出行，要么当天买单日票，要么直接用最早 6 天前买的七日票，要么直接用最早 29 天前买的三十日票。如果不出行，则当天不再额外花钱。

定义 `dp(d)` 表示截止到第 d（1-indexed）天的最低旅行成本，那么有：

$$
dp(d)=\begin{cases}
  dp(d-1) & \text{if not travel on day d} \\
  \min\begin{cases}
    dp(d-1)+costs[0] \\
    dp(d-7)+costs[1] \\
    dp(d-30)+costs[2]
  \end{cases}
\end{cases}
$$

定义 `dp(∀d < 1) = 0`。然后从 `d = 1` 递推到最后一个旅行日（`days[-1]`），最终结果为 `dp(days[-1])`。

因为最多只需要用到 30 天前的 dp 值，可以像 [2466. Count Ways To Build Good Strings](../2466-count-ways-to-build-good-strings/index.md) 那样用队列保持最新的至多 30 个值，节省一点儿空间。

时间复杂度 `O(days[-1])`，空间复杂度 `O(1)`（30 记为常数）。

## Code

{% asset_code coding/assets/983-minimum-cost-for-tickets/solution.py %}
