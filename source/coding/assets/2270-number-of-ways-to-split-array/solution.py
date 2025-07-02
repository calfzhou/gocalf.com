class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        valid = 0
        left = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= total - left: valid += 1

        return valid
