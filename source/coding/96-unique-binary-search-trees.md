---
title: 96. Unique Binary Search Trees
notebook: coding
tags:
- medium
katex: true
date: 2024-12-20 23:58:17
updated: 2024-12-20 23:58:17
---
## Problem

Given an integer `n`, return _the number of structurally unique **BST**'s (binary search trees) which has exactly_ `n` _nodes of unique values from_ `1` _to_ `n`.

<https://leetcode.com/problems/unique-binary-search-trees/>

**Example 1:**

{% invert %}
![case1](96-unique-binary-search-trees/case1.png)
{% endinvert %}

> Input: n = 3
> Output: 5

**Example 2:**

> Input: n = 1
> Output: 1

**Constraints:**

- `1 <= n <= 19`

## Test Cases

``` python
class Solution:
    def numTrees(self, n: int) -> int:
```

{% asset_code coding/96-unique-binary-search-trees/solution_test.py %}

## Thoughts

定义 `f(i)` 表示 1 到 i 所能组成的二叉搜索树的个数。初值 `f(0) = 1`，题目所求结果为 `f(n)`。

1 到 i 的每个数字都可以作为根节点。假设以 k 作为根节点，那么左边有 `k - 1` 个节点，共有 `f(k - 1)` 种 BSTs；右边有 `i - k` 个节点，共有 `f(i - k)` 中 BSTs；所以以 k 为根节点的 BST 共有 `f(k - 1) * f(i - k)` 个。

所以：

$$
f(i)=\sum_{k=1}^i\{f(k-1)\times f(i-k)\}
$$

时间复杂度 `O(n²)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/96-unique-binary-search-trees/solution.py %}
