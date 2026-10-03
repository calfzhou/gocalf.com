from collections import defaultdict


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        max2 = lambda a, b: a if a >= b else b
        occurs: dict[str, int] = defaultdict(int)
        for word in words2:
            counter: dict[str, int] = defaultdict(int)
            for c in word:
                counter[c] += 1

            for c, cnt in counter.items():
                occurs[c] = max2(occurs[c], cnt)

        result: list[str] = []
        for word in words1:
            counter: dict[str, int] = defaultdict(int)
            for c in word:
                counter[c] += 1

            for c, cnt in occurs.items():
                if counter[c] < cnt:
                    break
            else:
                result.append(word)

        return result
