class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b

        dp = [0] * (k + 1)
        cnt = 0
        for pile in piles:
            cnt = min2(cnt + len(pile), k)
            for i in range(1, min2(k, len(pile))):
                pile[i] += pile[i-1]

            for j in range(cnt, 0, -1):
                for i in range(min2(j, len(pile))):
                    dp[j] = max2(dp[j], dp[j-i-1] + pile[i])

        return dp[k]
