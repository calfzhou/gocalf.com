import pytest

from solution import Solution


@pytest.mark.parametrize('grid, expected', [
    ([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]], 7),
    ([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]], 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, grid, expected):
    assert sol.findMaxFish(grid.copy()) == expected
