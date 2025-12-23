class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        n = len(arr)
        dr = [0] * n # dr[i] = dr(i+1)
        for i in range(n - 1, 0, -1):
            dr[i-1] = max2(dr[i], 0) + arr[i]

        dl = dp = arr[0]
        for i in range(1, n):
            dp = max2(dp, dl + dr[i])
            dl = max2(dl, 0) + arr[i]
            dp = max2(dp, dl)

        return dp
