import math


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2: return 0

        mx = max(nums)
        mn = min(nums)
        if mx == mn: return 0

        sz = math.ceil((mx - mn) / (n - 1))
        cnt = 1 + (mx - mn) // sz
        buckets: list[list[int]] = [[None, None] for _ in range(cnt)]

        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b
        for x in nums:
            bucket = buckets[(x - mn) // sz]
            if bucket[0] is None:
                bucket[:] = x, x
            else:
                bucket[:] = min2(bucket[0], x), max2(bucket[1], x)

        max_gap = 0
        prev_large = None
        for small, large in buckets:
            if small is None: continue
            if prev_large is not None:
                max_gap = max2(max_gap, small - prev_large)
            prev_large = large

        return max_gap
