from functools import cache
from itertools import product
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        @cache
        def gen(i: int, j: int) -> list[TreeNode]:
            if i == j: return [TreeNode(i)]
            elif i > j: return [None]

            trees = []
            for k in range(i, j + 1):
                left = gen(i, k - 1)
                right = gen(k + 1, j)
                for l, r in product(left, right):
                    trees.append(TreeNode(k, l, r))

            return trees

        return gen(1, n)
