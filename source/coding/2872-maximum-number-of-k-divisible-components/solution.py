class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        tree = [[] for _ in range(n)] # tree[u]: u's neighbors.
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        cnt = 0
        stack = [(-1, 0, False)] # (parent, node, children done)
        while stack:
            p, u, ready = stack.pop()
            if ready:
                for v in tree[u]:
                    if v != p: values[u] += values[v]
                if values[u] % k == 0:
                    cnt += 1
            else:
                stack.append((p, u, True))
                for v in tree[u]:
                    if v != p: stack.append((u, v, False))

        return cnt
