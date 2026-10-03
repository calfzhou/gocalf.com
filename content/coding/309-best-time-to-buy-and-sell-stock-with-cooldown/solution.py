class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        hold = -prices[0]
        empty = p_empty = 0
        for price in prices:
            p_empty, hold, empty = empty, max2(hold, p_empty - price), max2(empty, hold + price)

        return empty
