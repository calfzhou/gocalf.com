from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        for val in sorted(counts, key=abs):
            if counts[val] == 0: # Already paired with another number.
                continue

            buddy = val * 2 # No need check whether counts[0] is even. If not, error will occurs later.
            if counts[val] > counts[buddy]: return False
            counts[buddy] -= counts[val] # No need to update counts[val].

        return True
