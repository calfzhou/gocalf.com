max2 = lambda a, b: a if a >= b else b

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for price in prices:
            buy1, sell1, buy2, sell2 = (
                max2(buy1, -price),
                max2(sell1, buy1 + price),
                max2(buy2, sell1 - price),
                max2(sell2, buy2 + price),
            )

        return sell2
