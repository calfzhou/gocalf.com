from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        answers = []
        colors: dict[int, int] = {} # colors[idx] means the color of the idx-th ball
        counts: dict[int, int] = defaultdict(int) # counts[color] means the number of balls with color `color`
        for idx, color in queries:
            counts[color] += 1
            if idx in colors:
                old_color = colors[idx]
                counts[old_color] -= 1
                if counts[old_color] == 0:
                    del counts[old_color]

            colors[idx] = color
            answers.append(len(counts))

        return answers
