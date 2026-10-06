from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        counter: dict[tuple[int], int] = defaultdict(int)
        for row in matrix:
            if row[0]:
                key = tuple(row)
            else:
                key = tuple(1 - x for x in row)
            counter[key] += 1

        return max(counter.values())
