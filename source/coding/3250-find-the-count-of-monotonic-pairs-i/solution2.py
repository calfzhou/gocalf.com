class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        n = len(nums)
        m = nums[-1]
        for i in range(1, n):
            if (d := nums[i] - nums[i-1]) > 0:
                m -= d
                if m < 0:
                    return 0

        # C(m+n, n)
        if m < n:
            m, n = n, m

        res = 1
        for j in range(n):
            res = res * (m + 1 + j) // (1 + j)

        return res % 1_000_000_007
