class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        max2 = lambda a, b: a if a >= b else b
        hold = -prices[0]
        empty = 0
        for price in prices:
            hold, empty = max2(hold, empty - price), max2(empty, hold + price - fee)

        return empty
