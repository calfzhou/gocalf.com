from collections import deque
from typing import Iterable

Player = int
State = tuple[int, int, Player] # (mouse position, cat position, current moving player)


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        DRAW, MOUSE, CAT = range(3)
        n = len(graph)
        winners: dict[State, Player] = {} # {state: winner}
        queue: list[State] = deque()

        # All determined states.
        for i in range(1, n):
            state = (0, i, CAT)
            winners[state] = MOUSE
            queue.append(state)

            for moving in (MOUSE, CAT):
                state = (i, i, moving)
                winners[state] = CAT
                queue.append(state)

        def prev_states(mouse: int, cat: int, moving: Player) -> Iterable[State]:
            if moving == MOUSE:
                for node in graph[cat]:
                    if node > 0:
                        yield mouse, node, CAT
            else:
                for node in graph[mouse]:
                    yield node, cat, MOUSE

        def move_cnt(mouse: int, cat: int, moving: Player) -> int:
            if moving == MOUSE:
                return len(graph[mouse])
            else:
                return sum(1 for node in graph[cat] if node > 0)

        initial = (1, 2, MOUSE)
        doubt_moves: dict[State, int] = {} # {state: the number of undetermined moves remaining}

        while queue:
            state = queue.popleft()
            winner = winners[state]
            if winner == state[2]:
                for p_state in prev_states(*state):
                    if p_state in winners: continue
                    if p_state not in doubt_moves: doubt_moves[p_state] = move_cnt(*p_state)
                    doubt_moves[p_state] -= 1
                    if doubt_moves[p_state] == 0:
                        if p_state == initial: return winner
                        winners[p_state] = winner
                        queue.append(p_state)
            else:
                for p_state in prev_states(*state):
                    if p_state in winners: continue
                    if p_state == initial: return winner
                    winners[p_state] = winner
                    queue.append(p_state)

        return DRAW
