from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        n = len(favorite)
        in_degrees = [0] * n
        for _, v in enumerate(favorite):
            in_degrees[v] += 1

        depths = [0] * n # depths[u]: the max length of acyclic chain point to u.
        zeros = deque(u for u in range(n) if in_degrees[u] == 0)
        while len(zeros):
            u = zeros.popleft()
            v = favorite[u]
            depths[v] = max2(depths[v], depths[u] + 1)
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                zeros.append(v)

        max_cycle = 0
        couple_total = 0
        for u in range(n):
            if in_degrees[u] == 0: continue
            length = 1
            v = favorite[u]
            while v != u:
                in_degrees[v] = 0
                length += 1
                v = favorite[v]

            if length == 2:
                couple_total += length + depths[u] + depths[favorite[u]]
            else:
                max_cycle = max2(max_cycle, length)

        return max2(max_cycle, couple_total)
