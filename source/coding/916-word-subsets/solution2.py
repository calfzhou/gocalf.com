from typing import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        occurs: dict[str, int] = Counter()
        for word in words2:
            counter = Counter(word)
            occurs |= counter

        return [word for word in words1 if Counter(word) >= occurs]
