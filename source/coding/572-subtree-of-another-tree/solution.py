from typing import Optional

from utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        while root or stack:
            if root:
                if self._is_same(root, subRoot):
                    return True
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right

        return False

    def _is_same(self, root1: TreeNode|None, root2: TreeNode|None) -> bool:
        stack = []
        while root1 or root2 or stack:
            if (not not root1) != (not not root2):
                return False
            elif root1:
                if root1.val != root2.val:
                    return False
                stack.append((root1, root2))
                root1 = root1.left
                root2 = root2.left
            elif stack:
                root1, root2 = stack.pop()
                root1 = root1.right
                root2 = root2.right

        return True
