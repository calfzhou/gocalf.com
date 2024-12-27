class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [-1] * len(graph)

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
                        return False

        return True
