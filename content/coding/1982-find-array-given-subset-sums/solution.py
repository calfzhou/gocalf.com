from collections import Counter


class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        arr = [None] * n
        sums.sort() # It doesn't matter whether `reverse` is True or False.
        m = len(sums)

        for i in range(n):
            d = sums[0] - sums[1] # d or -d must in arr.
            m >>= 1
            sums1 = [0] * m
            sums2 = [0] * m
            counts = Counter(sums)
            j = 0
            for a in sums:
                if counts[a] == 0: continue
                b = a - d
                counts[a] -= 1
                counts[b] -= 1 # b must exist.
                sums1[j] = a
                sums2[j] = b
                j += 1

            # sums1 and sums2 are both sorted.
            if d in sums1:
                arr[i] = d
                sums = sums2
            else:
                arr[i] = -d
                sums = sums1

        return arr
