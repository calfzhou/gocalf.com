from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # adjacencies[u]: list of (v, w).
        adjacencies: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in times:
            adjacencies[u-1].append((v-1, w))

        costs = [-1] * n
        costs[k-1] = 0
        queue = [(0, k-1)]
        while queue:
            c_u, u = heappop(queue)
            if c_u > costs[u]: # Pruning.
                continue

            for v, w in adjacencies[u]:
                if (c_v := costs[u] + w) < costs[v] or costs[v] == -1:
                    costs[v] = c_v
                    heappush(queue, (c_v, v))

        max_cost = -1
        for c in costs:
            if c == -1:
                return -1
            elif c > max_cost:
                max_cost = c

        return max_cost
