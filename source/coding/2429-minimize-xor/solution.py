class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b2 = num2.bit_count()
        b1 = num1.bit_count()

        mask = 1
        while b1 > b2:
            if num1 & mask:
                num1 ^= mask
                b1 -= 1
            mask <<= 1

        while b1 < b2:
            if num1 & mask == 0:
                num1 |= mask
                b1 += 1
            mask <<= 1

        return num1
