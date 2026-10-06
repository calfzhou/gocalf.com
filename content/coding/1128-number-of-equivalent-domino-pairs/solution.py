from typing import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counts = Counter((a, b) if a <= b else (b, a) for a, b in dominoes)
        return sum(k * (k-1) // 2 for k in counts.values() if k > 1)
