from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        tmp = factorial(n)
        return factorial(n << 1) // tmp // tmp // (n + 1)
