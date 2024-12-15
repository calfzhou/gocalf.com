class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        prev = prices[0]
        for price in prices:
            if price > prev: max_profit += price - prev
            prev = price
        return max_profit
