class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        u = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                u[j] += u[j-1]

        return u[-1]
