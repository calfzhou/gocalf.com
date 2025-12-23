import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('n, expected', [
    (2, [0,1,1]),
    (5, [0,1,1,2,1,2]),

    (8, [0,1,1,2,1,2,2,3,1]),
])
class Test:
    def test_solution(self, n, expected):
        sol = Solution()
        assert sol.countBits(n) == expected

    def test_solution2(self, n, expected):
        sol = Solution2()
        assert sol.countBits(n) == expected

    def test_solution3(self, n, expected):
        sol = Solution3()
        assert sol.countBits(n) == expected
