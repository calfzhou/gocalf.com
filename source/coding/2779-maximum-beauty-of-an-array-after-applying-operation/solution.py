class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        k <<= 1
        max_len = 1
        l = 0
        r = 1
        while r < n:
            if nums[r] - nums[l] > k:
                l += 1
            else:
                max_len = max(max_len, r - l + 1)
                r += 1

        return max_len
