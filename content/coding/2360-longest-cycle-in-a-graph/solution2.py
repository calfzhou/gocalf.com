class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        n = len(edges)
        max_cycle = -1
        visits = [0] * n # visits[u]: the first time visiting node u.
        time = 1
        for u in range(n):
            if visits[u]: continue

            v = u
            while v >= 0 and not visits[v]:
                visits[v] = time
                time += 1
                v = edges[v]

            if v >= 0 and visits[v] >= visits[u]: # v is visited twice starting from u.
                max_cycle = max2(max_cycle, time - visits[v])

        return max_cycle
