---
title: 3250. Find the Count of Monotonic Pairs I
notebook: coding
tags:
- hard
date: 2024-11-29 00:28:30
updated: 2024-11-29 16:27:33
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
{% diagramsnet assets/3250-find-the-count-of-monotonic-pairs-i/cnt-i-a.drawio %}
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

## Math

先看只有两个数字，且两个数字相等（记为 `m`）的情况。

可以看作是有两行棋子，每行都有 m 个。划一条竖线，竖线左边的棋子数量非递减变化（即 `arr1`），右边的棋子数量非递增变化（即 `arr2`）。

{% invert %}
{% diagramsnet assets/3250-find-the-count-of-monotonic-pairs-i/path-m-m.drawio %}
{% endinvert %}

如上图。这里把棋子上下对齐，让竖线变成折线，效果是一样的（后边称之为「界线」）。在界线左边的棋子数分别是 2 和 4，是非递减的；右边是 3 和 1，是非递增的。

不同的拆分方案对应于不同的界线。把界线改造成下图的样子，让它从左上角 `(0, 0)` 出发，到右下角 `(n, m)` 结束。

{% invert %}
{% diagramsnet assets/3250-find-the-count-of-monotonic-pairs-i/path-m-m-2.drawio %}
{% endinvert %}

为了始终符合单调数组对的要求，这条界线就只能往右走或往下走。这就跟 [62. Unique Paths](../62-unique-paths/index.md) 完全一样。可知从 `(0, 0)` 到 `(n, m)` 可能的界线数量为 `C(m+n, n) = C(m+n, m)`。

再看第一行棋子多一些的情况，比如第一行有 `m + d` 个，第二行有 `m` 个。

{% invert %}
{% diagramsnet assets/3250-find-the-count-of-monotonic-pairs-i/path-md-m.drawio %}
{% endinvert %}

为了确保符合单调数组对的要求，第一行多的 `d` 个棋子，只能排在最右侧（永远在界线右边）。界线仍然是从 `(0, 0)` 到 `(n, m)`，共 `C(m+n, n)` 种。

接着看第二行棋子多一些的情况，比如第一行有 `m` 个，第二行有 `m + d` 个。

{% invert %}
{% diagramsnet assets/3250-find-the-count-of-monotonic-pairs-i/path-m-md.drawio %}
{% endinvert %}

这时候需要把第二行多的 `d` 个棋子排在最左边（永远在界线左边）。那么界线就需要从 `(0, d)` 开始，到 `(n, m+d)` 结束，可行的方案数量刚好还是 `C(m+n, n)` 种。

看起来似乎是只要取两行数字中较小的就行。但扩展到多行时却不对，因为需要注意，第一行多和第二行多，多出来的棋子摆放的位置是不同的。上下相邻的两行，如果上边一行的棋子多，需要沿着左边缘对齐；而如果是下边一行的棋子多，则需要沿着右边缘对齐。

看个四行的例子 `[5, 7, 5, 7]`：

{% invert %}
{% diagramsnet assets/3250-find-the-count-of-monotonic-pairs-i/path-n.drawio %}
{% endinvert %}

可见界线始终是从第一行第一个棋子的左上角出发，到最后一行最后一个棋子的右下角结束。不妨设最后一行的棋子数为 `m`。每相邻两行，如果上一行的棋子数量偏少，就需要把上一行往右挪一些，挪的格数等于两行之差。如果上一行的棋子数偏多，则左侧直接对齐即可。最终第一行第一个棋子左上角，到最后一行最后一个棋子右下角，之间横向距离为 $m-\sum_{i=1}^{n-1}\{\max\{0,nums[i]-nums[i-1]\}\}$。记 $\sum_{i=1}^{n-1}\{\max\{0,nums[i]-nums[i-1]\}\}$ 为 `D`，那么界线的方案数量为 `C(m-D+n, n)`。

显然如果 `D = m`，则界线就只能是一条竖直线；而如果 `D > m` 则无解（因为界线不能往左走）。

计算 `C(m-D+n, n)` 的方法可以参考 [62. Unique Paths](../62-unique-paths/index.md)。时间复杂度 `O(n)`（需要遍历 `nums` 算出 `D`，然后计算 `C(m-D+n, n)` 的时间为 `O(min{n, m-D}) < O(n)`），空间复杂度 `O(1)`。

{% asset_code coding/3250-find-the-count-of-monotonic-pairs-i/solution2.py %}
