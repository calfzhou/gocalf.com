from heapq import heappop, heappush


class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]

        def dijkstra(src: int, dst: int) -> int:
            dists = [n] * n # dist[u]: the distance from `src` to `dst`.
            dists[src] = 0
            queue = [(0, src)] # A min-heap queue of (dists[u], u)
            while queue:
                dist, u = heappop(queue)
                if u == dst:
                    return dist
                elif dist > dists[u]: # Duplicated vertex in queue.
                    continue

                # Update u's not-done adjacent vertices' distances.
                dist += 1
                for v in graph[u]:
                    if dist < dists[v]:
                        dists[v] = dist
                        heappush(queue, (dists[v], v))

            return n

        min_dis = n
        for u, v in edges:
            if graph[u] and graph[v]:
                dis = dijkstra(u, v)
                if dis == 2:
                    return 3
                elif dis < min_dis:
                    min_dis = dis

            graph[u].append(v)
            graph[v].append(u)

        return min_dis + 1 if min_dis < n else -1
