from collections import deque


class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        n = len(edges)
        in_degrees = [0] * n
        for _, v in enumerate(edges):
            if v >= 0: in_degrees[v] += 1

        zeros = deque(u for u in range(n) if in_degrees[u] == 0)
        while len(zeros):
            u = zeros.popleft()
            v = edges[u]
            if v < 0: continue
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                zeros.append(v)

        max_cycle = -1
        for u in range(n):
            if in_degrees[u] == 0: continue
            length = 1
            v = edges[u]
            while v != u:
                in_degrees[v] = 0
                length += 1
                v = edges[v]

            max_cycle = max2(max_cycle, length)

        return max_cycle
