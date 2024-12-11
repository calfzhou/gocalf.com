class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        k <<= 1
        l = 0
        for r in range(1, n):
            if nums[r] - nums[l] > k:
                l += 1

        return n - l
