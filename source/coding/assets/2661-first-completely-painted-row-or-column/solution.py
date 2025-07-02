class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        mn = m * n
        indices = [(0, 0)] * (mn + 1)
        for r in range(m):
            for c in range(n):
                indices[mat[r][c]] = (r, c)

        rows = [n] * m
        cols = [m] * n
        for i, num in enumerate(arr):
            r, c = indices[num]
            rows[r] -= 1
            if rows[r] == 0:
                return i
            cols[c] -= 1
            if cols[c] == 0:
                return i
