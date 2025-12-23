---
title: 95. Unique Binary Search Trees II
notebook: coding
tags:
- medium
date: 2024-12-21 01:34:21
updated: 2024-12-21 01:34:21
---
## Problem

Given an integer `n`, return _all the structurally unique **BST**'s (binary search trees), which has exactly_ `n` _nodes of unique values from_ `1` _to_ `n`. Return the answer in **any order**.

<https://leetcode.com/problems/unique-binary-search-trees-ii/>

**Example 1:**

{% invert %}
![case1](assets/96-unique-binary-search-trees/case1.png)
{% endinvert %}

> Input: `n = 3`
> Output: `[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]`

**Example 2:**

> Input: `n = 1`
> Output: `[[1]]`

**Constraints:**

- `1 <= n <= 8`

## Test Cases

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
```

{% asset_code coding/assets/95-unique-binary-search-trees-ii/solution_test.py %}

## Thoughts

跟 [96. Unique Binary Search Trees](../95-unique-binary-search-trees-ii/index.md) 一样，只不过这里是要列举出所有可能的 BST 来（这回不能直接用卡塔兰数的数学公式了）。

用递归来实现吧，借助 Python 内置的 [`functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache) 缓存一些中间结果来加速（甚至复用一些二叉树节点）。

当然也可以用循环来做，自己维护缓存 `dp[i][j]` 记录从 i 到 j 的所有 BST。循环的时候，第一重对子问题的规模循环，可以避免引用到尚未计算的 dp。

## Code

### Recursively

{% asset_code coding/assets/95-unique-binary-search-trees-ii/solution.py %}

### Iteratively

{% asset_code coding/assets/95-unique-binary-search-trees-ii/solution2.py %}
