class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        n = len(board)
        r0, c0 = next((r, c) for r in range(n) for c in range(n) if board[r][c] == 'R')
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cnt = 0
        for dr, dc in dirs:
            r, c = r0, c0
            while True:
                r += dr
                c += dc
                if not (0 <= r < n and 0 <= c < n):
                    break
                elif board[r][c] == 'p':
                    cnt += 1
                    break
                elif board[r][c] != '.':
                    break

        return cnt
