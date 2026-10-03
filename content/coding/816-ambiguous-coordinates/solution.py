from itertools import product
from typing import Iterable


class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def numbers(l: int, r: int) -> Iterable[str]:
            """Enumerate all possible numbers for substring s[l:r]"""
            if r == l + 1:
                yield s[l] # The single-digit integer.
                return

            if s[l] != '0':
                yield s[l:r] # The multi-digits integer.

            if s[r-1] == '0':
                return # Tailing-zero is not allowed when decimal point exists.

            if s[l] == '0':
                yield f'0.{s[l+1:r]}' # Leading-zero is only allowed for `0.x`.
            else:
                yield from (f'{s[l:i]}.{s[i:r]}' for i in range(l + 1, r))

        n = len(s)
        return [*(f'({a}, {b})' for i in range (2, n-1) for a, b in product(numbers(1, i), numbers(i, n-1)))]
