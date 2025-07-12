class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices
