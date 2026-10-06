class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row_counts = [sum(row) for row in grid]

        total = 0
        for j in range(n):
            col_count = 0
            server_row = -1
            for i in range(m):
                if grid[i][j]:
                    col_count += 1
                    server_row = i

            if col_count > 1:
                total += col_count
            elif col_count == 1 and row_counts[server_row] > 1:
                total += 1

        return total
