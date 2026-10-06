from bisect import bisect_right
from itertools import accumulate


def is_special(n: int) -> bool:
    s = str(n ** 2)
    m = len(s)

    def backtrack(pos: int, target: int) -> bool:
        if pos == m:
            return target == 0

        for i in range(pos, m):
            left = int(s[pos:i + 1])
            if left > target:
                break
            if backtrack(i + 1, target - left):
                return True

        return False

    return backtrack(0, n)


MAX = 1001
specials = [i for i in range(1, MAX) if is_special(i)]
square_sums = list(accumulate(i ** 2 for i in specials))


class Solution:
    def punishmentNumber(self, n: int) -> int:
        ip = bisect_right(specials, n)
        return square_sums[ip-1]
