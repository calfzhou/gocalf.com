from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        po = m * n # Pacific Ocean
        ao = po + 1 # Atlantic Ocean
        adjacencies: list[list[int]] = [[] for _ in range(ao + 1)]

        # Build the graph (using adjacency list).
        idx = 0
        for i, row in enumerate(heights):
            for j, h in enumerate(row):
                if i == 0 or j == 0:
                    adjacencies[po].append(idx)
                if i == m - 1 or j == n - 1:
                    adjacencies[ao].append(idx)

                if i > 0 and heights[i-1][j] <= h:
                    adjacencies[idx - n].append(idx)
                if i < m - 1 and heights[i+1][j] <= h:
                    adjacencies[idx + n].append(idx)
                if j > 0 and heights[i][j-1] <= h:
                    adjacencies[idx - 1].append(idx)
                if j < n - 1 and heights[i][j+1] <= h:
                    adjacencies[idx + 1].append(idx)

                idx += 1

        # Find Pacific Ocean and Atlantic Ocean's reachable vertices.
        po_cells = self._traverse_reachable(adjacencies, po)
        ao_cells = self._traverse_reachable(adjacencies, ao)

        # Calc the intersect of the two oceans' reachable vertices, in 2d coordinate format.
        return [[*divmod(v, n)] for v in po_cells & ao_cells]

    def _traverse_reachable(self, adjacencies: list[list[int]], root: int) -> set[int]:
        reachable = set()
        stack = [root]
        while stack:
            vertex = stack.pop()
            neighbors = [v for v in adjacencies[vertex] if v not in reachable]
            stack.extend(neighbors)
            reachable.update(neighbors)

        return reachable
