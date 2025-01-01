import pytest

from solution import Solution


@pytest.mark.parametrize('matrix, expected', [
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
    ([["0","1"],["1","0"]], 1),
    ([["0"]], 0),

    ([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]], 4),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, matrix, expected):
    assert sol.maximalSquare(matrix) == expected
