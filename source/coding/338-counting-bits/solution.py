class Solution:
    def countBits(self, n: int) -> list[int]:
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            cnt = 0
            j = i
            while j > 0:
                cnt += j & 1
                j >>= 1
            counts[i] = cnt

        return counts
