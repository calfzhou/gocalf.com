class Solution:
    def hammingWeight(self, n: int) -> int:
        table = [
            0, 1, 1, 2,
            1, 2, 2, 3,
            1, 2, 2, 3,
            2, 3, 3, 4,
        ]
        cnt = 0
        while n > 0:
            cnt += table[n & 0x0f]
            n >>= 4

        return cnt
