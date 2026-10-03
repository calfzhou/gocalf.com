---
title: 3395. Subsequences with a Unique Middle Mode I
notebook: coding
tags:
- hard
katex: true
date: 2025-01-04 22:29:23
updated: 2025-01-05 22:24:20
---
## Problem

> 唯一中间众数子序列。

Given an integer array `nums`, find the number of subsequences of size 5 of `nums` with a **unique middle mode**.

> A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Since the answer may be very large, return it **modulo** `10⁹ + 7`.

A **mode** of a sequence of numbers is defined as the element that appears the **maximum** number of times in the sequence.

> **众数** 指的是一个数字序列中出现次数 **最多** 的元素。

A sequence of numbers contains a **unique mode** if it has only one mode.

> 如果一个数字序列众数只有一个，我们称这个序列有 **唯一众数** 。

A sequence of numbers `seq` of size 5 contains a **unique middle mode** if the _middle element_ (`seq[2]`) is a **unique mode**.

> 一个大小为 5 的数字序列 `seq` ，如果它中间的数字（`seq[2]`）是唯一众数，那么称它是 **唯一中间众数** 序列。

<https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/>

**Example 1:**

> Input: `nums = [1,1,1,1,1,1]`
> Output: `6`
> Explanation:
> `[1, 1, 1, 1, 1]` is the only subsequence of size 5 that can be formed, and it has a unique middle mode of 1. This subsequence can be formed in 6 different ways, so the output is 6.

**Example 2:**

> Input: `nums = [1,2,2,3,3,4]`
> Output: `4`
> Explanation:
> `[1, 2, 2, 3, 4]` and `[1, 2, 3, 3, 4]` each have a unique middle mode because the number at index 2 has the greatest frequency in the subsequence. `[1, 2, 2, 3, 3]` does not have a unique middle mode because 2 and 3 appear twice.

**Example 3:**

> Input: nums = [0,1,2,3,4,5,6,7,8]
> Output: 0
> Explanation:
> There is no subsequence of length 5 with a unique middle mode.

**Constraints:**

- `5 <= nums.length <= 1000`
- `-10⁹ <= nums[i] <= 10⁹`

## Test Cases

```python
class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

> 虽然几个测试用例都刚好是非递减排列的 nums，但题目中并没有给出这个条件，输入的 nums 可以是任意顺序的。

以任意位置 i（`2 ≤ i < n - 2`）作为子序列的中间位置，计算符合「唯一中间众数」的子序列个数。

位置 i 的左边有 `l = i` 个数字，右边有 `r = n - i` 个数字。从左右两边各任选两个数字，组成一个子序列，一共有 $\binom{l}{2}⋅\binom{r}{2}$ 种方案。但所有这些方案中有一些不符合「唯一中间众数」的要求，需要排除掉。不妨设 `nums[i] = a`。

另外记 $l_x$ 表示在 nums 中 i 的左边，数字 x 的个数，$r_x$ 表示在 nums 中 i 的右边，数字 x 的个数（如果 i 是变量，则即为 $l_{x,i}$、$r_{x,i}$）。可以先遍历一遍 nums，记录所有数字的总数，即为 $r_x$ 的初值（$l_x$ 初值为 0），然后在遍历 i 的过程中，根据 `nums[i]` 的值不断更新 $l_{nums[i]}$ 和 $r_{nums[i]}$（给 $r_{nums[i]}$ 减去 1，加到 $l_{nums[i]}$ 上）。

1. 子序列的左边和右边都没有 a：共 $(l-l_a)⋅(r-r_a)$ 种。
2. 子序列的一边是 a 和一个任意其他（非 a）数字 b，另一边是 b 和任意其他（非 a、非 b）数字 c。
   1. a 在左边：共 $l_a⋅l_b⋅r_b⋅(r-r_a-r_b)$ 种。
   2. a 在右边：共 $l_b⋅(l-l_a-l_b)⋅r_a⋅r_b$ 种。
3. 子序列的一边是两个任意其他（非 a）数字 b，另一边有一个 a（另一个数字可以是 b，也可以是除 a、b 外的任何数字）。
   1. a 在左边：共 $l_a⋅(l-l_a)⋅\binom{r_b}{2}$ 种。
   2. a 在右边：共 $\binom{l_b}{2}⋅r_a⋅(r-r_a)$ 种。

设 nums 种共有 K 个各不相同的数字，时间复杂度 `O(K * n) ≈ O(n²)`，空间复杂度 `O(K) ≈ O(n)`。

> 虽然可以在 nums 能组成的任意长度为 5 的子序列总数 $\binom{n}{5}$ 基础上，减去每个 i 对应的需要排除的量，不需要从 0 开始累加每个 i 对应的 $\binom{l}{2}⋅\binom{r}{2}$，但运行速度反而会慢不少。

## Code

{% snippet solution.py %}

> 这里其实有大量计算是重复的，因为 lb、rb 并不是每次都变，还可以进一步优化。

## O(n)

重新看一下上边复杂度最高的计算部分：

$$
\begin{array}{rcl}
  \sum_{b\ne a}( & & l_a⋅l_b⋅r_b⋅(r-r_a-r_b) \\
  & + & l_b⋅(l-l_a-l_b)⋅r_a⋅r_b \\
  & + & l_a⋅(l-l_a)⋅\binom{r_b}{2} \\
  & + & \binom{l_b}{2}⋅r_a⋅(r-r_a) \\
  ) & &
\end{array}
$$

展开得到：

$$
\begin{array}{rcl}
  \sum_{b\ne a}( & & r⋅l_a⋅l_b⋅r_b - l_a⋅r_a⋅l_b⋅r_b - l_a⋅l_b⋅r_b^2 \\
  & + & l⋅r_a⋅l_b⋅r_b - l_a⋅r_a⋅l_b⋅r_b - r_a⋅l_b^2⋅r_b \\
  & + & \frac{1}{2}(l⋅l_a⋅r_b^2 - l⋅l_a⋅r_b - l_a^2⋅r_b^2 + l_a^2⋅r_b) \\
  & + & \frac{1}{2}(r⋅r_a⋅l_b^2 - r_a^2⋅l_b^2 - r⋅r_a⋅l_b + r_a^2⋅l_b) \\
  ) & & \\
  \\
  = & & (r⋅l_a + l⋅r_a - 2⋅l_a⋅r_a)\sum_{b\ne a}l_b⋅r_b \\
  & - & l_a\sum_{b\ne a}l_b⋅r_b^2 \\
  & - & r_a\sum_{b\ne a}l_b^2⋅r_b \\
  & + & \frac{1}{2}(r⋅r_a - r_a^2)\sum_{b\ne a}l_b^2-l_b \\
  & + & \frac{1}{2}(l⋅l_a - l_a^2)\sum_{b\ne a}r_b^2-r_b
\end{array}
$$

其中的每一项 $\sum_{b\ne a}$ 都需要从 `O(K) ≈ O(n)` 时间复杂度改造成 `O(1)` 时间复杂度。

以 $l_b⋅r_b$ 为例，记 $A(i)=\sum_{b}l_{b,i}⋅r_{b,i}$（注意这里还没有 a 呢，所以 b 表示 nums 中所有的数字）。假设已经有了 $A(i-1)$ 的值，看循环到 i 的时候应该怎么处理。循环到 i 时，依然设 `nums[i] = a`，显然其他任意的 b，$l_b$ 和 $r_b$ 都没变，这时候只需要减去 a（在 `i - 1` 处）相关的值，即 $\sum_{b\ne a}l_b⋅r_b=A(i-1)-l_{a,i-1}⋅r_{a,i-1}$（注意 $l_{a,i}=l_{a,i-1}$、$r_{a,i}=r_{a,i-1}-1$）。在循环 i 结束前，需要把 $A(i)$ 计算出来备用，只需要把 a（在 `i + 1` 处）相关的新值加回去即可，即 $A(i)=l_{a,i+1}⋅r_{a,i+1}+\sum_{b\ne a}l_b⋅r_b$（注意 $l_{a,i+1}=l_{a,i}+1$、$r_{a,i+1}=r_{a,i}$）（这里 $A(i)$ 的值跟定义其实有小区别，但这样计算比较方便）。

> 说难吧倒是真的没多难，但是 **实 在 是 太 繁 琐 了**！稍不留神就错，错一点儿可能只会让部分 case 失败，排查的时候还得手算模拟对比。实在太考验心智了。

最终时间复杂度 `O(n)`，空间复杂度 `O(K) ≈ O(n)`。Runtime beats 100%，还算没辜负眼花缭乱的一天。

{% snippet solution2.py %}
