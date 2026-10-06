def prod(a, b): return ((
    a[0][0] * b[0][0] + a[0][1] * b[1][0],
    a[0][0] * b[0][1] + a[0][1] * b[1][1],
), (
    a[1][0] * b[0][0] + a[1][1] * b[1][0],
    a[1][0] * b[0][1] + a[1][1] * b[1][1],
))


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        mask = 1
        n1 = n
        while n1 := n1 >> 1:
            mask <<= 1

        m = ((1, 1), (1, 0))
        res = m
        while mask := mask >> 1:
            res = prod(res, res)
            if n & mask:
                res = prod(res, m)

        return res[0][0]
