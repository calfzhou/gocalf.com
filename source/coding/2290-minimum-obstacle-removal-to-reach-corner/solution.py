from heapq import heappop, heappush
from math import inf


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        # dists[i][j]: the distance from [0][0] to [i][j].
        dists: list[list[int]] = [[inf] * n for _ in range(m)]

        # Dijkstra.
        dists[0][0] = 0
        queue = [(0, 0, 0)] # A min-heap queue of (dists[i][j], i, j)
        while queue:
            # Get the best start vertex u = (ui, uj).
            dist, ui, uj = heappop(queue)
            if ui == m - 1 and uj == n - 1:
                return dist >> 1
            elif dist > dists[ui][uj]: # Duplicated vertex in queue.
                continue

            # Update u's not-done adjacent vertices' distances.
            dist += grid[ui][uj]
            for di, dj in dirs:
                vi = ui + di
                vj = uj + dj
                if 0 <= vi < m and 0 <= vj < n and dist + grid[vi][vj] < dists[vi][vj]:
                    dists[vi][vj] = dist + grid[vi][vj]
                    heappush(queue, (dists[vi][vj], vi, vj))
