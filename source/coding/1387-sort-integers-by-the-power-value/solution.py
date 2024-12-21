from functools import cache


@cache
def power(x: int) -> int:
    if x == 1:
        return 1
    elif x & 1:
        return 1 + power(3 * x + 1)
    else:
        return 1 + power(x >> 1)


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(range(lo, hi + 1), key=lambda val: power(val))[k - 1]
