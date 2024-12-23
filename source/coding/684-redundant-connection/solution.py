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
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        disjoint = DisjointSet(len(edges))
        for u, v in edges:
            if not disjoint.union(u - 1, v - 1):
                return [u, v]
