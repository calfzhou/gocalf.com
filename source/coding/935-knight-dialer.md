---
title: 935. Knight Dialer
notebook: coding
tags:
- medium
katex: true
date: 2024-12-10 14:29:41
updated: 2024-12-10 14:29:41
---
## Problem

The chess knight has a **unique movement**, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an **L**). The possible movements of chess knight are shown in this diagram:

A chess knight can move as indicated in the chess diagram below:

{% image 935-knight-dialer/board.png width:200px %}

We have a chess knight and a phone pad as shown below, the knight **can only stand on a numeric cell** (i.e. blue cell).

{% image 935-knight-dialer/dailer.png width:150px %}

Given an integer `n`, return how many distinct phone numbers of length `n` we can dial.

You are allowed to place the knight **on any numeric cell** initially and then you should perform `n - 1` jumps to dial a number of length `n`. All jumps should be **valid** knight jumps.

As the answer may be very large, **return the answer modulo** `10⁹ + 7`.

<https://leetcode.cn/problems/knight-dialer/>

**Example 1:**

> Input: `n = 1`
> Output: `10`
> Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

**Example 2:**

> Input: `n = 2`
> Output: `20`
> Explanation: All the valid number we can dial are `[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]`.

**Example 3:**

> Input: `n = 3131`
> Output: `136006598`
> Explanation: Please take care of the mod.

**Constraints:**

- `1 <= n <= 5000`

## Test Cases

``` python
class Solution:
    def knightDialer(self, n: int) -> int:
```

{% asset_code coding/935-knight-dialer/solution_test.py %}

## Thoughts

记 `cnts(d, i)` 表示按 i 次按键，且最后一个是 d（`0 <= d <= 9`）的情况下，能得到的长度为 i 的不同电话号码数量。题目所求结果为 $\sum_{d=0}^9cnts(d,n)$。

显然有初始值 `cnts(d, 1) = 1`。递推式为 $cnts(d,i)=\sum_s{cnts(s,i-1)}$，其中 s 是所有能一步跳到 d 的按键，可以按照键盘的结构计算出来，也可以提前计算好，用的时候直接查表。

| d | s       |
|---|---------|
| 0 | 4, 6    |
| 1 | 6, 8    |
| 2 | 7, 9    |
| 3 | 4, 8    |
| 4 | 0, 3, 9 |
| 5 | n/a     |
| 6 | 0, 1, 7 |
| 7 | 2, 6    |
| 8 | 1, 3    |
| 9 | 2, 4    |

直接按照初始值加递推公式计算即可。

因为计算 `cnts(*, i)` 时只需要用到 `cnts(*, i-1)`，所以只需要保留前一组 `cnts` 结果即可。

时间复杂度 `O(n)`，空间复杂度 `O(1)`（按键的个数记为常数）。

## Code

{% asset_code coding/935-knight-dialer/solution.py %}

## Faster

上边的每次循环里需要计算 10 组，每一组还要计算 2 到 3 次不等。可以发现有些按键是完全对称的，它们的 `cnts` 值永远都一样。

观察按键布局，很容易发现首先当 `i > 1` 时，按键 `5` 永远不可达，可以丢弃。剩下的 9 个按键，可以分为 4 组，每组内各个按键的 `cnts` 是始终一致的。这 4 组分别为：

- A: 1, 3, 7, 9
- B: 2, 8
- C: 4, 6
- D: 0

把每个按键数字的分组对应更新到上边的表中得到：

| g(d) | d | s       | g(s)    |
|------|---|---------|---------|
| D    | 0 | 4, 6    | C, C    |
| A    | 1 | 6, 8    | C, B    |
| B    | 2 | 7, 9    | A, A    |
| A    | 3 | 4, 8    | C, B    |
| C    | 4 | 0, 3, 9 | D, A, A |
| n/a  | 5 | n/a     | n/a     |
| C    | 6 | 0, 1, 7 | D, A, A |
| A    | 7 | 2, 6    | B, C    |
| B    | 8 | 1, 3    | A, A    |
| A    | 9 | 2, 4    | B, C    |

可以得到初值和递推公式：

$$
\begin{cases}
  A_1=B_1=C_1=D_1=1 \\
  A_{i}=B_{i-1}+C_{i-1} \\
  B_{i}=2\times A_{i-1} \\
  C_{i}=2\times A_{i-1}+D_{i-1} \\
  D_{i}=2\times C_{i-1}
\end{cases}
$$

最终的结果应为 $4\times A_n+2\times B_n+2\times C_n+D_n$。

时间和空间复杂度不变，但运算量会少很多。

{% asset_code coding/935-knight-dialer/solution2.py %}

## O(log n)

在 [70. Climbing Stairs](70-climbing-stairs) 中使用矩阵幂运算用 `O(log n)` 时间计算斐波那契（Fibonacci）数，这里也可以用类似的方法。

把上边关于 A、B、C、D 的递推式改造成矩阵形式：

$$
\begin{bmatrix}
  A_n \\
  B_n \\
  C_n \\
  D_n
\end{bmatrix}
=\begin{bmatrix}
  0 & 1 & 1 & 0 \\
  2 & 0 & 0 & 0 \\
  2 & 0 & 0 & 1 \\
  0 & 0 & 2 & 0
\end{bmatrix}
\times\begin{bmatrix}
  A_{n-1} \\
  B_{n-1} \\
  C_{n-1} \\
  D_{n-1}
\end{bmatrix}
$$

递推展开可得：

$$
\begin{bmatrix}
  A_n \\
  B_n \\
  C_n \\
  D_n
\end{bmatrix}
=\begin{bmatrix}
  0 & 1 & 1 & 0 \\
  2 & 0 & 0 & 0 \\
  2 & 0 & 0 & 1 \\
  0 & 0 & 2 & 0
\end{bmatrix}^{n-1}
\times\begin{bmatrix}
  1 \\
  1 \\
  1 \\
  1
\end{bmatrix}
$$

所以最终结果为：

$$
\begin{bmatrix}
  4 & 2 & 2 & 1
\end{bmatrix}
\times\begin{bmatrix}
  0 & 1 & 1 & 0 \\
  2 & 0 & 0 & 0 \\
  2 & 0 & 0 & 1 \\
  0 & 0 & 2 & 0
\end{bmatrix}^{n-1}
\times\begin{bmatrix}
  1 \\
  1 \\
  1 \\
  1
\end{bmatrix}
$$

中间的矩阵幂运算可以用 `O(log n)` 时间完成。

因为本题会一直对 `10⁹ + 7` 取模，不涉及到大整数计算，所以二进制位数带来的时间复杂度是常数，最终时间复杂度是 `O(log n)`。

{% asset_code coding/935-knight-dialer/solution3.py %}

附：三段代码的运行时长（μs）对比：

| n     | [solution](935-knight-dialer/solution.py) | [solution2](935-knight-dialer/solution2.py) | [solution3](935-knight-dialer/solution3.py) |
|-------|--------:|-------:|------:|
| 30    |   148.6 |   14.3 | 144.8 |
| 100   |   510.2 |   48.7 | 185.8 |
| 300   |  1606.7 |  145.9 | 245.0 |
| 1000  |  5115.4 |  505.8 | 315.6 |
| 3000  | 15224.8 | 1529.9 | 371.3 |
| 10000 | 51101.8 | 5175.0 | 395.5 |
