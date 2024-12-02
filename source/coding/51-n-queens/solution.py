class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        queens: list[int] = [None] * n # queens[i] = j, means there is a queue in (i, j).
        cols = [False] * n
        slashes = [False] * ((n<<1) - 1)
        backslashes = list(slashes)

        def backtrace(i: int):
            if i == n:
                results.append(['Q'.rjust(j+1, '.').ljust(n, '.') for j in queens])
                return

            for j in range(n):
                if any((cols[j], slashes[i+j], backslashes[i-j])): continue
                queens[i] = j
                cols[j] = slashes[i+j] = backslashes[i-j] = True
                backtrace(i + 1)
                cols[j] = slashes[i+j] = backslashes[i-j] = False

        backtrace(0)
        return results
