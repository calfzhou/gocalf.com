class Solution:
    def countBits(self, n: int) -> list[int]:
        counts = [0] * (n + 1)
        power = 1
        next_power = 2
        for i in range(1, n + 1):
            if i == next_power:
                power = next_power
                next_power <<= 1
            counts[i] = 1 + counts[i - power]

        return counts
