from collections import defaultdict
from math import ceil


def dfs(tree: dict[int, list[int]], u: int) -> tuple[int, int]:
    """Finds the farthest node from u, and the distance between them."""
    visited = [False] * len(tree)
    farthest = u, 0
    stack = [farthest] # (node, depth)
    while stack:
        u, d = stack.pop()
        if visited[u]: continue
        visited[u] = True
        if d > farthest[1]:
            farthest = u, d

        d += 1
        for v in tree[u]:
            if not visited[v]: stack.append((v, d))

    return farthest


def diameter(edges: list[list[int]]) -> int:
    if not edges: return 0
    tree: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    u, _ = dfs(tree, 0)
    _, d = dfs(tree, u)
    return d


class Solution:
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        ds = list(map(diameter, (edges1, edges2)))
        return max(ds[0], ds[1], 1 + ceil(ds[0] / 2) + ceil(ds[1] / 2))
