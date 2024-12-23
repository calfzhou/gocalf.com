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
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)

        bad = None
        parents: dict[int, int] = {} # v: u, where (u, v) is an edge.
        for e in edges:
            if e[1] in parents:
                bad = e
                break
            parents[e[1]] = e[0]

        loop = None
        disjoint = DisjointSet(n)
        for e in edges:
            if e == bad: continue # Important!
            if not disjoint.union(e[0] - 1, e[1] - 1):
                loop = e
                break

        if not loop:
            return bad
        elif not bad:
            return loop
        else:
            return [parents[bad[1]], bad[1]]
