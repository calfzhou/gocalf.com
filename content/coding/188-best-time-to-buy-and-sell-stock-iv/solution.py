min2 = lambda a, b: a if a <= b else b
max2 = lambda a, b: a if a >= b else b


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        k = min2(k, len(prices) >> 1)
        if k == 0: return 0
        buys = [-prices[0]] * k
        sells = [0] * k
        for price in prices:
            prev_sell = 0
            for j in range(k):
                prev_sell, buys[j], sells[j] = (
                    sells[j],
                    max2(buys[j], prev_sell - price),
                    max2(sells[j], buys[j] + price),
                )

        return sells[-1]
