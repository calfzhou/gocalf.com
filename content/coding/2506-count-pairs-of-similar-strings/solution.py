from collections import defaultdict


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        counts: dict[tuple[str], int] = defaultdict(int) # sorted chars -> count
        for word in words:
            chars = tuple(sorted(set(word)))
            counts[chars] += 1

        total = 0
        for count in counts.values():
            total += count * (count - 1) // 2

        return total
