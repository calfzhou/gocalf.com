from functools import cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2)] # ↖ ↗ ↘ ↙
        dp = [[1.0] * n for _ in range(n)]
        new_dp = [[0] * n for _ in range(n)]
        for _ in range(k):
            for r in range(n):
                for c in range(n):
                    p = 0.0
                    for dr, dc in dirs:
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            p += dp[r+dr][c+dc]
                    new_dp[r][c] = p / 8

            dp, new_dp = new_dp, dp

        return dp[row][column]
