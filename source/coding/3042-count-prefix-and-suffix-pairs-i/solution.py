from itertools import combinations


class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        return sum(1 for s1, s2 in combinations(words, 2) if s2.startswith(s1) and s2.endswith(s1))
