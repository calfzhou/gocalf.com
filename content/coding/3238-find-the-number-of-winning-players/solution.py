class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        win_count = 0
        # color_counts[i]: player i's ball color distribution.
        color_counts: list[dict[int, int]] = {i: {} for i in range(n)}
        max_picks = [0] * n # max_picks[i]: player i's largest count of balls of the same color.
        for i, c in pick:
            if max_picks[i] > i:
                continue

            counts = color_counts[i]
            counts[c] = cnt = counts.get(c, 0) + 1
            if cnt > max_picks[i]:
                max_picks[i] = cnt
                if cnt > i and (win_count := win_count + 1) == n:
                    break

        return win_count
