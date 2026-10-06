class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        counts = [0] * 24 # log2(1e7, 2)
        for num in candidates:
            i = 0
            while num > 0:
                counts[i] += num & 1
                num >>= 1
                i += 1

        return max(counts)
