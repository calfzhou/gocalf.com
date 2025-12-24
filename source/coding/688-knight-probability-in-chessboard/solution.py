from functools import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2)] # ↖ ↗ ↘ ↙

        @cache
        def dfs(i: int, r: int, c: int) -> float:
            if i == k:
                return 1.0

            p = 0.0
            for dr, dc in dirs:
                if 0 <= r + dr < n and 0 <= c + dc < n:
                    p += dfs(i + 1, r + dr, c + dc)

            return p / 8

        return dfs(0, row, column)
