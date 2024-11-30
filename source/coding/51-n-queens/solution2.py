class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        queens: list[int] = [0] * n # queens[i] = j, means there is a queue in (i, j).
        kill = lambda i: any(queens[r] == queens[i] or abs(r - i) == abs(queens[r] - queens[i]) for r in range(i))

        i = 0
        while queens[0] < n:
            if queens[i] == n:
                i -= 1
                queens[i] += 1
            elif kill(i):
                queens[i] += 1
            elif i < n - 1:
                i += 1
                queens[i] = 0
            else:
                results.append(['Q'.rjust(j+1, '.').ljust(n, '.') for j in queens])
                i -= 1
                queens[i] += 1

        return results
