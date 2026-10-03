class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        counts = [0, 0]
        idx = 0
        while n > 0:
            if n & 1:
                counts[idx] += 1
            n >>= 1
            idx = 1 - idx

        return counts
