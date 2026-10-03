class Solution:
    def maxSpending(self, values: list[list[int]]) -> int:
        prices = [p for shop in values for p in shop]
        prices.sort()
        return sum(p * d for d, p in enumerate(prices, 1))
