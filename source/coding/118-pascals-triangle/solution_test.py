import pytest

from solution import Solution


@pytest.mark.parametrize('numRows, expected', [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (1, [[1]]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, numRows, expected):
    assert sol.generate(numRows) == expected
