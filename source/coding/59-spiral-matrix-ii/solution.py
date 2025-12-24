class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0)) # →, ↓, ←, ↑
        limits = [n, n - 1] # ↔︎, ↕
        i = 0
        j = -1
        dir = 0
        move = 0
        for idx in range(1, n * n + 1):
            i += steps[dir][0]
            j += steps[dir][1]
            matrix[i][j] = idx
            move += 1
            if move == limits[dir & 1]:
                limits[dir & 1] -= 1
                dir = (dir + 1) % 4
                move = 0

        return matrix
