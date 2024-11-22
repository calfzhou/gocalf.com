class Solution:
    def countBits(self, n: int) -> list[int]:
        counts = [0] * (n + 1)
        prev = 0
        for i in range(1, n + 1):
            common = i & prev
            add = i ^ common
            if add == i:
                counts[i] = 1 # 2's power.
            else:
                remove = prev ^ common
                counts[i] = counts[prev] - counts[remove] + counts[add]
            prev = i

        return counts
