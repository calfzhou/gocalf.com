from collections import deque


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        last_day = days[-1]
        dp = deque([0], maxlen=30)
        i = 0
        for d in range(1, last_day + 1):
            if days[i] == d:
                i += 1
                dp.append(min(
                    dp[-1] + costs[0],
                    dp[max2(-7, -d)] + costs[1],
                    dp[max2(-30, -d)] + costs[2],
                ))
            else:
                dp.append(dp[-1])

        return dp[-1]
