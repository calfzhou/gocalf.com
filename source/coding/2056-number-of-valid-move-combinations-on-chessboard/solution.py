from collections import defaultdict


class Solution:
    def countCombinations(self, pieces: list[str], positions: list[list[int]]) -> int:
        m = 8
        n = len(pieces)
        passing: dict[tuple[int, int], set[int]] = defaultdict(set) # (row, col): {pass-by time}
        parking: dict[tuple[int, int], int] = {} # (row, col): stay here from when
        dirs = {
            'rook': ((-1,0), (1,0), (0,-1), (0,1)), # ↑ ↓ ← →
            'bishop': ((-1,-1), (-1,1), (1,-1), (1,1)), # ↖ ↗ ↙ ↘
        }
        dirs['queen'] = dirs['rook'] + dirs['bishop']

        def dfs(k: int) -> int:
            if k == n:
                return 1

            cnt = 0
            r, c = positions[k]
            if not passing[(r, c)]: # Stay here won't block pieces[0:k] pass by.
                passing[(r, c)].add(0)
                parking[(r, c)] = 0
                cnt += dfs(k + 1)
                del parking[(r, c)]

            for dr, dc in dirs[pieces[k]]:
                t = 0
                r, c = positions[k]
                passing[(r, c)].add(t)
                while True:
                    t += 1
                    r += dr
                    c += dc
                    if not (1 <= r <= m and 1 <= c <= m): # Out of board.
                        break
                    if t in passing[(r, c)] or parking.get((r, c), m) <= t: # Blocked by pieces[0:k].
                        break

                    if all(t1 < t for t1 in passing[(r, c)]): # Stay here won't block pieces[0:k] pass by.
                        passing[(r, c)].add(t)
                        parking[(r, c)] = t
                        cnt += dfs(k + 1)
                        del parking[(r, c)]
                    else:
                        passing[(r, c)].add(t) # Pass but not stay.

                r0, c0 = positions[k]
                while r != r0 or c != c0:
                    t -= 1
                    r -= dr
                    c -= dc
                    passing[(r, c)].remove(t)

            return cnt

        return dfs(0)
