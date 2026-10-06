class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        min2 = lambda a, b: a if a <= b else b
        ps = largest = nums[0]
        low = 0
        for i in range(1, len(nums)):
            low = min2(low, ps) # low(i-1) = min(low(i-2), ps(i-1))
            ps += nums[i] # ps(i) = ps(i-1) + nums[i]
            largest = max2(largest, ps - low) # s(i) = ps(i) - low(i-1)

        return largest
