class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        dl = dd = dp = arr[0]
        for i in range(1, len(arr)):
            dd = max2(dl, dd + arr[i])
            dl = max2(dl, 0) + arr[i]
            dp = max2(dp, max2(dd, dl))

        return dp
