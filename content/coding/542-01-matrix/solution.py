class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        min2 = lambda a, b: a if a <= b else b
        m = len(mat)
        n = len(mat[0])
        dp = [[m+n] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if i > 0: dp[i][j] = min2(dp[i][j], 1 + dp[i-1][j])
                    if j > 0: dp[i][j] = min2(dp[i][j], 1 + dp[i][j-1])
                else:
                    dp[i][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j]:
                    if i < m - 1: dp[i][j] = min2(dp[i][j], 1 + dp[i+1][j])
                    if j < n - 1: dp[i][j] = min2(dp[i][j], 1 + dp[i][j+1])

        return dp
