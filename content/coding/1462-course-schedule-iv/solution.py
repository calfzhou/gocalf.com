class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        graph: list[list[int]] = [[] for _ in range(n)]
        for u, v in prerequisites:
            graph[u].append(v)

        downstream: list[set[int]] = [set() for _ in range(n)]

        def dfs(u: int) -> set[int]:
            for v in graph[u]:
                if v not in downstream[u]:
                    downstream[u].add(v)
                    downstream[u] |= dfs(v)

            return downstream[u]

        for u in range(n):
            dfs(u)

        return [v in downstream[u] for u, v in queries]
