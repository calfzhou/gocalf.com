from collections import defaultdict
from itertools import combinations


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        prods: dict[int, int] = defaultdict(int) # product -> count of pairs
        for a, b in combinations(nums, 2):
            prods[a * b] += 1

        return sum(m * (m - 1) << 2 for m in prods.values() if m > 1)
