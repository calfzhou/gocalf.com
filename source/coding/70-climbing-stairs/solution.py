class Solution:
    def climbStairs(self, n: int) -> int:
        pp, p = 0, 1
        for _ in range(1, n + 1):
            pp, p = p, p + pp

        return p
