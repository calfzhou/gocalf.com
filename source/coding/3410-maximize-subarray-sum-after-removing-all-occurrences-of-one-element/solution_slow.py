class Solution:
    def maxSubarraySum(self, nums: list[int]) -> int:
        candidates = {v for v in nums if v < 0}
        candidates.add(0)

        largest = nums[0]
        for removed in candidates:
            s = 0
            for v in nums:
                if v == removed: continue
                s += v
                largest = max(largest, s)
                s = max(s, 0)

        return largest
