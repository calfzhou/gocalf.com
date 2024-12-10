MOD = 1_000_000_007


def prod(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    # `a` is an m*k matrix, `b` is a k*n matrix.
    # Returns a m*n matrix which is a x b.
    m = len(a)
    k = len(b)
    n = len(b[0])
    res = [[sum(a[r][i] * b[i][c] for i in range(k)) % MOD for c in range(n)] for r in range(m)]
    return res


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10

        n -= 1
        mask = 1
        n1 = n
        while n1 := n1 >> 1:
            mask <<= 1

        m = [[0, 1, 1, 0], [2, 0, 0, 0], [2, 0, 0, 1], [0, 0, 2, 0]]
        res = m
        while mask := mask >> 1:
            res = prod(res, res)
            if n & mask:
                res = prod(res, m)

        m0 = [[1], [1], [1], [1]]
        k = [[4, 2, 2, 1]]
        res = prod(k, prod(res, m0))
        return res[0][0] % MOD
