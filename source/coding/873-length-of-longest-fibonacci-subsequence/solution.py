from itertools import combinations


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        s = set(arr)
        n = len(arr)
        longest = 0
        for i, j in combinations(range(n), 2):
            a, b = arr[i], arr[j]
            count = 2
            while a + b in s:
                a, b = b, a + b
                count += 1

            if count > longest:
                longest = count

        return longest if longest > 2 else 0
