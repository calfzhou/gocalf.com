from heapq import heappop, heappush
from math import inf


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, left, down, up.
        m = len(grid)
        n = len(grid[0])
        # dists[i][j] is the distance from (0, 0) to (i, j).
        dists: list[list[int]] = [[inf] * n for _ in range(m)]

        # Dijkstra's algorithm.
        dists[0][0] = 0
        queue = [(0, 0, 0)] # A min-heap queue of (dists[i][j], i, j).
        while queue:
            # Get the best start vertex u = (ui, uj).
            dist, ui, uj = heappop(queue)
            if ui == m - 1 and uj == n - 1:
                return dist
            elif dists[ui][uj] < dist:
                continue

            for k, (di, dj) in enumerate(dirs, 1):
                vi, vj = ui + di, uj + dj
                if 0 <= vi < m and 0 <= vj < n:
                    new_dist = dist + (grid[ui][uj] != k)
                    if new_dist < dists[vi][vj]:
                        dists[vi][vj] = new_dist
                        heappush(queue, (new_dist, vi, vj))
