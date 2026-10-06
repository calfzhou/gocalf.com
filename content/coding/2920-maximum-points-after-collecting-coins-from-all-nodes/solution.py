class Solution:
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        tree: list[list[int]] = [[] for _ in range(len(coins))]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        MAX = 14 # (10**4).bit_length() or max(coins).bit_length()
        max2 = lambda a, b: a if a >= b else b

        def dfs(root: int, parent: int) -> list[int]:
            points = [0] * MAX
            for child in tree[root]:
                if child != parent:
                    child_points = dfs(child, root)
                    for i, point in enumerate(child_points):
                        if point == 0:
                            break
                        points[i] += point

            coin = coins[root]
            for i in range(MAX - 1):
                p1 = coin - k + points[i]
                coin >>= 1
                p2 = coin + points[i + 1]
                points[i] = max2(p1, p2)
            points[-1] = coin - k
            return points

        return dfs(0, -1)[0]
