from collections import deque
from functools import cache

Player = int
Position = tuple[int, int]
State = tuple[Position, Position, Player] # (mouse position, cat position, current moving player)


class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        _, MOUSE, CAT = range(3)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        winners: dict[State, Player] = {} # state -> winner
        queue: list[State] = deque()

        # Find the initial state.
        m0 = c0 = f0 = (0, 0)
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 'M':
                    m0 = (r, c)
                elif cell == 'C':
                    c0 = (r, c)
                elif cell == 'F':
                    f0 = (r, c)

        @cache
        def prev_states(mouse: Position, cat: Position, moving: Player) -> list[State]:
            states = []
            if moving == MOUSE:
                states.append((mouse, cat, CAT))
                for dr, dc in dirs:
                    r, c = cat
                    for _ in range(catJump):
                        r -= dr
                        c -= dc
                        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '#':
                            break
                        states.append((mouse, (r, c), CAT))
            else:
                states.append((mouse, cat, MOUSE))
                for dr, dc in dirs:
                    r, c = mouse
                    for _ in range(mouseJump):
                        r -= dr
                        c -= dc
                        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '#':
                            break
                        states.append(((r, c), cat, MOUSE))

            return states

        def move_cnt(mouse: Position, cat: Position, moving: Player) -> int:
            cnt = 1 # 1 for staying at the same position
            if moving == MOUSE:
                for dr, dc in dirs:
                    r, c = mouse
                    for _ in range(mouseJump):
                        r += dr
                        c += dc
                        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '#':
                            break
                        cnt += 1
            else:
                for dr, dc in dirs:
                    r, c = cat
                    for _ in range(catJump):
                        r += dr
                        c += dc
                        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '#':
                            break
                        cnt += 1

            return cnt

        # Known winning states.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '#':
                    continue

                state = (f0, (r, c), CAT)
                winners[state] = MOUSE
                queue.append(state)

                state = ((r, c), f0, MOUSE)
                winners[state] = CAT
                queue.append(state)

                for moving in (MOUSE, CAT):
                    state = ((r, c), (r, c), moving)
                    winners[state] = CAT
                    queue.append(state)

        initial = (m0, c0, MOUSE)
        doubt_moves: dict[State, int] = {} # state -> number of remaining undetermined moves

        while queue:
            state = queue.popleft()
            winner = winners[state]
            if winner == state[2]:
                for p_state in prev_states(*state):
                    if p_state in winners: continue
                    if p_state not in doubt_moves: doubt_moves[p_state] = move_cnt(*p_state)
                    doubt_moves[p_state] -= 1
                    if doubt_moves[p_state] == 0:
                        if p_state == initial: return winner == MOUSE
                        winners[p_state] = winner
                        queue.append(p_state)
            else:
                for p_state in prev_states(*state):
                    if p_state in winners: continue
                    if p_state == initial: return winner == MOUSE
                    winners[p_state] = winner
                    queue.append(p_state)

        return False # DRAW
