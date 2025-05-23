class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []
        q: list[int] = [0] * n # q[i] = j, means there is a queue in (i, j).
        cols = [False] * n
        slashes = [False] * ((n<<1) - 1)
        backslashes = list(slashes)

        i = 0
        while q[0] < n:
            if q[i] == n:
                i -= 1
                cols[q[i]] = slashes[i+q[i]] = backslashes[i-q[i]] = False
                q[i] += 1
            elif any((cols[q[i]], slashes[i+q[i]], backslashes[i-q[i]])):
                q[i] += 1
            elif i < n - 1:
                cols[q[i]] = slashes[i+q[i]] = backslashes[i-q[i]] = True
                i += 1
                q[i] = 0
            else:
                results.append(['Q'.rjust(j+1, '.').ljust(n, '.') for j in q])
                i -= 1
                cols[q[i]] = slashes[i+q[i]] = backslashes[i-q[i]] = False
                q[i] += 1

        return results
