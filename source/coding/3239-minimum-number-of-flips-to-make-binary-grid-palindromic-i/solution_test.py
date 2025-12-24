import pytest

from solution import Solution


@pytest.mark.parametrize('grid, expected', [
    ([[1,0,0],[0,0,0],[0,0,1]], 2),
    ([[0,1],[0,1],[0,0]], 1),
    ([[1],[0]], 0),
])
class Test:
    def test_solution(self, grid, expected):
        sol = Solution()
        assert sol.minFlips(grid) == expected
