from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        max2 = lambda a, b: a if a >= b else b
        dp = lambda u: u.val if u else (0, 0)
        stack = []
        prev = None
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            elif stack[-1].right != prev:
                node = stack[-1].right
                prev = None
            else:
                prev = stack.pop() # prev is the LRN visiting node, its left and right child both done.
                prev.val = (
                    prev.val + dp(prev.left)[1] + dp(prev.right)[1],
                    max2(*dp(prev.left)) + max2(*dp(prev.right)),
                )

        return max2(*root.val)
