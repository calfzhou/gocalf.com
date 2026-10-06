# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        parents = [root]
        reverse = True
        while parents[0].left:
            if reverse:
                children = [c for node in reversed(parents) for c in (node.right, node.left)]
            else:
                children = [c for node in reversed(parents) for c in (node.left, node.right)]

            j = 0
            for node in parents:
                node.left = children[j]
                node.right = children[j+1]
                j += 2

            parents = children
            reverse = not reverse

        return root
