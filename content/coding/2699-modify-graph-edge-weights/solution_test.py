from collections import defaultdict
from heapq import heappop, heappush
from math import inf
import pytest

from solution import Solution


@pytest.mark.parametrize('n, edges, source, destination, target, expected', [
    (
        5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5,
        [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
    ),
    (
        3, [[0,1,-1],[0,2,5]], 0, 2, 6,
        []
    ),
    (
        4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6,
        [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
    ),

    (
        4, [[0,1,5],[1,2,7],[2,3,7],[3,1,9],[3,0,-1],[0,2,-1]], 2, 3, 7,
        [[0,1,5],[1,2,7],[2,3,7],[3,1,9],[3,0,1000000005],[0,2,6]]
    ),
    (
        4, [[0,1,1],[1,2,2],[2,3,3]], 0, 2, 1,
        []
    ),

    (
        4, [[0,1,-1], [1,2,-1], [2,3,1], [1,3,5]], 3, 0, 10,
        [[0,1,1], [1,2,8], [2,3,1], [1,3,5]]
    ),
    (
        4, [[0,1,-1], [1,2,-1], [2,3,1], [1,3,5]], 0, 3, 10,
        [[0,1,8], [1,2,1], [2,3,1], [1,3,5]]
    ),
])
class Test:
    def test_solution(self, n, edges, source, destination, target, expected):
        sol = Solution()
        res = sol.modifiedGraphEdges(n, edges.copy(), source, destination, target)
        res = self._sort(res)
        expected = self._sort(expected)
        if res != expected:
            edges = self._sort(edges)
            self._verify(n, edges, source, destination, target, res)

    def _sort(self, edges):
        return sorted((*sorted(e[:2]), e[2]) for e in edges)

    def _verify(self, n, origin, source, destination, target, result):
        assert len(result) == len(origin)
        for r, o in zip(result, origin):
            if o[2] == -1:
                assert r[:2] == o[:2]
                assert r[2] > 0
            else:
                assert r == o

        graph = defaultdict(dict)
        for u, v, w in result:
            graph[u][v] = graph[v][u] = w if w > 0 else inf

        # Dijkstra.
        dists = [inf] * n # dist[u]: the distance from source to u.
        dists[source] = 0
        queue = [(0, source)] # A min-heap queue of (dists[u], u)
        while queue:
            dist, u = heappop(queue)
            if u == destination:
                assert dist == target
                return
            elif dist > dists[u]: # Duplicated vertex in queue.
                continue

            # Update u's not-done adjacent vertices' distances.
            for v, w in graph[u].items():
                if dist + w < dists[v]:
                    dists[v] = dist + w
                    heappush(queue, (dists[v], v))

        assert False # `destination` is not reachable from`source`.
