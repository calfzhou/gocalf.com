class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == '0':
                    continue

                cnt += 1
                grid[i][j] = '0'
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    if r > 0 and grid[r-1][c] == '1':
                        grid[r-1][c] = '0'
                        stack.append((r-1, c))
                    if r < m-1 and grid[r+1][c] == '1':
                        grid[r+1][c] = '0'
                        stack.append((r+1, c))
                    if c > 0 and grid[r][c-1] == '1':
                        grid[r][c-1] = '0'
                        stack.append((r, c-1))
                    if c < n-1 and grid[r][c+1] == '1':
                        grid[r][c+1] = '0'
                        stack.append((r, c+1))

        return cnt
