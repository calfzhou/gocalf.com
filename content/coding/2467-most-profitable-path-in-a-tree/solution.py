class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        tree = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs_bob(node: int, parent: int) -> bool:
            if node == bob:
                bob_path.append(node)
                return True

            for child in tree[node]:
                if child != parent and dfs_bob(child, node):
                    bob_path.append(node)
                    return True

            return False

        bob_path = []
        dfs_bob(0, -1)
        h = len(bob_path)
        for i in range(h // 2):
            amount[bob_path[i]] = 0
        if h % 2 == 1:
            amount[bob_path[i + 1]] //= 2

        def dfs(node: int, parent: int) -> int:
            return amount[node] + max((dfs(child, node) for child in tree[node] if child != parent), default=0)

        return dfs(0, -1)
