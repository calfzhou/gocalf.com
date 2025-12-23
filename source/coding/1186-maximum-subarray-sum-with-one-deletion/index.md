---
title: 1186. Maximum Subarray Sum with One Deletion
notebook: coding
tags:
- medium
katex: true
date: 2025-01-06 16:05:11
updated: 2025-01-08 17:35:33
---
## Problem

Given an array of integers, return the maximum sum for a **non-empty** subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be **non-empty** after deleting one element.

<https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/>

**Example 1:**

> Input: `arr = [1,-2,0,3]`
> Output: `4`
> Explanation: Because we can choose `[1, -2, 0, 3]` and drop -2, thus the subarray `[1, 0, 3]` becomes the maximum value.

**Example 2:**

> Input: `arr = [1,-2,-2,3]`
> Output: `3`
> Explanation: We just choose `[3]` and it's the maximum sum.

**Example 3:**

> Input: `arr = [-1,-1,-1,-1]`
> Output: `-1`
> Explanation: The final subarray needs to be non-empty. You can't choose `[-1]` and delete -1 from it, then get an empty subarray to make the sum equals to 0.

**Constraints:**

- `1 <= arr.length <= 10⁵`
- `-10⁴ <= arr[i] <= 10⁴`

## Test Cases

``` python
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
```

{% asset_code coding/assets/1186-maximum-subarray-sum-with-one-deletion/solution_test.py %}

## Thoughts

[53. Maximum Subarray](../53-maximum-subarray/index.md) 的进阶版，可以删掉至多一个数字。

在 [53. Maximum Subarray](../53-maximum-subarray/index.md) 中提到「如果一个 subarray 的和大于 0，把它与下一个数相加的结果一定比下一个数自身大。反之，应该从下一个数开启新的 subarray」。整理一下状态值和状态转移。

定义 `dl(i)` 表示以 i 为右端点的最大 subarray 和（至少包含 `arr[i]`），可得：

$$
\begin{cases}
  dl(0)=arr[0] \\
  dl(i)=\max\{dl(i-1),0\}+arr[i]
\end{cases}
$$

那么 arr 的最大 subarray 和为：

$$
\max_{0\le i<n}{dl(i)}
$$

如果删掉一个位置的数字，显然只有删掉负数才会有帮助，删掉之后可以把其前后的 subarries 连起来，才有可能得到更大的和。

仿照 dl 定义 `dr(i)` 表示以 i 为左端点的最大 subarray 和（至少包含 `arr[i]`），可得：

$$
\begin{cases}
  dr(n-1)=arr[n-1] \\
  dr(i)=\max\{dr(i+1),0\}+arr[i]
\end{cases}
$$

如果删掉位置 i 的数字，左右两边拼起来的和为 `dl(i-1) + dr(i+1)`。那么允许删除至多一个数字情况下的最大 subarray 和为：

$$
\max\begin{cases}
  \max_{0\le i<n}{dl(i)} \\
  \max_{0<i<n-1}\{dl(i-1)+dr(i+1)\}
\end{cases}
$$

其中 dl 只需要保留最新的一个值，dr 需要缓存整个数组。时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/1186-maximum-subarray-sum-with-one-deletion/solution.py %}

## Less Space

看怎么能不用 `O(n)` 的辅助空间。

依然用 `dl(i)` 表示以 i 为右端点的最大 subarray 和（至少包含 `arr[i]`）。用 `dd(i)` 表示以 i 为右端点但是删掉至多一个数字之后的最大 subarray 和（虽然以 i 为右端点，但是 `arr[i]` 可以是被删掉的，此时应至少包含 `arr[i-1]` 以确保 subarray 不为空）。那么 `dd(i)` 要么取 `dl(i-1)`（即删掉 `arr[i]`），要么取 `dd(i-1) + arr[i-1]`（保持原本已经可能删掉了的那个数字的删除状态，那就不能再删掉 `arr[i]`）。所以：

$$
\begin{cases}
  dl(0)=arr[0] \\
  dl(i)=\max\{dl(i-1),0\}+arr[i]
\end{cases}
$$

$$
\begin{cases}
  dd(0)=arr[0] \\
  dd(i)=\max\{dl(i-1),dd(i-1)+arr[i]\}
\end{cases}
$$

这样允许删除至多一个数字情况下的最大 subarray 和为：

$$
\max\begin{cases}
  \max_{0\le i<n}{dl(i)} \\
  \max_{0\le i<n}{dd(i)}
\end{cases}
$$

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

{% asset_code coding/assets/1186-maximum-subarray-sum-with-one-deletion/solution2.py %}

> 开始没直接用这个办法是没想好怎么处理「至多删除一个」数字，因为在 subarray 之外的数字，删不删是没影响的。实际上 dd 表示的就是「至多」删除一次，不是一定要删除一次，只要在递推过程中不会多删除就可以了，至于删了更大还是不删更大，是自适应的。

## Another DP

在 [53. Maximum Subarray](../53-maximum-subarray/index.md) 定义的 [第二种 DP](../53-maximum-subarray/index.md#Another-DP) 的基础上，重新看如何解本题。沿用那边定义的 `ps(i) = Σarr[0...i]` 和 `low(i)`（`arr[0...i]` 的（小于等于零的）最小前缀和）。

$$
\begin{array}{rcl}
  ps(i) & = &\sum_{j=0}^{i}arr[j] \\
  low(i) & = & \min\{0, \min_{0\le j\le i}ps(j)\}
\end{array}
$$

[上边](../1186-maximum-subarray-sum-with-one-deletion/index.md#Less-Space) 定义的 dl 可以用 ps 和 low 重写为：$dl(i)=ps(i)-low(i-1)$（不用 `low(i)` 因为需要保证 subarray 不为空）。

然后把 dd 也改造成在 ps 里减去一个值的形式，如 `dd = ps - low2`，可得：

$$
\begin{array}{rl}
  low2(i) & =ps(i)-dd(i) \\
  & =ps(i)-\max\{dl(i-1),dd(i-1)+arr[i]\} \\
  & =\min\begin{cases}
    ps(i)-dl(i-1) \\
    ps(i)-dd(i-1)-arr[i]
  \end{cases} \\
  & =\min\begin{cases}
    ps(i)-(ps(i-1)-low(i-2)) \\
    (ps(i-1)+arr[i])-dd(i-1)-arr[i]
  \end{cases} \\
  & =\min\begin{cases}
    low(i-2)+arr[i] \\
    low2(i-1)
  \end{cases}
\end{array}
$$

其中 $low(i-2)+arr[i]$ 对应了删掉 `arr[i]`（那就至少保留 `arr[i-1]`）的情况。

可见 `low2(i)` 的含义是 `arr[0...i]` 的（小于等于零的）最小前缀和再加上额外被删掉的数字所能得到的最小值，在 `ps(i)` 中减去此最小值，就是以 i 为右端点但是删掉至多一个数字之后的最大 subarray 和。

最后整个 arr 允许删除至多一个数字情况下的最大 subarray 和为：

$$
\begin{array}{rl}
  & \max\begin{cases}
    \max_{0\le i<n}{dl(i)} \\
    \max_{0\le i<n}{dd(i)}
  \end{cases} \\
  = & \max_{0\le i<n}\{ps(i)-\min\{low(i-1),low2(i)\}\}
\end{array}

$$

{% asset_code coding/assets/1186-maximum-subarray-sum-with-one-deletion/solution3.py %}
