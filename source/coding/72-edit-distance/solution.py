class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2): word1, word2 = word2, word1
        n = len(word2)
        dp = [j for j in range(n + 1)]
        for i, c1 in enumerate(word1, 1):
            p_dp, dp[0] = dp[0], i
            for j, c2 in enumerate(word2, 1):
                if c1 == c2:
                    p_dp, dp[j] = dp[j], p_dp
                else:
                    p_dp, dp[j] = dp[j], 1 + min(dp[j-1], dp[j], p_dp)

        return dp[n]
