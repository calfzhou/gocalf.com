class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        MOD = 1_000_000_007
        cnts = [1] * 4
        tmp = [0] * 4
        for _ in range(n - 1):
            tmp[0] = (cnts[1] + cnts[2]) % MOD # Digits 1, 3, 7, 9.
            tmp[1] = (cnts[0] << 1) % MOD # Digits 2, 8.
            tmp[2] = (tmp[1] + cnts[3]) % MOD # Digits 4, 6.
            tmp[3] = (cnts[2] << 1) % MOD # Digit 0.
            cnts, tmp = tmp, cnts

        return sum((cnts[0] << 2, cnts[1] << 1, cnts[2] << 1, cnts[3])) % MOD
