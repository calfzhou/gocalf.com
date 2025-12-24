class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        max2 = lambda a, b: a if a >= b else b
        areas = [0, 0] # areas[idx] = area of island idx
        n = len(grid)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        idx = 2
        max_area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 1:
                    continue

                area = 1
                grid[i][j] = idx
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            area += 1
                            grid[nr][nc] = idx
                            stack.append((nr, nc))

                areas.append(area)
                idx += 1
                max_area = max2(max_area, area)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = set()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            neighbors.add(grid[nr][nc])

                    max_area = max2(max_area, 1 + sum(areas[idx] for idx in neighbors))

        return max_area
