---
title: 2337. Move Pieces to Obtain a String
notebook: coding
tags:
- medium
date: 2024-12-05 15:17:16
updated: 2024-12-05 15:17:16
---
## Problem

You are given two strings `start` and `target`, both of length `n`. Each string consists **only** of the characters `'L'`, `'R'`, and `'_'` where:

- The characters `'L'` and `'R'` represent pieces, where a piece `'L'` can move to the **left** only if there is a **blank** space directly to its left, and a piece `'R'` can move to the **right** only if there is a **blank** space directly to its right.
- The character `'_'` represents a blank space that can be occupied by **any** of the `'L'` or `'R'` pieces.

Return `true` _if it is possible to obtain the string_ `target` _by moving the pieces of the string_ `start` _**any** number of times_. Otherwise, return `false`.

<https://leetcode.com/problems/move-pieces-to-obtain-a-string/>

**Example 1:**

> Input: `start = "_L__R__R_", target = "L______RR"`
> Output: `true`
> Explanation: We can obtain the string target from start by doing the following moves:
>
> - Move the first piece one step to the left, start becomes equal to `"L___R__R_"`.
> - Move the last piece one step to the right, start becomes equal to `"L___R___R"`.
> - Move the second piece three steps to the right, start becomes equal to `"L______RR"`.
> Since it is possible to get the string target from start, we return true.

**Example 2:**

> Input: `start = "R_L_", target = "__LR"`
> Output: `false`
> Explanation: The `'R'` piece in the string start can move one step to the right to obtain `"_RL_".`
> After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

**Example 3:**

> Input: `start = "_R", target = "R_"`
> Output: `false`
> Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

**Constraints:**

- `n == start.length == target.length`
- `1 <= n <= 10⁵`
- `start` and `target` consist of the characters `'L'`, `'R'`, and `'_'`.

## Test Cases

``` python
class Solution:
    def canChange(self, start: str, target: str) -> bool:
```

{% asset_code coding/2337-move-pieces-to-obtain-a-string/solution_test.py %}

## Thoughts

首先 `start` 和 `target` 中 `L` 和 `R` 的排列顺序必须完全一致，否则怎么移动都没用。

从 `start` 和 `target` 最左开始，分别取下一个非空白的 piece（设下标分别为 i、j），如果两个 piece 不一样（一个是 `L` 另一个是 `R`）则一定不行。

如果两个 pieces 都是 `L`，则 `i < j` 时不行。反之，如果两个 pieces 都是 `R`，则 `i > j` 时不行。

因为有可能一个字符串先扫描完了，需要检查另一个字符串剩余的部分是否都是空白，如果还有非空白的 piece 也不行。

`O(n)` 时间，`O(1)` 空间。

还有一个办法是同步扫描 `start` 和 `target`（下标始终一致）。用变量记录 `start` 里有几个 `R` 在右移中，或者在 `target` 里见到了几个 `L` 等着 `start` 提供（需求量）（两种情况不能同时出现，可以用一个变量的正数和负数记录）。根据 `start` 和 `target` 当前的 piece 判断是否可行。

1. `start` 当前 piece 是 `R`：如果在等着 `L` 则失败；否则 `R` 数量加一。
2. `target` 当前 piece 是 `R`：如果 `R` 数量为 0 则失败；否则 `R` 数量减一。
3. `target` 当前 piece 是 `L`：如果已经有 `R` 了则失败；否则 `L` 的需求量加一。
4. `start` 当前 piece 是 `L`：如果 `L` 的需求量为 0 则失败；否则 `L` 需求量减一。

注意边界条件要求 2 必须在 1 之后判定，4 必须在 3 之后判定。

也是 `O(n)` 时间，`O(1)` 空间。

## Code

{% asset_code coding/2337-move-pieces-to-obtain-a-string/solution.py %}

{% asset_code coding/2337-move-pieces-to-obtain-a-string/solution2.py %}
