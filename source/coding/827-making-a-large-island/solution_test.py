import copy
import pytest

from solution import Solution


@pytest.mark.parametrize('grid, expected', [
    ([[1,0],[0,1]], 3),
    ([[1,1],[1,0]], 4),
    ([[1,1],[1,1]], 4),

    ([[0,1,0],[1,0,1],[1,0,0]], 5),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, grid, expected):
    assert sol.largestIsland(copy.deepcopy(grid)) == expected
