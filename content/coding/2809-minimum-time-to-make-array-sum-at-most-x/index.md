---
title: 2809. Minimum Time to Make Array Sum At Most x
notebook: coding
tags:
- hard
- difficult
katex: true
date: 2024-12-14 16:33:42
updated: 2024-12-14 16:33:42
---
## Problem

You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length. Every second, for all indices `0 <= i < nums1.length`, value of `nums1[i]` is incremented by `nums2[i]`. **After** this is done, you can do the following operation:

- Choose an index `0 <= i < nums1.length` and make `nums1[i] = 0`.

You are also given an integer `x`.

Return _the **minimum** time in which you can make the sum of all elements of_ `nums1` _to be **less than or equal** to_ `x`, _or_ `-1` _if this is not possible._

<https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/>

**Example 1:**

> Input: `nums1 = [1,2,3], nums2 = [1,2,3], x = 4`
> Output: `3`
> Explanation:
> For the 1st second, we apply the operation on `i = 0`. Therefore `nums1 = [0,2+2,3+3] = [0,4,6]`.
> For the 2nd second, we apply the operation on `i = 1`. Therefore `nums1 = [0+1,0,6+3] = [1,0,9]`.
> For the 3rd second, we apply the operation on `i = 2`. Therefore `nums1 = [1+1,0+2,0] = [2,2,0]`.
> Now sum of `nums1` = 4. It can be shown that these operations are optimal, so we return 3.

**Example 2:**

> Input: `nums1 = [1,2,3], nums2 = [3,3,3], x = 4`
> Output: `-1`
> Explanation: It can be shown that the sum of `nums1` will always be greater than `x`, no matter which operations are performed.

**Constraints:**

- `1 <= nums1.length <= 10³`
- `1 <= nums1[i] <= 10³`
- `0 <= nums2[i] <= 10³`
- `nums1.length == nums2.length`
- `0 <= x <= 10⁶`

## Test Cases

```python
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
```

{% snippet solution_test.py %}

## Thoughts

虽然题目没有明示，但「第 0 秒」也是允许的，所以先检查 `nums1` 的总和是否小于等于 `x`，是的话直接返回 0。

易知对任何一个位置 i，最多只需要操作一次，所以最多对所有位置都操作一次（用时 n 秒，n 是 `nums1` 和 `nums2` 的长度）。分别看第 1 秒、第 2 秒、……、第 n 秒之后，总和是否能小于等于 `x`。如果都不能则返回 -1。

为了方便，下边以 `aᵢ` 表示最初时的 `nums1[i-1]`，`bᵢ` 表示 `nums2[i-1]`。

计算第 t（`1 ≤ t ≤ n`）秒时，`nums1` 的总和。首先如果不做操作，则为 $\sum_{i=1}^n\{a_i+t\times b_i\}$，这是个定值。然后看 t 次操作总共减去多少，设在第 s 秒（`1 ≤ s ≤ t`）时，对位置 $i_s$ 操作，那么总共会减去 $\sum_{s=1}^t\{a_{i_s}+s\times b_{i_s}\}$。对第二个式子取最大值，就可以得到在第 t 秒时，`nums1` 总和的最小值，判定是否小于等于 `x` 即可。

其中的 $\sum_{s=1}^t\{s\times b_{i_s}\}$ 这个部分跟 [2931. Maximum Spending After Buying Items](../2931-maximum-spending-after-buying-items/index.md) 其实是一样的，对于确定的集合 $\{i_1,i_2,\dots,i_t\}$，当 $b_{i_1}\le b_{i_2}\le\dots\le b_{i_t}$ 时，总和最大。也就是说从 n 个位置中任选 t 个，那么在每一秒，都从尚未操作的位置中选 `nums2` 值最小的那个位置进行操作。所以关键就在于选哪 t 个位置。

不妨先对 `nums2` 按非递减的顺序排序，当然也要同步重排 `nums1` 以保持对应关系，之后对于任意的 `1 <= i < j <= n`，都有 $b_i\le b_j$。排序逻辑示意：

```python
indices = sorted(range(n), key=lambda i: nums2[i])
nums1 = [nums1[i] for i in indices]
nums2 = [nums2[i] for i in indices]
```

定义 **从前 i 个位置中任选 t 个（`t ≤ i`）进行操作，到第 t 秒时累计减去的最大值** 为：

$$
f(t,i)=\max_{\{1\le i_1\le i_2\le\dots\le i_t\le i\}}\sum_{s=1}^t\{a_{i_s}+s\times b_{i_s}\}
$$

在计算 `f(t, i)` 时，一个方案是把位置 i 选中，显然对位置 i 的操作可以减去 $a_i+t\times b_i$，接下来就看从 `i - 1` 个位置中选 `t - 1` 个，能减去的最大值是多少（即 `f(t-1, i-1)`）；另一个方案是不选位置 i，那就再看从 `i - 1` 个位置中选 t 个，能减去的最大值（即 `f(t, i-1)`）。所以：

$$
f(t,i)=\max\begin{cases}
  a_i+t\times b_i+f(t-1,i-1) \\
  f(t,i-1)
\end{cases}
$$

可以定义边界值：`f(0, i) = 0`，`f(t, t-1) = 0`。

> 需要注意，虽然看起来有关于 t 的递推式，并不表示操作也是按 t 递推的。实际上到第 `t - 1` 秒累计减去值最大的操作方案，并不一定是到第 t 秒累计减去值最大的操作方案的前 `t - 1` 步。从递推式的推导过程中也能看出来，其实是固定了 t，对 i 做递推。

令 t 从 1 遍历到 n，对于每个 t，计算所有 `1 ≤ i ≤ t` 的 `f(t, i)`。显然只会用到 `t - 1` 的 `f` 值，所以只需要用一个长度为 n 的数组记录 `t - 1` 的所有 `f` 值。而且对于每个 i ，也只会用到跟 `i - 1` 相关的 `f` 值，而且因为限定 `i ≥ t`，可选的 i 的数量也随着 t 的增加而递减，那计算完 `f(t, i)` 的值可以直接占用 `f(t-1, i-1)` 的存储位置，不需要再开辟一个长度为 n 的数组做记录。

时间复杂度是 `O(n²)`，空间复杂度 `O(n)`。

用一个具体的例子看一下 `f(t, i)` 的值，以及每个值是怎么来的。

设按 `nums2` 排序之后的两个数组分别为 `nums1 = [7, 8, 1, 6, 6, 7]`，`nums2 = [1, 1, 2, 2, 2, 3]`。

把所有的 $a_i+t\times b_i$ 记录在如下表格中。

> 显然 t > i 的情况是不用考虑的，因为如果会对位置 i 操作，一定不能在大于 i 的时刻 t 进行操作。

::: invert-when-dark
{% diagramsnet ai_plus_t_bi.drawio %}
:::

下表是按递推式算出来的所有 `f(t, i)`。其中红色的值取自 $a_i+t\times b_i+f(t-1,i-1)$（表示被选中），蓝色的值取自 $f(t,i-1)$（表示不选中）。

::: invert-when-dark
{% diagramsnet f_t_i.drawio %}
:::

## Code

{% snippet solution.py %}
