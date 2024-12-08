class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)
        cnt = 0

        # Check first row / column.
        for b in (lambda c: board[0][c], lambda r: board[r][0]):
            one = zero = 0 # The number of `1` and `0`s.
            wrong = 0 # The number of mis-placed `1` or `0`s.
            for j in range(n):
                v = b(j)
                one += v
                zero += 1 - v
                wrong += v ^ (j & 1)

            if not -1 <= one - zero <= 1:
                return -1

            if one > zero or one == zero and n - wrong < wrong:
                wrong = n - wrong

            cnt += wrong >> 1

        # Check whether other rows same with or complementary to the first row.
        for i in range(1, n):
            first = board[i][0] ^ board[0][0]
            for j in range(1, n):
                if board[i][j] ^ board[0][j] != first:
                    return -1

        return cnt
