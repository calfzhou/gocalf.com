class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        mn = m * n
        k %= mn
        if k == 0: return grid

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r, c = divmod(k, n)
                res[r][c] = grid[i][j]
                k = (k + 1) % mn

        return res
