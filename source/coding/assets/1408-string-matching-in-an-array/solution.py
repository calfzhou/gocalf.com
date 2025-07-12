class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        words.sort(key=lambda w: len(w))
        res = []
        n = len(words)
        for i in range(n - 1):
            a = words[i]
            for j in range(i + 1, n):
                b = words[j]
                if a in b:
                    res.append(a)
                    break

        return res
