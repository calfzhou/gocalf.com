
class Solution:
    def maxScore(self, s: str) -> int:
        max2 = lambda a, b: a if a >= b else b
        counts = [0, 0]
        counts[int(s[0])] += 1
        best = counts[0] - counts[1]
        for i in range(1, len(s) - 1):
            counts[int(s[i])] += 1
            best = max2(best, counts[0] - counts[1])

        counts[int(s[-1])] += 1
        return counts[1] + best
