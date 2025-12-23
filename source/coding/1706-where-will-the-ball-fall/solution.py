class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        n = len(grid[0])
        result = []
        for src in range(n):
            for row in grid:
                dest = src + row[src]
                if dest < 0 or dest >= n or row[dest] != row[src]:
                    result.append(-1)
                    break
                src = dest
            else:
                result.append(src)

        return result
