from math import ceil


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        if (n := len(nums)) == 1:
            return ceil(nums[0] / (maxOperations + 1))

        s = sum(nums)
        r = min(max(nums), ceil(s / (maxOperations + 1)))
        l = ceil(s / (n + maxOperations))
        while l <= r:
            m = (l + r) >> 1
            k = 0
            for a in filter(lambda a: a > m, nums):
                k += ceil(a / m) - 1
                if k > maxOperations: break

            if k > maxOperations:
                l = m + 1
            else:
                r = m - 1

        return r + 1
