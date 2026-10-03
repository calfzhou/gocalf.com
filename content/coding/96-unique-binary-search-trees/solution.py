class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            m = i >> 1
            cnt = 0
            for a in range(m):
                cnt += dp[a] * dp[i - 1 - a]
            cnt <<= 1
            if i & 1:
                cnt += dp[m] * dp[m]
            dp[i] = cnt

        return dp[n]
