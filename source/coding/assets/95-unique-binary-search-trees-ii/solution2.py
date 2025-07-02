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
        # dp[i][j]: all trees for i...j
        dp = [[[None] for _ in range(n + 2)] for _ in range(n + 2)]
        for size in range(1, n + 1):
            for i in range(1, n - size + 2):
                j = i + size - 1
                trees = []
                for k in range(i, j + 1):
                    for l, r in product(dp[i][k-1], dp[k+1][j]):
                        trees.append(TreeNode(k, l, r))

                dp[i][j] = trees

        return dp[1][n]
