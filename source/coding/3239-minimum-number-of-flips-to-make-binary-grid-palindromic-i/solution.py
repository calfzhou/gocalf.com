from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        flip_count_row = 0
        for row in grid:
            for j in range(n >> 1):
                if row[j] != row[-j - 1]:
                    flip_count_row += 1

        flip_count_col = 0
        for j in range(n):
            for i in range(m >> 1):
                if grid[i][j] != grid[-i - 1][j]:
                    flip_count_col += 1

        return min(flip_count_row, flip_count_col)
