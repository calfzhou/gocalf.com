class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        max2 = lambda a, b: a if a >= b else b
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_fish = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                fish = grid[i][j]
                grid[i][j] = 0
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                            fish += grid[nr][nc]
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                max_fish = max2(max_fish, fish)

        return max_fish
