class Solution:
    def findScore(self, nums: list[int]) -> int:
        n = len(nums)
        indices = list(range(n))
        indices.sort(key=lambda i: nums[i])
        marks = [False] * n
        score = 0
        for i in indices:
            if marks[i]: continue
            score += nums[i]
            marks[i] = True
            if i > 0: marks[i - 1] = True
            if i < n - 1: marks[i + 1] = True

        return score
