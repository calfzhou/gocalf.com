from typing import Optional

import sys
sys.path.insert(0, '..')
from _utils.binary_tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        backup = root
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root.left, root.right = root.right, root.left
                root = root.left # Original right child.
            else:
                root = stack.pop().right # Original left child.

        return backup
