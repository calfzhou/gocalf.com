from collections import deque


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        max2 = lambda a, b: a if a >= b else b
        MOD = 1_000_000_007
        total = 0
        dp = deque([1], maxlen=max2(zero, one))
        for i in range(1, high + 1):
            cnt = 0
            if i >= zero:
                cnt = dp[-zero]
            if i >= one:
                cnt = (cnt + dp[-one]) % MOD
            dp.append(cnt)

            if i >= low:
                total = (total + cnt) % MOD

        return total
