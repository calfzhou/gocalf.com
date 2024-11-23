---
title: 102. Binary Tree Level Order Traversal
notebook: coding
tags:
- medium
date: 2024-11-23 21:49:14
updated: 2024-11-23 21:49:14
---
## Problem

Given the `root` of a binary tree, return _the level order traversal of its nodes' values_. (i.e., from left to right, level by level).

<https://leetcode.com/problems/binary-tree-level-order-traversal/>

**Example 1:**

{% invert %}
{% image 102-binary-tree-level-order-traversal/case1.png %}
{% endinvert %}

> Input: `root = [3,9,20,null,null,15,7]`
> Output: `[[3],[9,20],[15,7]]`

**Example 2:**

> Input: `root = [1]`
> Output: `[[1]]`

**Example 3:**

> Input: `root = []`
> Output: `[]`

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Test Cases

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
```

{% asset_code coding/102-binary-tree-level-order-traversal/solution_test.py %}

## Thoughts

直接按层序（level-order）遍历，可以用队列加循环。待处理的节点加入队列时，同时把该节点的层数一起放入队列。节点的层数等于其父节点的层数加一。

## Code

{% asset_code coding/102-binary-tree-level-order-traversal/solution.py %}
