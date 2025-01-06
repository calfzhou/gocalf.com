---
title: 1186. Maximum Subarray Sum with One Deletion
notebook: coding
tags:
- medium
katex: true
date: 2025-01-06 16:05:11
updated: 2025-01-06 16:05:11
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

{% asset_code coding/1186-maximum-subarray-sum-with-one-deletion/solution_test.py %}

## Thoughts

[53. Maximum Subarray](53-maximum-subarray) 的进阶版，可以删掉至多一个数字。

在 [53. Maximum Subarray](53-maximum-subarray) 中提到「如果一个 subarray 的和大于 0，把它与下一个数相加的结果一定比下一个数自身大。反之，应该从下一个数开启新的 subarray」。整理一下状态值和状态转移。

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

{% asset_code coding/1186-maximum-subarray-sum-with-one-deletion/solution.py %}

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

{% asset_code coding/1186-maximum-subarray-sum-with-one-deletion/solution2.py %}

> 开始没直接用这个办法是没想好怎么处理「至多删除一个」数字，因为在 subarray 之外的数字，删不删是没影响的。实际上 dd 表示的就是「至多」删除一次，不是一定要删除一次，只要在递推过程中不会多删除就可以了，至于删了更大还是不删更大，是自适应的。
