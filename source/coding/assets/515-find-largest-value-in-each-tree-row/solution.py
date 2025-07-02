from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root: return []

        answer = []
        row = [root]
        while row:
            answer.append(max(node.val for node in row))
            row = [c for node in row for c in (node.left, node.right) if c]

        return answer
