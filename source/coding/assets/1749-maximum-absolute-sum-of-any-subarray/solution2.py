from itertools import accumulate


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        sums = list(accumulate(nums, initial=0))
        return max(sums) - min(sums)
