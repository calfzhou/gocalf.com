import pytest

from solution import Solution


@pytest.mark.parametrize('grid, expected', [
    ([[1,0],[0,1]], 0),
    ([[1,0],[1,1]], 3),
    ([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]], 4),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, grid, expected):
    assert sol.countServers(grid) == expected
