from heapq import heappop, heappush
from math import inf


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        # times[i][j]: the time from [0][0] to [i][j].
        times: list[list[int]] = [[inf] * n for _ in range(m)]

        # Dijkstra.
        times[0][0] = 0
        queue = [(0, 0, 0)] # A min-heap queue of (times[i][j], i, j)
        while queue:
            # Get the best start vertex u = (ui, uj).
            time, ui, uj = heappop(queue)
            if ui == m - 1 and uj == n - 1:
                return time
            elif time > times[ui][uj]: # Pruning.
                continue

            # Update u's adjacent vertices' distances.
            time += 1
            for di, dj in dirs:
                vi = ui + di
                vj = uj + dj
                if 0 <= vi < m and 0 <= vj < n:
                    time_v = time if grid[vi][vj] <= time else grid[vi][vj] + ((grid[vi][vj] - time) & 1)
                    if time_v < times[vi][vj]:
                        times[vi][vj] = time_v
                        heappush(queue, (time_v, vi, vj))
