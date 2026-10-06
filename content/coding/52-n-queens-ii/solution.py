class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        slashes = [False] * ((n<<1) - 1)
        backslashes = list(slashes)

        def backtrack(i: int) -> int:
            if i == n:
                return 1

            cnt = 0
            for j in range(n):
                if any((cols[j], slashes[i+j], backslashes[i-j])): continue
                cols[j] = slashes[i+j] = backslashes[i-j] = True
                cnt += backtrack(i + 1)
                cols[j] = slashes[i+j] = backslashes[i-j] = False

            return cnt

        return backtrack(0)
