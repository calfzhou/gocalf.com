from functools import cache
from math import inf


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        min2 = lambda a, b: a if a <= b else b

        @cache
        def dp(t: int, b: int, l: int, r: int) -> int:
            if b - t <= 1 and r - l <= 1: return 0

            cost = inf
            for i in range(t + 1, b):
                cost = min2(cost, horizontalCut[i-1] + dp(t, i, l, r) + dp(i, b, l, r))
            for j in range(l + 1, r):
                cost = min2(cost, verticalCut[j-1] + dp(t, b, l, j) + dp(t, b, j, r))

            return cost

        return dp(0, m, 0, n)
