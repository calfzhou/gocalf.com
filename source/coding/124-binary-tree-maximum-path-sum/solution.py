from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        max_sum = root.val
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
                prev = stack.pop() # prev is the LRN visiting node.
                l = prev.left.val if prev.left else 0
                r = prev.right.val if prev.right else 0
                max_sum = max(max_sum, prev.val + max(0, l, r, l + r))
                prev.val += max(0, l, r)

        return max_sum
