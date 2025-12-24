class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = a ^ b, (a & b) << 1
            a &= mask # Python specific.
            b &= mask # Python specific.

        if a & 0x80000000:
            a |= ~mask # Python specific.

        return a
