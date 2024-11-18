from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        s = 0
        for v in nums:
            s += v
            largest = max(largest, s)
            s = max(s, 0)

        return largest
