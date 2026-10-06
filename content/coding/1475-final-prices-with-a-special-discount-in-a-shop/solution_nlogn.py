from bisect import bisect_left, insort


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        indices = sorted(range(n), key=lambda i: (prices[i], -i))
        results = list(prices)
        valid_items = []
        for i in indices:
            idx = bisect_left(valid_items, i + 1)
            if idx < len(valid_items):
                results[i] -= prices[valid_items[idx]]
            insort(valid_items, i)

        return results
