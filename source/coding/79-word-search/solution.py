class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def find(r: int, c: int, k: int) -> bool:
            if not (0 <= r < m and 0 <= c < n and board[r][c] == word[k]):
                return False
            if k == w - 1:
                return True

            backup = board[r][c]
            board[r][c] = '' # Avoid reuse the same cell.
            found = any(find(r + dr, c + dc, k + 1) for dr, dc in dirs)
            board[r][c] = backup
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 0):
                    return True

        return False
