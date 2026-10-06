from collections import defaultdict


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n)) # parent[u]: u's parent node.
        self.depth = [0] * n # depth[u]: the max depth starting from u.

    def find(self, u: int) -> int:
        while self.parent[u] != u: u = self.parent[u]
        return u

    def union(self, u: int, v: int) -> bool:
        ur = self.find(u)
        vr = self.find(v)
        if ur == vr: return False

        if (diff := self.depth[ur] - self.depth[vr]) == 0:
            self.depth[ur] += 1
        elif diff < 0:
            ur, vr = vr, ur # Make sure that depth[ur] >= depth[vr]

        self.parent[vr] = ur
        return True


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        disjoint = DisjointSet(len(favorite))
        followers: dict[int, list[int]] = defaultdict(list) # {v: list of `u`s where u's favorite is v}
        circle_edges: list[tuple[int, int]] = []
        for u, v in enumerate(favorite):
            followers[v].append(u)
            if not disjoint.union(u, v):
                circle_edges.append((u, v))

        def path_length(u: int, v0: int) -> int:
            max_depth = 0
            stack = [(v, 1) for v in followers[u] if v != v0]
            while stack:
                u, depth = stack.pop()
                max_depth = max2(max_depth, depth)
                depth += 1
                for v in followers[u]:
                    stack.append((v, depth))

            return max_depth

        def circle_length(u: int, v: int) -> int:
            length = 1
            while v != u:
                v = favorite[v]
                length += 1

            return length

        largest_circle = 0
        couple_count = 0
        for u, v in circle_edges:
            if favorite[v] == u:
                couple_count += 2 + path_length(u, v) + path_length(v, u)
            else:
                largest_circle = max2(largest_circle, circle_length(u, v))

        return max2(largest_circle, couple_count)
