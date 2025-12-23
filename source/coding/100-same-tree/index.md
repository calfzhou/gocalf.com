---
title: 100. Same Tree
notebook: coding
tags:
- easy
date: 2024-11-23 19:15:36
updated: 2024-11-23 19:15:36
---
## Problem

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

<https://leetcode.com/problems/same-tree/>

**Example 1:**

{% invert %}
![case1](assets/100-same-tree/case1.png)
{% endinvert %}

> Input: `p = [1,2,3], q = [1,2,3]`
> Output: `true`

**Example 2:**

{% invert %}
![case2](assets/100-same-tree/case2.png)
{% endinvert %}

> Input: `p = [1,2,3], q = [1,2,3]`
> Output: `true`

**Example 3:**

{% invert %}
![case3](assets/100-same-tree/case3.png)
{% endinvert %}

> Input: `p = [1,2,1], q = [1,1,2]`
> Output: `false`

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10⁴ <= Node.val <= 10⁴`

## Test Cases

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
```

{% asset_code coding/assets/100-same-tree/solution_test.py %}

## Thoughts

在 [572. Subtree of Another Tree](../572-subtree-of-another-tree/index.md) 中包含了。

按前序（pre-order，NLR）同步遍历两棵二叉树。对于当前节点，如果一边有而另一边缺失，或者两边节点的值不同，直接返回 `false`。

## Code

{% asset_code coding/assets/100-same-tree/solution.py %}
