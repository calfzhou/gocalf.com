---
title: 572. Subtree of Another Tree
notebook: coding
tags:
- easy
date: 2024-11-18 23:41:31
updated: 2024-11-18 23:41:31
---
## Problem

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

<https://leetcode.com/problems/subtree-of-another-tree/>

**Example 1:**

{% invert %}
{% image 572-subtree-of-another-tree/case1.png %}
{% endinvert %}

> Input: `root = [3,4,5,1,2], subRoot = [4,1,2]`
> Output: `true`

**Example 2:**

{% invert %}
{% image 572-subtree-of-another-tree/case2.png %}
{% endinvert %}

> Input: `root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]`
> Output: `false`

**Constraints:**

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Test Cases

{% asset_code coding/572-subtree-of-another-tree/solution_test.py %}

## Thoughts

先看比较两颗二叉树是否相等。同时按同样的顺序遍历两颗树，只要出现一边有节点另一边是空，或者两边节点的值不同，就不相等。

比如用前序遍历（NLR）。可以用栈替代递归，给两个树各维持一个栈，或者用一个栈但每次把两棵树的节点打包入栈。

要判断 `subRoot` 是否是 `root` 的子树，先判断 `root` 跟 `subRoot` 是否相等，不相等的话再递归判定 `subRoot` 是不是 `root.left` 或 `root.right` 的子树。同样可以用栈替代递归，对 `root` 做 NLR 遍历，遍历到任何一个节点时，判断以该节点为根的子树是否跟 `subRoot` 相等。

设 `root` 和 `subRoot` 的节点数分别是 `n` 和 `m`，则时间复杂度为 `O(n * m)`。

## Code

{% asset_code coding/572-subtree-of-another-tree/solution.py %}

> 似乎用栈并不比直接用递归快。
