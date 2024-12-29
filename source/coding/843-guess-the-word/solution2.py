# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


import random


class Solution:
    def findSecretWord(self, words: list[str], master: 'Master') -> None:
        match = lambda i, j: sum(1 for a, b in zip(words[i], words[j]) if a == b)
        n = len(words)
        candidates = list(range(n))

        while True:
            choice = random.choice(candidates)
            m = master.guess(words[choice])
            if m == 6: break

            candidates = [i for i in candidates if match(choice, i) == m]
