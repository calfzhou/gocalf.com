class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        if max(nums) >= k: return 1

        min2 = lambda a, b: a if a <= b else b

        n = len(nums)
        l = 0
        r = r0 = 1
        res_r = 0 # Bit-or of nums[r0:r]
        min_len = n + 1
        while r < n:
            while nums[l] | res_r < k and r < n:
                res_r |= nums[r]
                r += 1

            while l < n and nums[l] | res_r >= k:
                min_len = min2(min_len, r - l)
                l += 1
                if l == r0:
                    r0 = r
                    res_r = 0
                    for i in range(r - 2, l - 1, -1):
                        nums[i] |= nums[i + 1]

        return -1 if min_len > n else min_len
