class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for n in range(1, numRows):
            row = [1] * (n + 1)
            for m in range(1, n // 2 + 1):
                row[m] = row[n - m] = row[m - 1] * (n - m + 1) // m
            res.append(row)

        return res
