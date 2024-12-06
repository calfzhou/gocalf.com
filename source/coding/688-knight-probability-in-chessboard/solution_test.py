import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('n, k, row, column, expected', [
    (3, 2, 0, 0, 0.06250),
    (1, 0, 0, 0, 1.00000),

    (8, 30, 6, 4, 0.00019),
])
class Test:
    def test_solution(self, n, k, row, column, expected):
        sol = Solution()
        assert sol.knightProbability(n, k, row, column) == pytest.approx(expected, abs=1e-5)

    def test_solution2(self, n, k, row, column, expected):
        sol = Solution2()
        assert sol.knightProbability(n, k, row, column) == pytest.approx(expected, abs=1e-5)
