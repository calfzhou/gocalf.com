class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        n = rowIndex
        res = [1] * (n + 1)
        for m in range(1, n // 2 + 1):
            res[m] = res[n - m] = res[m - 1] * (n - m + 1) // m

        return res
