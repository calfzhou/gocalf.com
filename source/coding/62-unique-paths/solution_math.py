class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        res = 1
        for j in range(n - 1):
            res *= m + j
            res //= 1 + j

        return res
