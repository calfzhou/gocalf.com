class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        prev = nums[0] & 1
        for i in range(1, len(nums)):
            if nums[i] & 1 == prev:
                return False
            prev = 1 - prev

        return True
