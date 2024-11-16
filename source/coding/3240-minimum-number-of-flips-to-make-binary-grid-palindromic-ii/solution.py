from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        m_half = m >> 1
        n_half = n >> 1
        flip_count = 0

        # Four-cells groups.
        for i in range(m_half):
            for j in range(n_half):
                s = grid[i][j] + grid[i][-j-1] + grid[-i-1][j] + grid[-i-1][-j-1]
                flip_count += min(s, 4 - s)

        # Center cell.
        if m & 1 & n:
            flip_count += grid[m_half][n_half]

        # Two-cells pairs (in middle row and middle column).
        one_one = 0 # The number of 1-1 pairs (mod 2).
        zero_one = 0 # The number of 0-1 and 1-0 pairs.
        if m & 1:
            for j in range(n_half):
                s = grid[m_half][j] + grid[m_half][-j-1]
                one_one ^= (s >> 1)
                zero_one += (s & 1)

        if n & 1:
            for i in range(m_half):
                s = grid[i][n_half] + grid[-i-1][n_half]
                one_one ^= (s >> 1)
                zero_one += (s & 1)

        flip_count += zero_one if zero_one > 0 else (one_one << 1)
        return flip_count
