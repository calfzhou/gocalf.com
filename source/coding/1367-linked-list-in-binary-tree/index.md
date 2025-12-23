---
title: 1367. Linked List in Binary Tree
notebook: coding
tags:
- medium
date: 2024-12-30 01:02:05
updated: 2024-12-30 01:02:05
---
## Problem

Given a binary tree `root` and a linked list with `head` as the first node.

Return True if all the elements in the linked list starting from the `head` correspond to some _downward path_ connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

<https://leetcode.cn/problems/linked-list-in-binary-tree/>

**Example 1:**

{% invert %}
![case1](assets/1367-linked-list-in-binary-tree/case1.png)
{% endinvert %}

> Input: `head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
> Output: `true`
> Explanation: Nodes in blue form a subpath in the binary Tree.

**Example 2:**

{% invert %}
![case2](assets/1367-linked-list-in-binary-tree/case2.png)
{% endinvert %}

> Input: `head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
> Output: `true`

**Example 3:**

> Input: `head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
> Output: `false`
> Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

**Constraints:**

- The number of nodes in the tree will be in the range `[1, 2500]`.
- The number of nodes in the list will be in the range `[1, 100]`.
- `1 <= Node.val <= 100` for each node in the linked list and binary tree.

## Test Cases

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
```

{% asset_code coding/assets/1367-linked-list-in-binary-tree/solution_test.py %}

## Thoughts

按某个顺序遍历二叉树，如前序遍历（pre-order，NLR）。对于当前节点，判断是否存在以其为起点的与给定链表一致的路径。

时间复杂度 `O(n * 2ᵐ) ≤ O(n²)`，其中 n 是二叉树的节点数量，m 是链表的节点数量。遍历整棵树的时间是 `O(n)`，对于其中每个节点，以其为起点跟链表比较的最坏时间复杂度是 `O(2ᵐ) ≤ O(n)`，这是高度为 m 的二叉树的叶子节点的量级。

> 不知道能否像 KMP 算法或者 AC 自动机（[3213. Construct String with Minimum Cost](../3213-construct-string-with-minimum-cost/index.md) 中用到）那样，以 `O(n + m)` 时间完成呢。本题跟 AC 自动机的场景是相反的，AC 自动机相当于在链表中找二叉树的每一条路径，而本题是在二叉树的每一条路径中找链表。

## Code

{% asset_code coding/assets/1367-linked-list-in-binary-tree/solution.py %}
