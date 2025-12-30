---
title: 104. Maximum Depth of Binary Tree
notebook: coding
tags:
- easy
date: 2024-11-23 22:27:00
updated: 2024-11-23 22:27:00
---
## Problem

Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

<https://leetcode.com/problems/maximum-depth-of-binary-tree/>

**Example 1:**

![case1](case1.png){.invert-when-dark}

> Input: `root = [3,9,20,null,null,15,7]`
> Output: `3`

**Example 2:**

> Input: `root = [1,null,2]`
> Output: `2`

**Constraints:**

**Constraints:**

- The number of nodes in the tree is in the range `[0, 10⁴]`.
- `-100 <= Node.val <= 100`

## Test Cases

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
```

{% asset_code solution_test.py %}

## Thoughts

相当于 [102. Binary Tree Level Order Traversal](../102-binary-tree-level-order-traversal/index.md) 的简化版，只记录层数，不输出节点的值。

直接用层序（level-order）遍历二叉树，或者其他顺序也行。

## Code

{% asset_code solution.py %}
