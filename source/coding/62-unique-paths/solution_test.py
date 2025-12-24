import pytest

from solution import Solution
from solution_math import Solution as SolutionMath


@pytest.mark.parametrize('m, n, expected', [
    (3, 7, 28),
    (3, 2, 3),

    (7, 4, 84),
])
class Test:
    def test_solution(self, m, n, expected):
        sol = Solution()
        assert sol.uniquePaths(m, n) == expected

    def test_solution(self, m, n, expected):
        sol = SolutionMath()
        assert sol.uniquePaths(m, n) == expected
