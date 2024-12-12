import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('values, expected', [
    ([[8,5,2],[6,4,1],[9,7,3]], 285),
    ([[10,8,6,4,2],[9,7,5,3,2]], 386),
])
class Test:
    def test_solution(self, values, expected):
        sol = Solution()
        assert sol.maxSpending(values) == expected

    def test_solution2(self, values, expected):
        sol = Solution2()
        assert sol.maxSpending(values) == expected
