from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)
        stack = [] # stack[i]'s right child is to be determined.
        virtual = root = TreeNode(None) # root's left child is to be determined.
        i = j = 0
        while i < n:
            if len(stack) > 1 and stack[-2].val == inorder[j]:
                stack.pop() # stack[-1] has no right child.
                j += 1
                continue

            node = TreeNode(preorder[i])
            if root is None:
                stack.pop().right = root = node
            else:
                root.left = root = node

            stack.append(root)
            i += 1
            if root.val == inorder[j]:
                j += 1
                root = None # root has no left child.

        return virtual.left
