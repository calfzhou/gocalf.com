class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        s = largest = nums[0]
        for i in range(1, len(nums)):
            s = max2(s, 0) + nums[i]
            largest = max2(largest, s)

        return largest
