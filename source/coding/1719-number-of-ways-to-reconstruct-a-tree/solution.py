from collections import defaultdict


class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        graph: dict[int, set[int]] = defaultdict(set) # x: set of `y`s, where [x, y] or [y, x] in pairs.
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)

        if len(graph) - 1 > max(len(buddies) for buddies in graph.values()):
            return 0 # No root.

        ways = 1
        tasks = [graph]
        while tasks:
            graph = tasks.pop()
            root = max(graph, key=lambda x: len(graph[x]))
            nodes = graph.pop(root)
            sub = {}
            for x in nodes:
                buddies = graph.pop(x)
                buddies.remove(root)
                if buddies - nodes:
                    return 0 # `root`'s child has connection outside the root's tree.
                sub[x] = buddies
            if graph: tasks.append(graph)

            n = len(sub) - 1
            roots = [x for x, buddies in sub.items() if len(buddies) == n]
            if roots: ways = 2

            for x in roots:
                del sub[x]
            for buddies in sub.values():
                buddies.difference_update(roots)
            for x in [x for x, buddies in sub.items() if not buddies]:
                del sub[x]

            if sub: tasks.append(sub)

        return ways
