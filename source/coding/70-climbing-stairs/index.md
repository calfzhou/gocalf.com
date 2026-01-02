---
title: 70. Climbing Stairs
notebook: coding
tags:
- easy
date: 2024-11-20 23:35:30
updated: 2024-11-20 23:35:30
katex: true
---
## Problem

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

<https://leetcode.com/problems/climbing-stairs/>

**Example 1:**

> Input: `n = 2`
> Output: `2`
> Explanation: There are two ways to climb to the top.
>
> 1. 1 step + 1 step
> 2. 2 steps

**Example 2:**

> Input: `n = 3`
> Output: `3`
> Explanation: There are three ways to climb to the top.
>
> 1. 1 step + 1 step + 1 step
> 2. 1 step + 2 steps
> 3. 2 steps + 1 step

**Constraints:**

- `1 <= n <= 45`

## Test Cases

```python
class Solution:
    def climbStairs(self, n: int) -> int:
```

{% snippet solution_test.py %}

## Thoughts

要走到第 n 个台阶，最后一步可能是上了一级或者两级，也就是要先走到 `n - 1` 或 `n - 2` 处。如果走到 `n - 1` 共有 `w[n-1]` 种不同的走法，走到 `n - 2` 共有 `w[n-2]` 种不同的走法，那么显然 `w[n] = w[n-1] + w[n-2]`。

初始值 `w[1] = 1`，并定义 `w[0] = 1`（一步不动也算一种方案）。

直接递推计算即可。时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% snippet solution.py %}

## O(log n)

斐波那契数列的定义是：

$$
\begin{cases}
  F_0=0 \\
  F_1=1 \\
  F_n=F_{n-1}+F_{n-2}
\end{cases}
$$

可见 `w` 跟斐波那契数列刚好错一位，即 $w[i]=F_{i+1}$。

斐波那契数列有基于矩阵幂运算的对数时间算法。

把 $F_n$ 和 $F_{n-1}$ 写成 `2 x 1` 大小的矩阵，代入递推公式可得：

$$
\begin{bmatrix}
  F_n \\
  F_{n-1}
\end{bmatrix}
=\begin{bmatrix}
  F_{n-1}+F_{n-2} \\
  F_{n-1}
\end{bmatrix}
=\begin{bmatrix}
  1 & 1 \\
  1 & 0
\end{bmatrix}
\times\begin{bmatrix}
  F_{n-1} \\
  F_{n-2}
\end{bmatrix}
$$

递推展开可得：

$$
\begin{bmatrix}
  F_n \\
  F_{n-1}
\end{bmatrix}
=\begin{bmatrix}
  1 & 1 \\
  1 & 0
\end{bmatrix}^{n-1}
\times\begin{bmatrix}
  F_1 \\
  F_0
\end{bmatrix}
=\begin{bmatrix}
  1 & 1 \\
  1 & 0
\end{bmatrix}^{n-1}
\times\begin{bmatrix}
  1 \\
  0
\end{bmatrix}
$$

所以：

$$
w[n]=F_{n+1}={\begin{bmatrix}
  1 & 1 \\
  1 & 0
\end{bmatrix}^n}_{1,1}
$$

幂运算可以用二分法加速，计算 n 次方的时间复杂度是 `O(log n)`：

$$
a^n=\begin{cases}
  (a^{n/2})^2 & \text{if }n\equiv 0\pmod{2} \\
  (a^{(n-1)/2})^2\times a & \text{otherwise}
\end{cases}
$$

{% snippet solution_log.py %}

线性复杂度和对数复杂度实际运算时间对比：

```text
[linear] n =    30:    1.393298 μs
[log(n)] n =    30:    7.942997 μs

[linear] n =   100:    4.241294 μs
[log(n)] n =   100:   10.184404 μs

[linear] n =   300:   12.726097 μs
[log(n)] n =   300:   14.227924 μs

[linear] n =  1000:   50.849684 μs
[log(n)] n =  1000:   20.762356 μs

[linear] n =  3000:  203.985965 μs
[log(n)] n =  3000:   35.360243 μs

[linear] n = 10000: 1754.791485 μs
[log(n)] n = 10000:  128.549821 μs
```

> $F_n$ 的二进制位数的增长趋势也是 `O(n)`，对于大一些的 n，递推法的时间复杂度实际是 `O(n²)`，基于矩阵幂运算方法的时间复杂度大约是 `O(n^1.6)`。
