import pytest

from solution import Solution


@pytest.mark.parametrize('grid, expected', [
    ([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]], 3),
    ([[1,1,3],[3,2,2],[1,1,4]], 0),
    ([[1,2],[4,3]], 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, grid, expected):
    assert sol.minCost(grid) == expected
