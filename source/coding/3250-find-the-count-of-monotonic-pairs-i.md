---
title: 3250. Find the Count of Monotonic Pairs I
notebook: coding
tags:
- hard
date: 2024-11-29 00:28:30
updated: 2024-11-29 00:28:30
katex: true
---
## Problem

You are given an array of **positive** integers `nums` of length `n`.

We call a pair of **non-negative** integer arrays `(arr1, arr2)` **monotonic** if:

- The lengths of both arrays are `n`.
- `arr1` is monotonically **non-decreasing**, in other words, `arr1[0] <= arr1[1] <= ... <= arr1[n - 1]`.
- `arr2` is monotonically **non-increasing**, in other words, `arr2[0] >= arr2[1] >= ... >= arr2[n - 1]`.
- `arr1[i] + arr2[i] == nums[i]` for all `0 <= i <= n - 1`.

Return the count of **monotonic** pairs.

Since the answer may be very large, return it **modulo** `10⁹ + 7`.

<https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-i/>

**Example 1:**

> Input: `nums = [2,3,2]`
> Output: `4`
> Explanation:
> The good pairs are:
>
> 1. ([0, 1, 1], [2, 2, 1])
> 2. ([0, 1, 2], [2, 2, 0])
> 3. ([0, 2, 2], [2, 1, 0])
> 4. ([1, 2, 2], [1, 1, 0])

**Example 2:**

> Input: `nums = [5,5,5,5]`
> Output: `126`

**Constraints:**

- `1 <= n == nums.length <= 2000`
- `1 <= nums[i] <= 50`

## Test Cases

``` python
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
```

{% asset_code coding/3250-find-the-count-of-monotonic-pairs-i/solution_test.py %}

## Thoughts

记 $cnt(i,a_i)$ 是 `nums[0:i+1]` 子数组，$arr1[i]=a_i$ 情况（$arr2[i]=nums[i]-a_i=b_i$）下，单调数组对的个数。题目所求总数即为 $\sum_{a_{n-1}=0}^{nums[n-1]}cnt(n-1,a_{n-1})$。

显然有初值 $cnt(0,a_0) = 1$，其中 $0\le a_0\le nums[0]$。

对于 `nums[i]`，先看 $a_i$ 的取值范围。除了基础的 $0\le a_i\le nums[i]$，还要看 `nums[i-1]` 的情况。

不妨设 `nums[i-1]` 在 `arr1` 中的值为 $a_{i-1}$，其取值范围是 $[a_{i-1}^{min},a_{i-1}^{max}]$（相应地在 `arr2` 中的值为 $b_{i-1}$，范围是 $[b_{i-1}^{min},b_{i-1}^{max}]$，其中 $a_{i-1}^{min}+b_{i-1}^{max} = a_{i-1}^{max}+b_{i-1}^{min} = nums[i-1]$）。

{% invert %}
{% diagramsnet 3250-find-the-count-of-monotonic-pairs-i/cnt-i-a.drawio %}
{% endinvert %}

显然有：

$$
\begin{cases}
  a_i\ge a_{i-1}^{min} \\
  0\le b_i\le b_{i-1}^{max}
\end{cases}
$$

可得 $a_i$ 的取值范围是：

$$
\max\{a_{i-1}^{min},a_{i-1}^{min}+nums[i]-nums[i-1]\}\le a_i\le nums[i]
$$

不在这个范围内的 $a_i$，对应的 $cnt(i,a_i)$ 就是 0。另外如果 $a_i$ 的取值范围是空集，说明 `nums[i]` 没有能满足单调数组对条件的拆分方案，导致这个数组都无法完成拆分，问题的结果即为 0。

对于某个具体的 $a_i$，再看 $a_{i-1}$ 的可选范围（即 $a_{i-1}$ 取哪些值，`nums[i]` 把 $a_i$ 放入 `arr1` 可以满足单调数组对条件）。显然有（其中 $b_{i-1}=nums[i-1]-a_{i-1}$）：

$$
\begin{cases}
  a_{i-1}^{min}\le a_{i-1}\le a_{i-1}^{max} \\
  a_{i-1}\le a_i \\
  b_{i-1}\ge b_i
\end{cases}
$$

可得 $a_{i-1}$ 的可选范围是（其中 $a_{i-1}\le a_{i-1}^{max}$ 应该是冗余的【TODO】，可以忽略）：

$$
a_{i-1}^{min}\le a_{i-1}\le\min\{a_i,a_i+nums[i-1]-nums[i]\}
$$

对于所有在范围内的 $a_{i-1}$，累加 $cnt(i-1,a_{i-1})$ 即可得到 $cnt(i,a_i)$ 的值，即：

$$
cnt(i,a_i)=\sum_{a_{i-1}=a_{i-1}^{min}}^{\min\{a_i,a_i+nums[i-1]-nums[i]\}}cnt(i-1,a_{i-1})
$$

按照递推公式，从 `i = 1` 一直推算到 `i = n - 1` 即可。每次只需要保留关于 `i` 和 `i - 1` 的两个 `cnt` 数组。另外初始值 $a_0^{min}=0$。

再另外由于 `arr1` 是单调非递减的，可知对于任意的 i，都有 $a_i^{max}\le nums[n-1]$。所以 `cnt` 数组只需要保留最多从 0 到 `nums[n-1]`（含）这么多的空间。

空间复杂度是 `O(nums[n-1])`。时间复杂度是 $O(n * nums[n-1])$。虽然每个 $cnt(i,a_i)$ 都对应了 `O(nums[i-1])` 个可选的 $a_{i-1}$，但这个范围是随着 $a_i$ 同步增加的，可以递推计算，使得每个 $cnt(i,a_i)$ 都用常数时间计算。

## Code

{% asset_code coding/3250-find-the-count-of-monotonic-pairs-i/solution.py %}
