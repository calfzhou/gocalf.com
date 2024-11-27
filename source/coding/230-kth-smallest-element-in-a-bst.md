---
title: 230. Kth Smallest Element in a BST
notebook: coding
tags:
- medium
date: 2024-11-23 22:14:01
updated: 2024-11-23 22:14:01
---
## Problem

Given the `root` of a binary search tree, and an integer `k`, return _the_ `kᵗʰ` _smallest value (**1-indexed**) of all the values of the nodes in the tree_.

<https://leetcode.com/problems/kth-smallest-element-in-a-bst/>

**Example 1:**

{% invert %}
{% image 230-kth-smallest-element-in-a-bst/case1.png %}
{% endinvert %}

> Input: `root = [3,1,4,null,2], k = 1`
> Output: `1`

**Example 2:**

{% invert %}
{% image 230-kth-smallest-element-in-a-bst/case2.png %}
{% endinvert %}

> Input: `root = [5,3,6,2,4,null,null,1], k = 3`
> Output: `3`

**Constraints:**

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10⁴`
- `0 <= Node.val <= 10⁴`

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## Test Cases

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
```

{% asset_code coding/230-kth-smallest-element-in-a-bst/solution_test.py %}

## Thoughts

直接按照中序（in-order，LNR）遍历 BST 二叉树。访问到的第 k 个节点，其值就是第 k 小的数。

时间复杂度 `O(n)`。虽然找到第 k 个节点就结束，但中序遍历的话，即便是找到值最小的节点，最坏情况也可能需要先路过所有的其他节点。

所以频繁增删的 BST，可能会变得不平衡导致需要花很长时间才能找到第 k 小的节点，可以对 BST 做平衡调节。

## Code

{% asset_code coding/230-kth-smallest-element-in-a-bst/solution.py %}
