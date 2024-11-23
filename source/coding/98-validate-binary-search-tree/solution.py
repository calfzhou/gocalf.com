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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_val = None
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if max_val is not None and root.val <= max_val:
                    return False
                max_val = root.val
                root = root.right

        return True
