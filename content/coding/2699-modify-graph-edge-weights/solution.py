from collections import defaultdict
from heapq import heappop, heappush
from math import inf


class Solution:
    def modifiedGraphEdges(self, n: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:
        MAX = 2_000_000_000
        graph = defaultdict(dict)
        modifies = set()
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
            if w < 0: modifies.add((u, v) if u < v else (v, u))

        def dijkstra(re_weight: int) -> tuple[list[int], list[int]]:
            dists = [inf] * n # dist[u]: the distance from `source` to u.
            predecessors = [None] * n # predecessors[u]: u's previous vertex in the shortest path.
            dists[source] = 0
            queue = [(0, source)] # A min-heap queue of (dists[u], u)
            while queue:
                dist, u = heappop(queue)
                if u == destination:
                    break
                elif dist > dists[u]: # Duplicated vertex in queue.
                    continue

                # Update u's not-done adjacent vertices' distances.
                for v, w in graph[u].items():
                    if w < 0: w = re_weight
                    if dist + w < dists[v]:
                        dists[v] = dist + w
                        predecessors[v] = u
                        heappush(queue, (dists[v], v))

            return dists, predecessors

        dist = dijkstra(inf)[0][destination]
        if dist < target:
            return []
        elif dist == target:
            return [[u, v, MAX if w < 0 else w] for u, v, w in edges]
        elif not modifies:
            return []

        while modifies:
            dists, predecessors = dijkstra(1)
            if (gap := target - dists[destination]) < 0:
                return []
            elif gap == 0:
                break

            in_path = set() # intersection(modifies, the shortest path)
            v = destination
            u = predecessors[v]
            while u is not None:
                if graph[u][v] < 0:
                    in_path.add((u, v) if u < v else (v, u))
                u, v = predecessors[u], u

            for u, v in modifies - in_path:
                graph[u][v] = graph[v][u] = MAX

            modifies = in_path
            u, v = modifies.pop()
            graph[u][v] = graph[v][u] = 1 + gap

        return [[u, v, abs(graph[u][v])] for u, v, _ in edges]
