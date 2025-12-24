class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b
        row_0_point = sum(grid[0]) - grid[0][0]
        row_1_point = 0
        min_robot2_point = row_0_point
        for i in range(1, len(grid[0])):
            row_0_point -= grid[0][i]
            row_1_point += grid[1][i-1]
            min_robot2_point = min2(min_robot2_point, max2(row_0_point, row_1_point))

        return min_robot2_point
