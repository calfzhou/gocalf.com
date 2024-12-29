# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


from collections import Counter
from math import inf


class Solution:
    def findSecretWord(self, words: list[str], master: 'Master') -> None:
        n = len(words)
        matches = [[6] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                m = sum(1 for a, b in zip(words[i], words[j]) if a == b)
                matches[i][j] = matches[j][i] = m

        candidates = list(range(n))
        while True:
            choice, remain = 0, inf
            for i in candidates:
                counter = Counter(matches[i][j] for j in candidates)
                m, cnt = counter.most_common(1)[0]
                if cnt < remain:
                    choice, remain = i, cnt

            m = master.guess(words[choice])
            if m == 6:
                break

            candidates = [i for i in candidates if matches[choice][i] == m]
