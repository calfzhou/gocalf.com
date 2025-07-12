from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        longest = [1] * n
        for i, v_i in enumerate(nums):
            for p in filter(lambda p: v_i > nums[p], range(i)):
                longest[i] = max(longest[i], longest[p] + 1)

        return max(longest)
