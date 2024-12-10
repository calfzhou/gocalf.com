class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 1_000_000_007
        srcs = [(4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4)]
        cnts = [1] * 10
        tmp = [0] * 10
        for _ in range(n - 1):
            for d, src in enumerate(srcs):
                tmp[d] = sum(cnts[s] for s in src) % MOD
            cnts, tmp = tmp, cnts

        return sum(cnts) % MOD
