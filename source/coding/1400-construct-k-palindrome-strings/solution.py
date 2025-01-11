from collections import defaultdict


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False

        parity: dict[str, int] = defaultdict(int) # {c: 1 if c is odd, 0 if even}
        for c in s:
            parity[c] = 1 - parity[c]

        return sum(parity.values()) <= k
