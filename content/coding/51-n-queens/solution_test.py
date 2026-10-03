import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('n, expected', [
    (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
    (1, [["Q"]]),
])
class Test:
    def test_solution(self, n, expected):
        sol = Solution()
        assert sorted(sol.solveNQueens(n)) == sorted(expected)

    def test_solution2(self, n, expected):
        sol = Solution2()
        assert sorted(sol.solveNQueens(n)) == sorted(expected)
