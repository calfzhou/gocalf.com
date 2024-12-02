import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('n, expected', [
    (4, 2),
    (1, 1),

    (8, 92),
])
class Test:
    def test_solution(self, n, expected):
        sol = Solution()
        assert sol.totalNQueens(n) == expected

    def test_solution2(self, n, expected):
        sol = Solution2()
        assert sol.totalNQueens(n) == expected
