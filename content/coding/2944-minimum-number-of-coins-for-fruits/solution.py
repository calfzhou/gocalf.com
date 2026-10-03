class Solution:
    def minimumCoins(self, prices: list[int]) -> int:
        n = len(prices)
        for i in range((n-3) // 2, -1, -1):
            prices[i] += min(prices[j] for j in range(i + 1, 2 * i + 3))

        return prices[0]

