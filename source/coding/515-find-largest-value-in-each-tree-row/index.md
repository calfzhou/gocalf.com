---
title: 515. Find Largest Value in Each Tree Row
notebook: coding
tags:
- medium
date: 2024-12-25 10:06:53
updated: 2024-12-25 10:06:53
---
## Problem

Given the `root` of a binary tree, return _an array of the largest value in each row_ of the tree **(0-indexed)**.

<https://leetcode.com/problems/find-largest-value-in-each-tree-row/>

**Example 1:**

{% invert %}
![case1](assets/515-find-largest-value-in-each-tree-row/case1.png)
{% endinvert %}

> Input: `root = [1,3,2,5,3,null,9]`
> Output: `[1,3,9]`

**Example 2:**

> Input: `root = [1,2,3]`
> Output: `[1,3]`

**Constraints:**

- The number of nodes in the tree will be in the range `[0, 10⁴]`.
- `-2³¹ <= Node.val <= 2³¹ - 1`

## Test Cases

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
```

{% asset_code coding/assets/515-find-largest-value-in-each-tree-row/solution_test.py %}

## Thoughts

直接像 [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/index.md) 一样逐层遍历（层序遍历）二叉树，记录每层的最大值即可。

## Code

{% asset_code coding/assets/515-find-largest-value-in-each-tree-row/solution.py %}
