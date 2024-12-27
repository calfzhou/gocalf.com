from math import inf


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        max_score = -inf
        max_left = values[0]
        for j in range(1, len(values)):
            max_score = max2(max_score, max_left + values[j] - j)
            max_left = max2(max_left, values[j] + j)

        return max_score
