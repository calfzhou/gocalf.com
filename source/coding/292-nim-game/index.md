---
title: 292. Nim Game
notebook: coding
tags:
- easy
katex: true
date: 2025-01-02 23:56:17
updated: 2025-01-02 23:56:17
---
## Problem

You are playing the following Nim Game with your friend:

- Initially, there is a heap of stones on the table.
- You and your friend will alternate taking turns, and **you go first**.
- On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
- The one who removes the last stone is the winner.

Given `n`, the number of stones in the heap, return `true` _if you can win the game assuming both you and your friend play optimally, otherwise return_ `false`.

<https://leetcode.com/problems/nim-game/>

**Example 1:**

> Input: `n = 4`
> Output: `false`
> Explanation: These are the possible outcomes:
>
> 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
> 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
> 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
>
> In all outcomes, your friend wins.

**Example 2:**

> Input: n = 1
> Output: true

**Example 3:**

> Input: n = 2
> Output: true

**Constraints:**

- `1 <= n <= 2³¹ - 1`

## Test Cases

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
```

{% asset_code coding/292-nim-game/solution_test.py %}

## Thoughts

定义 `dp(i)` 表示初始时有 i 个石子，先手玩家是否能赢。显然 `dp(1) = dp(2) = dp(3) = true`，因为先手玩家可以直接把所有石子拿走而获胜。

看任意的 i（`i > 3`）。先手玩家可以拿走 1 个、2 个或 3 个石子，如果这三种情况，有一种能让对方输，先手玩家就按对应的数量拿走石子即可。但如果三种情况，对方都能赢，那么先手玩家必输。所以看 `dp(i - 1)`、`dp(i - 2)` 和 `dp(i - 3)` 是否有 false（此时相当于子问题下，对方先手，false 就表示对方输），如果有则 `dp(i) = true`，否则 `dp(i) = false`。

$$
\begin{matrix}
  dp_i & =\lnot dp_{i-1}\lor\lnot dp_{i-2}\lor\lnot dp_{i-3} \\
  & =\lnot(dp_{i-1}\land dp_{i-2}\land dp_{i-3})
\end{matrix}
$$

易知从 1 开始，每连续 3 个 true 之后会有一个 false（`T, T, T, F, T, T, T, F, ……`）。所以可以直接推出 dp 的算式为：

$$
dp_i=i\not\equiv 0\pmod{4}
$$

## Code

{% asset_code coding/292-nim-game/solution.py %}
