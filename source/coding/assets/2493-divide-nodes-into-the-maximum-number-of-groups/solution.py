from collections import deque


class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        max2 = lambda a, b: a if a >= b else b
        graph: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        # Checks if the graph is bipartite.
        colors = [-1] * n
        for u in range(n):
            if colors[u] >= 0: continue
            colors[u] = 0
            stack = [u]
            while stack:
                u = stack.pop()
                cu = colors[u]
                cv = 1 - cu
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = cv
                        stack.append(v)
                    elif colors[v] == cu:
                        return -1

        def bfs_depth(u: int) -> int:
            """Returns the max (0-indexed) depth starting from `u`."""
            visited = [False] * n
            visited[u] = True
            queue = deque([u])
            depth = -1
            while queue:
                depth += 1
                for _ in range(len(queue)): # Process the whole layer together. All these nodes have the same depth.
                    u = queue.popleft()
                    for v in graph[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)

            return depth

        def diameter(u: int) -> int:
            """Returns the diameter of sub-graph contains `u`.
            Which is the max bfs-depth starting from every node of the sub-graph."""
            finished[u] = True
            stack = [u]
            d = 0
            while stack:
                u = stack.pop()
                d = max2(d, bfs_depth(u))
                for v in graph[u]:
                    if not finished[v]:
                        finished[v] = True
                        stack.append(v)

            return d

        group_cnt = 0
        finished = [False] * n
        for u in range(n):
            if finished[u]: continue
            group_cnt += diameter(u) + 1

        return group_cnt
