---
title: 62. Unique Paths
notebook: coding
tags:
- medium
date: 2024-11-19 01:14:33
updated: 2024-11-19 10:15:26
katex: true
---
## Problem

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

<https://leetcode.com/problems/unique-paths/>

**Example 1:**

{% invert %}
{% image 62-unique-paths/case1.png %}
{% endinvert %}

> Input: `m = 3, n = 7`
> Output: `28`

**Example 2:**

> Input: `m = 3, n = 2`
> Output: `3`
> Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
>
> 1. Right -> Down -> Down
> 2. Down -> Down -> Right
> 3. Down -> Right -> Down

**Constraints:**

- `1 <= m, n <= 100`

## Test Cases

{% asset_code coding/62-unique-paths/solution_test.py %}

## Thoughts

看任意的 i、j，要走到 `grid[i][j]`，需要从上边（`grid[i-1][j]`）或左边（`grid[i][j-1]`）过来，所以记 `u[i][j]` 为走到 `grid[i][j]` 的路径总数，显然有：

$$
u[i][j]=\begin{cases}
1 & \text{ if } i=0\lor j=0 \\
u[i-1][j]+u[i][j-1] & \text{ otherwise }
\end{cases}
$$

`u[m-1][n-1]` 即为最终结果。

推算过程中只需要保留最新的一行或一列，空间复杂度 `O(min{m, n})`，时间复杂度 `O(m * n)`。

## Code

{% asset_code coding/62-unique-paths/solution.py %}

## Math

如果把所有的 `u[i][j]` 都写下来，很容易发现这就是个斜的杨辉三角，`u[i][j]` 就对应于杨辉三角中 `i + j` 行（注意顶行是「行 0」）的 `i` 或 `j` 列（同样最左列也是「列 0」）。

{% invert %}
{% diagramsnet 62-unique-paths/pascal.drawio %}
{% endinvert %}

可以直接用杨辉三角的计算公式（组合数）：

$$
u[i][j]=\binom{i+j}{i}=\frac{(i+j)!}{i!j!}
$$

实际上从 `[0][0]` 走到 `[i][j]`，一共需要移动 `i + j` 次，其中有 `i` 次向下，其余 `j` 次向右。那么所有的可能路径数量，就等于从 `i + j` 次移动中，任选 `i` 次（向下走）的可能数，即 `C(i+j, i)`。

如果 i、j 不是很大，可以直接利用阶乘函数 `math.factorial` 计算，否则也可以自己展开阶乘公式对分子分母约分之后计算。不妨设 `j <= i`，可得：$C(i+j,i)=\frac{(i+1)(i+2)\cdots(i+j)}{1\times 2\times \cdots \times j}=(i+1)\div 1\times(i+2)\div 2\times(i+3)\div 3\times \cdots \times(i+j)\div j$。从左向右计算的时候，每次除法都一定能除尽，因为任意连续 n 个自然数中一定有一个是 n 的倍数。

整体时间复杂度为 `O(min{m,n})`，空间复杂度 `O(1)`。

{% asset_code coding/62-unique-paths/solution_math.py %}
