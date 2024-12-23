from collections import defaultdict


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n)) # parent[u]: u's parent node.
        self.depth = [0] * n # depth[u]: the max depth starting from u.

    def find(self, u: int) -> int:
        while self.parent[u] != u: u = self.parent[u]
        return u

    def union(self, u: int, v: int) -> None:
        ur = self.find(u)
        vr = self.find(v)
        # if ur == vr: return False

        if (diff := self.depth[ur] - self.depth[vr]) == 0:
            self.depth[ur] += 1
        elif diff < 0:
            ur, vr = vr, ur # Make sure that depth[ur] >= depth[vr]

        self.parent[vr] = ur
        # return True


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        indexing: dict[str, int] = {} # {email: account id}
        disjoint = DisjointSet(len(accounts))
        for uid, emails in enumerate(accounts):
            for j in range(1, len(emails)):
                email = emails[j]
                if email not in indexing:
                    indexing[email] = uid
                else:
                    disjoint.union(uid, indexing[email])

        merged: dict[int, list[str]] = defaultdict(list)
        for email, uid in indexing.items():
            uid = disjoint.find(uid)
            merged[uid].append(email)

        return [[accounts[uid][0], *sorted(emails)] for uid, emails in merged.items()]
