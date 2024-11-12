from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(i - v for i, v in enumerate(nums, 1))
