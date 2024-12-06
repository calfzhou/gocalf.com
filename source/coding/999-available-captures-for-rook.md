---
title: 999. Available Captures for Rook
notebook: coding
tags:
- easy
date: 2024-12-06 10:28:22
updated: 2024-12-06 10:28:22
---
## Problem

You are given an `8 x 8` **matrix** representing a chessboard. There is **exactly one** white rook represented by `'R'`, some number of white bishops `'B'`, and some number of black pawns `'p'`. Empty squares are represented by `'.'`.

A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece _or_ the edge of the board. A rook is **attacking** a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the **number of pawns** the white rook is **attacking**.

<https://leetcode.cn/problems/available-captures-for-rook/>

**Example 1:**

{% image 999-available-captures-for-rook/case1.png width:300px %}

> Input: `board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]`
> Output: `3`
> Explanation:
> In this example, the rook is attacking all the pawns.

**Example 2:**

{% image 999-available-captures-for-rook/case2.png width:300px %}

> Input: `board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]`
> Output: `0`
> Explanation:
> The bishops are blocking the rook from attacking any of the pawns.

**Example 3:**

{% image 999-available-captures-for-rook/case3.png width:300px %}

> Input: `board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]`
> Output: `3`
> Explanation:
> The rook is attacking the pawns at positions `b5`, `d6`, and `f5`.

**Constraints:**

- `board.length == 8`
- `board[i].length == 8`
- `board[i][j]` is either `'R'`, `'.'`, `'B'`, or `'p'`
- There is exactly one cell with `board[i][j] == 'R'`

## Test Cases

``` python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
```

{% asset_code coding/999-available-captures-for-rook/solution_test.py %}

## Thoughts

先找到 white rook 的位置，记为 `(r0, c0)`。从此位置开始，往上下左右四个方向逐格遍历，直到超出边界或遇到其他棋子。如果遇到的是 black pawns 则计数加一。

## Code

{% asset_code coding/999-available-captures-for-rook/solution.py %}
