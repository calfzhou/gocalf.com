from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))
        while len(queue) > 0:
            root, level = queue.popleft()
            if root is not None:
                queue.append((root.left, level + 1))
                queue.append((root.right, level + 1))

        return level
