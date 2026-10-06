import pytest

from solution import Solution
from solution_log import Solution as SolutionLog


@pytest.mark.parametrize('n, expected', [
    (2, 2),
    (3, 3),

    (15, 987),
    (45, 1836311903),
])
class Test:
    def test_solution(self, n, expected):
        sol = Solution()
        assert sol.climbStairs(n) == expected

    def test_solution(self, n, expected):
        sol = SolutionLog()
        assert sol.climbStairs(n) == expected
