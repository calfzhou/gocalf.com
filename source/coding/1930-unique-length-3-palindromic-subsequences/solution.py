from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        edges: dict[str, list[int]] = defaultdict(lambda: [-1, 0]) # char: [first position, last position]
        for i, c in enumerate(s):
            edge = edges[c]
            if edge[0] < 0:
                edge[0] = i
            else:
                edge[1] = i

        total = 0
        for l, r in edges.values():
            total += len(set(s[l+1:r]))

        return total
