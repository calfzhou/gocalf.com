---
title: 873. Length of Longest Fibonacci Subsequence
notebook: coding
tags:
- medium
katex: true
date: 2025-02-27 15:55:25
updated: 2025-02-27 15:55:25
---
## Problem

A sequence `x₁, x₂, ..., xₙ` is _Fibonacci-like_ if:

- `n >= 3`
- `xᵢ + xᵢ₊₁ == xᵢ₊₂` for all `i + 2 <= n`

Given a **strictly increasing** array `arr` of positive integers forming a sequence, return _the **length** of the longest Fibonacci-like subsequence of_ `arr`. If one does not exist, return `0`.

A **subsequence** is derived from another sequence `arr` by deleting any number of elements (including none) from `arr`, without changing the order of the remaining elements. For example, `[3, 5, 8]` is a subsequence of `[3, 4, 5, 6, 7, 8]`.

<https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/>

**Example 1:**

> Input: `arr = [1,2,3,4,5,6,7,8]`
> Output: `5`
> Explanation: The longest subsequence that is fibonacci-like: `[1,2,3,5,8]`.

**Example 2:**

> Input: `arr = [1,3,7,11,12,14,18]`
> Output: `3`
> Explanation: The longest subsequence that is fibonacci-like: `[1,11,12]`, `[3,11,14]` or `[7,11,18]`.

**Constraints:**

- `3 <= arr.length <= 1000`
- `1 <= arr[i] < arr[i + 1] <= 10⁹`

## Test Cases

```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

把 arr 中的数字放在哈希集合中以便能够快速确定某个数字是否存在。遍历 arr 所有可能的长度为 2 的组合，如 `arr[i]` 和 `arr[j]`，按 Fibonacci-like 的规则逐个检查下一个数字是否存在，并确定对应的 Fibonacci-like 序列的长度。

对于一对数字，计算以其开头的 Fibonacci-like 序列长度需要 `O(n)` 时间。因此总共需要 `O(n³)` 时间，`O(n)` 空间。

## Code

{% asset_code solution.py %}

## Faster

上边的计算过程有很多重复，比如以 `[1, 2]` 开头的时候，可以找到 Fibonacci-like 序列为 `[1, 2, 3, 5, 8]`；而以 `[2, 3]` 开头的时候，又找了一次 `[2, 3, 5, 8]`，重复了。所以考虑使用动态规划。

定义 `dp(y, z)` 表示以数字 y 和 z 结束的 Fibonacci-like 序列的长度，易知：

$$
dp(y,z)=\begin{cases}
  dp(z-y,y)+1 & \text{if }(z-y)\in arr \\
  2 & \text{otherwise}
\end{cases}
$$

遍历 arr 的每一个数字作为 z。对于特定的 z，遍历所有 z 左边的数字作为 y。令 `x = z - y`，看 x 是否存在，如果存在则取 `dp(x, y) + 1`，否则取 2。dp 值可以用字典记录。

一个可以做的短路处理是，逆序遍历 y，当 y 小于等于 z 的一半（即 `x ≥ y`）时就可以停止，更小的 y 完全不用处理。

为了节省一些空间（最开始一版直接 OOM 了），所有值为 2 的 dp 值可以不用记录，因为这是起始值。

时间复杂度 `O(n²)`，空间复杂度 `O(n²)`。

{% asset_code solution2.py %}
