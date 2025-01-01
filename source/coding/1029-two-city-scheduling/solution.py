class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda c: c[1] - c[0])
        n = len(costs) >> 1
        return sum(costs[i][1] for i in range(n)) + sum(costs[i][0] for i in range(n, n<<1))
