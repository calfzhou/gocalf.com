from itertools import accumulate

min2 = lambda a, b: a if a <= b else b


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        if numCarpets * carpetLen >= n:
            return 0

        floors = [int(x) for x in floor]
        dp = list(accumulate(floors)) # These are dp(i, 0).

        covered = 0
        for _ in range(numCarpets):
            prev = dp
            dp = [0] * n
            covered += carpetLen
            for i in range(covered, n):
                dp[i] = min2(dp[i-1] + floors[i], prev[i - carpetLen])

        return dp[-1]
