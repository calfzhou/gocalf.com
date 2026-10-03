import pytest

from solution import Solution


@pytest.mark.parametrize('grid, expected', [
    ([[0,1,3,2],[5,1,2,5],[4,3,8,6]], 7),
    ([[0,2,4],[3,2,1],[1,0,4]], -1),

    ([[0,1,99,99],[99,1,2,5],[99,99,99,6]], 7),
    ([[0,1,99,2],[5,1,2,5],[4,3,8,6]], 7),
])
class Test:
    def test_solution(self, grid, expected):
        sol = Solution()
        assert sol.minimumTime(grid) == expected
