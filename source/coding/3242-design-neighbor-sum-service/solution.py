from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        n2 = n * n
        self._adjacent_sums = [0] * n2
        self._diagonal_sums = [0] * n2

        g = lambda x, y: grid[x][y] if 0 <= x < n and 0 <= y < n else 0

        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                self._adjacent_sums[v] = g(i-1, j) + g(i, j-1) + g(i, j+1) + g(i+1, j)
                self._diagonal_sums[v] = g(i-1, j-1) + g(i-1, j+1) + g(i+1, j-1) + g(i+1, j+1)

    def adjacentSum(self, value: int) -> int:
        return self._adjacent_sums[value]

    def diagonalSum(self, value: int) -> int:
        return self._diagonal_sums[value]


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
