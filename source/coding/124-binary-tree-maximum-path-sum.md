---
title: 124. Binary Tree Maximum Path Sum
notebook: coding
tags:
- hard
date: 2024-11-26 01:12:58
updated: 2024-11-26 01:12:58
katex: true
---
## Problem

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return _the maximum **path sum** of any **non-empty** path_.

<https://leetcode.com/problems/binary-tree-maximum-path-sum/>

**Example 1:**

{% invert %}
{% image 124-binary-tree-maximum-path-sum/case1.png %}
{% endinvert %}

> Input: `root = [1,2,3]`
> Output: `6`
> Explanation: The optimal path is `2 -> 1 -> 3` with a path sum of `2 + 1 + 3 = 6`.

**Example 2:**

{% invert %}
{% image 124-binary-tree-maximum-path-sum/case2.png %}
{% endinvert %}

> Input: `root = [-10,9,20,null,null,15,7]`
> Output: `42`
> Explanation: The optimal path is `15 -> 20 -> 7` with a path sum of `15 + 20 + 7 = 42`.

**Constraints:**

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
```

{% asset_code coding/124-binary-tree-maximum-path-sum/solution_test.py %}

## Thoughts

对任意一个节点 u，如果能确定以其为根节点的子树内，**节点 u 包含其中** 的所有路径（或称必经路径）中的最大路径和（记为 `ps(u)`）。那么所有节点中，`ps` 的最大值即为题目所求的最大路径和。

对于节点 u，定义 `s(u)` 为 **以 u 为（最靠上）端点** 的所有路径（或称单边路径）中的最大路径和。显然有：

$$
s(u)=u.val+\max\{0,s(u.left),s(u.right)\}
$$

即要么节点 u 自成路径（单一节点），要么与其左子节点的最大单边路径连起来，要么与其右子节点的最大单边路径连起来。进而得到：

$$
ps(u)=\max\{s(u),u.val+s(u.left)+s(u.right)\}
$$

即要么是最大单边路径，要么左右两边最大单边路径连成的一整条 `∧` 形状的路径。

遍历二叉树（这里用后序（post-order，LRN）最方便），过程中记录每个节点的 `s` 值，以及所见到的最大的 `ps` 值。

`s(u)` 可以直接保存在 `u.val` 上，减少额外的空间消耗。

非递归的后序遍历也是用栈辅助，比前序（pre-order，NLR）和中序（in-order，LNR）稍微麻烦一点的地方是，根节点需要等其左右子节点都处理完再出栈。可以考虑添加一个临时变量记录前一次访问的节点，如果前一个节点是根节点（栈里最后一个节点）的右子节点，就说明左右子节点都处理完毕，可以从栈里把根节点弹出来进行处理。

## Code

{% asset_code coding/124-binary-tree-maximum-path-sum/solution.py %}
