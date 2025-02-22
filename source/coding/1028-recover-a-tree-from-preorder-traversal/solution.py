from typing import Iterable, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = [] # path from root to current node
        for level, val in self.tokenize(traversal):
            while len(stack) > level:
                stack.pop()

            node = TreeNode(val)
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

            stack.append(node)

        return stack[0]

    def tokenize(self, traversal: str) -> Iterable[tuple[int, int]]:
        level = 0
        for part in traversal.split('-'):
            if not part:
                level += 1
            else:
                yield level, int(part)
                level = 1
