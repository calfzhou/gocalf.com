from typing import Iterable


class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        if max(nums) >= k: return 1

        min2 = lambda a, b: a if a <= b else b

        def bits(x: int) -> Iterable[int]:
            i = 0
            while x > 0:
                if x & 1: yield i
                x >>= 1
                i += 1

        n = len(nums)
        counts = [0] * k.bit_length()
        l = r = 0
        res = 0
        min_len = n + 1
        while r < n:
            while res < k and r < n:
                res |= nums[r]
                for b in bits(nums[r]):
                    counts[b] += 1
                r += 1

            while res >= k:
                min_len = min2(min_len, r - l)
                for b in bits(nums[l]):
                    counts[b] -= 1
                    if counts[b] == 0:
                        res -= 1 << b
                l += 1

        return -1 if min_len > n else min_len
