from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)
        virtual = TreeNode(None)
        stack = [virtual] # path from root to current node
        i = j = 0
        while i < n:
            node = TreeNode(preorder[i])
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)
            while j < n and stack[-1].val == postorder[j]:
                stack.pop()
                j += 1

            i += 1

        return virtual.left
