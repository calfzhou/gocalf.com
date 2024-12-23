from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        total = 0
        parents = [root]
        while parents:
            children = [c for node in parents for c in (node.left, node.right) if c]

            m = len(children)
            total += m
            indices = sorted(range(m), key=lambda i: children[i].val)
            for i in range(m):
                if indices[i] < 0: continue
                while indices[i] >= 0:
                    indices[i], i = -1, indices[i]
                total -= 1

            parents = children

        return total
