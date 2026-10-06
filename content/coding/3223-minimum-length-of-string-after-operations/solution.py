from collections import defaultdict


class Solution:
    def minimumLength(self, s: str) -> int:
        counts = defaultdict(lambda: 2)
        for c in s:
            counts[c] = 3 - counts[c]

        return sum(k for k in counts.values())
