class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        queens: list[int] = [None] * n # queens[i] = j, means there is a queue in (i, j).
        remains = set(range(n))
        kill = lambda i, j: any(abs(r - i) == abs(queens[r] - j) for r in range(i))

        def backtrace(i: int):
            if i == n:
                results.append(['Q'.rjust(j+1, '.').ljust(n, '.') for j in queens])
                return

            for j in range(n):
                if j not in remains or kill(i, j): continue
                queens[i] = j
                remains.remove(j)
                backtrace(i + 1)
                remains.add(j)

        backtrace(0)
        return results
