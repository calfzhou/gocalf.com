---
title: 1524. Number of Sub-arrays With Odd Sum
notebook: coding
tags:
- medium
katex: true
date: 2025-02-26 15:54:51
updated: 2025-02-26 15:54:51
---
## Problem

Given an array of integers `arr`, return _the number of subarrays with an **odd** sum_.

Since the answer can be very large, return it modulo `10⁹ + 7`.

<https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/>

**Example 1:**

> Input: `arr = [1,3,5]`
> Output: `4`
> Explanation: All subarrays are `[[1],[1,3],[1,3,5],[3],[3,5],[5]]`
> All sub-arrays sum are `[1,4,9,3,8,5]`.
> Odd sums are `[1,9,3,5]` so the answer is 4.

**Example 2:**

> Input: `arr = [2,4,6]`
> Output: `0`
> Explanation: All subarrays are `[[2],[2,4],[2,4,6],[4],[4,6],[6]]`
> All sub-arrays sum are `[2,6,12,4,10,6]`.
> All sub-arrays have even sum and the answer is 0.

**Example 3:**

> Input: `arr = [1,2,3,4,5,6,7]`
> Output: `16`

**Constraints:**

- `1 <= arr.length <= 10⁵`
- `1 <= arr[i] <= 100`

## Test Cases

``` python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
```

{% asset_code coding/assets/1524-number-of-sub-arrays-with-odd-sum/solution_test.py %}

## Thoughts

只有包含奇数个奇数的子数组之和是奇数。

第一个奇数是一个可行的子数组。另外如果第一个奇数左边有 `l(1)` 个偶数，右边有 `r(1)` 个偶数，第一个奇数及其左右各任意个偶数构成的子数组都可以。那么只包含第一个奇数的可行子数组总数为 `(l(1) + 1) * (r(1) + 1)`。可以定义 `L(i) = l(i) + 1`，`R(i) = r(i) + 1`，则为 `L(1) * R(1)`。

> 易知 `R(i) = L(i+1)`，`L(i) = R(i-1)`。

第一个到第三个奇数也是一个可行的子数组，同理可知，包含且只包含这三个奇数的可行子数组总数为 `L(1) * R(3))`。而只包含第三个奇数的可行子数组总数为 `L(3) * R(3)`。可知以第三个奇数为最后一个奇数的可行子数组总数为 `(L(1) + L(3)) * R(3)`。

类似地，对于奇数 `2k + 1`，以第 `2k + 1` 个奇数为最后一个奇数的可行子数组总数为：

$$
cnt(2k+1)=R(2k+1)\times\sum_{i=1,3,5,\dots,2k+1}{L(i)}
$$

同理，对于偶数 `2k`，以第 `2k` 个奇数为最后一个奇数的可行子数组总数为：

$$
cnt(2k)=R(2k)\times\sum_{i=2,4,6,\dots,2k}{L(i)}
$$

最后把以任何奇数为最后一个奇数的可行子数组总数累加。

上边两个式子中的求和项，类似于前缀和，可以随着 k 的增加递推计算（动态规划）。

时间复杂度 `O(n)`。

如果事先算好所有的 `L(i)` 和 `R(i)` 并存下来，则需要 `O(n)` 空间，也可以边算边用，只需要 `O(1)` 空间。

## Code

`O(n)` 空间：

{% asset_code coding/assets/1524-number-of-sub-arrays-with-odd-sum/solution.py %}

`O(1)` 空间：

{% asset_code coding/assets/1524-number-of-sub-arrays-with-odd-sum/solution2.py %}

## Another Way

根据 `R(i) = L(i+1)`，`L(i) = R(i-1)`，重新定义 `E(0)` 到 `E(m)`（其中 m 表示 arr 中一共有 m 个奇数）：

$$
\begin{cases}
  E(0)=L(1) \\
  E(1)=R(1)=L(2) \\
  E(2)=R(2)=L(3) \\
  \cdots \\
  E(m-1)=R(m-1)=L(m) \\
  E(m)=R(m)
\end{cases}
$$

也就是 `E(0)` 表示第一个奇数左边的偶数个数加一；`E(m)` 表示最后一个（第 m 个）奇数右边的偶数个数加一；`E(i)` 表示第 i 个和第 `i + 1` 个奇数之间的偶数个数加一。

根据上边提到的「以某个奇数为最后一个奇数的可行子数组总数」，累加出来得到题目的结果，即：

$$
\begin{array}{rcl}
  total & = & \sum_{i=1}^m{cnt(i)} \\
  \\
  & = & \sum_{i=1}^m{\{R(i)\times\sum_{j=i,i-2,i-4,\dots}{L(j)}\}} \\
  \\
  & = & \sum_{i=1}^m{\{E(i)\times\sum_{j=i-1,i-3,i-5,\dots}{E(j)}\}} \\
  \\
  & = & E(1)\times E(0) \\
  & + & E(2)\times E(1) \\
  & + & E(3)\times[E(2)+E(0)] \\
  & + & E(4)\times[E(3)+E(1)] \\
  & + & E(5)\times[E(4)+E(2)+E(0)] \\
  & + & E(6)\times[E(5)+E(3)+E(1)] \\
  & + & \cdots
\end{array}
$$

最后那个展开的表达式，前两行合并可以得到 $[E(2)+E(0)]\times E(1)$；再与第三行合并得到 $[E(3)+E(1)]\times[E(2)+E(0)]$；再与第四行合并得到 $[E(4)+E(2)+E(0)]\times[E(3)+E(1)]$；……。最终可以得到：

$$
total=[E(0)+E(2)+E(4)+\cdots]\times[E(1)+E(3)+E(5)+\cdots]
$$

即数组 E 中所有偶数项之和，与所有奇数项之和，的乘积。

`E(1)` 相当于 arr 的所有前缀子数组中，只包含 1 个奇数的个数；`E(3)` 相当于包含 1 个 或 3 个奇数的前缀子数组个数；……；数组 E 的最后一个奇数项，表示包含奇数个奇数的前缀子数组个数。类似地 `E(0)` 相当于包含 0 个奇数的前缀子数组个数（注意空数组也算）；……；数组 E 的最后一个偶数项，表示包含偶数个奇数的前缀子数组个数。二者之积即为题目结果。

> 这个乘积的数学含义可以再梳理一下。TODO

{% asset_code coding/assets/1524-number-of-sub-arrays-with-odd-sum/solution3.py %}
