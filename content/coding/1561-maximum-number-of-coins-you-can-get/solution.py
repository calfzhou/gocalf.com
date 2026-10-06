class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)
        return sum(piles[i] for i in range(1, len(piles) // 3 * 2, 2))
