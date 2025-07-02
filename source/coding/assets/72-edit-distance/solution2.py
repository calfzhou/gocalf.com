class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[i + j for j in range(n + 1)] for i in range(m + 1)]
        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

        return dp[m][n]
