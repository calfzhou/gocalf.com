class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        v = [0] * n
        s = [0] * n
        max_s = 0
        for i in range(m):
            h = 0
            prev_s = 0
            for j in range(n):
                if matrix[i][j] == '0':
                    h = 0
                    v[j] = 0
                    prev_s, s[j] = s[j], 0
                else:
                    h += 1
                    v[j] += 1
                    prev_s, s[j] = s[j], min(prev_s + 1, h, v[j])
                    if s[j] > max_s:
                        max_s = s[j]

        return max_s * max_s
