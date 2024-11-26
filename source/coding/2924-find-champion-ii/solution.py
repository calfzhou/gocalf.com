class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        weak = [False] * n
        for _, v in edges:
            weak[v] = True

        champion = -1
        for u, is_weak in enumerate(weak):
            if not is_weak:
                if champion >= 0:
                    return -1
                champion = u

        return champion
