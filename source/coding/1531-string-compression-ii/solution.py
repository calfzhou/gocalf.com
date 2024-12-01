from math import log10


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n - 2: return n - k

        clen = lambda n: n if n < 2 else int(log10(n)) + 2
        dp = [[n] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1): # Substring s[:i].
            for d in range(min(i, k) + 1): # Max number of deletions, 0 <= d <= k.
                if d > 0:
                    dp[i][d] = min(dp[i][d], dp[i-1][d-1])

                r = cnt = 0
                for j in range(i, 0, -1):
                    if s[j-1] == s[i-1]:
                        cnt += 1
                    else:
                        dp[i][d] = min(dp[i][d], dp[j][d-r] + clen(cnt))
                        if r == d: break
                        r += 1
                else:
                    dp[i][d] = min(dp[i][d], dp[0][d-r] + clen(cnt))

        return dp[n][k]
