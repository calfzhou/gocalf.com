---
title: 297. Serialize and Deserialize Binary Tree
notebook: coding
tags:
- hard
date: 2024-11-16 22:09:26
updated: 2024-11-16 22:09:26
---
## Problem

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as [how LeetCode serializes a binary tree](https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

<https://leetcode.com/problems/serialize-and-deserialize-binary-tree/>

**Example 1:**

{% invert %}
{% image 297-serialize-and-deserialize-binary-tree/case1.png %}
{% endinvert %}

> Input: `root = [1,2,3,null,null,4,5]`
> Output: `[1,2,3,null,null,4,5]`

**Example 2:**

> Input: `root = []`
> Output: `[]`

**Constraints:**

- The number of nodes in the tree is in the range `[0, 10⁴]`.
- `-1000 <= Node.val <= 1000`

## Test Cases

``` python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```

{% asset_code coding/297-serialize-and-deserialize-binary-tree/solution_test.py %}

## Thoughts

序列化的时候按照某个顺序遍历二叉树，依次打印访问到的节点的数据。可以用前序（pre-order，NLR）、中序（in-order，LNR）、后序（post-order，LRN）、层序（level-order）。

需要记录一定的分隔符（如对应位置的空节点），在反序列化的时候才能确定边界。

序列化时候几种遍历顺序都很容易实现，主要看反序列化的时候怎么比较方便。

LeetCode 用的是层序，并把空的子节点用 `null` 记录占位。层序在序列化和反序列化的时候，用队列辅助循环处理。

用前序遍历（NLR）。如果左右子节点为空，需要记占位符，直接用空字符串表示。节点值之间用逗号分割。序列化和反序列化的时候，都用栈辅助，避免递归。

比如上边 example 1 中的二叉树，会序列化为 `"1,2,,,3,4,,,5,"`。

## Code

{% asset_code coding/297-serialize-and-deserialize-binary-tree/solution.py %}

可以看到序列化和反序列化的操作逻辑是完全一致的，唯一的区别就是前者在遍历过程中把节点的值读出来，后者把获取到的值和父子关系写到节点上。

另外反序列化的时候，通过一个指向根节点的虚拟节点，可以简化边界值的处理逻辑。
