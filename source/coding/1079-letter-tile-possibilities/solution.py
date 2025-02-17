from collections import defaultdict
from math import factorial


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts: dict[str, int] = defaultdict(int)
        for tile in tiles:
            counts[tile] += 1

        counts = list(counts.values())
        n = len(counts)

        def backtrack(i: int, occurs: list[int]) -> int:
            if i == n:
                total = factorial(sum(occurs))
                for freq in occurs:
                    total //= factorial(freq)
                return total

            total = backtrack(i + 1, occurs)
            count = counts[i]
            occurs.append(0)
            for j in range(1, count + 1):
                occurs[-1] = j
                total += backtrack(i + 1, occurs)

            del occurs[-1]
            return total

        total = backtrack(0, []) - 1 # Exclude the empty subset.
        return total
