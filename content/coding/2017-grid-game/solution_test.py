import pytest

from solution import Solution


@pytest.mark.parametrize('grid, expected', [
    ([[2,5,4],[1,5,1]], 4),
    ([[3,3,1],[8,5,2]], 4),
    ([[1,3,1,15],[1,3,3,1]], 7),

    ([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]], 63),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, grid, expected):
    assert sol.gridGame(grid) == expected
