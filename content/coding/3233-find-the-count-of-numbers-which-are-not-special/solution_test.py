import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('l, r, expected', [
    (5, 7, 3),
    (4, 16, 11),

    (1, 500**2, 500**2 - 95),
    (1, 1000**2, 1000**2 - 168),
    (1, 1009**2, 1009**2 - 169),
    (1, 30000**2, 30000**2 - 3245),
    (500**2, 30000**2, (30000**2 - 500**2 + 1) - (3245 - 95)),

    (19122653, 68803552, 49680455),
    (10086764, 96508040, 86420515),
])
class Test:
    def test_solution(self, l, r, expected):
        sol = Solution()
        assert sol.nonSpecialCount(l, r) == expected

    def test_solution2(self, l, r, expected):
        sol = Solution2()
        assert sol.nonSpecialCount(l, r) == expected
