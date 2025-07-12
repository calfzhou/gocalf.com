import pytest

from solution import Solution


@pytest.mark.parametrize('rowIndex, expected', [
    (3, [1,3,3,1]),
    (0, [1]),
    (1, [1,1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, rowIndex, expected):
    assert sol.getRow(rowIndex) == expected
