class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n > 1:
            nums[1] = max(nums[0], nums[1])

        for i in range(2, n):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])

        return nums[-1]
