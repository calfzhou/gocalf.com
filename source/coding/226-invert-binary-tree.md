---
title: 226. Invert Binary Tree
notebook: coding
tags:
- easy
date: 2024-11-23 18:58:59
updated: 2024-11-23 18:58:59
---
## Problem

Given the `root` of a binary tree, invert the tree, and return _its root_.

<https://leetcode.com/problems/invert-binary-tree/>

**Example 1:**

{% invert %}
![case1](226-invert-binary-tree/case1.png)
{% endinvert %}

> Input: `root = [4,2,7,1,3,6,9]`
> Output: `[4,7,2,9,6,3,1]`

**Example 2:**

{% invert %}
![case2](226-invert-binary-tree/case2.png)
{% endinvert %}

> Input: `root = [4,2,7,1,3,6,9]`
> Output: `[4,7,2,9,6,3,1]`

**Example 3:**

> Input: `root = []`
> Output: `[]`

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Test Cases

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
```

{% asset_code coding/226-invert-binary-tree/solution_test.py %}

## Thoughts

按任何顺序遍历二叉树，前序（pre-order，NLR），对于当前节点，交换左右子节点即可。

## Code

{% asset_code coding/226-invert-binary-tree/solution.py %}
