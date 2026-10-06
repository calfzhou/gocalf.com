import pytest

from solution import Solution


@pytest.mark.parametrize('matrix, expected', [
    ([[0,1],[1,1]], 1),
    ([[0,1],[1,0]], 2),
    ([[0,0,0],[0,0,1],[1,1,0]], 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, matrix, expected):
    assert sol.maxEqualRowsAfterFlips(matrix) == expected
