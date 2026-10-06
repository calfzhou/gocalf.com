class Solution:
    def canJump(self, nums: list[int]) -> bool:
        r = len(nums) - 1
        for l in range(r - 1, -1, -1):
            if nums[l] >= r - l:
                r = l

        return r == 0
