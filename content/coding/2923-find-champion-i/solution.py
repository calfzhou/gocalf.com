class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        for i, row in enumerate(grid):
            if row.count(0) == 1:
                return i
