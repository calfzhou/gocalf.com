class Solution:
    def reverseBits(self, n: int) -> int:
        mask_l = 1
        mask_r = 1 << 31
        mask = mask_l | mask_r
        for _ in range(16):
            if (pair := n & mask) != 0 and pair != mask:
                n ^= mask
            mask_l <<= 1
            mask_r >>= 1
            mask = mask_l | mask_r

        return n
