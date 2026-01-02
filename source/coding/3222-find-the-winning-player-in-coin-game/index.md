---
title: 3222. Find the Winning Player in Coin Game
notebook: coding
tags:
- easy
date: 2024-11-27 13:08:55
updated: 2024-11-27 13:08:55
---
## Problem

You are given two **positive** integers `x` and `y`, denoting the number of coins with values 75 and 10 _respectively_.

Alice and Bob are playing a game. Each turn, starting with **Alice**, the player must pick up coins with a **total** value 115. If the player is unable to do so, they **lose** the game.

Return the _name_ of the player who wins the game if both players play **optimally**.

<https://leetcode.cn/problems/find-the-winning-player-in-coin-game/>

**Example 1:**

> Input: `x = 2, y = 7`
> Output: `"Alice"`
> Explanation:
> The game ends in a single turn:
> Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.

**Example 2:**

> Input: `x = 4, y = 11`
> Output: `"Bob"`
> Explanation:
> The game ends in 2 turns:
> Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.
> Bob picks 1 coin with a value of 75 and 4 coins with a value of 10.

**Constraints:**

- `1 <= x, y <= 100`

## Test Cases

```python
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
```

{% snippet solution_test.py %}

## Thoughts

因为 `105 = 75 * 1 + 10 * 4` 是唯一的拿硬币方案，所以看二元组 `(x, y)` 除以 `(1, 4)` 的整数部分，是几就表示可以拿几次硬币。如果次数是奇数则 Alice 赢，否则 Bob 硬。

`(x, y) // (1, 4) = min(x // 1, y // 4)`。

## Code

{% snippet solution.py %}
