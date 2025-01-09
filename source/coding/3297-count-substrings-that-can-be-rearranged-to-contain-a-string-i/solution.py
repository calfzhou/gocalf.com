from collections import defaultdict


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        if n1 < len(word2):
            return 0

        needs = defaultdict(int)
        for c in word2:
            needs[c] += 1
        miss = len(needs)

        total = 0
        i = j = 0
        while not (miss and j == n1):
            if miss:
                if (c := word1[j]) in needs:
                    needs[c] -= 1
                    if needs[c] == 0:
                        miss -= 1
                j += 1
            else:
                total += n1 - j + 1
                if (c := word1[i]) in needs:
                    needs[c] += 1
                    if needs[c] == 1:
                        miss += 1
                i += 1

        return total
