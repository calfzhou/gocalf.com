from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:

    def __init__(self, root: Optional['TreeNode']):
        self._vals: set[int] = set()

        def dfs(node: Optional['TreeNode'], val: int) -> None:
            if node is None:
                return
            self._vals.add(val)
            val = 2 * val + 1
            dfs(node.left, val)
            dfs(node.right, val + 1)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self._vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
