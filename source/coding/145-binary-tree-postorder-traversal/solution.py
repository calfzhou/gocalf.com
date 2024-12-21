from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        prev = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            elif stack[-1].right != prev:
                root = stack[-1].right
                prev = None
            else:
                prev = stack.pop()
                res.append(prev.val)

        return res
