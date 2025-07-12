from collections import deque


class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(u: int) -> int:
            depths = [-1] * n # >= 0 means visited.
            queue = deque()
            queue.append((u, u)) # (prev node, node)
            while len(queue):
                p, u = queue.popleft()
                if depths[u] >= 0: continue
                depths[u] = depths[p] + 1
                for v in graph[u]:
                    if v == p: continue
                    if depths[v] >= 0: return depths[u] + depths[v] + 1
                    queue.append((u, v))

            return -1

        min_cycle = -1
        for u in range(n):
            cycle = bfs(u)
            if cycle > 0 and (min_cycle == -1 or min_cycle > cycle):
                min_cycle = cycle

        return min_cycle
