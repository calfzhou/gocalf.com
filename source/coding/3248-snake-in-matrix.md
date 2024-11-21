---
title: 3248. Snake in Matrix
notebook: coding
tags:
- easy
date: 2024-11-21 10:05:04
updated: 2024-11-21 10:05:04
---
## Problem

There is a snake in an `n x n` matrix `grid` and can move in **four possible directions**. Each cell in the `grid` is identified by the position: `grid[i][j] = (i * n) + j`.

The snake starts at cell 0 and follows a sequence of commands.

You are given an integer `n` representing the size of the `grid` and an array of strings `commands` where each `command[i]` is either `"UP"`, `"RIGHT"`, `"DOWN"`, and `"LEFT"`. It's guaranteed that the snake will remain within the `grid` boundaries throughout its movement.

Return the position of the final cell where the snake ends up after executing `commands`.

<https://leetcode.cn/problems/snake-in-matrix/>

**Example 1:**

> Input: `n = 2, commands = ["RIGHT","DOWN"]`
> Output: `3`
> Explanation:
> {% invert %}
{% diagramsnet 3248-snake-in-matrix/case1.drawio %}
{% endinvert %}

**Example 2:**

> Input: `n = 3, commands = ["DOWN","RIGHT","UP"]`
> Output: `1`
> Explanation:
> {% invert %}
{% diagramsnet 3248-snake-in-matrix/case2.drawio %}
{% endinvert %}

**Constraints:**

- `2 <= n <= 10`
- `1 <= commands.length <= 100`
- `commands` consists only of `"UP"`, `"RIGHT"`, `"DOWN"`, and `"LEFT"`.
- The input is generated such the snake will not move outside of the boundaries.

## Test Cases

{% asset_code coding/3248-snake-in-matrix/solution_test.py %}

## Thoughts

`i = j = 0`。

- UP: `i--`
- RIGHT: `j++`
- DOWN: `i++`
- LEFT: `j--`

## Code

{% asset_code coding/3248-snake-in-matrix/solution.py %}
