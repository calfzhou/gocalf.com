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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        while p or q or stack:
            if (not not p) != (not not q):
                return False
            elif p:
                if p.val != q.val:
                    return False
                stack.append((p, q))
                p = p.left
                q = q.left
            elif stack:
                p, q = stack.pop()
                p = p.right
                q = q.right

        return True
