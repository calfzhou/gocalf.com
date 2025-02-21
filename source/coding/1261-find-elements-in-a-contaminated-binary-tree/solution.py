from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:

    def __init__(self, root: Optional['TreeNode']):
        self._root = root

    def find(self, target: int) -> bool:
        branches: list[int] = [] # 1 for left, 0 for right.
        while target > 0:
            branches.append(target & 1)
            target = (target - 1) // 2

        node = self._root
        for branch in reversed(branches):
            if node is None:
                return False
            node = node.left if branch == 1 else node.right

        return node is not None


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
