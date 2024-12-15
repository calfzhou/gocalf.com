

from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = sorted(Counter(arr).values(), reverse=True)
        m = len(arr) >> 1
        for i, freq in enumerate(counts, 1):
            m -= freq
            if m <= 0:
                return i
