from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = [0] * (m * n)

        steps = ((0, 1), (1, 0), (0, -1), (-1, 0)) # →, ↓, ←, ↑
        limits = [n, m - 1] # ↔︎, ↕
        i = 0
        j = -1
        dir = 0
        move = 0
        for idx in range(m * n):
            i += steps[dir][0]
            j += steps[dir][1]
            res[idx] = matrix[i][j]
            move += 1
            if move == limits[dir & 1]:
                limits[dir & 1] -= 1
                dir = (dir + 1) % 4
                move = 0

        return res
