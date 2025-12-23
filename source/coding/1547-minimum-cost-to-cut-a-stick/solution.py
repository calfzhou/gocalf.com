from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts_ex = [0, *sorted(cuts), n]
        costs = [[0] * (m + 1) for _ in range(m + 1)]
        for c in range(1, m + 1): # m: number of cut points between p and q.
            for p in range(0, m + 1 - c):
                q = p + c + 1
                cost = min(costs[p][p+r-1] + costs[p+r][q-1] for r in range(1, c + 1))
                cost += cuts_ex[q] - cuts_ex[p]
                costs[p][q-1] = cost

        return costs[0][m]
