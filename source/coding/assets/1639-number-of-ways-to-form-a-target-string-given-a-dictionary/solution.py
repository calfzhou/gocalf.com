from collections import defaultdict


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        m = len(target)
        n = len(words[0])
        if m > n: return 0

        occurs: list[dict[str, int]] = [defaultdict(int) for _ in range(n)]
        for word in words:
            for i, c in enumerate(word):
                occurs[i][c] += 1

        n -= m - 1
        dp = [1] * (n + 1)
        dp[0] = 0
        MOD = 1_000_000_007
        for i in range(m):
            for j in range(1, n+1):
                freq = occurs[i+j-1][target[i]]
                dp[j] = (dp[j-1] + dp[j] * freq) % MOD

        return dp[n]
