from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r - 1:
            m = (l + r) >> 1
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] < nums[m]:
                l = m + 1
            else: # nums[m] < nums[r]
                r = m

        return min(nums[l], nums[r])
